#!/usr/bin/env python3
"""Verify the Quantum Observatory store — standalone, no rendering.

Runs the full contract in ``observatory_src/schema/collections.json`` plus the
anti-hype and temporal-integrity rules, then exits nonzero on any issue.
Fail closed by design: a corrupt or leaky store must stop the build, the same
way a failed gate stops a publish.

Usage:
    python3 scripts/check_observatory.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import observatory_lib


def main() -> int:
    store = observatory_lib.load_store()
    schema = observatory_lib.load_schema()
    errors = observatory_lib.validate(store, schema)
    counts = {
        name: len(doc.get("entries", []))
        for name, doc in store.items()
        if isinstance(doc, dict) and isinstance(doc.get("entries"), list)
    }
    for err in errors:
        print("FAIL  %s" % err)
    if errors:
        print("\n%d issue(s). The store is not publishable." % len(errors))
        return 1
    total = sum(counts.values())
    detail = ", ".join("%s=%d" % kv for kv in sorted(counts.items()))
    print(
        "ok    observatory store: %d entries (%s); as_of %s"
        % (total, detail, observatory_lib.store_as_of(store))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
