from __future__ import annotations

import importlib.util
import sys
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


build = load_module("darshan_build_test", ROOT / "scripts" / "build.py")


class MarkdownRenderingTests(unittest.TestCase):
    def test_only_fully_labelled_lists_become_field_lists(self):
        labelled = build.md_to_html("- **Agent.** A lab\n- **Control.** A veto")
        mixed = build.md_to_html("- **Agent.** A lab\n- ordinary item")
        plain = build.md_to_html("- first\n- second")

        self.assertIn('<ul class="fields">', labelled)
        self.assertNotIn('class="fields"', mixed)
        self.assertNotIn('class="fields"', plain)

    def test_heading_ids_are_unique_and_unicode_stable(self):
        body = (
            "<h2>Same</h2><h2>Same</h2>"
            "<h3>食い違う</h3><h4>Card name</h4>"
        )
        rendered, _ = build.add_heading_ids_and_toc(
            body, min_headings=99, min_words=99
        )

        self.assertIn('id="same"', rendered)
        self.assertIn('id="same-2"', rendered)
        self.assertIn('id="食い違う"', rendered)
        self.assertIn('id="card-name"', rendered)

    def test_long_labelled_piece_gets_closed_contents_disclosure(self):
        headings = "".join("<h2>Section %d</h2>" % i for i in range(8))
        body = headings + "<p>%s</p>" % ("word " * 100)
        rendered, toc = build.add_heading_ids_and_toc(
            body, min_headings=8, min_words=50
        )

        self.assertIn("<details", toc)
        self.assertNotIn("<details open", toc)
        self.assertIn("8 sections", toc)
        self.assertIn('href="#section-0"', toc)
        self.assertIn('id="section-0"', rendered)

    def test_sentence_headings_do_not_generate_noisy_contents(self):
        sentence = (
            "This is a full-sentence finding whose length makes it a poor "
            "navigation label for a contents disclosure"
        )
        body = "".join("<h2>%s %d</h2>" % (sentence, i) for i in range(8))
        body += "<p>%s</p>" % ("word " * 100)

        rendered, toc = build.add_heading_ids_and_toc(
            body, min_headings=8, min_words=50, max_median_label=60
        )

        self.assertEqual("", toc)
        self.assertIn('id="this-is-a-full-sentence-finding', rendered)

    def test_contents_follows_opening_authorship_note(self):
        body = "<p>Written by an AI.</p>\n<hr>\n<p>Opening argument.</p>"
        result = build.insert_toc(body, "<details>Contents</details>")

        self.assertLess(result.index("Written by"), result.index("<details>"))
        self.assertLess(result.index("<details>"), result.index("Opening argument"))

    def test_disclosed_authorship_note_gets_secondary_byline_role(self):
        body = "<p><em>Written by an AI under operator authority.</em></p>"
        rendered = build.decorate_article_body(body)

        self.assertIn('class="byline"', rendered)

    def test_table_is_keyboard_scrollable_region(self):
        rendered = build.md_to_html(
            "| Name | Value |\n|---|---|\n| Long row | **7.0** |"
        )

        self.assertIn('class="table-wrap"', rendered)
        self.assertIn('class="cols-2"', rendered)
        self.assertIn('role="region"', rendered)
        self.assertIn('tabindex="0"', rendered)
        self.assertIn("<strong>7.0</strong>", rendered)


if __name__ == "__main__":
    unittest.main()
