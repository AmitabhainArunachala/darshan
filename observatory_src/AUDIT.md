# Repository audit — where the Quantum Observatory lands

Date: 2026-09-19 · Scope: `AmitabhainArunachala/darshan` @ `main`

## What the repo is

Darshan is a zero-dependency static publication. Articles in `articles/` are
built by `scripts/build.py` into standalone HTML. A knowledge garden in
`garden_src/` is built by `scripts/build_garden.py` into `garden/` — a
canonical 55-room taxonomy grouped into seven series, plus wing documents.
`scripts/check_garden.py` independently verifies the source/verdict contract:
every room must carry an independent verdict JSON bound to the exact source
bytes by SHA-256. `scripts/publish.py` is the gated direct-publish path for
articles. `tests/` holds `unittest` suites for the article builder and the
publisher.

Compute Ecology exists today as a doctrine document —
`garden_src/_wings/compute-ecology-guidestone.md` (`status: guiding`). It is
loaded by `build_garden.py` but skipped during render because wing publishing is
keyed to `WING_PAGES` (silicon → `seeing-the-silicon.html`). The closest
published surface is the *Seeing the Silicon* wing. One CE research artifact
lives at `research/portfolio-snapshots/2026-09-16-ai-compute-energy-40k-quick-portfolio-snapshot.md`.

## Reuse

- `templates/base.html` + `style.css`: masthead/footer chrome, theme toggle,
  `--paper/--rule/--faint/--accent` palette. Observatory pages reuse the base
  template verbatim via `render()`/`template()` imported from
  `scripts/build_garden.py`.
- `build_garden.parse_front_matter`, `md_to_html`, `check_well_formed`
  (`BalanceChecker`): narrative case-study pages are markdown with the same
  front-matter shape; generated HTML passes through the same well-formedness
  gate.
- `check_garden.canonical_json_sha256`: canonical JSON hashing, reused for
  ledger integrity.
- Convention: `X_src/` → generated `X/` at repo root, deterministic output,
  committed generated files.

## Extension (new code genuinely required)

- `observatory_src/` — ledgers (`data/`), declarative contracts (`schema/`),
  narrative pages (`pages/`), and this audit + design doc (`docs/`).
- `scripts/build_observatory.py` — validates the whole store, then renders
  `observatory/*.html`. Fails closed: any validation error → nothing written.
- `scripts/check_observatory.py` — standalone verifier for the same contract,
  so CI/reviewers can check without rendering.
- `tests/test_observatory.py` — schema, provenance, temporal, anti-hype,
  determinism, and negative-fixture tests.
- `observatory/` — generated pages.

## Conflicts found

- **PR "#56" (DARPA/Quantum Motion presentation) is not in this repository's
  history or any accessible repo** — GitHub code and PR search return no
  DARPA/Quantum-Motion presentation under `AmitabhainArunachala`. Per the spec's
  stop conditions, its content is treated as unavailable, not reconstructed;
  the sources it would have contributed are sourced directly instead.
- The garden's `REQUIRED_META`/room taxonomy is a teaching-room contract. The
  observatory is a data instrument, not a room — it is deliberately kept
  outside `SERIES`/`EXPECTED_SLUGS` so `check_garden.py`'s 55-room contract is
  untouched. One corridor link is added in the silicon wing source
  (`garden_src/_wings/silicon.md`) and one in `garden/index.html` generation
  is avoided — discoverability comes from the wing page and the observatory's
  own chrome.
- No migrations needed. `scripts/build.py`, `scripts/publish.py`,
  `scripts/build_garden.py`, `scripts/check_garden.py` are not modified.

## What is NOT built here

- No JS framework, no runtime, no database. The store is canonical JSON; the
  site is generated HTML+SVG. `as-of` queries are computed at build time into
  static snapshots.
- No wholesale ingestion. Sources carry citation metadata and retrieval dates;
  bodies are not vendored.
