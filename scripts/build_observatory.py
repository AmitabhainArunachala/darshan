#!/usr/bin/env python3
"""Build the Quantum Observatory — Compute Ecology's instrument for the
quantum field.

Reads ``observatory_src/data/*.json`` (the ledgers) plus narrative pages in
``observatory_src/pages/`` and writes static pages under ``observatory/``.

Fail closed: the store is validated before a single byte is written. If the
validator reports anything, the build exits nonzero and emits no output.

Deterministic: no wall clock is consulted. The displayed ``as_of`` is the
store's own transaction-time watermark, not the machine's date.

Usage:
    python3 scripts/build_observatory.py
"""

from __future__ import annotations

import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_garden
import observatory_lib

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = observatory_lib.OUTPUT_DIR
PAGES_DIR = observatory_lib.PAGES_DIR

NAV = [
    ("index.html", "Field"),
    ("companies.html", "Companies"),
    ("architectures.html", "Architectures"),
    ("institutions.html", "Institutions"),
    ("evidence.html", "Evidence"),
    ("forecasts.html", "Forecasts"),
    ("bottlenecks.html", "Bottlenecks"),
    ("graph.html", "Map"),
    ("hindcast.html", "Hindcast"),
    ("questions.html", "Questions"),
    ("sources.html", "Sources"),
    ("methodology.html", "Method"),
]

QO_STYLES = """<style>
body.qo-page-body { font-size: 1.05rem; }
.qo-nav { border-block: 1px solid var(--rule); display: flex; flex-wrap: wrap;
  gap: .15rem .9rem; margin: 0 0 2.4rem; padding: .6rem 0; }
.qo-nav a { color: var(--faint); font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: .74rem; font-weight: 700; letter-spacing: .13em; text-decoration: none;
  text-transform: uppercase; }
.qo-nav a[aria-current="page"], .qo-nav a:hover { color: var(--accent); }
.qo-kicker { color: var(--accent); font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: .72rem; letter-spacing: .14em; margin: 0 0 .5rem; text-transform: uppercase; }
.qo-lede { border-left: 3px solid var(--accent); color: var(--faint); font-size: 1.18rem;
  font-style: italic; line-height: 1.6; margin: 1.2rem 0 2rem; padding-left: 1.2rem; }
.qo-grid { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
  margin: 1.4rem 0 2.4rem; }
.qo-card { border: 1px solid var(--rule); border-top: 3px solid var(--accent); padding: 1rem 1.1rem; }
.qo-card h3 { margin: .15rem 0 .4rem; font-size: 1.05rem; }
.qo-card p { color: var(--faint); font-size: .92rem; margin: .35rem 0; }
.qo-meta { color: var(--faint); font-size: .8rem; margin: 0 0 2rem; }
.qo-meta code { font-size: .78rem; }
.qo-table-wrap { overflow-x: auto; margin: 1.4rem 0 2.4rem; }
.qo-table { border-collapse: collapse; font-size: .88rem; line-height: 1.45; width: 100%; }
.qo-table th, .qo-table td { border: 1px solid var(--rule); padding: .5rem .6rem;
  text-align: left; vertical-align: top; }
.qo-table th { background: var(--accent-soft); white-space: nowrap; }
.qo-badge { border: 1px solid var(--rule); border-radius: 3px; display: inline-block;
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; font-size: .68rem;
  letter-spacing: .06em; padding: .12rem .45rem; text-transform: uppercase; white-space: nowrap; }
.qo-badge--self { color: var(--faint); }
.qo-badge--ind { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
.qo-badge--warn { border-color: #a33; color: #a33; }
.qo-src { font-size: .8rem; color: var(--faint); }
.qo-src a { color: inherit; }
.qo-figure { border: 1px solid var(--rule); margin: 1.6rem 0 2.4rem; padding: 1rem 1.2rem; }
.qo-figure figcaption { color: var(--faint); font-size: .82rem; font-style: italic; margin-top: .6rem; }
.qo-figure svg { display: block; height: auto; max-width: 100%; }
.qo-axis-note { color: var(--faint); font-size: .84rem; }
.qo-nye { color: #a33; font-weight: 700; }
.qo-list-plain { list-style: none; margin: 0; padding: 0; }
.qo-list-plain li { border-bottom: 1px solid var(--rule); padding: .8rem 0; }
.qo-falsifier { background: var(--accent-soft); border-left: 3px solid var(--accent);
  font-size: .9rem; margin: .8rem 0; padding: .6rem .9rem; }
.qo-question { border: 1px solid var(--rule); border-left: 4px solid #a33; margin: 0 0 .9rem;
  padding: .8rem 1rem; }
.qo-question[data-status="bounded"] { border-left-color: var(--accent); }
.qo-hindcast-belief { border: 1px solid var(--rule); margin: 0 0 1rem; padding: 1rem 1.1rem; }
.qo-hindcast-verdict { font-weight: 650; }
.qo-subtle { color: var(--faint); font-size: .9rem; }
.qo-timeline { list-style: none; margin: 0; padding: 0; }
.qo-timeline li { border-left: 2px solid var(--rule); margin: 0; padding: .4rem 0 .9rem 1.1rem;
  position: relative; }
.qo-timeline li::before { background: var(--paper); border: 2px solid var(--accent); border-radius: 50%;
  content: ""; height: .5rem; left: -.38rem; position: absolute; top: .85rem; width: .5rem; }
.qo-date { color: var(--faint); font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: .74rem; letter-spacing: .05em; }
@media (max-width: 52em) { .qo-nav { gap: .1rem .7rem; } }
</style>"""

