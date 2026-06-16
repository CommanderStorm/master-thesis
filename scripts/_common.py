from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import pandas as pd


def load_jsonl_dir(input_dir: Path) -> list[dict]:
    """Load every *.jsonl file under input_dir into a flat list of records.
    """
    rows: list[dict] = []
    skipped = 0
    for path in sorted(input_dir.glob("*.jsonl")):
        with path.open() as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    skipped += 1
                    print(f"WARNING: skipping malformed JSON at {path}:{lineno}: {exc}",
                          file=sys.stderr)
    if skipped:
        print(f"WARNING: skipped {skipped} malformed line(s) total", file=sys.stderr)
    if not rows:
        raise SystemExit(f"No JSONL files found under {input_dir}")
    return rows


def load_jsonl_df(path: Path) -> "pd.DataFrame":
    """Load a single JSONL file into a DataFrame, one record per non-blank line."""
    import pandas as pd

    rows: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if not rows:
        raise SystemExit(f"No data found in {path}")
    return pd.DataFrame(rows)


def fmt_bytes(val: float) -> str:
    """Format a byte count with a human-readable unit suffix."""
    if val >= 1e9:
        return f"{val / 1e9:.2f} GB"
    if val >= 1e6:
        return f"{val / 1e6:.1f} MB"
    if val >= 1e3:
        return f"{val / 1e3:.0f} KB"
    return f"{val:.0f} B"
