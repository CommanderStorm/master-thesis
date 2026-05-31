## Abstract

- **investigating automatic, joint style and data optimization for MapLibre-based map rendering pipelines**
  - source: `00_abstract.tex:1`
  - type: `scope`

- **Interactive web maps built on vector tiles face complex performance constraints**
  - source: `00_abstract.tex:2`
  - type: `qualitative`

- **Every frame requires fetching tiles over the network, decoding them, evaluating style expressions for each feature, and submitting draw calls to the graphics API**
  - source: `00_abstract.tex:3`
  - type: `scope`

- **style authoring and tile data preparation have traditionally been treated as independent concerns**
  - source: `00_abstract.tex:4`
  - type: `qualitative`

- **optimizer operates at three levels**
  - source: `00_abstract.tex:6`
  - type: `number`

- **Expression rewrites via peephole rules to style's JSON expressions via fixpoint iteration, including constant folding, algebraic simplification, stats-driven folding from tile statistics, and selectivity-based predicate reordering**
  - source: `00_abstract.tex:8`
  - type: `scope`

- **structural passes work on a typed representation of the full style document to do dead layer elimination, metadata refinement, layer merging, and cleanup**
  - source: `00_abstract.tex:9`
  - type: `scope`

- **pruning advisory derived from the optimized style removes unused properties, geometry types, and feature values, and the surviving content is re-encoded into the columnar MapLibre Tiles format with automatic encoding strategy selection**
  - source: `00_abstract.tex:11`
  - type: `scope`

- **evaluated across 15 styles and 18 scenarios**
  - source: `00_abstract.tex:13`
  - type: `number`

- **running 19 cumulative ablation steps and one plain-tile-shaving comparison**
  - source: `00_abstract.tex:13`
  - type: `number`

- **Tile shaving dominates load-time improvements, achieving load-time reductions of 63–74% (median 71%) and FPS gains of 100–200% (median 152%) across the ten deep-corpus styles we benchmarked end-to-end**
  - source: `00_abstract.tex:14`
  - type: `number`

- **For the 11 OMT-compatible styles where we measured tile shaving without browser rendering, shaving effectiveness varied 19.8–46.3%**
  - source: `00_abstract.tex:15`
  - type: `number`

- **MLT encoder reduces total tile volume by 28% over the reference encoder and 12% over gzip-compressed MVT on the Germany \ac{OMT} tileset**
  - source: `00_abstract.tex:16`
  - type: `number`

- **Style-level optimizations alone reduce style transfer size, primarily benefiting initial load**
  - source: `00_abstract.tex:17`
  - type: `qualitative`

- **Across 13 unseen styles in a static-only generalization corpus the static passes produce a median 31.4% raw reduction (after gzip median 11.4%, range 3.9–22.4%) with identical rendering output**
  - source: `00_abstract.tex:18`
  - type: `number`

- **two levels compose additively rather than synergistically at the aggregate level**
  - source: `00_abstract.tex:19`
  - type: `qualitative`

- **Per-scenario synergy appears in 17 of 36 style-scenario pairs**
  - source: `00_abstract.tex:20`
  - type: `number`