LADDER_LABELS = {
    "company_claim": "Company claim",
    "technical_disclosure": "Technical disclosure",
    "peer_review": "Peer review",
    "independent_benchmark": "Independent benchmark",
    "independent_testbed": "Independent testbed",
    "replication": "Replication",
    "system_utility": "System utility",
}
CLAIM_LABELS = {
    "funding": "Funding",
    "selection": "Program selection",
    "procurement": "Procurement",
    "partnership": "Partnership",
    "roadmap": "Roadmap",
}
STATUS_LABELS = {
    "open": "Open",
    "achieved": "Achieved",
    "achieved_late": "Achieved late",
    "slipped": "Slipped",
    "superseded": "Superseded",
    "resolved_true": "Resolved TRUE",
    "resolved_false": "Resolved FALSE",
    "void": "Void",
    "bounded": "Bounded",
    "resolved_unknown": "Resolved: UNKNOWN",
    "resolved": "Resolved",
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=False)


def esc_attr(value: object) -> str:
    return html.escape(str(value), quote=True)


def _entries(store: dict, coll: str) -> list[dict]:
    return observatory_lib._entries(store, coll)


def _by_id(store: dict, coll: str) -> dict[str, dict]:
    return {e["id"]: e for e in _entries(store, coll)}


def source_links(store: dict, entry: dict) -> str:
    """Render provenance chips for an entry's source_ids/source_id."""
    sources = observatory_lib.sources_for(store, entry)
    parts = []
    for s in sources:
        label = s.get("id", "?")
        parts.append(
            '<a href="%s" title="%s">[%s]</a>'
            % (esc_attr(s.get("url", "#")), esc_attr(s.get("title", "")), esc(label))
        )
    if not parts:
        return '<span class="qo-src">no cited source</span>'
    return '<span class="qo-src">%s</span>' % " ".join(parts)


def class_badge(eclass: str, independent: bool | None = None) -> str:
    label = LADDER_LABELS.get(eclass) or CLAIM_LABELS.get(eclass) or eclass
    if eclass in observatory_lib.INDEPENDENT_CLASSES:
        cls = "qo-badge qo-badge--ind"
    elif eclass in observatory_lib.NON_EVIDENCE_CLASSES:
        cls = "qo-badge qo-badge--warn"
    else:
        cls = "qo-badge qo-badge--self"
    return '<span class="%s">%s</span>' % (cls, esc(label))


def subnav(current: str) -> str:
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        links.append('<a href="%s"%s>%s</a>' % (href, cur, esc(label)))
    return '<nav class="qo-nav" aria-label="Observatory">%s</nav>' % "".join(links)


def observatory_base(*, title: str, description: str, content: str, current: str) -> str:
    page = build_garden.render(
        build_garden.template("base.html"),
        title=html.escape(title, quote=False),
        description=html.escape(description, quote=True),
        root="../",
        content=subnav(current) + content,
    )
    page = page.replace(
        '<a href="../garden/index.html">Garden</a>',
        '<a href="../garden/index.html">Garden</a>\n    <a href="index.html">Observatory</a>',
        1,
    )
    page = page.replace("</head>", QO_STYLES + "\n</head>", 1)
    page = page.replace("<body>", '<body class="qo-page-body">', 1)
    return page


# ---------------------------------------------------------------- charts


def evidence_ladder_svg(store: dict, subject_id: str | None = None) -> str:
    """Per-ladder-class evidence counts for a subject (or the whole field)."""
    counts = {c: 0 for c in observatory_lib.EVIDENCE_LADDER}
    for e in _entries(store, "evidence"):
        if subject_id is None or e.get("subject_id") == subject_id:
            counts[e["evidence_class"]] = counts.get(e["evidence_class"], 0) + 1
    width, row_h, pad_l, pad_t = 560, 22, 170, 8
    height = pad_t * 2 + row_h * len(observatory_lib.EVIDENCE_LADDER)
    bar_w = 44
    rows = []
    for i, cls in enumerate(observatory_lib.EVIDENCE_LADDER):
        y = pad_t + i * row_h
        n = counts.get(cls, 0)
        ind = cls in observatory_lib.INDEPENDENT_CLASSES
        fill = "var(--accent)" if ind else "var(--faint)"
        label = LADDER_LABELS[cls]
        rows.append(
            '<text x="%d" y="%d" font-size="11" fill="var(--faint)" text-anchor="end">%s</text>'
            % (pad_l - 8, y + 14, esc(label))
        )
        for k in range(n):
            rows.append(
                '<rect x="%d" y="%d" width="34" height="12" fill="%s" opacity="%.2f"/>'
                % (pad_l + k * (bar_w - 6), y + 4, fill, 0.9 - 0.12 * k)
            )
        if n == 0:
            rows.append(
                '<text x="%d" y="%d" font-size="10" fill="var(--faint)" font-style="italic">none recorded</text>'
                % (pad_l + 4, y + 13)
            )
    return (
        '<svg viewBox="0 0 %d %d" role="img" aria-label="Evidence by rung">%s</svg>'
        % (width, height, "".join(rows))
    )


def confidence_svg(conf: dict) -> str:
    """Four-axis confidence decomposition as range bars; NOT YET ESTIMABLE
    renders as an empty track — honesty, not a thin fake bar."""
    axes = [
        ("technical_architecture", "Technical architecture"),
        ("execution", "Execution"),
        ("market_utility", "Market utility"),
        ("value_capture", "Value capture"),
    ]
    width, row_h, pad_l, pad_t = 560, 34, 170, 10
    height = pad_t * 2 + row_h * len(axes)
    track_x, track_w = pad_l, 340
    rows = []
    for i, (key, label) in enumerate(axes):
        y = pad_t + i * row_h
        axis = conf["axes"][key]
        rows.append(
            '<text x="%d" y="%d" font-size="11" fill="var(--faint)" text-anchor="end">%s</text>'
            % (pad_l - 10, y + 14, esc(label))
        )
        rows.append(
            '<rect x="%d" y="%d" width="%d" height="10" fill="none" stroke="var(--rule)"/>'
            % (track_x, y + 4, track_w)
        )
        if axis["kind"] == "range":
            x0 = track_x + axis["low"] * track_w
            w = (axis["high"] - axis["low"]) * track_w
            rows.append(
                '<rect x="%.1f" y="%d" width="%.1f" height="10" fill="var(--accent)" opacity=".75"/>'
                % (x0, y + 4, max(w, 2))
            )
            rows.append(
                '<text x="%d" y="%d" font-size="10" fill="var(--faint)">%.2f–%.2f</text>'
                % (track_x + track_w + 8, y + 13, axis["low"], axis["high"])
            )
        else:
            rows.append(
                '<text x="%d" y="%d" font-size="10" fill="#a33" font-weight="700">NOT YET ESTIMABLE</text>'
                % (track_x + track_w + 8, y + 13)
            )
    return (
        '<svg viewBox="0 0 %d %d" role="img" aria-label="Confidence decomposition">%s</svg>'
        % (width, height, "".join(rows))
    )


