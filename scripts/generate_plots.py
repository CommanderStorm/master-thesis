# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "plotly>=6.0",
#     "pandas>=2.0",
#     "numpy>=1.24",
#     "kaleido>=0.4",
# ]
# ///

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from _common import journal_layout

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
OUTPUT_DIR = SCRIPT_DIR.parent / "figures"
FORMATS = ["pdf"]

FIG_WIDTH = 720
FIG_HEIGHT = 440

# Okabe-Ito palette (CVD-safe)
SOURCE_COLORS = {
    "MVT": "#0072B2",
    "MVT-shaved": "#56B4E9",
    "MLT-Java": "#E69F00",
    "MLT-Rust": "#009E73",
    "MLT-Rust-shaved": "#CC79A7",
}

SOURCE_PATTERNS = {
    "MVT": "",
    "MVT-shaved": "/",
    "MLT-Java": "\\",
    "MLT-Rust": "x",
    "MLT-Rust-shaved": ".",
}

SOURCE_MARKERS = {
    "MVT": "circle",
    "MVT-shaved": "square",
    "MLT-Java": "diamond",
    "MLT-Rust": "triangle-up",
    "MLT-Rust-shaved": "cross",
}

SOURCE_DISPLAY = {
    "MVT": "MVT",
    "MVT-shaved": "MVT (shaved)",
    "MLT-Java": "MLT (reference)",
    "MLT-Rust": "MLT (this work)",
    "MLT-Rust-shaved": "MLT (this work, shaved)",
}

COMPRESSION_DASHES = {
    "plain": "solid",
    "gzip": "dash",
    "brotli": "dot",
    "zstd": "dashdot",
}

LAYOUT_DEFAULTS = journal_layout()


def export_figure(
    fig: go.Figure, name: str,
    width: int = FIG_WIDTH, height: int = FIG_HEIGHT,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for fmt in FORMATS:
        path = OUTPUT_DIR / f"{name}.{fmt}"
        fig.write_image(str(path), scale=2, width=width, height=height)
        print(f"  → {path}")


def plot_encoder_comparison_per_zoom(df: pd.DataFrame) -> None:
    print("Generating encoder_comparison_per_zoom…")

    compressions = ["plain", "gzip", "brotli", "zstd"]
    comp_titles = {
        "plain": "Plain (uncompressed)",
        "gzip": "Gzip",
        "brotli": "Brotli",
        "zstd": "Zstd",
    }
    abs_positions = {"plain": (1, 1), "gzip": (1, 2), "brotli": (2, 1), "zstd": (2, 2)}
    rel_positions = {"plain": (3, 1), "gzip": (3, 2), "brotli": (4, 1), "zstd": (4, 2)}

    fig = make_subplots(
        rows=4, cols=2,
        subplot_titles=[comp_titles[c] for c in compressions] +
                       [f"{comp_titles[c]} - % of MVT" for c in compressions],
        shared_xaxes=False,
        vertical_spacing=0.10,
        horizontal_spacing=0.08,
    )

    show_legend_for: set[str] = set()

    for comp in compressions:
        sub = df[df["compression"] == comp]
        row, col = abs_positions[comp]
        for source in ["MVT", "MLT-Java", "MLT-Rust"]:
            s = sub[sub["source"] == source].sort_values("zoom")
            if s.empty:
                continue
            show = source not in show_legend_for
            show_legend_for.add(source)
            fig.add_trace(go.Bar(
                x=s["zoom"],
                y=s["total_bytes"],
                name=SOURCE_DISPLAY[source],
                marker_color=SOURCE_COLORS[source],
                marker_pattern_shape=SOURCE_PATTERNS[source],
                showlegend=show,
                legendgroup=source,
            ), row=row, col=col)

        mvt = sub[sub["source"] == "MVT"].set_index("zoom")["total_bytes"]
        row, col = rel_positions[comp]
        for source in ["MLT-Java", "MLT-Rust"]:
            s = sub[sub["source"] == source].sort_values("zoom").set_index("zoom")
            if s.empty:
                continue
            common = mvt.index.intersection(s.index)
            ratio_pct = (s.loc[common, "total_bytes"] / mvt.loc[common]) * 100
            fig.add_trace(go.Bar(
                x=list(common),
                y=ratio_pct.values,
                marker_color=SOURCE_COLORS[source],
                marker_pattern_shape=SOURCE_PATTERNS[source],
                showlegend=False,
                legendgroup=source,
            ), row=row, col=col)
        if col == 2:
            fig.add_hline(
                y=100, line_dash="dash", line_color=SOURCE_COLORS["MVT"],
                row=row, col=col,
                annotation_text="MVT",
                annotation_position="top right",
            )
        else:
            fig.add_hline(
                y=100, line_dash="dash", line_color=SOURCE_COLORS["MVT"],
                row=row, col=col,
            )

    fig.update_layout(
        **LAYOUT_DEFAULTS,
        barmode="group",
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5,
            yanchor="top",
            y=-0.08,
            bgcolor="rgba(255,255,255,0.8)",
        ),
        height=1440,
    )
    for r in (1, 2, 3, 4):
        fig.update_xaxes(
            title_text="Zoom level",
            title_standoff=5,
            dtick=2,
            row=r,
        )
    fig.update_yaxes(row=1, col=1, title_text="Total size (bytes)")
    fig.update_yaxes(row=2, col=1, title_text="Total size (bytes)")
    fig.update_yaxes(row=3, col=1, title_text="% of MVT")
    fig.update_yaxes(row=4, col=1, title_text="% of MVT")
    fig.update_annotations(font_size=22)

    export_figure(fig, "encoder_comparison_per_zoom", height=1440)


