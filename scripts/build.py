#!/usr/bin/env python3
"""Darshan static site builder.

Stdlib only. Reads articles/*.md + templates/, writes index.html,
about.html, and articles/*.html. Verifies every generated page parses
clean before declaring success.

Usage:  python3 scripts/build.py
"""

import html
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
TEMPLATES_DIR = ROOT / "templates"

SITE_NAME = "Darshan"
SITE_TAGLINE = "A signal of clear seeing in an age of information overload"

DRAFT_BANNER = (
    '<div class="draft-banner"><strong>Draft — pending discernment pass.</strong> '
    "This piece has not yet survived both fires of the editorial law and has not "
    "received sign-off. It appears here as a working document; do not cite or "
    "circulate.</div>"
)


# ---------------------------------------------------------------- templates

def template(name):
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8")


def render(tpl, **tokens):
    out = tpl
    for key, value in tokens.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = re.search(r"\{\{[a-z_]+\}\}", out)
    if leftover:
        raise ValueError("unfilled template token: " + leftover.group(0))
    return out


# ------------------------------------------------------------- front matter

def parse_front_matter(text):
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("\n")
        end = None
        for i, line in enumerate(parts[1:], start=1):
            if line.strip() == "---":
                end = i
                break
        if end is not None:
            for line in parts[1:end]:
                if ":" in line:
                    key, _, value = line.partition(":")
                    meta[key.strip().lower()] = value.strip()
            body = "\n".join(parts[end + 1:])
    return meta, body


# ----------------------------------------------------------------- markdown