# ---------------------------------------------------------------- pages


def page_index(store: dict) -> str:
    as_of = observatory_lib.store_as_of(store)
    co_case = [e for e in _entries(store, "companies") if e["depth"] == "case_study"]
    fc_open = [e for e in _entries(store, "forecasts") if e["status"] == "open"]
    q_open = [e for e in _entries(store, "questions") if e["status"] in {"open", "bounded"}]
    bn = _entries(store, "bottlenecks")

    def stat(n: int, label: str) -> str:
        return '<div class="qo-card"><h3>%d</h3><p>%s</p></div>' % (n, esc(label))

    cards = "".join(
        [
            stat(len(_entries(store, "companies")), "companies on the register"),
            stat(len(_entries(store, "architectures")), "competing architectures"),
            stat(len(_entries(store, "institutions")), "observing institutions"),
            stat(len(_entries(store, "evidence")), "evidence entries"),
            stat(len(_entries(store, "claims")), "recorded claims"),
            stat(len(_entries(store, "forecasts")), "forecasts on the ledger"),
            stat(len(bn), "tracked bottlenecks"),
            stat(len(q_open), "unresolved questions"),
        ]
    )
    case_links = "".join(
        '<li><a href="%s.html"><strong>%s</strong></a> — %s</li>'
        % (esc_attr(e["id"][3:]), esc(e["name"]), esc(e["registry_note"]))
        for e in sorted(co_case, key=lambda x: x["id"])
    )
    open_fc = "".join(
        "<li>%s <span class='qo-date'>resolves %s</span><br><span class='qo-subtle'>%s</span></li>"
        % (esc(e["statement"]), esc(e["resolves_by"]), esc(e["resolution_criteria"]))
        for e in sorted(fc_open, key=lambda x: x["resolves_by"])
    )
    content = """
<p class="qo-kicker">Compute Ecology · Quantum Observatory</p>
<h1 class="article-title">The Quantum Field, Kept Honest</h1>
<p class="qo-lede">Map the field. Preserve time. Measure claims. Track bottlenecks.
Record predictions. Learn which signals deserve confidence.</p>
<p class="qo-meta">Ledger as of <code>%s</code> (the store's transaction-time watermark — no
wall clock is consulted during the build). Every entry carries <code>recorded_on</code> plus its
domain dates; every claim cites its sources by id.</p>
<div class="qo-grid">%s</div>
<h2>Case studies</h2>
<ul class="qo-list-plain">%s</ul>
<h2>The evidence ladder — field-wide</h2>
<figure class="qo-figure">%s
<figcaption>Each block is one ledger entry at that rung. Entries above <em>peer review</em>
must be measured by someone who is not the subject — the validator fails closed otherwise.</figcaption></figure>
<h2>Open forecasts</h2>
<ul class="qo-list-plain">%s</ul>
<h2>Reading order</h2>
<p class="qo-subtle">Start with <a href="methodology.html">Method</a> to learn what each badge
means. Then the two case studies, then <a href="graph.html">the map</a> for where value and
supply-chain dependence actually sit. <a href="hindcast.html">Hindcast</a> shows what this
system believed at the end of 2024 and what arrived afterward.</p>
""" % (
        esc(as_of),
        cards,
        case_links,
        evidence_ladder_svg(store),
        open_fc,
    )
    return observatory_base(
        title="Quantum Observatory · Compute Ecology",
        description="A bitemporal evidence ledger for the quantum-computing field: claims, measurements, forecasts, bottlenecks, and what they were believed to mean.",
        content=content,
        current="index.html",
    )


def page_methodology(store: dict) -> str:
    ladder_rows = "".join(
        "<tr><td>%d</td><td><code>%s</code></td><td>%s</td><td>%s</td></tr>"
        % (
            i + 1,
            cls,
            esc(LADDER_LABELS[cls]),
            "yes — measured_by_family must differ from the subject and at least one "
            "non-self source family is required" if cls in observatory_lib.INDEPENDENT_CLASSES else "no",
        )
        for i, cls in enumerate(observatory_lib.EVIDENCE_LADDER)
    )
    claim_rows = "".join(
        "<tr><td><code>%s</code></td><td>%s</td></tr>" % (cls, esc(CLAIM_LABELS[cls]))
        for cls in sorted(observatory_lib.NON_EVIDENCE_CLASSES)
    )
    content = """
<p class="qo-kicker">Method</p>
<h1 class="article-title">How the Observatory Decides What It Knows</h1>
<p class="qo-lede">Every number on this site answers three questions: who measured it,
when did the ledger learn it, and what would prove it wrong.</p>
<h2>Two clocks</h2>
<p>Each entry carries <code>recorded_on</code> — <em>transaction time</em>, when the entry
entered the ledger — and domain dates for when the fact is true in the world. An as-of
query means <code>recorded_on ≤ T</code>. The <a href="hindcast.html">hindcast</a> view is
computed from that rule, and a leakage test proves a 2024 snapshot cites only facts that
were public in 2024.</p>
<h2>The evidence ladder</h2>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Rung</th><th>Class</th><th>Meaning</th><th>Independence required</th></tr>
%s
</table></div>
<h2>Claims that are not evidence</h2>
<p>Five claim classes are recorded for provenance but can never appear as evidence:</p>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Class</th><th>Meaning</th></tr>
%s
</table></div>
<h2>Prohibited transforms</h2>
<p>The following transitions require <em>separate evidence</em> each time — never inferred
from the previous rung: funded → validated; selected → proven; qubits → useful scale;
benchmark win → general advantage; quantum advantage → economic advantage; system delivered
→ customer value; roadmap → forecast fact; funding → technical progress; patent → working
tech; partnership → revenue.</p>
<h2>Confidence decomposition</h2>
<p>There is no headline score. Each case-study subject carries a four-axis range —
technical architecture, execution, market utility, value capture — and
<span class="qo-nye">NOT YET ESTIMABLE</span> is a valid answer, displayed as an empty track
rather than a thin fake bar.</p>
<h2>Fail closed</h2>
<p><code>scripts/check_observatory.py</code> enforces the schema, citation resolution,
independence rules, milestone evidence requirements, forecast resolution hygiene, and
temporal-leakage limits. Any violation stops the build before output is written. UNKNOWN
is acceptable; fabricated precision is not.</p>
<p class="qo-subtle">Design rationale and the full entity list: <code>observatory_src/DESIGN.md</code>
in the repository. Machine-enforced contract: <code>observatory_src/schema/collections.json</code>.</p>
""" % (
        ladder_rows,
        claim_rows,
    )
    return observatory_base(
        title="Method · Quantum Observatory",
        description="The rules the observatory enforces: the evidence ladder, non-evidence claim classes, prohibited transforms, and fail-closed validation.",
        content=content,
        current="methodology.html",
    )