def plot_shaving_effectiveness_per_zoom(df: pd.DataFrame) -> None:
    print("Generating shaving_effectiveness_per_zoom…")

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=["Plain (uncompressed)", "Gzip", "Brotli", "Zstd"],
        shared_xaxes=True,
        shared_yaxes=True,
        vertical_spacing=0.12,
        horizontal_spacing=0.08,
    )

    positions = {"plain": (1, 1), "gzip": (1, 2), "brotli": (2, 1), "zstd": (2, 2)}
    show_legend_for: set[str] = set()
    series = ["MVT", "MVT-shaved", "MLT-Rust", "MLT-Rust-shaved"]
    # No reference MLT here, so short labels stay unambiguous and fit one row.
    short_names = {
        "MVT": "MVT",
        "MVT-shaved": "MVT (shaved)",
        "MLT-Rust": "MLT",
        "MLT-Rust-shaved": "MLT (shaved)",
    }

    for comp, (row, col) in positions.items():
        sub = df[df["compression"] == comp]
        for source in series:
            s = sub[sub["source"] == source].sort_values("zoom")
            if s.empty:
                continue
            show = source not in show_legend_for
            show_legend_for.add(source)
            fig.add_trace(go.Bar(
                x=s["zoom"],
                y=s["total_bytes"],
                name=short_names[source],
                marker_color=SOURCE_COLORS[source],
                marker_pattern_shape=SOURCE_PATTERNS[source],
                showlegend=show,
                legendgroup=source,
            ), row=row, col=col)

    fig.update_layout(
        **journal_layout(margin=dict(l=70, r=20, t=30, b=95)),
        barmode="group",
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5,
            yanchor="top",
            y=-0.18,
            bgcolor="rgba(0,0,0,0)",
        ),
    )
    fig.update_xaxes(title_text="Zoom level", dtick=2, row=2)
    fig.update_yaxes(row=1, col=1, title_text="Total size (bytes)")
    fig.update_yaxes(row=2, col=1, title_text="Total size (bytes)")
    fig.update_annotations(font_size=15)

    export_figure(fig, "shaving_effectiveness_per_zoom", height=470)


def plot_compression_ratio_per_zoom(df: pd.DataFrame) -> None:
    print("Generating compression_ratio_per_zoom…")

    fig = go.Figure()

    for comp in ["plain", "gzip", "brotli", "zstd"]:
        sub = df[df["compression"] == comp]
        mvt = sub[sub["source"] == "MVT"].set_index("zoom")["total_bytes"]

        for source in ["MLT-Java", "MLT-Rust"]:
            src = sub[sub["source"] == source].set_index("zoom")["total_bytes"]
            if src.empty:
                continue
            common = mvt.index.intersection(src.index)
            ratio = src.loc[common] / mvt.loc[common]

            fig.add_trace(go.Scatter(
                x=list(common),
                y=ratio.values,
                mode="lines+markers",
                name=f"{SOURCE_DISPLAY[source]} / {comp}",
                marker=dict(color=SOURCE_COLORS[source], size=7, symbol=SOURCE_MARKERS[source]),
                line=dict(color=SOURCE_COLORS[source], width=2, dash=COMPRESSION_DASHES[comp]),
                hovertemplate=f"{SOURCE_DISPLAY[source]} ({comp})<br>Zoom %{{x}}<br>Ratio: %{{y:.3f}}<extra></extra>",
            ))

    fig.add_hline(y=1.0, line_dash="dash", line_color=SOURCE_COLORS["MVT"], annotation_text="1.0 (parity)")

    fig.update_layout(
        **LAYOUT_DEFAULTS,
        xaxis=dict(title="Zoom level", dtick=1),
        yaxis=dict(title="Size ratio vs MVT"),
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)"),
    )

    export_figure(fig, "compression_ratio_per_zoom")


