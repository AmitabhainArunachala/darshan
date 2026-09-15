from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


publish = load_module("darshan_publish_test", ROOT / "scripts" / "publish.py")


def article_text(
    *,
    status: str = "published",
    date: str = "2026-09-15",
    pipeline: str = "readings-in-fire/2026-09-15-test-piece",
    body: str = "Body.",
) -> str:
    return (
        "---\n"
        "title: Test Piece\n"
        "date: %s\n"
        "status: %s\n"
        "pipeline: %s\n"
        "---\n\n%s\n"
    ) % (date, status, pipeline, body)


class PublisherValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / "articles").mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def write_article(self, name="2026-09-15-test-piece.md", **kwargs):
        path = self.root / "articles" / name
        path.write_text(article_text(**kwargs), encoding="utf-8")
        return path

    def test_safe_path_accepts_article_and_rejects_traversal(self):
        path = self.write_article()
        self.assertEqual(
            "articles/2026-09-15-test-piece.md",
            publish.normalize_repo_file(self.root, str(path), article=True),
        )
        with self.assertRaisesRegex(publish.PublishError, "traversal"):
            publish.normalize_repo_file(
                self.root, "articles/../outside.md", article=True
            )

    def test_symlink_and_secret_shaped_paths_are_rejected(self):
        target = self.write_article()
        link = self.root / "articles" / "2026-09-15-link.md"
        try:
            link.symlink_to(target)
        except OSError:
            self.skipTest("symlinks unavailable")
        with self.assertRaisesRegex(publish.PublishError, "symlink"):
            publish.normalize_repo_file(self.root, str(link), article=True)

        secret = self.root / ".env"
        secret.write_text("TOKEN=secret", encoding="utf-8")
        with self.assertRaisesRegex(publish.PublishError, "secret-shaped"):
            publish.normalize_repo_file(self.root, ".env")

    def test_direct_publisher_requires_explicit_published_status(self):
        path = self.write_article(status="draft")
        with self.assertRaisesRegex(publish.PublishError, "accepts only"):
            publish.validate_article(self.root, str(path.relative_to(self.root)))

        path.write_text(
            article_text(status="forthcoming"), encoding="utf-8"
        )
        with self.assertRaisesRegex(publish.PublishError, "accepts only"):
            publish.validate_article(self.root, str(path.relative_to(self.root)))

    def test_article_requires_date_status_and_pipeline(self):
        path = self.root / "articles" / "2026-09-15-test-piece.md"
        path.write_text(
            "---\ntitle: Test Piece\ndate: 2026-09-15\n---\n\nBody.\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(publish.PublishError, "status, pipeline"):
            publish.validate_article(self.root, str(path.relative_to(self.root)))

    def test_duplicate_front_matter_key_is_rejected(self):
        path = self.root / "articles" / "2026-09-15-test-piece.md"
        path.write_text(
            "---\n"
            "title: First\n"
            "title: Second\n"
            "date: 2026-09-15\n"
            "status: published\n"
            "pipeline: readings-in-fire/2026-09-15-test-piece\n"
            "---\n\nBody.\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(publish.PublishError, "duplicate"):
            publish.validate_article(self.root, str(path.relative_to(self.root)))

    def test_filename_date_must_match_front_matter(self):
        path = self.write_article(date="2026-09-14")
        with self.assertRaisesRegex(publish.PublishError, "filename must begin"):
            publish.validate_article(self.root, str(path.relative_to(self.root)))

    def test_pipeline_body_must_match_and_checker_must_pass(self):
        site_path = self.write_article(body="Approved body.")
        article = publish.validate_article(
            self.root, str(site_path.relative_to(self.root))
        )

        pipeline_root = self.root / "pipeline"
        package = (
            pipeline_root
            / "reports"
            / "darshan"
            / "articles"
            / "readings-in-fire"
            / "2026-09-15-test-piece"
        )
        package.mkdir(parents=True)
        (package / "piece.md").write_text(
            "---\ntitle: Test Piece\nstatus: published\n---\n\nApproved body.\n",
            encoding="utf-8",
        )
        (package / "approval.json").write_text(
            json.dumps({"approved_by": "operator", "title": "Test Piece"}),
            encoding="utf-8",
        )
        checker = pipeline_root / "scripts" / "darshan"
        checker.mkdir(parents=True)
        (checker / "check_darshan_editorial.py").write_text(
            "def check_piece_dir(piece_dir, root):\n    return []\n",
            encoding="utf-8",
        )

        self.assertEqual(
            pipeline_root,
            publish.validate_editorial_package(
                article,
                [pipeline_root],
                checker_path=checker / "check_darshan_editorial.py",
            ),
        )

        (package / "piece.md").write_text(
            "---\ntitle: Test Piece\nstatus: published\n---\n\nDifferent body.\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(publish.PublishError, "body does not match"):
            publish.validate_editorial_package(
                article,
                [pipeline_root],
                checker_path=checker / "check_darshan_editorial.py",
            )

    def test_unexpected_generated_drift_fails_closed(self):
        article = publish.Article(
            relpath="articles/2026-09-15-test-piece.md",
            title="Test",
            published_on="2026-09-15",
            status="published",
            pipeline="readings-in-fire/2026-09-15-test-piece",
            body="Body",
        )
        with self.assertRaisesRegex(publish.PublishError, "outside"):
            publish.validate_blast_radius(
                [
                    article.relpath,
                    article.html_relpath,
                    "index.html",
                    "articles/unrelated.html",
                ],
                [article.relpath],
                [article],
                allow_generated_drift=False,
            )

    def test_no_push_commit_gets_durable_local_branch(self):
        repo = self.root / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
        (repo / "file.txt").write_text("one", encoding="utf-8")
        subprocess.run(["git", "add", "file.txt"], cwd=repo, check=True)
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Test",
                "-c",
                "user.email=test@example.invalid",
                "commit",
                "-qm",
                "initial",
            ],
            cwd=repo,
            check=True,
        )
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo, text=True
        ).strip()

        name = publish._safe_branch(repo, "preview", sha)
        resolved = subprocess.check_output(
            ["git", "rev-parse", name], cwd=repo, text=True
        ).strip()

        self.assertEqual(sha, resolved)
        self.assertTrue(name.startswith("darshan-preview/"))

    def test_auto_detection_refuses_implicit_article_deletion(self):
        repo = self.root / "deletion-repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
        (repo / "articles").mkdir()
        article = repo / "articles" / "2026-09-15-test-piece.md"
        article.write_text(article_text(), encoding="utf-8")
        subprocess.run(["git", "add", "articles"], cwd=repo, check=True)
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Test",
                "-c",
                "user.email=test@example.invalid",
                "commit",
                "-qm",
                "initial",
            ],
            cwd=repo,
            check=True,
        )
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo, text=True
        ).strip()
        subprocess.run(
            ["git", "update-ref", "refs/remotes/origin/main", sha],
            cwd=repo,
            check=True,
        )
        article.unlink()

        with self.assertRaisesRegex(publish.PublishError, "separate.*unpublish"):
            publish.changed_articles(repo)

    def test_remote_normalization_accepts_https_and_ssh(self):
        expected = "AmitabhainArunachala/darshan"
        self.assertEqual(
            expected,
            publish._remote_repository(
                "https://github.com/AmitabhainArunachala/darshan.git"
            ),
        )
        self.assertEqual(
            expected,
            publish._remote_repository(
                "git@github.com:AmitabhainArunachala/darshan.git"
            ),
        )


if __name__ == "__main__":
    unittest.main()