def page_companies(store: dict) -> str:
    companies = sorted(_entries(store, "companies"), key=lambda e: e["name"])
    arch = _by_id(store, "architectures")
    rows = []
    for c in companies:
        a = arch.get(c["architecture_id"], {})
        depth = (
            '<a href="%s.html">case study</a>' % esc_attr(c["id"][3:])
            if c["depth"] == "case_study"
            else "registry"
        )
        rows.append(
            "<tr><td><strong>%s</strong>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (
                esc(c["name"]),
                '<br><span class="qo-src">%s</span>' % esc(c["id"]) if False else "",
                esc(a.get("name", c["architecture_id"])),
                esc(c["hq"]),
                esc(c["founded"]),
                esc(c["status"]),
                depth,
            )
        )
    content = """
<p class="qo-kicker">Registry</p>
<h1 class="article-title">Companies</h1>
<p class="qo-lede">Twenty companies on the register — two at case-study depth, the rest as
registry entries with the same provenance rules and less narrative.</p>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Company</th><th>Architecture</th><th>HQ</th><th>Founded</th><th>Status</th><th>Depth</th></tr>
%s
</table></div>
<p class="qo-subtle">Registry rows are real entries — same schema, same citation rules —
they just carry no narrative yet. Promotion to case study happens when the evidence
ledger justifies it, not when the company is fashionable.</p>
""" % "".join(rows)
    return observatory_base(
        title="Companies · Quantum Observatory",
        description="Quantum-computing companies on the register: Quantum Motion and PsiQuantum at case-study depth; the QBI and NQCC cohorts as registry entries.",
        content=content,
        current="companies.html",
    )


