## Introduction

- **MapLibre GL JS and Mapbox GL JS deliver maps by streaming tiled geometry to the browser**
  - source: `01_intro.tex:8`
  - type: `name`

- **MapLibre GL JS last accessed 2026-05-28**
  - source: `01_intro.tex:8`
  - type: `url`

- **Mapbox GL JS last accessed 2026-05-28**
  - source: `01_intro.tex:8`
  - type: `url`

- **A slow network stalls the per-tile path; a battery- or thermally-bound device stalls the per-frame path**
  - source: `01_intro.tex:6-7`
  - type: `qualitative`

- **Direct energy measurement is outside the scope of this work**
  - source: `01_intro.tex:14`
  - type: `scope`

- **Unstable network connections on trains or aeroplanes translate to degraded user experiences**
  - source: `01_intro.tex:15`
  - type: `qualitative`

- **A style filter that matches on a property value may simplify to a form that no longer references this property after constant folding with tile-level statistics**
  - source: `01_intro.tex:20`
  - type: `qualitative`

## Research Goals

- **Automatic, style- and data-driven co-optimization for MapLibre-based map rendering pipelines**
  - source: `01_intro.tex:26`
  - type: `name`

- **Three research questions guide the work**
  - source: `01_intro.tex:27`
  - type: `number`

- **Techniques investigated: expression simplification, dead layer elimination, layer merging, tile shaving, columnar re-encoding**
  - source: `01_intro.tex:31`
  - type: `name`

- **The optimizer emits a replacement that is visually equivalent and strictly idempotent**
  - source: `01_intro.tex:36`
  - type: `qualitative`

## Contributions

- **No prior work treats both style and tile sides jointly under a soundness criterion**
  - source: `01_intro.tex:47`
  - type: `qualitative`

- **Style-driven tile shaving is novel**
  - source: `01_intro.tex:52-53`
  - type: `qualitative`

- **Adaptive multi-strategy encoding for MLT columnar format is novel**
  - source: `01_intro.tex:54`
  - type: `name`

- **Style-level passes refine the pruning advisory; cross-family interaction stays additive rather than synergistic**
  - source: `01_intro.tex:55`
  - type: `qualitative`

- **End-to-end implementation in Rust and Java**
  - source: `01_intro.tex:57`
  - type: `name`

- **Implementation integrates MapLibre style runtime and MLT tile pipeline**
  - source: `01_intro.tex:58`
  - type: `name`

- **Germany \ac{OMT} tileset provides encoder-only, style-independent baseline**
  - source: `01_intro.tex:61`
  - type: `name`

- **Ten-style \ac{OMT} deep corpus carries end-to-end browser benchmarks**
  - source: `01_intro.tex:62`
  - type: `number`

- **Eleven-style OMT-compatible subset measured for tile-shaving effectiveness only**
  - source: `01_intro.tex:63`
  - type: `number`

- **Thirteen-style Maputnik generalization corpus evaluated under static style passes alone**
  - source: `01_intro.tex:64`
  - type: `number`

- **Together they span 18 scenarios and 19 cumulative ablation steps under fixed pass ordering**
  - source: `01_intro.tex:65`
  - type: `number`

## Outline

- **Cumulative ablation across 15 styles and 18 scenarios**
  - source: `01_intro.tex:72`
  - type: `number`

- **Tile shaving and columnar re-encoding named as primary levers**
  - source: `01_intro.tex:72`
  - type: `qualitative`
