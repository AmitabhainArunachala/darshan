# Darshan

A publication for seeing clearly after the feed. Static, zero-dependency, no trackers.

Build the publication: `python3 scripts/build.py`.

Publish an approved article directly to the live site — no pull request:

```sh
python3 scripts/publish.py --dry-run   # full gate, tests, build, and exact diff
python3 scripts/publish.py             # publish changed articles and wait for Pages
```

Each article sent to `main` must declare:

```yaml
status: published
pipeline: readings-in-fire/2026-09-15-example-slug
```

The publisher locates that package in the canonical `dharma_swarm` checkout
or one of its registered worktrees, runs the canonical editorial checker, and
requires the pipeline `piece.md` body to match the site article exactly.
`draft` and `forthcoming` sources build locally but cannot use the direct
publisher. A rejected push leaves a local recovery branch; `--no-push` leaves
a local preview branch. Use `--include <file>` for an intentional stylesheet,
template, builder, or asset change.

Build the knowledge garden: `python3 scripts/build_garden.py --strict`. Sources
live in `garden_src/`; generated pages live in `garden/`, with
`garden/index.html` as the front door.

Verify the complete first planting and its independent verdicts:
`python3 scripts/check_garden.py`.

Seeing the Silicon was planted on 2026-09-02.

v0.0.0.1.