def company_page(store: dict, company: dict, page_md: dict[str, str]) -> str:
    cid = company["id"]
    arch = _by_id(store, "architectures").get(company["architecture_id"], {})
    claims = sorted(
        [e for e in _entries(store, "claims") if e.get("subject_id") == cid],
        key=lambda e: e.get("date", ""),
    )
    evidence = sorted(
        [e for e in _entries(store, "evidence") if e.get("subject_id") == cid],
        key=lambda e: observatory_lib.LADDER_RANK.get(e["evidence_class"], 0),
    )
    milestones = sorted(
        [e for e in _entries(store, "milestones") if e.get("subject_id") == cid],
        key=lambda e: (e.get("promised") or "9999", e["id"]),
    )
    forecasts = [
        e for e in _entries(store, "forecasts") if e.get("subject_id") == cid
    ]
    conf = next(
        (e for e in _entries(store, "confidence") if e.get("subject_id") == cid), None
    )
    bottlenecks = [
        e
        for e in _entries(store, "bottlenecks")
        if e.get("architecture_id") == company["architecture_id"]
    ]

    narrative = build_garden.md_to_html(page_md["body"], set())

    claims_rows = "".join(
        "<tr><td class='qo-date'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        % (esc(e["date"]), esc(e["claim"]), class_badge(e["claim_class"]), source_links(store, e))
        for e in claims
    )
    ev_rows = "".join(
        "<tr><td class='qo-date'>%s</td><td><code>%s</code></td><td>%s</td><td>%s</td><td>%s · %s</td><td>%s</td><td>%s</td></tr>"
        % (
            esc(e["date"]),
            esc(e["metric"]),
            esc(e["qualifier"]),
            class_badge(e["evidence_class"]),
            esc(e["measured_by_family"]),
            "independent" if e["independent_of_subject"] else "self/contextual",
            source_links(store, e),
            esc(e["note"]),
        )
        for e in evidence
    )
    ms_rows = "".join(
        "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        % (
            esc(e["description"]),
            esc(e.get("promised") or "—"),
            esc(e.get("achieved_on") or "—"),
            esc(STATUS_LABELS.get(e["status"], e["status"])),
            ", ".join('<a href="evidence.html">%s</a>' % esc(x) for x in e.get("evidence_ids", [])) or "—",
        )
        for e in milestones
    )
    fc_rows = "".join(
        "<tr><td><code>%s</code></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        % (
            esc(e["id"]),
            esc(e["statement"]),
            esc(e["resolves_by"]),
            esc(STATUS_LABELS.get(e["status"], e["status"])),
            esc(e["resolution_criteria"]),
        )
        for e in forecasts
    )
    bn_html = "".join(
        '<div class="qo-card"><h3>%s</h3><p>%s</p><p><strong>Falsifier:</strong> %s</p></div>'
        % (esc(e["name"]), esc(e["description"]), esc(e["falsifier"]))
        for e in bottlenecks
    )
    conf_html = ""
    if conf:
        axes_reasons = "".join(
            "<tr><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (
                esc(k.replace("_", " ")),
                ("%s" % ("%.2f–%.2f" % (v["low"], v["high"]))) if v["kind"] == "range" else '<span class="qo-nye">NOT YET ESTIMABLE</span>',
                esc(v["reason"]),
            )
            for k, v in conf["axes"].items()
        )
        inc = "".join("<li>%s</li>" % esc(x) for x in conf["evidence_increasing"])
        dec = "".join("<li>%s</li>" % esc(x) for x in conf["evidence_decreasing"])
        unres = "".join("<li>%s</li>" % esc(x) for x in conf["unresolved"])
        fals = "".join('<div class="qo-falsifier">%s</div>' % esc(x) for x in conf["falsifiers"])
        decisive = "".join(
            "<tr><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (esc(d["milestone"]), esc(d["deadline"]), esc(d["resolution"]))
            for d in conf["next_decisive"]
        )
        conf_html = """
<h2 id="confidence">Confidence decomposition <span class="qo-date">as of %s</span></h2>
<figure class="qo-figure">%s<figcaption>No headline score by design — each axis is a range
with a stated reason, and NOT YET ESTIMABLE renders as an empty track.</figcaption></figure>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Axis</th><th>Range</th><th>Reason</th></tr>%s</table></div>
<div class="qo-grid">
<div class="qo-card"><h3>Would raise confidence</h3><ul>%s</ul></div>
<div class="qo-card"><h3>Would lower confidence</h3><ul>%s</ul></div>
<div class="qo-card"><h3>Unresolved</h3><ul>%s</ul></div>
</div>
<h3>Next decisive checkpoints</h3>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Milestone</th><th>Deadline</th><th>Resolution</th></tr>%s</table></div>
<h3>Falsifiers</h3>%s
""" % (
            esc(conf["as_of"]),
            confidence_svg(conf),
            axes_reasons,
            inc,
            dec,
            unres,
            decisive,
            fals,
        )

    content = """
<p class="qo-kicker">Case study · %s</p>
<h1 class="article-title">%s</h1>
<p class="qo-lede">%s</p>
<p class="qo-meta">Architecture: <a href="architectures.html">%s</a> · HQ %s · founded %s ·
ledger as of <code>%s</code></p>
%s
<h2 id="claims">Claims on record</h2>
<p class="qo-subtle">Claims are provenance, not evidence. Funding, selection, procurement,
partnership, and roadmap claims can never promote a result.</p>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Date</th><th>Claim</th><th>Class</th><th>Sources</th></tr>%s</table></div>
<h2 id="evidence">Evidence ledger</h2>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Date</th><th>Metric</th><th>Qualifier</th><th>Class</th><th>Measured by</th><th>Sources</th><th>Note</th></tr>%s</table></div>
<figure class="qo-figure">%s<figcaption>Evidence distribution by ladder rung for this
subject — blocks above <em>peer review</em> required a non-self measuring family.</figcaption></figure>
<h2 id="milestones">Milestones and promises</h2>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>Description</th><th>Promised</th><th>Achieved</th><th>Status</th><th>Evidence</th></tr>%s</table></div>
<h2 id="bottlenecks">Critical bottleneck</h2>
<div class="qo-grid">%s</div>
%s
<h2 id="forecasts">Forecasts touching this subject</h2>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>ID</th><th>Statement</th><th>Resolves by</th><th>Status</th><th>Resolution criteria</th></tr>%s</table></div>
""" % (
        esc(arch.get("name", "")),
        esc(company["name"]),
        esc(company["registry_note"]),
        esc(arch.get("name", company["architecture_id"])),
        esc(company["hq"]),
        esc(company["founded"]),
        esc(observatory_lib.store_as_of(store)),
        narrative,
        claims_rows,
        ev_rows,
        evidence_ladder_svg(store, cid),
        ms_rows,
        bn_html or '<div class="qo-card"><p>No bottleneck tracked for this architecture.</p></div>',
        conf_html,
        fc_rows or '<tr><td colspan="5">No forecasts reference this subject.</td></tr>',
    )
    return observatory_base(
        title="%s · Quantum Observatory" % company["name"],
        description=company["registry_note"],
        content=content,
        current="companies.html",
    )


def page_architectures(store: dict) -> str:
    caps = _by_id(store, "capabilities")
    companies = _entries(store, "companies")
    by_arch: dict[str, list[str]] = {}
    for c in companies:
        by_arch.setdefault(c["architecture_id"], []).append(c["name"])
    cards = []
    for a in sorted(_entries(store, "architectures"), key=lambda e: e["id"]):
        deps = "".join(
            "<li><strong>%s</strong> — %s</li>"
            % (esc(caps[d]["name"]), esc(caps[d]["note"]))
            for d in a["key_dependencies"]
            if d in caps
        )
        fals = "".join('<div class="qo-falsifier">%s</div>' % esc(f) for f in a["falsifiers"])
        who = ", ".join(sorted(by_arch.get(a["id"], []))) or "—"
        cards.append(
            """<div class="qo-card" style="grid-column: 1 / -1">
<h3>%s <span class="qo-src">%s</span></h3>
<p>%s</p>
<p><strong>Companies:</strong> %s</p>
<p><strong>Scaling hypothesis:</strong> %s</p>
<details><summary class="qo-src">Dependencies &amp; falsifiers</summary>
<ul>%s</ul>%s</details>
<p>%s</p></div>"""
            % (
                esc(a["name"]),
                esc(a["id"]),
                esc(a["summary"]),
                esc(who),
                esc(a["scaling_hypothesis"]),
                deps,
                fals,
                source_links(store, a),
            )
        )
    content = """
<p class="qo-kicker">Registry</p>
<h1 class="article-title">Architectures</h1>
<p class="qo-lede">Ten competing ways to build a utility-scale quantum computer. Each entry
carries its scaling hypothesis, its physical dependencies, and the falsifiers that would
kill the thesis.</p>
<div class="qo-grid">%s</div>
""" % "".join(cards)
    return observatory_base(
        title="Architectures · Quantum Observatory",
        description="Competing quantum-computing architectures with dependencies, scaling hypotheses, and falsifiers.",
        content=content,
        current="architectures.html",
    )


