from __future__ import annotations

import copy
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import observatory_lib  # noqa: E402
import build_observatory  # noqa: E402


def fresh_store() -> dict:
    return copy.deepcopy(observatory_lib.load_store())


def schema() -> dict:
    return observatory_lib.load_schema()


def errors_for(store: dict) -> list[str]:
    return observatory_lib.validate(store, schema())


class StoreContractTests(unittest.TestCase):
    def test_real_store_is_clean(self):
        errors = errors_for(fresh_store())
        self.assertEqual([], errors)

    def test_ids_are_unique_across_collections(self):
        store = fresh_store()
        dup = dict(store["sources"]["entries"][0])
        dup["id"] = store["companies"]["entries"][0]["id"]
        store["sources"]["entries"].append(dup)
        errors = errors_for(store)
        self.assertTrue(any("already used" in e for e in errors), errors)

    def test_every_source_reference_resolves(self):
        store = fresh_store()
        store["claims"]["entries"][0]["source_id"] = "src-does-not-exist"
        errors = errors_for(store)
        self.assertTrue(
            any("not in allowed collection" in e or "unresolved" in e for e in errors),
            errors,
        )

    def test_schema_field_must_match(self):
        store = fresh_store()
        store["evidence"]["schema"] = "darshan.qo-evidence/v99"
        errors = errors_for(store)
        self.assertTrue(any("wrong schema" in e for e in errors), errors)

    def test_missing_required_field_fails(self):
        store = fresh_store()
        del store["forecasts"]["entries"][0]["resolution_criteria"]
        errors = errors_for(store)
        self.assertTrue(any("resolution_criteria" in e for e in errors), errors)

    def test_unexpected_field_fails(self):
        store = fresh_store()
        store["companies"]["entries"][0]["hype_score"] = 9
        errors = errors_for(store)
        self.assertTrue(any("unexpected field" in e for e in errors), errors)


class AntiHypeTests(unittest.TestCase):
    """Negative fixtures: each of these mutations must make the store fail."""

    def test_independent_evidence_cannot_be_self_measured(self):
        store = fresh_store()
        ev = next(
            e for e in store["evidence"]["entries"]
            if e["evidence_class"] == "independent_testbed"
        )
        ev["measured_by_family"] = "self"
        errors = errors_for(store)
        self.assertTrue(any("self-measured" in e for e in errors), errors)

    def test_independent_evidence_needs_nonself_source_family(self):
        store = fresh_store()
        ev = next(
            e for e in store["evidence"]["entries"]
            if e["evidence_class"] == "independent_testbed"
        )
        # point it only at the subject's own press release
        ev["source_ids"] = ["src-qm-nqcc-delivery-2025-09-15"]
        errors = errors_for(store)
        self.assertTrue(any("non-self source" in e for e in errors), errors)

    def test_independence_flag_must_be_true_for_independent_class(self):
        store = fresh_store()
        ev = next(
            e for e in store["evidence"]["entries"]
            if e["evidence_class"] == "independent_testbed"
        )
        ev["independent_of_subject"] = False
        errors = errors_for(store)
        self.assertTrue(any("independent_of_subject" in e for e in errors), errors)

    def test_non_evidence_classes_cannot_appear_as_evidence(self):
        store = fresh_store()
        store["evidence"]["entries"][0]["evidence_class"] = "funding"
        errors = errors_for(store)
        self.assertTrue(errors, "funding must be rejected as an evidence class")

    def test_achieved_milestone_requires_evidence(self):
        store = fresh_store()
        achieved = next(
            m
            for m in store["milestones"]["entries"]
            if m["status"] in {"achieved", "achieved_late"}
            and m["kind"] in {"roadmap_promise", "program_deliverable"}
        )
        achieved["evidence_ids"] = []
        errors = errors_for(store)
        self.assertTrue(any("requires evidence" in e for e in errors), errors)

    def test_slipped_milestone_cannot_have_achieved_on(self):
        store = fresh_store()
        slipped = next(
            (m for m in store["milestones"]["entries"] if m["status"] == "slipped"), None
        )
        if slipped is None:
            self.skipTest("no slipped milestone in store")
        slipped["achieved_on"] = "2026-01-01"
        errors = errors_for(store)
        self.assertTrue(any("must not have achieved_on" in e for e in errors), errors)


