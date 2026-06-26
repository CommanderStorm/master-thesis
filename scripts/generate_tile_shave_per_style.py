# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "plotly>=6.0",
#     "pandas>=2.0",
#     "kaleido>=0.4",
# ]
# ///

import argparse
from pathlib import Path

import plotly.graph_objects as go

from _common import fmt_bytes, journal_layout, load_jsonl_df

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
OUTPUT_DIR = SCRIPT_DIR.parent / "figures"
FORMATS = ["png", "pdf"]

FIG_WIDTH = 720
FIG_HEIGHT = 272

BAR_COLOR = "#0072B2"
BAR_COLOR_ALT = "#56B4E9"

LAYOUT_DEFAULTS = journal_layout(margin=dict(l=110, r=60, t=20, b=55))


def export_figure(fig: go.Figure, name: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for fmt in FORMATS:
        path = OUTPUT_DIR / f"{name}.{fmt}"
        fig.write_image(str(path), scale=2, width=FIG_WIDTH, height=FIG_HEIGHT)
        print(f"  -> {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=Path,
        default=DATA_DIR / "tile_shave_per_style.jsonl",
    )
    args = parser.parse_args()

    df = load_jsonl_df(args.input)
    df = df.sort_values("reduction_pct", ascending=True)

    print(f"Loaded {len(df)} styles")
    print(f"  Reduction range: {df['reduction_pct'].min():.1f}% - {df['reduction_pct'].max():.1f}%")
    print(f"  Mean reduction:  {df['reduction_pct'].mean():.1f}%")
    print(f"  Median reduction: {df['reduction_pct'].median():.1f}%")
    print()

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=df["style_id"],
        x=df["reduction_pct"],
        orientation="h",
        marker_color=BAR_COLOR,
        text=[f"{v:.1f}%" for v in df["reduction_pct"]],
        textposition="outside",
        textfont=dict(size=12),
    ))

    fig.update_layout(
        **LAYOUT_DEFAULTS,
        xaxis_title="Tile data reduction (%)",
        xaxis=dict(range=[0, max(df["reduction_pct"]) * 1.15]),
        yaxis_title=None,
        showlegend=False,
    )

    print("Generating tile_shave_per_style figure:")
    export_figure(fig, "tile_shave_per_style")
    print()

    print("LaTeX-ready stats:")
    print(f"  Min reduction:  {df['reduction_pct'].min():.1f}%  ({df.iloc[0]['style_id']})")
    print(f"  Max reduction:  {df['reduction_pct'].max():.1f}%  ({df.iloc[-1]['style_id']})")
    print(f"  Mean reduction: {df['reduction_pct'].mean():.1f}%")
    print(f"  Median:         {df['reduction_pct'].median():.1f}%")
    print(f"  Total dropped:  {df['tiles_dropped'].sum()} tiles across all styles")
    print()

    for _, row in df.iterrows():
        print(f"  {row['style_id']:20s}  {fmt_bytes(row['original_bytes'])} -> {fmt_bytes(row['pruned_bytes'])}  "
              f"({row['reduction_pct']:.1f}%, {int(row['tiles_dropped'])} dropped)")


if __name__ == "__main__":
    main()
