## Summary of Contributions

- **joint style and tile co-optimization as a transformation $\mathcal{O}: \mathcal{S} \times \mathcal{T} \to \mathcal{S} \times \mathcal{T}$ under visual equivalence and strict idempotency**
  - source: `06_conclusion.tex:11`
  - type: `scope`

- **round-trip proptest and libFuzzer harness reported no soundness regressions across the corpus**
  - source: `06_conclusion.tex:13`
  - type: `name`

- **three-level co-optimization strategy**
  - source: `06_conclusion.tex:15`
  - type: `scope`

- **The three levels turn out to be complementary rather than redundant**
  - source: `06_conclusion.tex:16`
  - type: `qualitative`

- **Style-driven tile shaving is the dominant contributor to load-time and transfer-size improvements**
  - source: `06_conclusion.tex:18`
  - type: `qualitative`

- **Adaptive multi-strategy encoding in MLT encoder reduces tile volume by 28% over the fixed-plan reference baseline**
  - source: `06_conclusion.tex:19`
  - type: `number`

- **The advantage persists under every wire compressor tested**
  - source: `06_conclusion.tex:20`
  - type: `qualitative`

- **preprocessing cost characterized on the Germany \ac{OMT} tileset**
  - source: `06_conclusion.tex:22`
  - type: `name`

- **full single-threaded pipeline completes in under 7 minutes**
  - source: `06_conclusion.tex:23`
  - type: `number`

- **With 16-thread parallelism the wall-clock time drops to approximately 2 minutes**
  - source: `06_conclusion.tex:24`
  - type: `number`

- **multi-strategy encoder competition increases single-threaded re-encoding cost by a factor of 1.95×**
  - source: `06_conclusion.tex:25`
  - type: `number`

- **below the naïve 4× expectation**
  - source: `06_conclusion.tex:26`
  - type: `number`

- **empirical evaluation conducted across 15 styles, 18 scenarios, and 19 cumulative ablation steps**
  - source: `06_conclusion.tex:28`
  - type: `number`

- **full pipeline reduces total tile volume on the Germany \ac{OMT} tileset by 36% relative to gzip-compressed MVT**
  - source: `06_conclusion.tex:29`
  - type: `number`

- **Our encoder alone accounts for 12%, with style-driven tile shaving providing the remainder**
  - source: `06_conclusion.tex:30`
  - type: `number`

- **improves end-to-end load times by 63–74% (median 71%) across the ten deep-corpus styles benchmarked with tile data**
  - source: `06_conclusion.tex:31`
  - type: `number`

## Key Findings

- **combined style+shaving reduction is approximately the sum of the individual reductions**
  - source: `06_conclusion.tex:38`
  - type: `qualitative`

- **The three families are independently useful and can be deployed selectively rather than requiring joint adoption**
  - source: `06_conclusion.tex:39`
  - type: `qualitative`

- **mobile deployment on a constrained network should prioritize tile shaving and re-encoding**
  - source: `06_conclusion.tex:41`
  - type: `scope`

- **desktop deployment bottlenecked by draw calls benefits most from the structural passes alone**
  - source: `06_conclusion.tex:42`
  - type: `qualitative`

- **frame-time consistency metric worsens as the pipeline gets faster**
  - source: `06_conclusion.tex:44`
  - type: `qualitative`

- **Sustained frame rates above 2000 FPS expose small GC-pauses as proportionally large outliers**
  - source: `06_conclusion.tex:45`
  - type: `number`

- **raw reductions of 3–68% across the Maputnik generalization corpus**
  - source: `06_conclusion.tex:49`
  - type: `number`

- **iterating until no rule fires is sound for any order, even though the system is not confluent**
  - source: `06_conclusion.tex:50`
  - type: `qualitative`

## Research Questions Revisited

### R1: Size and Rendering Impact of Co-Optimizations

- **structural optimizations reduce the gzip-compressed style by 14.1% for Fiord and 4.9% for Liberty at step 15**
  - source: `06_conclusion.tex:57`
  - type: `number`

- **The pipeline is not uniformly effective**
  - source: `06_conclusion.tex:58`
  - type: `qualitative`

- **Verbose institutional styles with hundreds of layers benefit far more than compact basemaps**
  - source: `06_conclusion.tex:59`
  - type: `qualitative`

- **overview-dominated scenarios benefit more than street-level panning**
  - source: `06_conclusion.tex:59`
  - type: `qualitative`

- **remaining OMT-compatible styles in the deep corpus tile-shaving effectiveness of 19.8–46.3%**
  - source: `06_conclusion.tex:60`
  - type: `number`

- **thirteen-style Maputnik generalization corpus evaluated under static style passes alone**
  - source: `06_conclusion.tex:61`
  - type: `number`

### R2: Technique Effectiveness and Interactions

- **constant folding and expression simplification dominate the reductions**
  - source: `06_conclusion.tex:65`
  - type: `qualitative`

- **simplify filters into forms the structural passes can exploit**
  - source: `06_conclusion.tex:65`
  - type: `qualitative`

- **single successful fold cascades through enclosing expressions**
  - source: `06_conclusion.tex:65`
  - type: `qualitative`

- **dead elimination and layer merging dominate because they reduce the per-frame draw-call count directly**
  - source: `06_conclusion.tex:66`
  - type: `qualitative`

- **dead elimination removes gaps between mergeable layers that would otherwise prevent the merge pass from recognizing adjacency**
  - source: `06_conclusion.tex:67`
  - type: `qualitative`

- **Data-level optimizations operate on a different axis from both**
  - source: `06_conclusion.tex:68`
  - type: `qualitative`

