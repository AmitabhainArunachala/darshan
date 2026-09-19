#!/usr/bin/env python3
"""Quantum Observatory store: loading, validation, and as-of views.

Shared by ``build_observatory.py`` (render) and ``check_observatory.py``
(verify). Everything here is stdlib-only and deterministic — no wall clock is
consulted anywhere; the store's own ``as_of`` is the only "now".

Two clocks (see observatory_src/DESIGN.md):
  * ``recorded_on`` — transaction time: when the entry entered the ledger.
  * domain dates — when the fact is true in the world.

``as_of(store, date)`` returns the store as it stood on that date: entries with
``recorded_on`` later than the date are invisible. Hindcast snapshots are built
on top of that view, so leakage is impossible by construction — and the
validator proves it anyway.
"""

from __future__ import annotations

import calendar
import json
import re
from datetime import date as _date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "observatory_src"
DATA_DIR = SRC_DIR / "data"
SCHEMA_DIR = SRC_DIR / "schema"
PAGES_DIR = SRC_DIR / "pages"
OUTPUT_DIR = ROOT / "observatory"

EVIDENCE_LADDER = [
    "company_claim",
    "technical_disclosure",
    "peer_review",
    "independent_benchmark",
    "independent_testbed",
    "replication",
    "system_utility",
]
LADDER_RANK = {name: i for i, name in enumerate(EVIDENCE_LADDER)}
INDEPENDENT_CLASSES = {
    "independent_benchmark",
    "independent_testbed",
    "replication",
    "system_utility",
}
NON_EVIDENCE_CLASSES = {"funding", "selection", "procurement", "partnership", "roadmap"}

# Cross-cutting sentinel: a forecast or bottleneck may concern the whole field.
MULTI_SENTINEL = "arch-multiple"
OPERATOR_SENTINEL = "ce-operator"