def page_institutions(store: dict) -> str:
    cards = []
    for inst in sorted(_entries(store, "institutions"), key=lambda e: e["name"]):
        programs = "".join(
            "<li><strong>%s</strong> — %s <span class='qo-date'>%s</span></li>"
            % (
                esc(p.get("name", "")),
                esc(p.get("role", "")),
                esc(p.get("window", "")),
            )
            for p in inst.get("programs", [])
        )
        cards.append(
            """<div class="qo-card">
<h3>%s</h3>
<p class="qo-src">%s · %s</p>
<p>%s</p>
<ul>%s</ul>
<p>%s</p></div>"""
            % (
                esc(inst["name"]),
                esc(inst["kind"].replace("_", " ")),
                esc(inst["jurisdiction"]),
                esc(inst["observes"]),
                programs or "<li>—</li>",
                source_links(store, inst),
            )
        )
    content = """
<p class="qo-kicker">Registry</p>
<h1 class="article-title">Institutions</h1>
<p class="qo-lede">The observers: who funds, evaluates, hosts, and measures. Selection by an
institution is a recorded claim — validation by one is evidence. They are different rungs.</p>
<div class="qo-grid">%s</div>
""" % "".join(cards)
    return observatory_base(
        title="Institutions · Quantum Observatory",
        description="Funding agencies, testbed operators, metrology institutes, and evaluators observing the quantum field.",
        content=content,
        current="institutions.html",
    )


def page_evidence(store: dict) -> str:
    rows = []
    for e in sorted(
        _entries(store, "evidence"),
        key=lambda e: (e["subject_id"], observatory_lib.LADDER_RANK[e["evidence_class"]]),
    ):
        subject = observatory_lib.subject_name(store, e["subject_id"])
        rows.append(
            "<tr><td><code>%s</code></td><td>%s</td><td class='qo-date'>%s</td><td><code>%s</code></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (
                esc(e["id"]),
                esc(subject),
                esc(e["date"]),
                esc(e["metric"]),
                class_badge(e["evidence_class"]),
                "%s · %s" % (esc(e["measured_by_family"]), "independent" if e["independent_of_subject"] else "self"),
                source_links(store, e),
                esc(e["note"]),
            )
        )
    content = """
<p class="qo-kicker">Ledger</p>
<h1 class="article-title">Evidence</h1>
<p class="qo-lede">Every measurement the observatory trusts enough to hold, with its rung,
its measurer's family, and its sources. Independence is enforced structurally: entries at
the top of the ladder must not be self-measured.</p>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>ID</th><th>Subject</th><th>Date</th><th>Metric</th><th>Class</th><th>Provenance</th><th>Sources</th><th>Note</th></tr>
%s</table></div>
""" % "".join(rows)
    return observatory_base(
        title="Evidence · Quantum Observatory",
        description="The measurement ledger: every evidence entry with ladder class, measuring family, independence flag, and sources.",
        content=content,
        current="evidence.html",
    )


def page_forecasts(store: dict) -> str:
    rows = []
    for e in sorted(_entries(store, "forecasts"), key=lambda e: e["resolves_by"]):
        rows.append(
            "<tr><td><code>%s</code></td><td><code>%s</code></td><td>%s</td><td class='qo-date'>%s → %s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (
                esc(e["id"]),
                esc(e["predictor_id"]),
                esc(e["statement"]),
                esc(e["made_on"]),
                esc(e["resolves_by"]),
                esc(STATUS_LABELS.get(e["status"], e["status"])),
                esc(e["resolution_criteria"]),
                source_links(store, e),
            )
        )
    content = """
<p class="qo-kicker">Ledger</p>
<h1 class="article-title">Forecasts</h1>
<p class="qo-lede">Recorded predictions with resolution criteria written <em>before</em> the
answer is known. A forecast may not resolve without cited evidence; an unresolved forecast
is itself information.</p>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>ID</th><th>Predictor</th><th>Statement</th><th>Made → resolves</th><th>Status</th><th>Criteria</th><th>Sources</th></tr>
%s</table></div>
<p class="qo-subtle"><code>ce-operator</code> rows are this system's own registered
predictions — the observatory grades itself on the same ledger it keeps for everyone else.</p>
""" % "".join(rows)
    return observatory_base(
        title="Forecasts · Quantum Observatory",
        description="Registered predictions with pre-written resolution criteria, resolution deadlines, and required evidence.",
        content=content,
        current="forecasts.html",
    )


def page_bottlenecks(store: dict) -> str:
    arch = _by_id(store, "architectures")
    ev = _by_id(store, "evidence")
    cards = []
    for b in sorted(_entries(store, "bottlenecks"), key=lambda e: e["architecture_id"]):
        a = arch.get(b["architecture_id"], {})
        best = b["current_best_evidence_id"]
        best_html = (
            "<code>%s</code> (%s)" % (esc(best), esc(LADDER_LABELS.get(ev.get(best, {}).get("evidence_class", ""), "—")))
            if best != "UNKNOWN" and best in ev
            else "<em>UNKNOWN — no evidence on file</em>"
        )
        cards.append(
            """<div class="qo-card" style="grid-column: 1 / -1">
<h3>%s <span class="qo-src">%s · trend %s</span></h3>
<p>%s</p>
<p><strong>Current best evidence:</strong> %s<br>
<strong>Required milestone:</strong> <code>%s</code></p>
<div class="qo-falsifier"><strong>Falsifier:</strong> %s</div>
<p>%s</p></div>"""
            % (
                esc(b["name"]),
                esc(a.get("name", b["architecture_id"])),
                esc(b["trend"]),
                esc(b["description"]),
                best_html,
                esc(b["required_milestone"]),
                esc(b["falsifier"]),
                source_links(store, b),
            )
        )
    content = """
<p class="qo-kicker">Ledger</p>
<h1 class="article-title">Bottlenecks</h1>
<p class="qo-lede">The physical constraint currently binding each architecture's path to
utility — the wall that moves, and what would falsify the claim that it is the wall.</p>
<div class="qo-grid">%s</div>
""" % "".join(cards)
    return observatory_base(
        title="Bottlenecks · Quantum Observatory",
        description="Per-architecture critical bottlenecks with current best evidence, required milestones, trends, and falsifiers.",
        content=content,
        current="bottlenecks.html",
    )


