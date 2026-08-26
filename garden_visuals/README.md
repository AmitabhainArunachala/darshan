# Darshan visual sources

These files are editorial source, not decoration metadata. Each room receives
three to five teaching visuals bound to specific H2/H3 IDs in its reviewed
Markdown. The first complete planting uses three per room; longer rooms can
grow without changing the renderer contract.

The contract is deliberately narrow:

- `after` must name a real generated heading ID in the same room.
- `claim_scope` defaults to `section-synthesis`. A visual that combines material
  from several sections must declare `room-synthesis` and enumerate two to
  eight real `evidence_sections`; placement and evidence are never conflated.
- `kind` is one of `sequence`, `layers`, `timeline`, `contrast`, or
  `constellation`.
- Every visual has a kicker, title, caption, and three to six labeled items.
- A visual may restate or organize claims already in its room. It must not add
  unsupported facts, numbers, quotations, or causal claims.
- Each rendered room must contain three to five teaching visuals and one shared
  series artwork.
- The renderer exposes each figure's placement and evidence headings as visible
  links and machine-readable attributes; this makes source scope challengeable
  instead of leaving it implicit.

`scripts/build_garden.py --strict` validates this contract, checks the source
artwork, inserts each visual beside its evidence section, and fails if anything
is missing or drifts.

Each manifest also preserves the exact built-in image-generation prompt for its
series plate. Full-resolution PNG masters and compact WebP delivery copies live
in `garden_assets/series/`; the generated site ships both through `<picture>` so
modern browsers avoid downloading the much larger fallback.

Independent review lives in `_verdicts/<series>.json`. Each room verdict binds
both the exact Markdown bytes and a canonical SHA-256 digest of that room's raw
visual entry. `scripts/check_garden.py` rejects missing, stale, malformed, or
still-FIX visual verdicts, so a polished panel cannot silently outrun its
evidence boundary.
