#!/usr/bin/env python3
"""Publish Darshan straight to the live site. No pull request, no merge.

    python3 scripts/publish.py                 # publish new/changed articles
    python3 scripts/publish.py --dry-run       # show what would happen
    python3 scripts/publish.py a.md --include style.css

Why this exists, and why it does not just `git push` from where you are:
GitHub Pages serves `main`. Working branches here routinely sit on top of
unrelated commits — a garden series, a redesign, draft articles marked "do not
cite or circulate". Pushing such a branch publishes all of it. This script
therefore never publishes the branch you are on. It builds a pristine checkout
of origin/main, copies in only the files you named, rebuilds, and pushes that.
The blast radius is the file list it prints before committing.

Stdlib only, like the rest of the site.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REMOTE = "origin"
LIVE_BRANCH = "main"
SITE_URL = "https://amitabhainarunachala.github.io/darshan"


class PublishError(RuntimeError):
    """Something went wrong that the operator must see and decide about."""


def git(*args, cwd=None, check=True, capture=True):
    proc = subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else None,
        text=True,
        capture_output=capture,
    )
    if check and proc.returncode != 0:
        raise PublishError(
            "git %s failed:\n%s" % (" ".join(args), (proc.stderr or proc.stdout).strip())
        )
    return (proc.stdout or "").strip()


def repo_root() -> Path:
    here = Path(__file__).resolve().parent
    return Path(git("rev-parse", "--show-toplevel", cwd=here))


def parse_status(path: Path) -> tuple[str, str]:
    """Return (title, status) from front matter. Empty title means unusable."""
    title, status = "", "published"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "", status
    if not text.startswith("---"):
        return "", status
    for line in text.split("\n")[1:]:
        if line.strip() == "---":
            break
        key, _, value = line.partition(":")
        key, value = key.strip().lower(), value.strip()
        if key == "title":
            title = value
        elif key == "status":
            status = value.lower()
    return title, status


def changed_articles(root: Path) -> list[str]:
    """Articles new or modified relative to the live branch."""
    base = "%s/%s" % (REMOTE, LIVE_BRANCH)
    tracked = git("diff", "--name-only", base, "--", "articles", cwd=root).split("\n")
    untracked = git(
        "ls-files", "--others", "--exclude-standard", "--", "articles", cwd=root
    ).split("\n")
    out = {p for p in tracked + untracked if p.endswith(".md") and p.strip()}
    return sorted(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Publish Darshan directly to the live site (no PR)."
    )
    ap.add_argument("paths", nargs="*", help="article .md files (default: auto-detect)")
    ap.add_argument("--include", action="append", default=[],
                    help="extra repo-relative file to carry (e.g. style.css)")
    ap.add_argument("--dry-run", action="store_true", help="show, do not publish")
    ap.add_argument("--no-push", action="store_true", help="commit locally, do not push")
    ap.add_argument("-m", "--message", default=None, help="commit message")
    args = ap.parse_args(argv)

    root = repo_root()

    print("fetching %s/%s ..." % (REMOTE, LIVE_BRANCH))
    git("fetch", REMOTE, LIVE_BRANCH, cwd=root)

    carry = list(dict.fromkeys(
        [str(Path(p).resolve().relative_to(root)) if Path(p).is_absolute() else p
         for p in args.paths] + list(args.include)
    ))
    if not args.paths:
        auto = changed_articles(root)
        carry = list(dict.fromkeys(auto + list(args.include)))

    missing = [p for p in carry if not (root / p).is_file()]
    if missing:
        raise PublishError("not found: %s" % ", ".join(missing))
    if not carry:
        print("nothing to publish — no new or changed articles. (clean no-op)")
        return 0

    print("\nwill publish:")
    blocked = []
    for rel in carry:
        if rel.startswith("articles/") and rel.endswith(".md"):
            title, status = parse_status(root / rel)
            if not title:
                blocked.append("%s has no title: in its front matter" % rel)
            flag = "" if status == "published" else "  [%s]" % status.upper()
            print("  %-52s %s%s" % (rel, title or "(no title)", flag))
        else:
            print("  %-52s (supporting file)" % rel)
    if blocked:
        raise PublishError("; ".join(blocked))

    if args.dry_run:
        print("\n--dry-run: nothing written, nothing pushed.")
        return 0

    work = Path(tempfile.mkdtemp(prefix="darshan-publish-"))
    tree = work / "site"
    try:
        git("worktree", "add", "--detach", str(tree),
            "%s/%s" % (REMOTE, LIVE_BRANCH), cwd=root)

        for rel in carry:
            dest = tree / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / rel, dest)

        print("\nbuilding ...")
        build = subprocess.run(
            [sys.executable, "scripts/build.py"], cwd=str(tree),
            text=True, capture_output=True,
        )
        tail = (build.stdout or "").strip().split("\n")[-1:]
        print("  " + (tail[0] if tail else ""))
        if build.returncode != 0:
            raise PublishError("build failed:\n%s" % (build.stderr or build.stdout))
        if "0 parse failure" not in build.stdout:
            raise PublishError("build reported parse failures; refusing to publish")
        for rel in carry:
            if rel.startswith("articles/") and "SKIP %s" % Path(rel).name in build.stdout:
                raise PublishError("%s was skipped by the builder (bad front matter)" % rel)

        git("add", "-A", cwd=tree)
        if not git("status", "--porcelain", cwd=tree):
            print("\nalready live — the site is byte-identical. (clean no-op)")
            return 0

        titles = [parse_status(root / r)[0] for r in carry
                  if r.startswith("articles/") and r.endswith(".md")]
        titles = [t for t in titles if t]
        subject = args.message or (
            "darshan: publish %s" % ", ".join('"%s"' % t for t in titles)
            if titles else "darshan: site update"
        )
        git("-c", "user.name=Darshan publisher",
            "-c", "user.email=publisher@darshan.local",
            "commit", "-q", "-m", subject, cwd=tree)

        if args.no_push:
            print("\n--no-push: committed in the scratch worktree only.")
            return 0

        print("pushing to %s/%s ..." % (REMOTE, LIVE_BRANCH))
        push = subprocess.run(
            ["git", "push", REMOTE, "HEAD:%s" % LIVE_BRANCH],
            cwd=str(tree), text=True, capture_output=True,
        )
        if push.returncode != 0:
            err = (push.stderr or push.stdout).strip()
            if "non-fast-forward" in err or "fetch first" in err or "rejected" in err:
                raise PublishError(
                    "push rejected — %s/%s moved while publishing. "
                    "Nothing was published. Re-run to rebase on the new tip."
                    % (REMOTE, LIVE_BRANCH)
                )
            raise PublishError("push failed:\n%s" % err)

        print("\npublished.")
        for rel in carry:
            if rel.startswith("articles/") and rel.endswith(".md"):
                print("  %s/articles/%s.html" % (SITE_URL, Path(rel).stem))
        print("\nGitHub Pages usually takes under a minute to rebuild.")
        return 0
    finally:
        subprocess.run(["git", "worktree", "remove", "--force", str(tree)],
                       cwd=str(root), capture_output=True)
        subprocess.run(["git", "worktree", "prune"], cwd=str(root), capture_output=True)
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PublishError as exc:
        print("\npublish aborted: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    except KeyboardInterrupt:
        raise SystemExit(130)