def page_graph(store: dict) -> str:
    graph = store["graph"]
    nodes = {n["id"]: n for n in graph["nodes"]}
    caps = _by_id(store, "capabilities")
    arch = _by_id(store, "architectures")
    inst = _by_id(store, "institutions")

    # value-accrual view: each capability -> requiring architectures -> suppliers
    sections = []
    for cap_id, cap in sorted(caps.items()):
        req = [arch[a]["name"] for a in cap["shared_with_architectures"] if a in arch]
        suppliers = ", ".join(cap["suppliers"])
        shared_note = (
            '<span class="qo-badge qo-badge--warn">shared dependency</span>'
            if len(req) > 1
            else '<span class="qo-badge">single-architecture</span>'
        )
        sections.append(
            """<div class="qo-card">
<h3>%s %s</h3>
<p class="qo-src">%s · suppliers: %s</p>
<p>%s</p>
<p><strong>Required by:</strong> %s</p>
<p>%s</p></div>"""
            % (
                esc(cap["name"]),
                shared_note,
                esc(cap["kind"]),
                esc(suppliers),
                esc(cap["note"]),
                esc(", ".join(sorted(req)) or "—"),
                source_links(store, cap),
            )
        )

    edge_rows = "".join(
        "<tr><td>%s</td><td><code>%s</code></td><td>%s</td><td>%s</td></tr>"
        % (
            esc(nodes[e["from"]]["label"]),
            esc(e["relation"]),
            esc(nodes[e["to"]]["label"]),
            esc(e["note"]),
        )
        for e in sorted(graph["edges"], key=lambda e: e["id"])
    )
    content = """
<p class="qo-kicker">Map</p>
<h1 class="article-title">Where Value and Dependence Sit</h1>
<p class="qo-lede">The dependency and value-accrual map: which physical capabilities each
architecture cannot route around, who supplies them, and which dependencies are shared
across competitors — the positions where leverage accumulates.</p>
<h2>Supply nodes</h2>
<div class="qo-grid">%s</div>
<h2>Edges</h2>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>From</th><th>Relation</th><th>To</th><th>Note</th></tr>
%s</table></div>
""" % ("".join(sections), edge_rows)
    return observatory_base(
        title="Dependency & Value-Accrual Map · Quantum Observatory",
        description="Physical capabilities, their suppliers, the architectures that require them, and shared dependencies across competitors.",
        content=content,
        current="graph.html",
    )


def page_hindcast(store: dict) -> str:
    beliefs = store["beliefs"]
    now = observatory_lib.store_as_of(store)
    ev = _by_id(store, "evidence")
    cl = _by_id(store, "claims")
    parts = []
    for snap in beliefs.get("snapshots", []):
        cutoff = snap["as_of"]
        post = [
            e for e in _entries(store, "evidence")
            if isinstance(e.get("date"), str) and e["date"] > cutoff
        ]
        post_claims = [
            e for e in _entries(store, "claims")
            if isinstance(e.get("date"), str) and e["date"] > cutoff
        ]
        blocks = []
        for b in snap["entries"]:
            basis = []
            for evid in b.get("basis_evidence_ids", []):
                e = ev.get(evid)
                if e:
                    basis.append(
                        '<li><code>%s</code> %s — %s (%s)</li>'
                        % (evid, esc(e["metric"]), esc(e["qualifier"]), esc(LADDER_LABELS.get(e["evidence_class"], "")))
                    )
            for clid in b.get("basis_claim_ids", []):
                c = cl.get(clid)
                if c:
                    basis.append(
                        '<li><code>%s</code> %s — <em>claim, not evidence</em> (%s)</li>'
                        % (clid, esc(c["claim"]), esc(CLAIM_LABELS.get(c["claim_class"], c["claim_class"])))
                    )
            blocks.append(
                """<div class="qo-hindcast-belief">
<p class="qo-hindcast-verdict">%s</p>
<p class="qo-src">held as <code>%s</code></p>
<ul>%s</ul>
<p class="qo-subtle">%s</p></div>"""
                % (
                    esc(b["statement"]),
                    esc(b["confidence"]),
                    "".join(basis) or "<li>No basis recorded</li>",
                    esc(b["note"]),
                )
            )
        post_ev = "".join(
            '<li>%s — <code>%s</code> %s <span class="qo-date">%s</span></li>'
            % (
                esc(observatory_lib.subject_name(store, e["subject_id"])),
                esc(e["id"]),
                esc(e["metric"]),
                esc(e["date"]),
            )
            for e in sorted(post, key=lambda e: e["date"])
        )
        post_cl = "".join(
            '<li>%s — %s <span class="qo-date">%s</span></li>'
            % (esc(observatory_lib.subject_name(store, c["subject_id"])), esc(c["claim"]), esc(c["date"]))
            for c in sorted(post_claims, key=lambda c: c["date"])
        )
        parts.append(
            """
<h2>Snapshot: %s <span class="qo-date">%s</span></h2>
%s
<h3>What the ledger gained after %s</h3>
<p class="qo-subtle">Computed deterministically: every evidence entry and claim whose
domain date postdates the snapshot. This is the calibration check — did the field deliver
what the beliefs implied it might?</p>
<h4>Evidence</h4><ul class="qo-list-plain">%s</ul>
<h4>Claims (not evidence)</h4><ul class="qo-list-plain">%s</ul>
"""
            % (
                esc(cutoff),
                esc(snap.get("label", "")),
                "".join(blocks),
                esc(cutoff),
                post_ev or "<li>—</li>",
                post_cl or "<li>—</li>",
            )
        )
    content = """
<p class="qo-kicker">Hindcast</p>
<h1 class="article-title">What the System Believed, and When</h1>
<p class="qo-lede">Belief snapshots pinned to a date, with the evidence and claims that
justified them — and everything that arrived afterward. A belief is only honest if you can
reconstruct why it was held.</p>
<p class="qo-meta">Ledger now: <code>%s</code>. Leakage check: a snapshot may only cite
facts whose domain date and publication precede its as_of; the validator enforces it.</p>
%s
""" % (esc(now), "".join(parts))
    return observatory_base(
        title="Hindcast · Quantum Observatory",
        description="Belief snapshots by date with their evidential basis, and the evidence that arrived afterward — calibration as a first-class view.",
        content=content,
        current="hindcast.html",
    )