ID_RE = re.compile(r"^[a-z][a-z0-9-]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MONTH_RE = re.compile(r"^\d{4}-\d{2}$")


def _is_date(value: object) -> bool:
    if not isinstance(value, str) or not DATE_RE.match(value):
        return False
    try:
        _date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _is_month(value: object) -> bool:
    return isinstance(value, str) and MONTH_RE.match(value) is not None


def _is_dateish(value: object) -> bool:
    return _is_date(value) or _is_month(value) or value == "UNKNOWN"


def _check_field(errors: list[str], where: str, spec: dict, value: object) -> None:
    ftype = spec.get("type", "str")
    if value is None:
        # present-null is legal only for nullable_date and any
        if ftype not in {"nullable_date", "any"} and spec.get("required", False):
            errors.append(f"{where}: missing required field")
        return
    if ftype == "str" and not isinstance(value, str):
        errors.append(f"{where}: expected string, got {type(value).__name__}")
    elif ftype == "id":
        if not isinstance(value, str) or not ID_RE.match(value):
            errors.append(f"{where}: bad id {value!r}")
    elif ftype == "date" and not _is_date(value):
        errors.append(f"{where}: not an ISO date: {value!r}")
    elif ftype == "month" and not _is_month(value):
        errors.append(f"{where}: not an ISO month: {value!r}")
    elif ftype == "nullable_date" and value is not None and not _is_date(value):
        errors.append(f"{where}: not a date or null: {value!r}")
    elif ftype == "number" and not isinstance(value, (int, float)):
        errors.append(f"{where}: not a number: {value!r}")
    elif ftype == "bool" and not isinstance(value, bool):
        errors.append(f"{where}: not a boolean: {value!r}")
    elif ftype == "enum":
        if value not in spec.get("values", []):
            errors.append(f"{where}: {value!r} not in {spec.get('values')}")
    elif ftype == "list_str":
        if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
            errors.append(f"{where}: expected list of strings")
    elif ftype == "list_id":
        if not isinstance(value, list) or not all(
            isinstance(x, str) and (ID_RE.match(x) or x in {"UNKNOWN", MULTI_SENTINEL}) for x in value
        ):
            errors.append(f"{where}: expected list of ids")
    elif ftype == "list_obj":
        if not isinstance(value, list) or not all(isinstance(x, dict) for x in value):
            errors.append(f"{where}: expected list of objects")
    elif ftype == "obj" and not isinstance(value, dict):
        errors.append(f"{where}: expected object")
    elif ftype == "any":
        pass


def _validate_entry(
    errors: list[str], collection: str, entry: object, fields: dict
) -> None:
    where = f"{collection}.{entry.get('id', '?') if isinstance(entry, dict) else '?'}"
    if not isinstance(entry, dict):
        errors.append(f"{collection}: entry is not an object")
        return
    for name, spec in fields.items():
        value = entry.get(name)
        if value is None and spec.get("required", False) and spec.get("type") not in {"nullable_date", "any"}:
            errors.append(f"{where}: missing required field '{name}'")
            continue
        _check_field(errors, f"{where}.{name}", spec, value)
    # Unknown keys are allowed only as explicit 'note'/'label' additions.
    for key in sorted(set(entry) - set(fields)):
        errors.append(f"{where}: unexpected field '{key}'")


def load_store(data_dir: Path | None = None) -> dict:
    """Load every ledger file. Returns {collection: {...}, 'graph': ..., 'beliefs': ...}."""
    data_dir = data_dir or DATA_DIR
    store: dict = {}
    for path in sorted(data_dir.glob("*.json")):
        store[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return store


def load_schema(schema_dir: Path | None = None) -> dict:
    schema_dir = schema_dir or SCHEMA_DIR
    return json.loads((schema_dir / "collections.json").read_text(encoding="utf-8"))


def _entries(store: dict, collection: str) -> list[dict]:
    doc = store.get(collection, {})
    return doc.get("entries", []) if isinstance(doc, dict) else []


def all_ids(store: dict) -> dict[str, str]:
    """Map every declared id -> collection it lives in."""
    index: dict[str, str] = {}
    collections = [
        "sources", "institutions", "capabilities", "architectures",
        "companies", "claims", "evidence", "milestones", "forecasts",
        "bottlenecks", "questions", "confidence",
    ]
    for coll in collections:
        for entry in _entries(store, coll):
            if isinstance(entry, dict) and "id" in entry:
                index[entry["id"]] = coll
    graph = store.get("graph", {})
    for node in graph.get("nodes", []):
        index[node["id"]] = "graph_nodes"
        if node.get("ref_id"):
            index.setdefault(node["ref_id"], f"graph_ref({node['kind']})")
    for snap in store.get("beliefs", {}).get("snapshots", []):
        for entry in snap.get("entries", []):
            index[entry["id"]] = "beliefs"
    index[MULTI_SENTINEL] = "sentinel"
    index[OPERATOR_SENTINEL] = "sentinel"
    index["UNKNOWN"] = "sentinel"
    return index


def as_of(store: dict, cutoff: str) -> dict:
    """Store as it stood on ``cutoff``: drop entries recorded later."""
    out: dict = {}
    for name, doc in store.items():
        if not isinstance(doc, dict):
            out[name] = doc
            continue
        if "entries" in doc:
            kept = [
                e for e in doc["entries"]
                if not isinstance(e, dict) or e.get("recorded_on", "9999") <= cutoff
            ]
            out[name] = {**doc, "entries": kept, "as_of": cutoff}
        elif name == "beliefs":
            kept_snaps = [s for s in doc.get("snapshots", []) if s.get("as_of", "9999") <= cutoff]
            out[name] = {**doc, "snapshots": kept_snaps, "as_of": cutoff}
        else:
            out[name] = {**doc, "as_of": cutoff}
    return out


def store_as_of(store: dict) -> str:
    """The store's own 'now': max recorded_on across entries."""
    latest = "0000-00-00"
    for doc in store.values():
        if not isinstance(doc, dict):
            continue
        for entry in doc.get("entries", []):
            if isinstance(entry, dict):
                r = entry.get("recorded_on")
                if isinstance(r, str) and _is_date(r) and r > latest:
                    latest = r
        for snap in doc.get("snapshots", []):
            for entry in snap.get("entries", []):
                r = snap.get("as_of")
                if isinstance(r, str) and _is_date(r) and r > latest:
                    pass  # snapshots are views, not transaction time
    # fall back to each file's declared as_of if no recorded_on exists
    if latest == "0000-00-00":
        for doc in store.values():
            if isinstance(doc, dict):
                a = doc.get("as_of")
                if isinstance(a, str) and _is_date(a) and a > latest:
                    latest = a
    return latest


def validate(store: dict, schema: dict, *, build_as_of: str | None = None) -> list[str]:
    """Validate the whole store. Returns a list of issues; empty means clean.

    Fail closed: every rule violation is an error, and any error means the
    builder must not emit output.
    """
    errors: list[str] = []
    collections_spec = schema["collections"]

    # 1. Structural schema validation per collection file.
    for name, spec in collections_spec.items():
        doc = store.get(name)
        if doc is None:
            errors.append(f"missing data file for collection '{name}'")
            continue
        if doc.get("schema") != spec["schema_field"]:
            errors.append(f"{name}: wrong schema tag {doc.get('schema')!r}")
        entries = doc.get("entries")
        if not isinstance(entries, list):
            errors.append(f"{name}: 'entries' must be a list")
            continue
        for entry in entries:
            _validate_entry(errors, name, entry, spec["fields"])

    # graph + beliefs have bespoke shapes
    graph = store.get("graph", {})
    if graph.get("schema") != schema["graph"]["schema_field"]:
        errors.append("graph: wrong schema tag")
    node_ids: set[str] = set()
    for node in graph.get("nodes", []):
        _validate_entry(errors, "graph.nodes", node, schema["graph"]["node_fields"])
        if isinstance(node, dict) and node.get("id"):
            if node["id"] in node_ids:
                errors.append(f"graph.nodes.{node['id']}: duplicate id")
            node_ids.add(node["id"])
    edge_ids: set[str] = set()
    for edge in graph.get("edges", []):
        _validate_entry(errors, "graph.edges", edge, schema["graph"]["edge_fields"])
        if isinstance(edge, dict):
            if edge.get("id") in edge_ids:
                errors.append(f"graph.edges.{edge.get('id')}: duplicate id")
            edge_ids.add(edge.get("id"))
            for key in ("from", "to"):
                if edge.get(key) not in node_ids:
                    errors.append(f"graph.edges.{edge.get('id')}: '{key}' references missing node {edge.get(key)!r}")

    beliefs = store.get("beliefs", {})
    if beliefs.get("schema") != schema["beliefs"]["schema_field"]:
        errors.append("beliefs: wrong schema tag")
    for snap in beliefs.get("snapshots", []):
        if not _is_date(snap.get("as_of")):
            errors.append(f"beliefs snapshot: bad as_of {snap.get('as_of')!r}")
        for entry in snap.get("entries", []):
            _validate_entry(errors, f"beliefs.{snap.get('as_of')}", entry, schema["beliefs"]["entry_fields"])

    # 2. Unique ids globally.
    seen: dict[str, str] = {}
    for name in collections_spec:
        for entry in _entries(store, name):
            if isinstance(entry, dict) and isinstance(entry.get("id"), str):
                if entry["id"] in seen:
                    errors.append(f"{name}.{entry['id']}: id already used in {seen[entry['id']]}")
                seen[entry["id"]] = name

    ids = all_ids(store)
    source_ids = {e["id"] for e in _entries(store, "sources")}
    sources_by_id = {e["id"]: e for e in _entries(store, "sources")}
    company_ids = {e["id"] for e in _entries(store, "companies")}
    evidence_ids = {e["id"] for e in _entries(store, "evidence")}
    evidence_by_id = {e["id"]: e for e in _entries(store, "evidence")}
    claim_ids = {e["id"] for e in _entries(store, "claims")}
    milestone_ids = {e["id"] for e in _entries(store, "milestones")}
    arch_ids = {e["id"] for e in _entries(store, "architectures")}
    cap_ids = {e["id"] for e in _entries(store, "capabilities")}
    inst_ids = {e["id"] for e in _entries(store, "institutions")}

    def need(cond: bool, msg: str) -> None:
        if not cond:
            errors.append(msg)

    # 3. Citation resolution — every source reference must exist.
    def check_source_refs(where: str, refs: object) -> None:
        if not isinstance(refs, list):
            return
        for ref in refs:
            if ref != "UNKNOWN" and ref not in source_ids:
                errors.append(f"{where}: unresolved source id {ref!r}")

    def check_id_ref(where: str, ref: object, allowed: set[str] | None = None) -> None:
        if ref in {"UNKNOWN", MULTI_SENTINEL, OPERATOR_SENTINEL}:
            return
        if allowed is not None:
            if ref not in allowed:
                errors.append(f"{where}: id {ref!r} not in allowed collection")
        elif ref not in ids:
            errors.append(f"{where}: unresolved id {ref!r}")

    for c in collections_spec:
        for e in _entries(store, c):
            if not isinstance(e, dict):
                continue
            w = f"{c}.{e.get('id', '?')}"
            if "source_ids" in e:
                check_source_refs(f"{w}.source_ids", e["source_ids"])
            if "source_id" in e:
                check_id_ref(f"{w}.source_id", e["source_id"], source_ids)
        # per-collection reference checks
    for e in _entries(store, "companies"):
        check_id_ref(f"companies.{e['id']}.architecture_id", e.get("architecture_id"), arch_ids)
    for e in _entries(store, "claims"):
        check_id_ref(f"claims.{e['id']}.subject_id", e.get("subject_id"))
        # a claim's subject should exist among companies/architectures
        need(
            e.get("subject_id") in company_ids or e.get("subject_id") in arch_ids or e.get("subject_id") in inst_ids,
            f"claims.{e['id']}: subject_id {e.get('subject_id')!r} is not a company/architecture/institution",
        )
    for e in _entries(store, "evidence"):
        w = f"evidence.{e['id']}"
        check_id_ref(f"{w}.subject_id", e.get("subject_id"))
        if e.get("subject_kind") == "company":
            need(e.get("subject_id") in company_ids, f"{w}: subject_id not a company")
        elif e.get("subject_kind") == "architecture":
            need(
                e.get("subject_id") in arch_ids or e.get("subject_id") == MULTI_SENTINEL,
                f"{w}: subject_id not an architecture",
            )
        check_source_refs(f"{w}.source_ids", e.get("source_ids"))
        # anti-hype: independent-class evidence requires real independence
        if e.get("evidence_class") in INDEPENDENT_CLASSES:
            need(
                e.get("measured_by_family") != "self",
                f"{w}: {e.get('evidence_class')} evidence cannot be self-measured",
            )
            need(
                e.get("independent_of_subject") is True,
                f"{w}: {e.get('evidence_class')} requires independent_of_subject",
            )
            srcs = e.get("source_ids", [])
            has_nonself = any(
                sources_by_id.get(s, {}).get("publisher_family") != "self" for s in srcs
            )
            need(
                has_nonself,
                f"{w}: independent-class evidence needs a non-self source family",
            )
        # measured date must be a real dateish
        if not _is_dateish(e.get("date")):
            errors.append(f"{w}.date: not a date: {e.get('date')!r}")
    for e in _entries(store, "milestones"):
        w = f"milestones.{e['id']}"
        check_id_ref(f"{w}.subject_id", e.get("subject_id"))
        for ev in e.get("evidence_ids", []):
            check_id_ref(f"{w}.evidence_ids", ev, evidence_ids)
        # achieved technical milestones need evidence; program stages are
        # selection events (claims), not measurements
        if e.get("status") in {"achieved", "achieved_late"} and e.get("kind") in {
            "roadmap_promise",
            "program_deliverable",
        }:
            need(
                len(e.get("evidence_ids", [])) > 0,
                f"{w}: achieved {e.get('kind')} requires evidence",
            )
        if e.get("status") == "achieved_late":
            need(
                e.get("promised") is not None and e.get("achieved_on") is not None
                and e["promised"] < e["achieved_on"],
                f"{w}: achieved_late requires promised < achieved_on",
            )
        if e.get("status") == "slipped":
            need(
                e.get("achieved_on") is None,
                f"{w}: slipped milestones must not have achieved_on",
            )
    for e in _entries(store, "forecasts"):
        w = f"forecasts.{e['id']}"
        check_id_ref(f"{w}.predictor_id", e.get("predictor_id"))
        check_id_ref(f"{w}.subject_id", e.get("subject_id"))
        need(bool(e.get("resolution_criteria", "").strip()), f"{w}: missing resolution_criteria")
        if e.get("status") in {"resolved_true", "resolved_false"}:
            need(len(e.get("resolution_evidence_ids", [])) > 0, f"{w}: resolved without evidence")
            need(e.get("resolved_on") is not None, f"{w}: resolved without resolved_on")
            for ev in e.get("resolution_evidence_ids", []):
                check_id_ref(f"{w}.resolution_evidence_ids", ev, evidence_ids)
                ev_entry = evidence_by_id.get(ev)
                if ev_entry and _is_date(ev_entry.get("date", "")) and e.get("resolved_on"):
                    need(
                        ev_entry["date"] <= e["resolved_on"],
                        f"{w}: resolution evidence {ev} is dated after resolved_on",
                    )
        if e.get("status") == "open":
            need(e.get("resolved_on") is None, f"{w}: open forecast has resolved_on")
        need(
            e.get("resolves_by") is not None,
            f"{w}: forecast without resolves_by",
        )
    for e in _entries(store, "bottlenecks"):
        w = f"bottlenecks.{e['id']}"
        check_id_ref(f"{w}.architecture_id", e.get("architecture_id"))
        if e.get("current_best_evidence_id") != "UNKNOWN":
            check_id_ref(f"{w}.current_best_evidence_id", e.get("current_best_evidence_id"), evidence_ids)
        if e.get("required_milestone") != "UNKNOWN":
            check_id_ref(f"{w}.required_milestone", e.get("required_milestone"), milestone_ids)
    for e in _entries(store, "confidence"):
        w = f"confidence.{e['id']}"
        check_id_ref(f"{w}.subject_id", e.get("subject_id"), company_ids)
        axes = e.get("axes", {})
        if isinstance(axes, dict):
            need(set(axes) == {"technical_architecture", "execution", "market_utility", "value_capture"}, f"{w}.axes: wrong axis set")
            for axis, val in axes.items():
                if not isinstance(val, dict):
                    errors.append(f"{w}.axes.{axis}: not an object")
                    continue
                kind = val.get("kind")
                need(kind in {"range", "not_yet_estimable"}, f"{w}.axes.{axis}: bad kind {kind!r}")
                need(bool(str(val.get("reason", "")).strip()), f"{w}.axes.{axis}: missing reason")
                if kind == "range":
                    low, high = val.get("low"), val.get("high")
                    need(isinstance(low, (int, float)) and isinstance(high, (int, float)) and 0 <= low <= high <= 1, f"{w}.axes.{axis}: bad range")
    for e in _entries(store, "questions"):
        w = f"questions.{e['id']}"
        for lid in e.get("linked_ids", []):
            check_id_ref(f"{w}.linked_ids", lid)
    for node in graph.get("nodes", []):
        if node.get("ref_id"):
            check_id_ref(f"graph.nodes.{node['id']}.ref_id", node["ref_id"])
    for edge in graph.get("edges", []):
        check_source_refs(f"graph.edges.{edge['id']}.source_ids", edge.get("source_ids"))

    # 4. Temporal integrity — hindcast snapshots may only cite knowledge that
    # existed in the world by the cutoff: the fact's domain date must precede
    # the cutoff AND at least one of its sources must have been published by
    # then. recorded_on (transaction time) is irrelevant here — Genesis records
    # everything at once; what matters is whether the fact was public in 2024.
    def _fact_after_cutoff(value: object, cutoff: str) -> bool:
        """A fact dated `value` is provably after `cutoff` only if its earliest
        possible interpretation postdates it — month precision means the fact
        could be anywhere in the month, so it leaks unless the whole month
        precedes the cutoff."""
        if not isinstance(value, str):
            return True  # unparseable domain date → cannot prove it precedes
        if _is_date(value):
            return value > cutoff
        if _is_month(value):
            last = calendar.monthrange(int(value[:4]), int(value[5:7]))[1]
            return f"{value}-{last:02d}" > cutoff
        return False  # UNKNOWN dates cannot leak via date (source check still applies)

    def _published_by_cutoff(src_ids: list, cutoff: str) -> bool:
        for sid in src_ids:
            pub = sources_by_id.get(sid, {}).get("published")
            if isinstance(pub, str) and _is_date(pub) and pub <= cutoff:
                return True
        return False

    evidence_domain = {
        e["id"]: (e.get("date"), e.get("source_ids", []))
        for e in _entries(store, "evidence")
    }
    claims_by_id = {e["id"]: e for e in _entries(store, "claims")}
    for snap in beliefs.get("snapshots", []):
        cutoff = snap.get("as_of", "9999-12-31")
        for entry in snap.get("entries", []):
            w = f"beliefs.{cutoff}.{entry.get('id', '?')}"
            for ev in entry.get("basis_evidence_ids", []):
                if ev not in evidence_ids:
                    errors.append(f"{w}: basis evidence {ev!r} does not exist")
                    continue
                ev_date, ev_srcs = evidence_domain[ev]
                if _fact_after_cutoff(ev_date, cutoff):
                    errors.append(
                        f"{w}: evidence {ev} is dated {ev_date} — future knowledge in {cutoff} snapshot"
                    )
                elif not _published_by_cutoff(ev_srcs, cutoff):
                    errors.append(
                        f"{w}: evidence {ev} has no source published by {cutoff} — leakage"
                    )
            for cl in entry.get("basis_claim_ids", []):
                cl_entry = claims_by_id.get(cl)
                if cl_entry is None:
                    errors.append(f"{w}: basis claim {cl!r} does not exist")
                    continue
                if _fact_after_cutoff(cl_entry.get("date"), cutoff):
                    errors.append(
                        f"{w}: claim {cl} is dated {cl_entry.get('date')} — future knowledge in {cutoff} snapshot"
                    )
                elif not _published_by_cutoff([cl_entry.get("source_id")], cutoff):
                    errors.append(
                        f"{w}: claim {cl} has no source published by {cutoff} — leakage"
                    )

    # 5. No entry may postdate its own file's declared as_of watermark —
    # a store that claims a boundary cannot contain records past it.
    for name in collections_spec:
        doc = store.get(name, {})
        watermark = doc.get("as_of") or build_as_of or store_as_of(store)
        if not _is_date(watermark):
            errors.append(f"{name}: missing or invalid as_of watermark")
            continue
        for e in _entries(store, name):
            r = e.get("recorded_on") if isinstance(e, dict) else None
            if isinstance(r, str) and _is_date(r) and r > watermark:
                errors.append(
                    f"{name}.{e.get('id')}: recorded_on {r} is after as_of {watermark}"
                )

    return errors


def sources_for(store: dict, entry: dict) -> list[dict]:
    by_id = {s["id"]: s for s in _entries(store, "sources")}
    refs = entry.get("source_ids") or ([entry["source_id"]] if entry.get("source_id") else [])
    return [by_id[r] for r in refs if r in by_id]


def subject_name(store: dict, subject_id: str) -> str:
    for coll in ("companies", "architectures", "institutions"):
        for e in _entries(store, coll):
            if e.get("id") == subject_id:
                return e.get("name") or e.get("id")
    return subject_id