def _inline(text):
    """Inline markdown on already-escaped text: code, links, bold, italic."""
    stash = []

    def keep(fragment):
        stash.append(fragment)
        return "\x00%d\x00" % (len(stash) - 1)

    text = re.sub(
        r"`([^`]+)`", lambda m: keep("<code>%s</code>" % m.group(1)), text
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: keep('<a href="%s">%s</a>' % (m.group(2), m.group(1))),
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def md_to_html(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            block = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            out.append(
                "<pre><code>%s</code></pre>"
                % html.escape("\n".join(block), quote=False)
            )
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"(#{1,6})\s+(.*)", stripped)
        if m:
            level = len(m.group(1))
            text = _inline(html.escape(m.group(2), quote=False))
            out.append("<h%d>%s</h%d>" % (level, text, level))
            i += 1
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while i < n and lines[i].strip().startswith(">"):
                quote_lines.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = md_to_html("\n".join(quote_lines))
            out.append("<blockquote>%s</blockquote>" % inner)
            continue

        if re.match(r"[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"[-*]\s+", lines[i].strip()):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                i += 1
                while i < n and lines[i].startswith("  ") and lines[i].strip():
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            out.append(
                "<ul>%s</ul>"
                % "".join(
                    "<li>%s</li>" % _inline(html.escape(t, quote=False))
                    for t in items
                )
            )
            continue

        if re.match(r"\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"\d+\.\s+", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                i += 1
                while i < n and lines[i].startswith("  ") and lines[i].strip():
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            out.append(
                "<ol>%s</ol>"
                % "".join(
                    "<li>%s</li>" % _inline(html.escape(t, quote=False))
                    for t in items
                )
            )
            continue

        para = []
        while i < n and lines[i].strip() and not _is_block_start(lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % _inline(html.escape(" ".join(para), quote=False)))

    return "\n".join(out)


def _is_block_start(stripped):
    return bool(
        stripped.startswith(("#", ">", "```"))
        or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped)
        or re.match(r"[-*]\s+", stripped)
        or re.match(r"\d+\.\s+", stripped)
    )


# ------------------------------------------------------------------- checks

VOID_TAGS = {"meta", "link", "br", "hr", "img", "input", "source", "wbr"}


class BalanceChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if not self.stack:
            self.errors.append("stray closing </%s>" % tag)
        elif self.stack[-1] != tag:
            self.errors.append(
                "mismatched </%s>, expected </%s>" % (tag, self.stack[-1])
            )
            self.stack.pop()
        else:
            self.stack.pop()


def check_well_formed(path):
    checker = BalanceChecker()
    checker.feed(path.read_text(encoding="utf-8"))
    checker.close()
    if checker.stack:
        checker.errors.append("unclosed tags: " + ", ".join(checker.stack))
    return checker.errors


# -------------------------------------------------------------------- build

def display_date(iso):
    try:
        d = date.fromisoformat(iso)
        return "%d %s %d" % (d.day, d.strftime("%B"), d.year)
    except ValueError:
        return iso


def load_articles():
    articles = []
    for path in sorted(ARTICLES_DIR.glob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        if "title" not in meta or "date" not in meta:
            print("SKIP %s: front matter needs at least title: and date:" % path.name)
            continue
        articles.append(
            {
                "slug": path.stem,
                "title": meta["title"],
                "date": meta["date"],
                "status": meta.get("status", "draft").lower(),
                "issue": meta.get("issue", ""),
                "summary": meta.get("summary", ""),
                "body_html": md_to_html(body),
            }
        )
    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles


def prune_stale(generated_names):
    stale = [f for f in ARTICLES_DIR.glob("*.html") if f.name not in generated_names]
    for f in stale:
        f.unlink()
        print(f"pruned stale output: articles/{f.name}")
    leftover = [f.name for f in ARTICLES_DIR.glob("*.html") if f.name not in generated_names]
    assert not leftover, f"stale article outputs survived pruning: {leftover}"


def build():
    base = template("base.html")
    written = []

    articles = load_articles()

    for art in articles:
        if art["status"] == "forthcoming":
            continue
        meta_bits = display_date(art["date"])
        issue_display = " · %s" % html.escape(art["issue"]) if art["issue"] else ""
        if art["status"] == "draft":
            issue_display += " · Draft"
        page_content = render(
            template("article.html"),
            date_display=meta_bits,
            issue_display=issue_display,
            title=html.escape(art["title"], quote=False),
            draft_banner=DRAFT_BANNER if art["status"] == "draft" else "",
            body=art["body_html"],
        )
        page = render(
            base,
            title="%s · %s" % (art["title"], SITE_NAME),
            description=art["summary"] or SITE_TAGLINE,
            root="../",
            content=page_content,
        )
        out_path = ARTICLES_DIR / (art["slug"] + ".html")
        out_path.write_text(page, encoding="utf-8")
        written.append(out_path)

    prune_stale({p.name for p in written})

    items = []
    for art in articles:
        fc = art["status"] == "forthcoming"
        badge = (
            '<span class="badge-draft">Forthcoming</span>' if fc
            else '<span class="badge-draft">Draft</span>' if art["status"] == "draft"
            else ""
        )
        summary = (
            '\n<p class="summary">%s</p>'
            % _inline(html.escape(art["summary"], quote=False))
            if art["summary"]
            else ""
        )
        title_html = (
            html.escape(art["title"], quote=False) if fc
            else '<a href="articles/%s.html">%s</a>'
            % (art["slug"], html.escape(art["title"], quote=False))
        )
        if art["title"].lower().startswith("claim trace"):
            items.append(
                '<li class="companion">\n<span class="piece-title">%s%s</span>\n</li>'
                % (title_html, badge)
            )
        else:
            items.append(
                '<li>\n<span class="when">%s</span>\n'
                '<span class="piece-title">%s%s</span>%s\n</li>'
                % (display_date(art["date"]), title_html, badge, summary)
            )

    index_page = render(
        base,
        title="%s — seeing clearly after the feed" % SITE_NAME,
        description=SITE_TAGLINE,
        root="",
        content=render(template("index.html"), article_items="\n".join(items)),
    )
    index_path = ROOT / "index.html"
    index_path.write_text(index_page, encoding="utf-8")
    written.append(index_path)

    about_page = render(
        base,
        title="About · %s" % SITE_NAME,
        description="What Darshan is: the vow, the seven desks, and the editorial law.",
        root="",
        content=template("about.html"),
    )
    about_path = ROOT / "about.html"
    about_path.write_text(about_page, encoding="utf-8")
    written.append(about_path)

    failures = 0
    for path in written:
        errors = check_well_formed(path)
        rel = path.relative_to(ROOT)
        if errors:
            failures += 1
            print("FAIL  %s" % rel)
            for err in errors:
                print("      - %s" % err)
        else:
            print("ok    %s" % rel)

    print(
        "\n%d page(s) written, %d article(s), %d parse failure(s)."
        % (len(written), len(articles), failures)
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(build())