def page_questions(store: dict) -> str:
    ids = observatory_lib.all_ids(store)
    cards = []
    for q in sorted(_entries(store, "questions"), key=lambda e: (e["status"] != "open", e["id"])):
        linked = ", ".join(
            "<code>%s</code>" % esc(l) for l in q["linked_ids"] if l in ids
        )
        cards.append(
            '<div class="qo-question" data-status="%s"><strong>%s</strong> '
            '<span class="qo-badge">%s</span><p class="qo-subtle">%s</p>'
            '<p class="qo-src">linked: %s</p></div>'
            % (
                esc_attr(q["status"]),
                esc(q["question"]),
                esc(STATUS_LABELS.get(q["status"], q["status"])),
                esc(q["note"]),
                linked or "—",
            )
        )
    content = """
<p class="qo-kicker">Registry</p>
<h1 class="article-title">Unresolved Questions</h1>
<p class="qo-lede">What the observatory does not know and refuses to paper over. UNKNOWN is
an acceptable state; fabricated precision is not.</p>
%s
""" % "".join(cards)
    return observatory_base(
        title="Unresolved Questions · Quantum Observatory",
        description="Open and bounded questions the observatory refuses to paper over — the explicit unknowns.",
        content=content,
        current="questions.html",
    )


def page_sources(store: dict) -> str:
    rows = []
    for s in sorted(_entries(store, "sources"), key=lambda e: (e.get("published") or "9999", e["id"])):
        rows.append(
            "<tr><td><code>%s</code></td><td><a href=\"%s\">%s</a></td><td>%s</td><td><code>%s</code></td><td>%s</td><td class='qo-date'>%s</td><td>%s</td></tr>"
            % (
                esc(s["id"]),
                esc_attr(s["url"]),
                esc(s["title"]),
                esc(s["publisher"]),
                esc(s["publisher_family"]),
                esc(s["published"]),
                esc(s["retrieved"]),
                esc(s.get("note", "")),
            )
        )
    content = """
<p class="qo-kicker">Registry</p>
<h1 class="article-title">Sources</h1>
<p class="qo-lede">Every cited source with its publisher, family, publication date, and the
day the ledger retrieved it. Publisher family is relative to the subject — a company's own
release about itself is <code>self</code>, forever.</p>
<div class="qo-table-wrap"><table class="qo-table">
<tr><th>ID</th><th>Source</th><th>Publisher</th><th>Family</th><th>Published</th><th>Retrieved</th><th>Note</th></tr>
%s</table></div>
""" % "".join(rows)
    return observatory_base(
        title="Sources · Quantum Observatory",
        description="The source registry: publisher, family, publication and retrieval dates for every citation in the ledgers.",
        content=content,
        current="sources.html",
    )


# ---------------------------------------------------------------- build


def load_pages() -> dict[str, dict[str, str]]:
    pages: dict[str, dict[str, str]] = {}
    for path in sorted(PAGES_DIR.glob("*.md")):
        meta, body = build_garden.parse_front_matter(path.read_text(encoding="utf-8"))
        pages[meta["slug"]] = {**meta, "body": body}
    return pages


def build() -> int:
    store = observatory_lib.load_store()
    schema = observatory_lib.load_schema()
    errors = observatory_lib.validate(store, schema)
    if errors:
        for err in errors:
            print("FAIL  %s" % err)
        print("\nStore invalid — no output written. Fail closed.")
        return 1

    pages_src = load_pages()
    written: dict[str, str] = {}
    written["index.html"] = page_index(store)
    written["methodology.html"] = page_methodology(store)
    written["companies.html"] = page_companies(store)
    written["architectures.html"] = page_architectures(store)
    written["institutions.html"] = page_institutions(store)
    written["evidence.html"] = page_evidence(store)
    written["forecasts.html"] = page_forecasts(store)
    written["bottlenecks.html"] = page_bottlenecks(store)
    written["graph.html"] = page_graph(store)
    written["hindcast.html"] = page_hindcast(store)
    written["questions.html"] = page_questions(store)
    written["sources.html"] = page_sources(store)

    for company in _entries(store, "companies"):
        if company["depth"] != "case_study":
            continue
        slug = company["id"][3:]
        if slug not in pages_src:
            print("FAIL  company %s is case_study depth but pages/%s.md is missing" % (company["id"], slug))
            return 1
        written["%s.html" % slug] = company_page(store, company, pages_src[slug])

    OUTPUT_DIR.mkdir(exist_ok=True)
    expected = set(written)
    for name in sorted(OUTPUT_DIR.glob("*.html")):
        if name.name not in expected:
            name.unlink()
    issues = 0
    for name, doc in sorted(written.items()):
        path = OUTPUT_DIR / name
        path.write_text(doc, encoding="utf-8")
        errs = build_garden.check_well_formed(path)
        for err in errs:
            print("FAIL  %s: %s" % (name, err))
            issues += 1
    if issues:
        print("\n%d malformed output page(s)." % issues)
        return 1
    print(
        "ok    observatory: %d pages written to %s (as_of %s)"
        % (len(written), OUTPUT_DIR, observatory_lib.store_as_of(store))
    )
    return 0


if __name__ == "__main__":
    sys.exit(build())
