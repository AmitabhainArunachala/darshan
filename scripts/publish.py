#!/usr/bin/env python3
"""Publish an approved Darshan article directly to GitHub Pages.

Usage:

    python3 scripts/publish.py
    python3 scripts/publish.py --dry-run
    python3 scripts/publish.py articles/2026-09-15-two-lists-not-one.md
    python3 scripts/publish.py articles/article.md --include style.css

No pull request is involved. GitHub Pages serves ``main``, but this command
never pushes the branch it is run from. It creates a disposable worktree at
the fetched ``origin/main``, copies only the named source files, runs the
editorial gate, static checks, unit tests, and site build, shows the actual
generated diff, then performs a normal fast-forward push.

The direct path is deliberately fail-closed:

* articles need explicit ``title``, ISO ``date``, ``status: published``, and
  a ``pipeline`` reference;
* the referenced seven-stage editorial package must pass Darshan's canonical
  checker and its ``piece.md`` body must exactly match the site article;
* paths cannot escape the repository, traverse symlinks, or name obvious
  secret material;
* an unexpected generated-file blast radius aborts unless explicitly allowed;
* a rejected push preserves the built commit on a local recovery branch;
* ``--no-push`` preserves a local preview branch instead of discarding a
  detached commit;
* after a successful push, the command waits for the exact generated HTML to
  appear on GitHub Pages before claiming it is live.

Stdlib only, like the rest of the publication.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

REMOTE = "origin"
LIVE_BRANCH = "main"
EXPECTED_REPOSITORY = "AmitabhainArunachala/darshan"
SITE_URL = "https://amitabhainarunachala.github.io/darshan"
PIPELINE_POINTER = Path.home() / ".dharma" / "DHARMA_SWARM_ROOT"
PIPELINE_RE = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$"
)
VALID_STATUSES = frozenset({"draft", "forthcoming", "published"})
SENSITIVE_DIRS = frozenset({".git", ".ssh", ".aws", "secrets", "credentials"})
SENSITIVE_NAMES = frozenset(
    {
        ".env",
        "id_rsa",
        "id_ed25519",
        "credentials.json",
        "service-account.json",
    }
)
SENSITIVE_SUFFIXES = frozenset({".pem", ".key", ".p12", ".pfx"})


class PublishError(RuntimeError):
    """A publication condition failed and the operator must see why."""


@dataclass(frozen=True)
class Article:
    relpath: str
    title: str
    published_on: str
    status: str
    pipeline: str
    body: str

    @property
    def html_relpath(self) -> str:
        return str(Path(self.relpath).with_suffix(".html"))

    @property
    def live_url(self) -> str:
        return "%s/articles/%s.html" % (SITE_URL, Path(self.relpath).stem)


def command(args, cwd=None, check=True, capture=True):
    """Run a command and surface its complete failure, not a silent code."""
    proc = subprocess.run(
        list(args),
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=capture,
    )
    if check and proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).strip()
        raise PublishError("%s failed:\n%s" % (" ".join(args), detail))
    return proc


def git(*args, cwd=None, check=True):
    proc = command(["git", *args], cwd=cwd, check=check)
    return (proc.stdout or "").strip()


def repo_root() -> Path:
    here = Path(__file__).resolve().parent
    return Path(git("rev-parse", "--show-toplevel", cwd=here)).resolve()


def _remote_repository(url: str) -> str:
    value = url.strip()
    value = re.sub(r"^ssh://git@github\.com/", "", value)
    value = re.sub(r"^git@github\.com:", "", value)
    value = re.sub(r"^https?://github\.com/", "", value)
    return value.removesuffix(".git").strip("/")


def validate_remote(root: Path) -> None:
    url = git("remote", "get-url", REMOTE, cwd=root)
    actual = _remote_repository(url)
    if actual.lower() != EXPECTED_REPOSITORY.lower():
        raise PublishError(
            "refusing to publish to %r; expected GitHub repository %s"
            % (url, EXPECTED_REPOSITORY)
        )


def _contains_symlink(root: Path, rel: Path) -> bool:
    current = root
    for part in rel.parts:
        current = current / part
        if current.is_symlink():
            return True
    return False


def _looks_sensitive(rel: Path) -> bool:
    lowered = [part.lower() for part in rel.parts]
    name = rel.name.lower()
    return (
        any(part in SENSITIVE_DIRS for part in lowered)
        or name in SENSITIVE_NAMES
        or name.startswith(".env.")
        or rel.suffix.lower() in SENSITIVE_SUFFIXES
    )


def normalize_repo_file(root: Path, raw: str, *, article=False) -> str:
    """Return a safe normalized repo-relative file path."""
    if not raw or "\x00" in raw:
        raise PublishError("empty or NUL-containing path")

    supplied = Path(raw).expanduser()
    if ".." in supplied.parts:
        raise PublishError("path traversal is not allowed: %s" % raw)

    if supplied.is_absolute():
        try:
            rel = supplied.relative_to(root)
        except ValueError as exc:
            raise PublishError("path is outside the repository: %s" % raw) from exc
    else:
        rel = supplied

    rel = Path(*[part for part in rel.parts if part not in {"", "."}])
    if not rel.parts or rel.parts[0] == ".git":
        raise PublishError("invalid publication path: %s" % raw)
    if _looks_sensitive(rel):
        raise PublishError("refusing secret-shaped publication path: %s" % raw)
    if _contains_symlink(root, rel):
        raise PublishError("symlinked publication paths are not allowed: %s" % raw)

    source = (root / rel).resolve()
    try:
        source.relative_to(root)
    except ValueError as exc:
        raise PublishError("path resolves outside the repository: %s" % raw) from exc
    if not source.is_file():
        raise PublishError("not found or not a regular file: %s" % raw)

    if article and not (rel.parent == Path("articles") and rel.suffix == ".md"):
        raise PublishError(
            "article paths must be top-level articles/*.md files: %s" % raw
        )
    return rel.as_posix()


def read_front_matter(path: Path) -> tuple[dict[str, str], str]:
    """Parse Darshan's deliberately small ``key: value`` front matter."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise PublishError("%s has no opening front-matter delimiter" % path.name)

    try:
        end = next(
            i
            for i, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise PublishError("%s has no closing front-matter delimiter" % path.name) from exc

    meta: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise PublishError(
                "%s:%d is not a key: value front-matter line"
                % (path.name, number)
            )
        key, _, value = line.partition(":")
        key = key.strip().lower()
        if not key:
            raise PublishError("%s:%d has an empty metadata key" % (path.name, number))
        if key in meta:
            raise PublishError(
                "%s has duplicate front-matter key %r" % (path.name, key)
            )
        meta[key] = value.strip()

    body = "\n".join(lines[end + 1 :]).strip()
    return meta, body


def validate_article(root: Path, relpath: str) -> Article:
    path = root / relpath
    meta, body = read_front_matter(path)
    required = ("title", "date", "status", "pipeline")
    missing = [key for key in required if not meta.get(key, "").strip()]
    if missing:
        raise PublishError(
            "%s is missing required front matter: %s"
            % (relpath, ", ".join(missing))
        )

    status = meta["status"].lower()
    if status not in VALID_STATUSES:
        raise PublishError(
            "%s has invalid status %r; expected one of %s"
            % (relpath, status, ", ".join(sorted(VALID_STATUSES)))
        )
    if status != "published":
        raise PublishError(
            "%s is status: %s. Direct-to-main publishing accepts only "
            "status: published; preview drafts locally with scripts/build.py."
            % (relpath, status)
        )

    try:
        date.fromisoformat(meta["date"])
    except ValueError as exc:
        raise PublishError(
            "%s has invalid date %r; use YYYY-MM-DD" % (relpath, meta["date"])
        ) from exc
    if not Path(relpath).name.startswith(meta["date"] + "-"):
        raise PublishError(
            "%s filename must begin with its front-matter date %s-"
            % (relpath, meta["date"])
        )

    pipeline = meta["pipeline"].strip()
    if not PIPELINE_RE.fullmatch(pipeline):
        raise PublishError(
            "%s pipeline must be <desk>/<YYYY-MM-DD-slug>, got %r"
            % (relpath, pipeline)
        )
    if not body:
        raise PublishError("%s has an empty article body" % relpath)

    return Article(
        relpath=relpath,
        title=meta["title"].strip(),
        published_on=meta["date"],
        status=status,
        pipeline=pipeline,
        body=body,
    )


def _split_nul(value: str) -> list[str]:
    return [item for item in value.split("\x00") if item]


def changed_articles(root: Path) -> list[str]:
    """Return existing changed articles; refuse implicit unpublication."""
    base = "%s/%s" % (REMOTE, LIVE_BRANCH)
    deleted = _split_nul(
        git(
            "diff",
            "--name-only",
            "--diff-filter=D",
            "-z",
            base,
            "--",
            "articles",
            cwd=root,
        )
    )
    deleted = sorted(path for path in deleted if path.endswith(".md"))
    if deleted:
        raise PublishError(
            "article deletion is not an implicit publish operation: %s. "
            "Use a separate, explicit unpublish workflow."
            % ", ".join(deleted)
        )

    tracked = _split_nul(
        git(
            "diff",
            "--name-only",
            "--diff-filter=ACMRTUXB",
            "-z",
            base,
            "--",
            "articles",
            cwd=root,
        )
    )
    untracked = _split_nul(
        git(
            "ls-files",
            "--others",
            "--exclude-standard",
            "-z",
            "--",
            "articles",
            cwd=root,
        )
    )
    return sorted(
        {
            path
            for path in tracked + untracked
            if path.endswith(".md") and path.strip()
        }
    )


def _worktree_paths(seed: Path) -> list[Path]:
    proc = command(
        ["git", "worktree", "list", "--porcelain"],
        cwd=seed,
        check=False,
    )
    if proc.returncode != 0:
        return []
    roots = []
    for line in proc.stdout.splitlines():
        if line.startswith("worktree "):
            roots.append(Path(line[len("worktree ") :]).resolve())
    return roots


def discover_pipeline_roots(explicit: list[str]) -> list[Path]:
    seeds: list[Path] = [Path(raw).expanduser() for raw in explicit]

    env_root = os.environ.get("DARSHAN_PIPELINE_ROOT")
    if env_root:
        seeds.append(Path(env_root).expanduser())

    if PIPELINE_POINTER.is_file():
        pointer = PIPELINE_POINTER.read_text(encoding="utf-8").strip()
        if pointer:
            seeds.append(Path(pointer).expanduser())

    roots: list[Path] = []
    seen: set[Path] = set()
    for seed in seeds:
        resolved = seed.resolve()
        for candidate in [resolved, *_worktree_paths(resolved)]:
            if candidate in seen or not candidate.is_dir():
                continue
            seen.add(candidate)
            roots.append(candidate)
    return roots


def _load_editorial_checker(path: Path):
    name = "darshan_editorial_%s" % hashlib.sha256(
        str(path).encode()
    ).hexdigest()[:10]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise PublishError("cannot load editorial checker at %s" % path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def canonical_checker_path(roots: list[Path]) -> Path:
    """Use the canonical checker even when the package lives in a worktree."""
    candidates: list[Path] = []
    if PIPELINE_POINTER.is_file():
        pointer = PIPELINE_POINTER.read_text(encoding="utf-8").strip()
        if pointer:
            candidates.append(Path(pointer).expanduser().resolve())
    candidates.extend(roots)
    for root in candidates:
        path = root / "scripts" / "darshan" / "check_darshan_editorial.py"
        if path.is_file():
            return path
    raise PublishError(
        "canonical Darshan editorial checker not found; "
        "verify ~/.dharma/DHARMA_SWARM_ROOT"
    )


def validate_editorial_package(
    article: Article,
    roots: list[Path],
    *,
    checker_path: Path | None = None,
) -> Path:
    """Find one gate-clean pipeline package whose body is byte-equivalent."""
    attempted: list[str] = []
    valid: list[Path] = []
    checker_path = checker_path or canonical_checker_path(roots)
    checker = _load_editorial_checker(checker_path)

    for root in roots:
        articles_root = root / "reports" / "darshan" / "articles"
        piece_dir = articles_root / article.pipeline
        if not piece_dir.is_dir():
            continue

        try:
            findings = checker.check_piece_dir(piece_dir, articles_root)
        except Exception as exc:
            attempted.append("%s: checker failed: %s" % (root, exc))
            continue
        if findings:
            attempted.append(
                "%s: %s"
                % (root, "; ".join(str(finding) for finding in findings))
            )
            continue

        try:
            piece_meta, piece_body = read_front_matter(piece_dir / "piece.md")
            approval = json.loads(
                (piece_dir / "approval.json").read_text(encoding="utf-8")
            )
        except (OSError, ValueError, PublishError) as exc:
            attempted.append("%s: unreadable package: %s" % (root, exc))
            continue

        if piece_meta.get("status", "").lower() != "published":
            attempted.append("%s: pipeline piece is not status: published" % root)
            continue
        if piece_body != article.body:
            attempted.append("%s: pipeline piece body does not match site article" % root)
            continue
        if not isinstance(approval, dict) or not str(
            approval.get("approved_by", "")
        ).strip():
            attempted.append("%s: approval has no approved_by" % root)
            continue
        approved_title = str(approval.get("title", "")).strip()
        if approved_title and approved_title != article.title:
            attempted.append(
                "%s: approved title %r does not match %r"
                % (root, approved_title, article.title)
            )
            continue
        valid.append(root)

    if not valid:
        detail = "\n  - ".join(attempted) if attempted else "no matching package found"
        raise PublishError(
            "%s did not resolve to a gate-clean editorial package.\n  - %s\n"
            "Set --pipeline-root or DARSHAN_PIPELINE_ROOT if the approved "
            "package is in an unregistered checkout."
            % (article.pipeline, detail)
        )
    if len(valid) > 1:
        print(
            "  editorial package matched in %d worktrees; using %s"
            % (len(valid), valid[0])
        )
    return valid[0]


def run_checks(tree: Path, articles: list[Article], carry: list[str]) -> str:
    scripts = [tree / "scripts" / "build.py", tree / "scripts" / "publish.py"]
    command(
        [sys.executable, "-m", "py_compile", *[str(path) for path in scripts]],
        cwd=tree,
    )
    print("  static: build.py and publish.py import cleanly")

    tests = tree / "tests"
    if tests.is_dir() and any(tests.glob("test_*.py")):
        result = command(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "tests",
                "-p",
                "test_*.py",
            ],
            cwd=tree,
        )
        summary = (result.stderr or result.stdout).strip().splitlines()
        print("  tests: %s" % (summary[-1] if summary else "passed"))

    build = command([sys.executable, "scripts/build.py"], cwd=tree)
    output = build.stdout or ""
    tail = output.strip().splitlines()[-1:] or [""]
    print("  build: %s" % tail[0])
    if "0 parse failure" not in output:
        raise PublishError("build did not report zero parse failures")

    for article in articles:
        rendered = tree / article.html_relpath
        if not rendered.is_file():
            raise PublishError("builder did not create %s" % article.html_relpath)
        if '<div class="draft-banner">' in rendered.read_text(encoding="utf-8"):
            raise PublishError("%s rendered with a draft banner" % article.relpath)

    return output


def _actual_changes(tree: Path) -> list[str]:
    return _split_nul(git("diff", "--cached", "--name-only", "-z", cwd=tree))


def validate_blast_radius(
    changes: list[str],
    carry: list[str],
    articles: list[Article],
    *,
    allow_generated_drift: bool,
) -> None:
    allowed = set(carry)
    allowed.add("index.html")
    allowed.update(article.html_relpath for article in articles)

    renderer_changed = any(
        rel == "scripts/build.py" or rel.startswith("templates/") for rel in carry
    )
    if renderer_changed:
        allowed.add("about.html")
        allowed.update(
            rel
            for rel in changes
            if rel.startswith("articles/") and rel.endswith(".html")
        )

    unexpected = sorted(set(changes) - allowed)
    if unexpected and not allow_generated_drift:
        raise PublishError(
            "build changed files outside the declared blast radius:\n  %s\n"
            "Inspect them, then re-run with --allow-generated-drift only if "
            "the regeneration is intentional."
            % "\n  ".join(unexpected)
        )


def _safe_branch(root: Path, namespace: str, sha: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = "darshan-%s/%s-%s" % (namespace, stamp, sha[:8])
    name = base
    counter = 2
    while command(
        ["git", "show-ref", "--verify", "--quiet", "refs/heads/%s" % name],
        cwd=root,
        check=False,
    ).returncode == 0:
        name = "%s-%d" % (base, counter)
        counter += 1
    git("branch", name, sha, cwd=root)
    return name


def _capture_failure(tree: Path, label: str) -> Path | None:
    if not tree.is_dir():
        return None
    # Intent-to-add would omit file contents; stage the disposable tree so the
    # custody patch includes newly carried articles, tests, and assets too.
    command(["git", "add", "-A"], cwd=tree, check=False)
    patch = git("diff", "--cached", "--binary", "HEAD", cwd=tree, check=False)
    if not patch:
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    directory = Path.home() / ".dharma" / "darshan" / "publish-failures"
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / ("%s-%s.patch" % (stamp, label))
    path.write_text(patch + "\n", encoding="utf-8")
    return path


def _clean_disposable_worktree(root: Path, tree: Path, work: Path) -> None:
    if tree.is_dir():
        # This tree was created by this process under /tmp. Reset only that
        # disposable tree so normal (non-force) worktree removal can succeed.
        command(["git", "reset", "--hard", "HEAD"], cwd=tree, check=False)
        command(["git", "clean", "-fd"], cwd=tree, check=False)
        removed = command(
            ["git", "worktree", "remove", str(tree)],
            cwd=root,
            check=False,
        )
        if removed.returncode != 0:
            print(
                "warning: scratch worktree remains at %s: %s"
                % (tree, (removed.stderr or removed.stdout).strip()),
                file=sys.stderr,
            )
            return
    command(["git", "worktree", "prune"], cwd=root, check=False)
    shutil.rmtree(work, ignore_errors=True)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def wait_until_live(
    tree: Path, articles: list[Article], commit: str, timeout: int
) -> bool:
    if timeout <= 0:
        return True
    targets = [
        (article.live_url, (tree / article.html_relpath).read_bytes())
        for article in articles
    ]
    if not targets:
        targets = [(SITE_URL + "/index.html", (tree / "index.html").read_bytes())]

    deadline = time.monotonic() + timeout
    pending = dict(targets)
    while pending and time.monotonic() < deadline:
        for url, expected in list(pending.items()):
            request = urllib.request.Request(
                "%s?darshan=%s" % (url, commit[:12]),
                headers={
                    "Cache-Control": "no-cache",
                    "User-Agent": "darshan-publisher",
                },
            )
            try:
                with urllib.request.urlopen(request, timeout=10) as response:
                    actual = response.read()
            except (urllib.error.URLError, TimeoutError):
                continue
            if _sha256(actual) == _sha256(expected):
                del pending[url]
        if pending:
            time.sleep(3)
    return not pending


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Publish an approved Darshan article directly to the live site."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="top-level articles/*.md files (default: auto-detect)",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="extra repo-relative source or asset to carry",
    )
    parser.add_argument(
        "--pipeline-root",
        action="append",
        default=[],
        help="dharma_swarm checkout containing the approved editorial package",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="run the gate, tests, build, and diff without committing or pushing",
    )
    mode.add_argument(
        "--no-push",
        action="store_true",
        help="commit to a preserved local preview branch; do not push",
    )
    parser.add_argument(
        "--allow-generated-drift",
        action="store_true",
        help="allow intentional regenerated files outside the normal article scope",
    )
    parser.add_argument(
        "--wait-seconds",
        type=int,
        default=120,
        help="wait for exact HTML on GitHub Pages after push (default: 120; 0 disables)",
    )
    parser.add_argument("-m", "--message", default=None, help="commit message")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.wait_seconds < 0:
        raise PublishError("--wait-seconds cannot be negative")

    root = repo_root()
    validate_remote(root)

    print("fetching %s/%s ..." % (REMOTE, LIVE_BRANCH))
    git("fetch", REMOTE, LIVE_BRANCH, cwd=root)

    raw_articles = args.paths or changed_articles(root)
    article_paths = [
        normalize_repo_file(root, raw, article=True) for raw in raw_articles
    ]
    include_paths = [
        normalize_repo_file(root, raw, article=False) for raw in args.include
    ]
    carry = list(dict.fromkeys(article_paths + include_paths))
    if not carry:
        print("nothing to publish — no new or changed articles. (clean no-op)")
        return 0

    articles = [validate_article(root, relpath) for relpath in article_paths]
    pipeline_roots = discover_pipeline_roots(args.pipeline_root)

    print("\neditorial gate:")
    for article in articles:
        matched = validate_editorial_package(article, pipeline_roots)
        print("  PASS  %-46s %s" % (article.title, matched))

    print("\nwill carry:")
    for relpath in carry:
        article = next((a for a in articles if a.relpath == relpath), None)
        if article:
            print("  %-52s %s [PUBLISHED]" % (relpath, article.title))
        else:
            print("  %-52s (supporting file)" % relpath)

    work = Path(tempfile.mkdtemp(prefix="darshan-publish-", dir="/tmp"))
    tree = work / "site"
    committed = False
    failure_label = "precommit"
    try:
        git(
            "worktree",
            "add",
            "--detach",
            str(tree),
            "%s/%s" % (REMOTE, LIVE_BRANCH),
            cwd=root,
        )
        for relpath in carry:
            source = root / relpath
            destination = tree / relpath
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

        print("\nchecking and building ...")
        run_checks(tree, articles, carry)
        git("add", "-A", cwd=tree)
        changes = _actual_changes(tree)
        if not changes:
            print("\nalready live — generated output is byte-identical. (clean no-op)")
            return 0
        validate_blast_radius(
            changes,
            carry,
            articles,
            allow_generated_drift=args.allow_generated_drift,
        )
        git("diff", "--cached", "--check", cwd=tree)

        print("\nactual commit:")
        for relpath in changes:
            print("  %s" % relpath)
        stat = git("diff", "--cached", "--stat", cwd=tree)
        if stat:
            print("\n%s" % stat)

        if args.dry_run:
            print("\n--dry-run: gate and build passed; nothing committed or pushed.")
            return 0

        titles = [article.title for article in articles]
        subject = args.message or (
            "darshan: publish %s"
            % ", ".join('"%s"' % title for title in titles)
            if titles
            else "darshan: site update"
        )
        git(
            "-c",
            "user.name=Darshan publisher",
            "-c",
            "user.email=publisher@darshan.local",
            "commit",
            "-q",
            "-m",
            subject,
            cwd=tree,
        )
        committed = True
        commit = git("rev-parse", "HEAD", cwd=tree)

        if args.no_push:
            branch = _safe_branch(root, "preview", commit)
            print("\n--no-push: preserved local preview branch %s" % branch)
            return 0

        print("\npushing to %s/%s ..." % (REMOTE, LIVE_BRANCH))
        push = command(
            ["git", "push", REMOTE, "HEAD:%s" % LIVE_BRANCH],
            cwd=tree,
            check=False,
        )
        if push.returncode != 0:
            branch = _safe_branch(root, "recovery", commit)
            failure_label = "push"
            raise PublishError(
                "push failed; the built commit is preserved on local branch %s:\n%s"
                % (branch, (push.stderr or push.stdout).strip())
            )

        print("\npushed %s." % commit[:12])
        if wait_until_live(tree, articles, commit, args.wait_seconds):
            print("live:")
            for article in articles:
                print("  %s" % article.live_url)
            return 0

        print(
            "published, but GitHub Pages did not match the generated HTML "
            "within %d seconds." % args.wait_seconds,
            file=sys.stderr,
        )
        for article in articles:
            print("  pending: %s" % article.live_url, file=sys.stderr)
        return 2
    except Exception:
        if tree.is_dir() and not committed:
            captured = _capture_failure(tree, failure_label)
            if captured:
                print("failure patch captured at %s" % captured, file=sys.stderr)
        raise
    finally:
        _clean_disposable_worktree(root, tree, work)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PublishError as exc:
        print("\npublish aborted: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    except KeyboardInterrupt:
        raise SystemExit(130)
