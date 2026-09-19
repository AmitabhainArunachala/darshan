# Quantum Observatory — Genesis design

Schema namespace `darshan.qo/v1`. All data lives in `observatory_src/data/*.json`;
all generated output lands in `observatory/`. The store is canonical JSON —
`sort_keys`, two-space indent, UTF-8 — so diffs are meaningful and
`canonical_json_sha256` binds reviews to exact bytes.

## 1. Two clocks

Every ledger entry carries:

- `recorded_on` — *transaction time*: the date the entry entered this ledger.
  It is never backdated. Corrections are new entries, not edits of history.
- Domain time — when the thing is true in the world: `date` (event),
  `valid_from`/`valid_to` (interval facts), `made_on`/`resolves_by`
  (forecasts), `as_of` (snapshots).

An **as-of query** at date *T* returns exactly the entries with
`recorded_on <= T`. That is the whole mechanism: hindcasts are built from
`as_of` views, so nothing recorded later can leak into what "we believed" at
*T*. The validator enforces it structurally (see §6).

`UNKNOWN` is a first-class value — fields may carry it explicitly rather than
being omitted.

## 2. Entities

| File | Entry kind | Identity |
|---|---|---|
| `sources.json` | `source` | `src-*` |
| `institutions.json` | `institution` | `inst-*` |
| `capabilities.json` | `capability` (physical/supply-chain node) | `cap-*` |
| `architectures.json` | `architecture` | `arch-*` |
| `companies.json` | `company` | `co-*` |
| `claims.json` | `claim` | `cl-*` |
| `evidence.json` | `evidence` (a measurement or evaluation event) | `ev-*` |
| `milestones.json` | `milestone` (promised vs realized) | `ms-*` |
| `forecasts.json` | `forecast` | `fc-*` |
| `bottlenecks.json` | `bottleneck` | `bn-*` |
| `graph.json` | `nodes` + `edges` (value-accrual/dependency graph) | `gn-*` / `ge-*` |
| `beliefs.json` | `belief` entries inside dated `as_of` snapshots | `bl-*` |
| `questions.json` | `question` (unresolved research registry) | `q-*` |

IDs are stable, human-readable slugs (`co-quantum-motion`). All cross-references
must resolve; no orphan citations.

## 3. Source provenance and independence

A `source` records `publisher`, `url`, `kind`
(`press_release|journal_paper|preprint|government_page|regulatory_filing|standards_doc|conference|dataset|news|institution_page`),
`publisher_family` (`self|government|academic_journal|consortium|independent_press|research_lab`),
`published`, `retrieved`, `access` (`open|paywalled|registration`).

`source_family` chains matter more than URLs: two outlets reprinting one press
release are one family. The validator treats *independence* as a property of
the measuring body (`measured_by_family`), not of the URL.

## 4. The evidence ladder

`evidence_class` is an ordered enum:

```
company_claim < technical_disclosure < peer_review <
independent_benchmark < independent_testbed < replication < system_utility
```

Non-ladder event classes used in `claims.json` — `funding`, `selection`,
`procurement`, `partnership`, `roadmap` — are **claims**, never evidence. They
may sit beside the ladder; they may not stand on it.

Anti-hype invariants (enforced in `check_observatory.py`, not in prose):

- `evidence_class >= independent_benchmark` requires `measured_by_family != self`
  **and** the entry's `source_id` must not be a `self`-family source of the
  measured company.
- `procurement`/`funding`/`selection` claims may not be cited as `evidence`
  for any technical metric — a test fails if a resolved forecast or achieved
  milestone resolves through an evidence entry whose only source is a
  selection/procurement/funding announcement of the subject.
- A `forecast` requires `resolution_criteria` and `resolves_by`; a `resolved_*`
  forecast requires `resolution_evidence_ids`; `resolved_*` evidence must have
  `date <= resolved_on`.
- A `milestone` with `status: achieved` requires ≥1 `evidence_ids`; `slipped`
  requires `promised` < `achieved_on`-or-build `as_of`.

## 5. Confidence decomposition

Per company, the site renders four scored axes — `technical_architecture`,
`execution`, `market_utility`, `value_capture` — each of which is either
`{low, high}` (a bounded range) or the literal string `not_yet_estimable`,
plus four evidence blocks (increasing/decreasing confidence, unresolved
questions, next decisive observations, falsifiers). The estimator never emits
a single headline number. `not_yet_estimable` is a valid answer; the validator
requires a written reason for any numeric range.

## 6. Temporal integrity and hindcasts

`beliefs.json` is a list of snapshots `{as_of, entries: [{id, statement,
confidence, basis_evidence_ids}]}`. Rule: every `basis_evidence_ids` entry must
exist **and** have `recorded_on <= as_of`. The Genesis slice freezes
`as_of = 2024-12-31` — what the store would have shown before the 2025 NQCC
delivery and QBI Stage-B advancement — rendered beside the present state so
the calibration record starts now.

## 7. Rendering

`scripts/build_observatory.py`:

1. loads and validates the entire store (fail closed — no partial output);
2. renders `observatory/index.html`, one page per company, `architectures`,
   `institutions`, `evidence`, `forecasts`, `bottlenecks`, `graph`,
   `hindcast`, `questions`, `sources`, `methodology`;
3. draws charts as inline SVG computed from ledger rows — every plotted value
   is traceable to an `evidence`/`forecast`/`milestone` id shown on the page;
4. emits every page through `templates/base.html` and the `BalanceChecker`
   well-formedness gate;
5. contains **no wall-clock** — the only dates in output come from the data.

Determinism is testable: two builds are byte-identical.

## 8. Genesis population

- **Quantum Motion** — complete case study: MOS silicon-spin architecture,
  claim/evidence separation, NQCC testbed delivery, QBI Stage B position,
  bottlenecks, falsifiers, dependency graph.
- **Comparator: PsiQuantum** — photonic FBQC, US2QC→QBI Stage C, Omega chipset,
  GlobalFoundries manufacturing. Chosen because it shares the DARPA ladder at
  a different rung *and* a partially shared supplier ecology (cryogenics,
  foundry photonics) — the cross-architecture dependency view has something to
  compare against.
- Institutions: DARPA (QBI/US2QC), NQCC (testbeds), UKRI/Innovate UK, DOE/SLAC,
  QED-C, NPL, Metriq, EuroHPC-JU — each with exactly what it observes.
- Architecture registry covers every Stage-B modality so the map, not the
  marketing, decides scope.
