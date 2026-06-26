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


# Journal figure style, kept in sync with maplibre-optimiser/tests/bench/plot_style.py.
# plotly is imported lazily so plotly-free consumers (generate_ci.py) can import this.
FONT_FAMILY = "Liberation Serif, Nimbus Roman, Times New Roman, Times, DejaVu Serif, serif"
FONT_SIZE = 15
FONT_COLOR = "#000000"

_COLORWAY = [
    "#0072B2", "#D55E00", "#009E73", "#E69F00",
    "#CC79A7", "#56B4E9", "#F0E442", "#000000",
]


def register_journal_template() -> None:
    """Register the ``journal`` plotly template (idempotent)."""
    import plotly.graph_objects as go
    import plotly.io as pio

    if "journal" in pio.templates:
        return

    axis = dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        linecolor=FONT_COLOR,
        linewidth=1,
        ticks="outside",
        tickcolor=FONT_COLOR,
        ticklen=4,
        tickfont=dict(color=FONT_COLOR),
        title=dict(font=dict(color=FONT_COLOR)),
        automargin=True,
    )
    template = go.layout.Template()
    template.layout = go.Layout(
        font=dict(family=FONT_FAMILY, size=FONT_SIZE, color=FONT_COLOR),
        title=dict(font=dict(family=FONT_FAMILY, color=FONT_COLOR)),
        paper_bgcolor="white",
        plot_bgcolor="white",
        colorway=_COLORWAY,
        xaxis=dict(axis),
        yaxis=dict(axis),
        legend=dict(
            font=dict(color=FONT_COLOR),
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0,
        ),
    )
    pio.templates["journal"] = template


def journal_layout(**overrides: Any) -> dict:
    """``update_layout`` defaults for the journal template; ``overrides`` win."""
    register_journal_template()
    base = dict(
        template="journal",
        font=dict(family=FONT_FAMILY, size=FONT_SIZE, color=FONT_COLOR),
        margin=dict(l=70, r=20, t=30, b=55),
    )
    base.update(overrides)
    return base


def fmt_bytes(val: float) -> str:
    """Format a byte count with a human-readable unit suffix."""
    if val >= 1e9:
        return f"{val / 1e9:.2f} GB"
    if val >= 1e6:
        return f"{val / 1e6:.1f} MB"
    if val >= 1e3:
        return f"{val / 1e3:.0f} KB"
    return f"{val:.0f} B"
