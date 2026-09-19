# Quantum Observatory — operator's guide

The observatory is Compute Ecology's instrument for the quantum-computing
field: a bitemporal ledger of claims, evidence, forecasts, bottlenecks, and
beliefs, rendered as a static site under `observatory/`.

Read `DESIGN.md` first — it is the controlling document for the architecture.
`AUDIT.md` records the repository audit that preceded Genesis.

## Layout

```
observatory_src/
  AUDIT.md      — what the repo already provides, what QO reuses, what it must not touch
  DESIGN.md     — architecture and epistemic rules (controlling spec)
  README.md     — this file
  data/*.json   — the ledgers (one file per collection)
  pages/*.md    — narrative bodies for case-study companies
  schema/collections.json — the machine-enforced field contract
scripts/
  observatory_lib.py        — load, validate, as-of views
  check_observatory.py      — verify only; exits nonzero on any issue
  build_observatory.py      — validate, then render to observatory/
tests/test_observatory.py   — contract, anti-hype, temporal, and render tests
```

## Daily operations

```bash
python3 scripts/check_observatory.py   # verify the store, write nothing
python3 scripts/build_observatory.py   # validate, then render observatory/
python3 -m unittest discover -s tests  # whole suite, including QO tests
```

The build **fails closed**: any validator error means zero bytes written.

## The two clocks

- `recorded_on` — transaction time: the day the entry entered the ledger.
- Domain dates (`date`, `published`, `achieved_on`, `resolves_by`) — when the
  fact is true in the world.

As-of query = `recorded_on <= T`. Belief snapshots are *reconstructions* of
what was knowable at a date: they may cite facts whose `recorded_on` is later,
but the fact's domain date AND at least one of its sources' `published` date
must precede the snapshot's `as_of`. The validator enforces both.

## Adding an entry

1. Add the source(s) to `data/sources.json`. Publisher family is relative to
   the *subject*: a company's release about itself is `self`, a national lab's
   page about its own award is `government`, trade press is
   `independent_press`. Preserve source identity and retrieval date; do not
   vendor licensed text.
2. Add the entry to the right collection with a unique lowercase-dashed id.
   If the fact is a company announcement it is a **claim**, never evidence.
3. Evidence entries carry `evidence_class` on the ladder
   `company_claim < technical_disclosure < peer_review < independent_benchmark
   < independent_testbed < replication < system_utility`. Classes at or above
   `independent_benchmark` require `measured_by_family != "self"`,
   `independent_of_subject: true`, and at least one non-self source family.
4. `recorded_on` = the day you commit it. Never postdate a file's `as_of`
   watermark; bump the watermark the day you add entries.
5. Run the checker. Fix every FAIL — do not work around it.

## Things that are deliberately absent

- No headline score. Confidence is decomposed per axis; `not_yet_estimable`
  is a first-class value and renders as an empty track.
- No automated crawl of company news. Ingestion is deliberate: a claim enters
  when a human (or an operator-directed agent) decides it is worth recording
  and cites the source.
- No forecast may exist without `resolution_criteria` and `resolves_by`.

## When the rules block you

If the validator rejects an entry you believe is correct, the model is telling
you something is misclassified — promotion press into evidence, self-measurement
into independence, a promise into an achievement. Restate the entry at the
lower rung, or capture the missing independent source first. UNKNOWN is
acceptable. Fabricated precision is not.