MODE_COLORS = {
    "hybrid": "#009E73",
    "only-trigram": "#E69F00",
    "only-plain": "#0072B2",
}

MODE_PATTERNS = {
    "hybrid": "",
    "only-trigram": "/",
    "only-plain": "\\",
}


def plot_minhash_sweep(df: pd.DataFrame) -> None:
    print("Generating minhash_sweep…")

    fig = go.Figure()

    for mode in ["hybrid", "only-trigram", "only-plain"]:
        sub = df[df["mode"] == mode].sort_values("threshold")
        fig.add_trace(go.Bar(
            x=sub["threshold"],
            y=sub["total_bytes"],
            name=mode,
            marker_color=MODE_COLORS[mode],
            marker_pattern_shape=MODE_PATTERNS[mode],
        ))

    y_min = df["total_bytes"].min()
    y_max = df["total_bytes"].max()
    y_pad = (y_max - y_min) * 0.3
    fig.update_layout(
        **LAYOUT_DEFAULTS,
        barmode="group",
        xaxis=dict(title="Jaccard similarity threshold", dtick=0.025),
        yaxis=dict(
            title="Total mbtiles size (bytes)",
            range=[y_min - y_pad, y_max + y_pad],
        ),
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)"),
    )

    export_figure(fig, "minhash_sweep")


_MLT_CONFIG_MAP = {
    "step-00-baseline": "1: MVT baseline",
    "step-16-selectivity_reorder": "2: Style-only",
    "step-17-tile_shave_only": "3: Shaving-only",
    "step-18-tile_shave": "4: Style+shaving",
    "step-19-tile_rewrite": "5: Style+shaving+MLT",
}


def _load_mlt_config_ci() -> pd.DataFrame | None:
    ci_csv = DATA_DIR / "confidence_intervals.csv"
    if not ci_csv.exists():
        return None
    ci = pd.read_csv(ci_csv)
    ci = ci[ci["style"].isin(["fiord", "liberty"]) & ci["variant"].isin(_MLT_CONFIG_MAP)]
    if ci.empty:
        return None
    ci["config"] = ci["variant"].map(_MLT_CONFIG_MAP)
    return ci[["style", "config", "metric", "median", "ci_lo", "ci_hi"]].copy()


def main() -> None:
    tile_sizes_csv = DATA_DIR / "tile_sizes.csv"
    if not tile_sizes_csv.exists():
        sys.exit(f"tile_sizes.csv not found at {tile_sizes_csv}\nRun generate_data.py first.")

    df = pd.read_csv(tile_sizes_csv)

    plot_encoder_comparison_per_zoom(df)
    plot_shaving_effectiveness_per_zoom(df)
    plot_compression_ratio_per_zoom(df)

    sweep_csv = DATA_DIR / "minhash_sweep.csv"
    if sweep_csv.exists():
        sweep_df = pd.read_csv(sweep_csv)
        plot_minhash_sweep(sweep_df)
    else:
        print("\nSkipped: minhash_sweep (run generate_minhash_sweep.py first)")

    parser = argparse.ArgumentParser(description="Generate thesis figures.")
    parser.add_argument("--bench", type=Path, nargs="*", help="Benchmark JSONL file(s) with tile_shave variants")
    args, _ = parser.parse_known_args()

    if args.bench:
        bench_df = load_bench_jsonl(args.bench)
        if bench_df is not None:
            plot_interaction(bench_df)
    else:
        print("\nSkipped: interaction_plot (pass --bench <jsonl> with tile_shave data)")

    plot_rendering_metrics_mlt()

    print(f"\nAll figures written to {OUTPUT_DIR}")


# step-15 (no selectivity) and step-16 (with selectivity) both collapse into "style-only"
CONFIG_MAP = {
    "step-00-baseline": "1: MVT baseline",
    "step-15-layer_merge": "2: Style-only",
    "step-16-selectivity_reorder": "2: Style-only",
    "step-17-tile_shave_only": "3: Shaving-only",
    "step-18-tile_shave": "4: Style+shaving",
    "step-19-tile_rewrite": "5: Style+shaving+MLT",
}

CONFIG_COLORS = {
    "1: MVT baseline":      "#0072B2",
    "2: Style-only":        "#E69F00",
    "3: Shaving-only":      "#56B4E9",
    "4: Style+shaving":     "#009E73",
    "5: Style+shaving+MLT": "#CC79A7",
}