class ForecastTests(unittest.TestCase):
    def test_resolved_forecast_requires_evidence(self):
        store = fresh_store()
        fc = store["forecasts"]["entries"][0]
        fc["status"] = "resolved_true"
        fc["resolved_on"] = "2026-09-01"
        fc["resolution_evidence_ids"] = []
        errors = errors_for(store)
        self.assertTrue(any("resolved without evidence" in e for e in errors), errors)

    def test_resolution_evidence_must_predate_resolved_on(self):
        store = fresh_store()
        fc = store["forecasts"]["entries"][0]
        fc["status"] = "resolved_true"
        fc["resolved_on"] = "2020-01-01"
        fc["resolution_evidence_ids"] = ["ev-qm-charge-noise-2024"]
        errors = errors_for(store)
        self.assertTrue(any("after resolved_on" in e for e in errors), errors)

    def test_forecast_without_resolution_criteria_fails(self):
        store = fresh_store()
        store["forecasts"]["entries"][0]["resolution_criteria"] = "  "
        errors = errors_for(store)
        self.assertTrue(any("resolution_criteria" in e for e in errors), errors)

    def test_open_forecast_cannot_have_resolved_on(self):
        store = fresh_store()
        fc = next(
            f for f in store["forecasts"]["entries"] if f["status"] == "open"
        )
        fc["resolved_on"] = "2026-01-01"
        errors = errors_for(store)
        self.assertTrue(any("open forecast" in e for e in errors), errors)


class TemporalTests(unittest.TestCase):
    def test_as_of_view_filters_by_recorded_on(self):
        store = fresh_store()
        snap = observatory_lib.as_of(store, "2026-09-18")
        self.assertEqual(0, len(snap["evidence"]["entries"]))
        full = observatory_lib.as_of(store, "9999-12-31")
        self.assertEqual(
            len(store["evidence"]["entries"]), len(full["evidence"]["entries"])
        )

    def test_snapshot_cannot_cite_future_evidence(self):
        store = fresh_store()
        entry = store["beliefs"]["snapshots"][0]["entries"][0]
        entry["basis_evidence_ids"] = ["ev-qm-nqcc-installed-2025"]
        errors = errors_for(store)
        self.assertTrue(any("future knowledge" in e for e in errors), errors)

    def test_snapshot_cannot_cite_unpublished_source(self):
        store = fresh_store()
        # ev-qm-charge-noise-2024 is dated 2024-07-19 (pre-cutoff) but if its
        # source were published later, citing it in 2024 still leaks.
        for s in store["sources"]["entries"]:
            if s["id"] == "src-qm-npjqi-2024-07-19":
                s["published"] = "2025-06-01"
        errors = errors_for(store)
        self.assertTrue(any("no source published by" in e for e in errors), errors)

    def test_recorded_on_cannot_postdate_file_watermark(self):
        store = fresh_store()
        store["claims"]["entries"][0]["recorded_on"] = "2999-01-01"
        errors = errors_for(store)
        self.assertTrue(any("after as_of" in e for e in errors), errors)


class RenderTests(unittest.TestCase):
    def test_chart_counts_equal_ledger(self):
        store = fresh_store()
        svg = build_observatory.evidence_ladder_svg(store)
        rendered = svg.count("<rect")
        total = len(store["evidence"]["entries"])
        self.assertEqual(total, rendered)

    def test_confidence_svg_renders_not_yet_estimable_empty(self):
        conf = {
            "axes": {
                "technical_architecture": {"kind": "range", "low": 0.4, "high": 0.7, "reason": "x"},
                "execution": {"kind": "range", "low": 0.5, "high": 0.8, "reason": "x"},
                "market_utility": {"kind": "not_yet_estimable", "reason": "x"},
                "value_capture": {"kind": "not_yet_estimable", "reason": "x"},
            }
        }
        svg = build_observatory.confidence_svg(conf)
        self.assertEqual(2, svg.count("NOT YET ESTIMABLE"))
        self.assertEqual(4, svg.count('fill="none"'))

    def test_build_is_deterministic(self):
        store = fresh_store()
        page1 = build_observatory.page_index(store)
        page2 = build_observatory.page_index(fresh_store())
        self.assertEqual(page1, page2)

    def test_build_fails_closed_on_corrupt_store(self):
        corrupt = fresh_store()
        del corrupt["sources"]["entries"][0]
        original_loader = observatory_lib.load_store
        original_out = build_observatory.OUTPUT_DIR
        try:
            observatory_lib.load_store = lambda data_dir=None: corrupt  # type: ignore[misc]
            with tempfile.TemporaryDirectory() as tmp:
                build_observatory.OUTPUT_DIR = Path(tmp)
                code = build_observatory.build()
                self.assertEqual(1, code)
                self.assertEqual([], list(Path(tmp).glob("*.html")))
        finally:
            observatory_lib.load_store = original_loader
            build_observatory.OUTPUT_DIR = original_out

    def test_all_pages_well_formed(self):
        output = observatory_lib.OUTPUT_DIR
        pages = sorted(output.glob("*.html"))
        self.assertGreaterEqual(len(pages), 12)
        for path in pages:
            errors = __import__("build_garden").check_well_formed(path)
            self.assertEqual([], errors, "%s: %s" % (path.name, errors))


if __name__ == "__main__":
    unittest.main()
