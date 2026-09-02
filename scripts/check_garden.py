#!/usr/bin/env python3
"""Check the Darshan garden's source and independent-verdict contract.

This is intentionally stricter than the renderer. ``build_garden.py`` must be
able to publish a useful partial garden; this command answers a different
question: is the canonical 55-room first planting complete and reviewable?
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

import build_garden


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "garden_src"
VERDICT_DIR = SOURCE_DIR / "_verdicts"
VISUAL_VERDICT_DIR = ROOT / "garden_visuals" / "_verdicts"
VISUAL_VERDICT_SCHEMA = "darshan.visual-verdict-series/v1"

CLAUDE_AUTHORSHIP = (
    "*Written by Claude (Fable 5), an AI, for the Darshan garden. "
    "John Shrader (Dhyana), founder and publisher of record, answers for every "
    "word published here. Errors are corrected on the face of the page, dated.*"
)
CODEX_AUTHORSHIP = (
    "*Written by Codex, an AI, for the Darshan garden, completing Claude Fable 5’s "
    "interrupted first planting. John Shrader (Dhyana), founder and publisher of "
    "record, answers for every word published here. Errors are corrected on the "
    "face of the page, dated.*"
)
CODEX_AUTHORED_SLUGS = frozenset(
    {
        "mahavideha-kshetra",
        "taiwan",
        "elon-musk",
        "blockchain",
        "attention-economy",
        "futurism",
        "trends-gap",
    }
)
SILICON_AUTHORSHIP = (
    "*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. "
    "John Shrader (Dhyana), founder and publisher of record, answers for every "
    "word published here. Errors are corrected on the face of the page, dated.*"
)
# Plantings after the first carry their own date and authorship, keyed by series slug.
SERIES_PLANTINGS = {
    "silicon": {"date": "2026-09-02", "authorship": SILICON_AUTHORSHIP},
}
# Closed evidence schema: the seventh field binds a review to exact source bytes.
VERDICT_REQUIRED_KEYS = {
    "slug",
    "verdict",
    "contract",
    "facts",
    "voice",
    "must_fix",
    "source_sha256",
}
VISUAL_SERIES_VERDICT_KEYS = {
    "schema",
    "series",
    "reviewer",
    "reviewed_at",
    "rooms",
}
VISUAL_ROOM_VERDICT_KEYS = {
    "verdict",
    "visual_sha256",
    "source_sha256",
    "evidence",
    "facts",
    "uncertainty",
    "must_fix",
}


def canonical_json_sha256(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_raw_visual_entries() -> tuple[dict[str, dict[str, object]], list[str]]:
    entries: dict[str, dict[str, object]] = {}
    issues: list[str] = []
    for series_slug, _, expected_rooms in build_garden.SERIES:
        path = build_garden.VISUAL_SPECS_DIR / f"{series_slug}.json"
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            issues.append(f"{series_slug}: cannot load visual manifest: {exc}")
            continue
        rooms = data.get("rooms") if isinstance(data, dict) else None
        if not isinstance(rooms, dict):
            issues.append(f"{series_slug}: visual manifest rooms must be an object")
            continue
        expected_set = set(expected_rooms)
        actual_set = set(rooms)
        if actual_set != expected_set:
            issues.append(
                f"{series_slug}: visual manifest room set differs from canonical series"
            )
        for slug in expected_set & actual_set:
            entry = rooms[slug]
            if isinstance(entry, dict):
                entries[slug] = entry
            else:
                issues.append(f"{slug}: visual room entry must be an object")
    return entries, issues


def validate_visual_verdicts(
    visual_entries: dict[str, dict[str, object]],
    source_paths: dict[str, Path],
) -> tuple[dict[str, int], list[str]]:
    counts = {"PASS": 0, "FIX": 0, "missing": 0, "invalid": 0}
    issues: list[str] = []
    expected_series = {series_slug for series_slug, _, _ in build_garden.SERIES}
    actual_series = {
        path.stem for path in VISUAL_VERDICT_DIR.glob("*.json")
    } if VISUAL_VERDICT_DIR.is_dir() else set()
    for extra in sorted(actual_series - expected_series):
        counts["invalid"] += 1
        issues.append(f"visual verdict has unexpected series file: {extra}.json")

    for series_slug, _, room_slugs in build_garden.SERIES:
        path = VISUAL_VERDICT_DIR / f"{series_slug}.json"
        if not path.is_file():
            counts["missing"] += len(room_slugs)
            issues.append(f"{series_slug}: missing independent visual verdict set")
            continue
        try:
            verdict_set = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            counts["invalid"] += len(room_slugs)
            issues.append(f"{series_slug}: invalid visual verdict JSON: {exc}")
            continue
        if not isinstance(verdict_set, dict):
            counts["invalid"] += len(room_slugs)
            issues.append(f"{series_slug}: visual verdict set must be an object")
            continue
        local_issues: list[str] = []
        missing_keys = sorted(VISUAL_SERIES_VERDICT_KEYS - set(verdict_set))
        extra_keys = sorted(set(verdict_set) - VISUAL_SERIES_VERDICT_KEYS)
        if missing_keys:
            local_issues.append(f"missing keys: {', '.join(missing_keys)}")
        if extra_keys:
            local_issues.append(f"unexpected keys: {', '.join(extra_keys)}")
        if verdict_set.get("schema") != VISUAL_VERDICT_SCHEMA:
            local_issues.append("wrong schema")
        if verdict_set.get("series") != series_slug:
            local_issues.append("series does not match filename")
        reviewer = verdict_set.get("reviewer")
        if not isinstance(reviewer, str) or not reviewer.strip():
            local_issues.append("reviewer must be nonempty text")
        reviewed_at = verdict_set.get("reviewed_at")
        if not isinstance(reviewed_at, str):
            local_issues.append("reviewed_at must be an ISO date")
        else:
            try:
                date.fromisoformat(reviewed_at)
            except ValueError:
                local_issues.append("reviewed_at must be an ISO date")
        room_verdicts = verdict_set.get("rooms")
        if not isinstance(room_verdicts, dict):
            local_issues.append("rooms must be an object")
            room_verdicts = {}
        expected_rooms = set(room_slugs)
        if set(room_verdicts) != expected_rooms:
            local_issues.append("room verdict set differs from canonical series")
        if local_issues:
            counts["invalid"] += len(room_slugs)
            issues.extend(f"{series_slug}: {issue}" for issue in local_issues)
            continue

        for slug in room_slugs:
            verdict = room_verdicts[slug]
            room_issues: list[str] = []
            if not isinstance(verdict, dict):
                room_issues.append("room verdict must be an object")
                verdict = {}
            missing_room_keys = sorted(VISUAL_ROOM_VERDICT_KEYS - set(verdict))
            extra_room_keys = sorted(set(verdict) - VISUAL_ROOM_VERDICT_KEYS)
            if missing_room_keys:
                room_issues.append(f"missing keys: {', '.join(missing_room_keys)}")
            if extra_room_keys:
                room_issues.append(f"unexpected keys: {', '.join(extra_room_keys)}")
            result = verdict.get("verdict")
            if result not in {"PASS", "FIX"}:
                room_issues.append(f"invalid verdict value {result!r}")
            for key in ("evidence", "facts", "uncertainty", "must_fix"):
                value = verdict.get(key)
                if not isinstance(value, str) or not value.strip():
                    room_issues.append(f"{key} must be nonempty text")
            must_fix = verdict.get("must_fix", "")
            if isinstance(must_fix, str):
                if result == "PASS" and not re.match(
                    r"^none\b", must_fix, flags=re.IGNORECASE
                ):
                    room_issues.append("PASS verdict still names a required fix")
                if result == "FIX" and re.match(
                    r"^none\b", must_fix, flags=re.IGNORECASE
                ):
                    room_issues.append("FIX verdict does not name a required fix")
            visual_sha = verdict.get("visual_sha256")
            expected_visual = visual_entries.get(slug)
            if not isinstance(visual_sha, str) or not re.fullmatch(
                r"[0-9a-f]{64}", visual_sha
            ):
                room_issues.append("visual_sha256 must be 64 lowercase hex characters")
            elif expected_visual is None:
                room_issues.append("cannot bind missing visual room entry")
            elif visual_sha != canonical_json_sha256(expected_visual):
                room_issues.append("visual_sha256 does not match visual entry")
            source_sha = verdict.get("source_sha256")
            source_path = source_paths.get(slug)
            if not isinstance(source_sha, str) or not re.fullmatch(
                r"[0-9a-f]{64}", source_sha
            ):
                room_issues.append("source_sha256 must be 64 lowercase hex characters")
            elif source_path is None:
                room_issues.append("cannot bind missing room source")
            elif source_sha != hashlib.sha256(source_path.read_bytes()).hexdigest():
                room_issues.append("source_sha256 does not match room source")

            if room_issues:
                counts["invalid"] += 1
                issues.extend(f"{slug}: visual verdict {issue}" for issue in room_issues)
                continue
            counts[str(result)] += 1
            if result == "FIX":
                issues.append(f"{slug}: independent visual verdict remains FIX")
    return counts, issues


def word_count(body: str) -> int:
    # Bibliographies are evidence, not article prose. The workflow's writer
    # reports counted through the final prose section and excluded Sources.
    prose = re.split(r"^##\s+(?:\d+\.\s*)?Sources\s*$", body, 1, flags=re.MULTILINE | re.IGNORECASE)[0]
    return len(re.findall(r"\b[\w’'-]+\b", prose, flags=re.UNICODE))


def has_markdown_table(body: str) -> bool:
    lines = body.splitlines()
    return any(
        "|" in lines[index]
        and index + 1 < len(lines)
        and build_garden._is_table_separator(lines[index + 1].strip())
        for index in range(len(lines))
    )


def expected_authorship_footer(slug: str) -> str:
    series_slug = next(
        (series for series, _, rooms in build_garden.SERIES if slug in rooms), None
    )
    planting = SERIES_PLANTINGS.get(series_slug or "")
    if planting:
        return planting["authorship"]
    return CODEX_AUTHORSHIP if slug in CODEX_AUTHORED_SLUGS else CLAUDE_AUTHORSHIP


def validate_verdict(
    slug: str, verdict: object, source_path: Path | None
) -> tuple[str | None, list[str]]:
    """Validate one verdict completely before it can contribute PASS or FIX."""
    issues: list[str] = []
    if not isinstance(verdict, dict):
        return None, [f"{slug}: verdict must be a JSON object"]

    missing_keys = sorted(VERDICT_REQUIRED_KEYS - set(verdict))
    extra_keys = sorted(set(verdict) - VERDICT_REQUIRED_KEYS)
    if missing_keys:
        issues.append(
            f"{slug}: verdict missing required keys: {', '.join(missing_keys)}"
        )
    if extra_keys:
        issues.append(f"{slug}: verdict has unexpected keys: {', '.join(extra_keys)}")

    if verdict.get("slug") != slug:
        issues.append(f"{slug}: verdict slug is {verdict.get('slug')!r}")

    result = verdict.get("verdict")
    if not isinstance(result, str) or result not in {"PASS", "FIX"}:
        issues.append(f"{slug}: invalid verdict value {result!r}")

    for key in ("contract", "facts", "voice", "must_fix"):
        if not isinstance(verdict.get(key), str) or not verdict[key].strip():
            issues.append(f"{slug}: verdict missing non-empty {key!r}")

    must_fix = verdict.get("must_fix", "")
    if isinstance(must_fix, str):
        if result == "PASS" and not re.match(
            r"^none\b", must_fix, flags=re.IGNORECASE
        ):
            issues.append(f"{slug}: PASS verdict still names a required fix")
        if result == "FIX" and re.match(
            r"^none\b", must_fix, flags=re.IGNORECASE
        ):
            issues.append(f"{slug}: FIX verdict does not name a required fix")

    source_sha256 = verdict.get("source_sha256")
    digest_well_formed = isinstance(source_sha256, str) and bool(
        re.fullmatch(r"[0-9a-f]{64}", source_sha256)
    )
    if source_sha256 is not None and not digest_well_formed:
        issues.append(
            f"{slug}: verdict source_sha256 must be 64 lowercase hex characters"
        )

    if source_path is None:
        issues.append(f"{slug}: cannot validate verdict digest: room source is missing")
    else:
        try:
            source_bytes = source_path.read_bytes()
        except OSError as exc:
            issues.append(f"{slug}: cannot read room source for verdict digest: {exc}")
        else:
            if digest_well_formed:
                expected_sha256 = hashlib.sha256(source_bytes).hexdigest()
                if source_sha256 != expected_sha256:
                    issues.append(
                        f"{slug}: verdict source_sha256 does not match the reviewed source bytes"
                    )

    return (result if isinstance(result, str) and not issues else None), issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-verdicts",
        action="store_true",
        help="check source contracts without requiring independent verdict files",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    link_graph: dict[str, set[str]] = {}
    found = {path.stem: path for path in SOURCE_DIR.glob("*.md")}

    missing = sorted(build_garden.EXPECTED_SLUGS - set(found))
    extra = sorted(set(found) - build_garden.EXPECTED_SLUGS)
    if missing:
        errors.append("missing room sources: " + ", ".join(missing))
    if extra:
        errors.append("unexpected room sources: " + ", ".join(extra))

    for slug in sorted(build_garden.EXPECTED_SLUGS & set(found)):
        path = found[slug]
        try:
            meta, body = build_garden.parse_front_matter(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{slug}: cannot parse source: {exc}")
            continue

        missing_keys = sorted(build_garden.REQUIRED_META - set(meta))
        extra_keys = sorted(set(meta) - build_garden.REQUIRED_META)
        if missing_keys:
            errors.append(f"{slug}: missing front-matter keys: {', '.join(missing_keys)}")
        if extra_keys:
            errors.append(f"{slug}: extra front-matter keys: {', '.join(extra_keys)}")
        if meta.get("slug") != slug:
            errors.append(f"{slug}: front-matter slug is {meta.get('slug')!r}")

        expected_series = next(
            series_slug
            for series_slug, _, room_slugs in build_garden.SERIES
            if slug in room_slugs
        )
        if meta.get("series") != expected_series:
            errors.append(
                f"{slug}: series is {meta.get('series')!r}; expected {expected_series!r}"
            )
        if meta.get("status", "").lower() != "draft":
            errors.append(f"{slug}: first-planting status must remain draft")
        planting_date = SERIES_PLANTINGS.get(expected_series, {}).get("date", "2026-08-25")
        if meta.get("date") != planting_date:
            errors.append(f"{slug}: date must be exactly {planting_date}")
        for key in ("title", "summary", "tags", "terms_defined"):
            if not meta.get(key, "").strip():
                errors.append(f"{slug}: {key} must be non-empty")
        tags = meta.get("tags", "")
        if tags != tags.lower():
            errors.append(f"{slug}: tags must be lowercase")

        count = word_count(body)
        if not 2500 <= count <= 4500:
            errors.append(f"{slug}: {count} body words; contract requires 2500–4500")

        headings = re.findall(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE)
        if len(headings) < 4:
            errors.append(f"{slug}: only {len(headings)} H2 sections")
        normalized = {
            re.sub(r"^\d+\.\s*", "", heading.lower().strip()) for heading in headings
        }
        conclusion_markers = (
            "conclusion",
            "what you can",
            "what the reader can",
            "where this leaves",
            "holding a forecast",
            "the arc, and where it points",
            "where the room opens out",
        )
        if not any(marker in heading for heading in normalized for marker in conclusion_markers):
            errors.append(f"{slug}: missing a recognizable conclusion movement")
        if not any("open questions" in heading for heading in normalized):
            errors.append(f"{slug}: missing an Open questions section")
        if "sources" not in normalized:
            errors.append(f"{slug}: missing a Sources section")
        if not has_markdown_table(body):
            errors.append(f"{slug}: no Markdown comparison table")
        if not re.search(
            r"worked example|walkthrough|try it|verify (?:it|this)|step by step|"
            r"check (?:it|this|yourself)|you can check|by hand|run it yourself|"
            r"whole trip in one command",
            body,
            flags=re.IGNORECASE,
        ):
            errors.append(f"{slug}: no worked-example or walkthrough marker")

        nonempty_body_lines = [line.strip() for line in body.splitlines() if line.strip()]
        footer_lines = [
            line.strip()
            for line in body.splitlines()
            if line.strip().startswith("*Written by ")
        ]
        expected_footer = expected_authorship_footer(slug)
        if (
            footer_lines != [expected_footer]
            or not nonempty_body_lines
            or nonempty_body_lines[-1] != expected_footer
        ):
            author = "Codex" if slug in CODEX_AUTHORED_SLUGS else "Claude (Fable 5)"
            errors.append(
                f"{slug}: authorship footer must appear exactly once at the end and identify {author}"
            )

        terms_linked_values = [
            value.strip()
            for value in meta.get("terms_linked", "").split(",")
            if value.strip()
        ]
        terms_linked = set(terms_linked_values)
        if len(terms_linked_values) != len(terms_linked):
            duplicates = sorted(
                value for value in terms_linked if terms_linked_values.count(value) > 1
            )
            errors.append(f"{slug}: duplicate terms_linked: {', '.join(duplicates)}")
        if slug in terms_linked:
            errors.append(f"{slug}: terms_linked must not link a room to itself")
        unknown_terms = sorted(terms_linked - build_garden.EXPECTED_SLUGS)
        if unknown_terms:
            errors.append(f"{slug}: unknown terms_linked: {', '.join(unknown_terms)}")
        targets = {
            target
            for _, href in build_garden.iter_markdown_links(body)
            if (target := build_garden._local_room_slug(href)) is not None
        }
        unlinked_terms = sorted(terms_linked - targets)
        if unlinked_terms:
            errors.append(
                f"{slug}: terms_linked absent from body links: {', '.join(unlinked_terms)}"
            )

        link_graph[slug] = targets
        unknown_targets = sorted(targets - build_garden.EXPECTED_SLUGS)
        if unknown_targets:
            errors.append(f"{slug}: internal links target unknown rooms: {', '.join(unknown_targets)}")
        undeclared_targets = sorted(targets - terms_linked)
        if undeclared_targets:
            errors.append(
                f"{slug}: body room links absent from terms_linked: {', '.join(undeclared_targets)}"
            )

    present_canonical = build_garden.EXPECTED_SLUGS & set(found)
    inbound = {slug: 0 for slug in present_canonical}
    undirected = {slug: set() for slug in present_canonical}
    for source, targets in link_graph.items():
        for target in targets & present_canonical:
            if target != source:
                inbound[target] += 1
                undirected[source].add(target)
                undirected[target].add(source)
    orphans = sorted(slug for slug, count in inbound.items() if count == 0)
    if orphans:
        errors.append("rooms with no inbound corridor: " + ", ".join(orphans))
    if undirected:
        start = next(iter(undirected))
        visited = {start}
        frontier = [start]
        while frontier:
            current = frontier.pop()
            unseen = undirected[current] - visited
            visited.update(unseen)
            frontier.extend(unseen)
        disconnected = sorted(set(undirected) - visited)
        if disconnected:
            errors.append("rooms outside the connected garden graph: " + ", ".join(disconnected))

    verdict_counts = {"PASS": 0, "FIX": 0, "missing": 0, "invalid": 0}
    visual_verdict_counts = {"PASS": 0, "FIX": 0, "missing": 0, "invalid": 0}
    if not args.skip_verdicts:
        for slug in sorted(build_garden.EXPECTED_SLUGS):
            path = VERDICT_DIR / f"{slug}.json"
            if not path.exists():
                verdict_counts["missing"] += 1
                errors.append(f"{slug}: missing independent verdict")
                continue
            try:
                verdict = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                verdict_counts["invalid"] += 1
                errors.append(f"{slug}: invalid verdict JSON: {exc}")
                continue
            result, verdict_errors = validate_verdict(slug, verdict, found.get(slug))
            if verdict_errors:
                verdict_counts["invalid"] += 1
                errors.extend(verdict_errors)
                continue
            if result is None:  # Defensive: validate_verdict guarantees this pairing.
                verdict_counts["invalid"] += 1
                errors.append(f"{slug}: verdict validation returned no result")
                continue
            verdict_counts[result] += 1
            if result == "FIX":
                errors.append(f"{slug}: independent verdict remains FIX")

        visual_entries, visual_entry_errors = load_raw_visual_entries()
        errors.extend(visual_entry_errors)
        loaded_rooms, visual_source_errors = build_garden.load_rooms()
        errors.extend(f"visual catalog source: {item}" for item in visual_source_errors)
        visual_catalog_errors: list[str] = []
        if not visual_source_errors:
            _, visual_catalog_errors = build_garden.load_visual_catalog(
                {room["slug"]: room for room in loaded_rooms}
            )
        errors.extend(f"visual catalog: {item}" for item in visual_catalog_errors)
        visual_verdict_counts, visual_verdict_errors = validate_visual_verdicts(
            visual_entries, found
        )
        errors.extend(visual_verdict_errors)

    for item in errors:
        print("ERROR " + item)
    for item in warnings:
        print("WARN  " + item)
    print(
        "\n%d/%d room sources present; %d directed room corridors; "
        "room verdicts PASS=%d FIX=%d missing=%d invalid=%d; "
        "visual verdicts PASS=%d FIX=%d missing=%d invalid=%d; "
        "%d error(s), %d warning(s)."
        % (
            len(present_canonical),
            len(build_garden.EXPECTED_SLUGS),
            sum(inbound.values()),
            verdict_counts["PASS"],
            verdict_counts["FIX"],
            verdict_counts["missing"],
            verdict_counts["invalid"],
            visual_verdict_counts["PASS"],
            visual_verdict_counts["FIX"],
            visual_verdict_counts["missing"],
            visual_verdict_counts["invalid"],
            len(errors),
            len(warnings),
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