CONFIG_PATTERNS = {
    "1: MVT baseline":      "",
    "2: Style-only":        "/",
    "3: Shaving-only":      "\\",
    "4: Style+shaving":     "x",
    "5: Style+shaving+MLT": ".",
}


def load_bench_jsonl(paths: list[Path]) -> pd.DataFrame | None:
    rows = []
    for p in paths:
        with open(p) as f:
            for line in f:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    if not rows:
        print("No benchmark data found.", file=sys.stderr)
        return None
    df = pd.DataFrame(rows)
    df = df[df["variant"].isin(CONFIG_MAP)]
    if df.empty:
        print("Benchmark JSONL has no tile_shave variants - skipping interaction/rendering plots.")
        return None
    df["config"] = df["variant"].map(CONFIG_MAP)
    print(f"\nLoaded {len(df)} benchmark records for configs: {sorted(df['config'].unique())}")
    return df


def plot_interaction(df: pd.DataFrame) -> None:
    print("Generating interaction_plot…")

    medians = df.groupby(["config", "style", "scenario"])["tile_bytes"].median().reset_index()

    baseline = medians[medians.config == "1: MVT baseline"].groupby("style")["tile_bytes"].median()
    shave_only = medians[medians.config == "3: Shaving-only"].groupby("style")["tile_bytes"].median()
    combined = medians[medians.config == "4: Style+shaving"].groupby("style")["tile_bytes"].median()

    styles = sorted(baseline.index)
    if not styles:
        print("  (skipped - not enough config data)")
        return

    # Fail loud if a style is missing from either series: the old `.get(s, baseline[s])`
    # fallback silently plotted a fake 0% reduction bar (since 1 - baseline/baseline = 0).
    missing = [s for s in styles if s not in shave_only.index or s not in combined.index]
    if missing:
        raise SystemExit(f"missing shave/combined data for styles: {missing}")
    shave_pct = [(1 - shave_only[s] / baseline[s]) * 100 for s in styles]
    combined_pct = [(1 - combined[s] / baseline[s]) * 100 for s in styles]

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Shaving-only (baseline advisory)", x=styles, y=shave_pct,
                         marker_color=CONFIG_COLORS["3: Shaving-only"],
                         marker_pattern_shape=CONFIG_PATTERNS["3: Shaving-only"]))
    fig.add_trace(go.Bar(name="Style+shaving (optimized advisory)", x=styles, y=combined_pct,
                         marker_color=CONFIG_COLORS["4: Style+shaving"],
                         marker_pattern_shape=CONFIG_PATTERNS["4: Style+shaving"]))

    fig.update_layout(
        **LAYOUT_DEFAULTS,
        barmode="group",
        xaxis=dict(title="Style"),
        yaxis=dict(title="% Tile Data Reduction vs Baseline"),
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)"),
    )
    export_figure(fig, "interaction_plot")


def plot_rendering_metrics_mlt() -> None:
    # one panel per (style, metric), exported as standalone PDF so LaTeX can
    # lay them out as subfigures
    print("Generating rendering_metrics_mlt panels…")

    ci = _load_mlt_config_ci()
    if ci is None:
        print("  Skipped (run generate_ci.py first)")
        return

    styles = ["fiord", "liberty"]
    metrics = ["loadMs", "fps"]
    y_titles = {"loadMs": "Load Time (ms)", "fps": "FPS"}

    config_order = [
        "1: MVT baseline",
        "2: Style-only",
        "3: Shaving-only",
        "4: Style+shaving",
        "5: Style+shaving+MLT",
    ]

    for style in styles:
        for metric in metrics:
            sub = ci[(ci["style"] == style) & (ci["metric"] == metric)]
            sub = sub.set_index("config").reindex(config_order)

            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=config_order,
                y=sub["median"].values,
                marker_color=[CONFIG_COLORS.get(c, "#999") for c in config_order],
                marker_pattern_shape=[CONFIG_PATTERNS.get(c, "") for c in config_order],
                error_y=dict(
                    type="data", symmetric=False,
                    array=(sub["ci_hi"] - sub["median"]).values,
                    arrayminus=(sub["median"] - sub["ci_lo"]).values,
                ),
                showlegend=False,
            ))
            fig.update_yaxes(title_text=y_titles[metric], automargin=True)
            fig.update_xaxes(tickangle=-45, automargin=True)
            layout = {
                **LAYOUT_DEFAULTS,
                "margin": dict(l=70, r=20, t=20, b=80),
            }
            fig.update_layout(**layout)

            export_figure(
                fig, f"rendering_metrics_mlt_{style}_{metric}",
                width=700, height=525,
            )


if __name__ == "__main__":
    main()