- **cross-family interaction is additive rather than synergistic in aggregate**
  - source: `06_conclusion.tex:70`
  - type: `qualitative`

### R3: Preprocessing Cost and Decode/Render/Transfer Trade-Offs

- **preprocessing-cost model decomposes the total cost into four additive stages (style optimizations, statistics collection, advisory computation, MLT re-encoding)**
  - source: `06_conclusion.tex:73`
  - type: `scope`

- **re-encoding is the dominant term**
  - source: `06_conclusion.tex:73`
  - type: `qualitative`

- **MLT decoder achieves 4.6–8.3× higher full-decode throughput than MVT+gzip across zoom levels 4, 7, and 13**
  - source: `06_conclusion.tex:76`
  - type: `number`

- **Transfer-size reduction is the most reliably measurable axis (deterministic under compression)**
  - source: `06_conclusion.tex:77`
  - type: `qualitative`

- **for style-level passes it primarily affects initial load**
  - source: `06_conclusion.tex:77`
  - type: `qualitative`

- **Tile-level volume reduction has the larger sustained impact as tiles are fetched continuously**
  - source: `06_conclusion.tex:78`
  - type: `qualitative`

- **Rendering throughput (FPS) for style-only optimizations is affected almost entirely by the structural passes rather than by the data-level passes**
  - source: `06_conclusion.tex:79`
  - type: `qualitative`

- **multi-level pipeline is therefore a set of complementary mechanisms that each address a different bottleneck**
  - source: `06_conclusion.tex:80`
  - type: `qualitative`

## Future Work

- **style optimizer already depends only on the style and can run at deployment time**
  - source: `06_conclusion.tex:91`
  - type: `qualitative`

- **pruning advisory could plausibly run as a lightweight serving-time filter built on column selection and predicate evaluation**
  - source: `06_conclusion.tex:92`
  - type: `qualitative`

- **adaptive query processing**
  - source: `06_conclusion.tex:92`
  - type: `citation`

- **Encoding strategy competition is the inherently batch part because it has to profile whole columns**
  - source: `06_conclusion.tex:93`
  - type: `qualitative`

- **decisions could be cached per schema**
  - source: `06_conclusion.tex:93`
  - type: `qualitative`

- **on-the-fly MVT-to-MLT re-encoding at the tile server or CDN edge**
  - source: `06_conclusion.tex:93`
  - type: `scope`

- **AnyBlox framework bundles lightweight WebAssembly decoders with the datasets they read**
  - source: `06_conclusion.tex:94`
  - type: `citation`

- **Shipping the MLT decoder as a WASM module along the tiles would decouple format evolution from client updates entirely**
  - source: `06_conclusion.tex:95`
  - type: `scope`

- **direct integration of the optimized MLT decoder into MapLibre GL JS**
  - source: `06_conclusion.tex:96`
  - type: `name`

- **MLT columnar layout permits skipping unreferenced columns entirely**
  - source: `06_conclusion.tex:100`
  - type: `qualitative`

- **late materialisation applied at the tile level rather than at the analytical-query level**
  - source: `06_conclusion.tex:100`
  - type: `citation`

- **column projection derived from the style's property references would make decode cost scale with the number of columns actually used rather than with the total schema width**
  - source: `06_conclusion.tex:101`
  - type: `qualitative`

- **selective decoding composes with tile shaving rather than competing with it**
  - source: `06_conclusion.tex:102`
  - type: `qualitative`

- **Shaving removes columns at encoding time (early materialisation), selective decoding skips them at decode time (late materialisation)**
  - source: `06_conclusion.tex:103`
  - type: `scope`

- **engine currently applies rules in a fixed priority order and is not confluent**
  - source: `06_conclusion.tex:107`
  - type: `qualitative`

- **equality saturation engine would explore equivalent forms simultaneously and pick the globally optimal one**
  - source: `06_conclusion.tex:108`
  - type: `citation`

- **equality saturation can be used to infer rewrite rules from input/output examples**
  - source: `06_conclusion.tex:109`
  - type: `citation`

- **learned predictor in the manner of Kraska et al.'s learned indexes**
  - source: `06_conclusion.tex:111`
  - type: `citation`

- **model trained on layer-level statistics (cardinality, spatial spread, value distribution) could pick a sort order without running every trial**
  - source: `06_conclusion.tex:112`
  - type: `qualitative`

- **Symbol layers are currently excluded from merging because the pass cannot reason about glyph-level collision**
  - source: `06_conclusion.tex:116`
  - type: `qualitative`

- **restricted variant that merges symbol layers sharing identical text-field expressions would recover most of the unmerged headroom**
  - source: `06_conclusion.tex:117`
  - type: `qualitative`

- **label-heavy styles have the most layers left on the table after the structural pass**
  - source: `06_conclusion.tex:117`
  - type: `qualitative`

- **MinHash similarity threshold (τ = 7.5%) was tuned on the Germany \ac{OMT} tileset**
  - source: `06_conclusion.tex:118`
  - type: `number`

- **have not characterized sensitivity across tilesets with different vocabulary distributions**
  - source: `06_conclusion.tex:119`
  - type: `scope`

- **legal and data-availability constraints around non-OSM schemas made this hard to attempt**
  - source: `06_conclusion.tex:119`
  - type: `qualitative`

- **Proprietary styles such as Mapbox Streets and Esri's vector basemaps are similarly closed off by their terms of service**
  - source: `06_conclusion.tex:120`
  - type: `name`

- **per-pass marginal contributions should be read as confirmed on open-source styles rather than universally claimed**
  - source: `06_conclusion.tex:120`
  - type: `scope`
