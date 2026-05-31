## Formalised Problem Statement

- **MapLibre style JSON document consumed**
  - source: `04_methods.tex:3`
  - type: `name`

- **Visually equivalent style with optimized tile data emitted**
  - source: `04_methods.tex:3`
  - type: `scope`

- **Set of syntactically valid MapLibre style JSON documents denoted as S**
  - source: `04_methods.tex:9`
  - type: `name`

- **Set of tile sets denoted as T, each a finite family indexed by source and (x, y, z)**
  - source: `04_methods.tex:10`
  - type: `scope`

- **Set of viewing states V includes six degrees of freedom plus viewport: (lat_center, lon_center, z, roll, pitch, bearing, viewport size)**
  - source: `04_methods.tex:11`
  - type: `number`

- **Bot symbol denotes runtime evaluation error aborting rendering**
  - source: `04_methods.tex:12`
  - type: `scope`

- **Rendering function R: S × T × V → I ∪ {⊥} is MapLibre's deterministic rendering**
  - source: `04_methods.tex:14-15`
  - type: `scope`

- **Optimizer O: S × T → S × T with (S', T') = O(S, T)**
  - source: `04_methods.tex:18`
  - type: `scope`

- **Preprocessing cost C_total(S, T) paid once, amortised across rendering sessions**
  - source: `04_methods.tex:19`
  - type: `scope`

- **Visual equivalence constraint: ∀v ∈ V: R(S, T, v) ≠ ⊥ ⇒ R(S', T', v) ≡ R(S, T, v)**
  - source: `04_methods.tex:29-30`
  - type: `scope`

- **Constraint asymmetric in ⊥: pass may suppress runtime error, never introduce one**
  - source: `04_methods.tex:32-33`
  - type: `scope`

- **Visual equivalence checked by discrete grid sampling of zooms and viewports**
  - source: `04_methods.tex:34`
  - type: `scope`

- **Stats-driven folding pass requires full census (sample rate 1.0) to soundly remove match arm**
  - source: `04_methods.tex:38-39`
  - type: `scope`

- **Metadata-refinement pass must reason about overzoom when tightening maxzoom**
  - source: `04_methods.tex:40`
  - type: `scope`

- **Strict idempotency constraint: ∀(s, t) ∈ S × T: O(O(s, t)) = O(s, t)**
  - source: `04_methods.tex:42-44`
  - type: `scope`

- **Expression-pass fixpoint enforces idempotency on style half**
  - source: `04_methods.tex:47`
  - type: `scope`

- **Deterministic, statistics-driven encoding choices enforce idempotency on tile half**
  - source: `04_methods.tex:48`
  - type: `scope`

## Scope

- **MapLibre GL JS targeted as system under test**
  - source: `04_methods.tex:53`
  - type: `name`

- **maplibre-gl-js is reference implementation and benchmark target (not Native or mobile renderers)**
  - source: `04_methods.tex:56`
  - type: `name`

- **Three pass families in scope: expression-level rewrites, structural rewrites, data-level rewrites**
  - source: `04_methods.tex:58`
  - type: `scope`

- **Energy measurement out of scope: no RAPL or battery deltas on desktop workstation**
  - source: `04_methods.tex:64-65`
  - type: `scope`

- **Lossy geometry transformations out of scope: coordinate-precision reduction, Visvalingam-Whyatt, Douglas-Peucker, polygon coalescing violate pixel-identity**
  - source: `04_methods.tex:66`
  - type: `scope`

- **Symbol-layer merging out of scope: CollisionIndex per-layer evaluation, merging alters label suppression order**
  - source: `04_methods.tex:69-71`
  - type: `scope`

- **Proprietary style corpora excluded: Mapbox Streets, Esri vector basemaps by terms of service**
  - source: `04_methods.tex:72`
  - type: `scope`

- **Tile schemas other than OMT excluded from deep-corpus evaluation**
  - source: `04_methods.tex:73`
  - type: `scope`

- **Stats-driven thresholds tuned on Germany OMT only**
  - source: `04_methods.tex:73`
  - type: `scope`

- **Online and incremental serving out of scope: optimizer is offline, one-shot rebuild**
  - source: `04_methods.tex:74-75`
  - type: `scope`

- **Reference MLT encoder not target of optimization, retained as baseline**
  - source: `04_methods.tex:76-77`
  - type: `scope`

## Approach and Basic Building Blocks

### Three-Level Optimization Pipeline

- **Expression passes operate on JSON representation applying peephole rewrites**
  - source: `04_methods.tex:98`
  - type: `scope`

- **Expression passes run to fixpoint with hard cap of 8 iterations**
  - source: `04_methods.tex:99`
  - type: `number`

- **Every style converges within 2-3 iterations, well below the 8 cap**
  - source: `04_methods.tex:100`
  - type: `number`

- **Styles from benchmarking and Maputnik corpora converge within 2-3 iterations**
  - source: `04_methods.tex:100`
  - type: `number`

- **Structural passes deserialize style into typed spec produced by codegen**
  - source: `04_methods.tex:102`
  - type: `scope`

- **Structural passes perform: dead layer elimination, metadata refinement, layer merging, cleanup**
  - source: `04_methods.tex:102`
  - type: `scope`

- **Cross-phase filter-to-property constant propagation bridges expression and structural phases**
  - source: `04_methods.tex:103`
  - type: `scope`

- **Data passes transform served tile data via style-driven pruning and MVT to MLT conversion**
  - source: `04_methods.tex:104`
  - type: `scope`

- **Phase ordering: expression passes first, then structural, then data**
  - source: `04_methods.tex:107-110`
  - type: `scope`

### Code Generation from v8.json

- **Structural passes operate on Rust types generated from MapLibre GL JS style specification**
  - source: `04_methods.tex:176`
  - type: `scope`

- **Codegen pipeline decodes v8.json, normalizes to MIR, generates Rust sources**
  - source: `04_methods.tex:180-186`
  - type: `scope`

- **MIR provides stable form between upstream sources and downstream consumers**
  - source: `04_methods.tex:182`
  - type: `scope`

- **MIR collapses paint/layout properties across multiple sections into per-layer field definitions**
  - source: `04_methods.tex:185`
  - type: `scope`

- **MIR carries type, default, and expression-capability metadata**
  - source: `04_methods.tex:185`
  - type: `scope`

- **Layer merging queries MIR to determine paint property expression-capability**
  - source: `04_methods.tex:189`
  - type: `scope`

- **Default stripping compares property values against specification defaults in generated types**
  - source: `04_methods.tex:190`
  - type: `scope`

### Implementation

- **Style optimizer is standalone Rust binary**
  - source: `04_methods.tex:194`
  - type: `name`

- **Tile re-encoder shares Cargo workspace with optimizer, split into encoder/decoder crate and Java wrapper**
  - source: `04_methods.tex:195`
  - type: `scope`

- **Diplomat generates cross-language bindings from annotated Rust types**
  - source: `04_methods.tex:196`
  - type: `name`

- **Diplomat replaces cbindgen/jextract approach**
  - source: `04_methods.tex:196`
  - type: `name`

- **Java wrapper exposes Panama FFM API (JEP 454) instead of JNI**
  - source: `04_methods.tex:197-198`
  - type: `name`

- **Each tile handed as batch of parallel MemorySegments for zero-copy access**
  - source: `04_methods.tex:199`
  - type: `scope`

## Building Optimizations

### Expression-Level Optimizations

- **Expression passes listed in Table with 8 passes: unary simplification, kind normalization, constant folding, stats-driven constant folding, expression simplification, default stripping, colour minification, selectivity reordering**
  - source: `04_methods.tex:222-229`
  - type: `scope`

- **17 rewrite rules implement constant folding**
  - source: `04_methods.tex:250`
  - type: `number`

- **Vacuous [\mlop{"all"}] rewrites to true (vacuous truth)**
  - source: `04_methods.tex:252`
  - type: `scope`

- **Vacuous [\mlop{"any"}] rewrites to false (vacuous disjunction)**
  - source: `04_methods.tex:252`
  - type: `scope`

- **Boolean absorption removes known-true operands from all, known-false from any**
  - source: `04_methods.tex:252`
  - type: `scope`

- **Cardinality threshold of 200 governs value tracking granularity**
  - source: `04_methods.tex:319`
  - type: `number`

- **Above 200 distinct values, statistics switch to cardinality-only mode**
  - source: `04_methods.tex:320`
  - type: `number`

- **Categorical properties in benchmark styles: class, subclass, admin_level, kind, land-use codes all below 200 distinct values in Germany tileset**
  - source: `04_methods.tex:323`
  - type: `scope`

- **High-cardinality string columns (feature names, identifiers) exceed 200 by one or more orders of magnitude**
  - source: `04_methods.tex:323`
  - type: `scope`

- **Range folding rules include: p < n, p ≤ n, p > n, p ≥ n, p = n, p ≠ n comparisons**
  - source: `04_methods.tex:291-302`
  - type: `scope`

- **Floating-point equality folds only at reported min/max values exactly (boundary comparison)**
  - source: `04_methods.tex:308-309`
  - type: `scope`

- **De Morgan's laws push negations inward**
  - source: `04_methods.tex:330`
  - type: `scope`

- **Boolean flattening merges nested all/any operators**
  - source: `04_methods.tex:336`
  - type: `scope`

- **any→in rewrite detects equality tests on same property within any, merges to in**
  - source: `04_methods.tex:342`
  - type: `scope`

- **Selectivity reordering depends on independence assumption from database query optimization**
  - source: `04_methods.tex:362`
  - type: `citation`

- **Selectivity formulas (sel): p=v, p<n, geometry-type t, p∈V, has p, p≠v**
  - source: `04_methods.tex:364-372`
  - type: `scope`

- **Independence assumption known imprecise for correlated predicates**
  - source: `04_methods.tex:376`
  - type: `scope`

- **Reordering heuristic needs ordering not absolute selectivity values**
  - source: `04_methods.tex:376-378`
  - type: `scope`

- **Predicate reordering benefit depends on proportion of evaluation cost (expected small for short filters)**
  - source: `04_methods.tex:379`
  - type: `scope`

- **Fixpoint applies rewrite rules until style JSON stops changing**
  - source: `04_methods.tex:382`
  - type: `scope`

- **Termination measure μ(S) = (n_AST(S), d_max(S), n_lit(S))**
  - source: `04_methods.tex:387-389`
  - type: `scope`

- **n_AST is total number of AST nodes, d_max is maximum nesting depth, n_lit is non-literal nodes**
  - source: `04_methods.tex:389`
  - type: `scope`

- **Majority of rules strictly decrease lexicographic measure**
  - source: `04_methods.tex:385-390`
  - type: `scope`

- **Two rules temporarily increase n_AST: De Morgan's law (4→5 nodes), distributive factoring**
  - source: `04_methods.tex:393-395`
  - type: `scope`

- **All styles converge within 3 iterations well below hard cap**
  - source: `04_methods.tex:398`
  - type: `scope`

- **Rewrite system not confluent: first matching rule fires**
  - source: `04_methods.tex:401`
  - type: `scope`

- **Selectivity reordering depends on data-dependent statistics**
  - source: `04_methods.tex:402`
  - type: `scope`

- **Different rule orderings yield visually equivalent output**
  - source: `04_methods.tex:403`
  - type: `scope`

### Structural Optimizations

- **Structural passes listed in Table with 6 passes: metadata stripping, dead layer/source elimination, metadata refinement, cleanup, layer merging, source zoom tightening**
  - source: `04_methods.tex:651-656`
  - type: `scope`

- **Dead layer when filter is literal false, source layer has zero features, or geometry-type mismatch**
  - source: `04_methods.tex:666`
  - type: `scope`

- **Geometry-type mismatch effective on \ac{OMT}h mixed geometry in single source layer**
  - source: `04_methods.tex:671`
  - type: `scope`

- **fill layers require polygons, circle requires points, line draws on polygons/lines not points, symbol on all three**
  - source: `04_methods.tex:671`
  - type: `scope`

- **Geometry-type check requires tile statistics (static and stats-driven variants)**
  - source: `04_methods.tex:672`
  - type: `scope`

- **Metadata refinement extracts implicit zoom bounds from filter predicates and paint ramps**
  - source: `04_methods.tex:675`
  - type: `scope`

- **Filter-based extraction recognizes zoom predicates: >=, >, <=, < forms**
  - source: `04_methods.tex:678`
  - type: `scope`

- **Within all node, intersects extracted bounds; within any, unions them**
  - source: `04_methods.tex:679-680`
  - type: `scope`

- **Extracted bounds rounded to integer zoom levels**
  - source: `04_methods.tex:681`
  - type: `scope`

- **Zoom interval extraction: >= n [n, ∞), > n [⌊n⌋+1, ∞), <= n [0, n], < n [0, ⌈n⌉-1]**
  - source: `04_methods.tex:685-688`
  - type: `scope`

- **all node intersection: z* = [max(l1,l2), min(u1,u2)]**
  - source: `04_methods.tex:693`
  - type: `scope`

- **any node union: z* = [min(l1,l2), max(u1,u2)]**
  - source: `04_methods.tex:697`
  - type: `scope`

- **Paint-based visibility for opacity: transitions from zero to non-zero at specific zoom**
  - source: `04_methods.tex:702-704`
  - type: `scope`

- **Symbol layers: either text or icon opacity must be non-zero**
  - source: `04_methods.tex:705`
  - type: `scope`

- **Other layer types: both size and opacity must be non-zero**
  - source: `04_methods.tex:706`
  - type: `scope`

- **Stats-driven refinement tightens bounds using actual tile coverage**
  - source: `04_methods.tex:708`
  - type: `scope`

- **minzoom is symmetric: raising never removes rendered pixel**
  - source: `04_methods.tex:715-716`
  - type: `scope`

- **maxzoom is asymmetric: tightened only when less than source maxzoom (overzoom)**
  - source: `04_methods.tex:717-719`
  - type: `scope`

- **Layer merging identifies adjacent layers with identical paint/layout properties**
  - source: `04_methods.tex:733`
  - type: `scope`

- **Fewer layers mean fewer rendering passes, each layer incurs setup costs**
  - source: `04_methods.tex:734-735`
  - type: `scope`

- **Painter loop: opaque pass top-to-bottom, translucent pass bottom-to-top**
  - source: `04_methods.tex:736`
  - type: `scope`

- **Each layer eliminated removes one renderLayer dispatch from each pass**
  - source: `04_methods.tex:737`
  - type: `scope`

- **Symbol layers per-layer CollisionIndex processing: LayerPlacement scope per-layer**
  - source: `04_methods.tex:739-740`
  - type: `scope`

- **Merging symbol layers interleaves symbols, changes collision order**
  - source: `04_methods.tex:742`
  - type: `scope`

- **Merge Phase 1: candidate identification scans for contiguous runs with same type/source/source-layer**
  - source: `04_methods.tex:746`
  - type: `scope`

- **Property mergeable if supports feature-driven expressions and not zoom ramp**
  - source: `04_methods.tex:747-749`
  - type: `scope`

- **Camera-only properties must be uniform across merged layers**
  - source: `04_methods.tex:752`
  - type: `scope`

- **Layer types supporting sort keys: fill, line, circle, fill-extrusion (not symbol)**
  - source: `04_methods.tex:753-754`
  - type: `scope`

- **Merge invariant Coverage: merged filter is disjunction of original filters**
  - source: `04_methods.tex:758-760`
  - type: `scope`

- **Merge invariant Painter order: synthezised sort key preserves inter-layer draw order**
  - source: `04_methods.tex:762-766`
  - type: `scope`

- **Merge invariant Layer scope: no per-layer behavior widened by merge**
  - source: `04_methods.tex:768-770`
  - type: `scope`

- **Filter-to-property propagation extracts equality constraints from layer filter**
  - source: `04_methods.tex:773`
  - type: `scope`

- **Propagation strictly intra-layer, constraints never flow to sibling layers**
  - source: `04_methods.tex:780`
  - type: `scope`

- **Propagation ignores feature-state references (set at render time)**
  - source: `04_methods.tex:782`
  - type: `scope`

- **Phase 2 match-pattern detection checks filters match ==, get, P on same property**
  - source: `04_methods.tex:784-786`
  - type: `scope`

- **Road styles frequently define separate layers for highway class values**
  - source: `04_methods.tex:787`
  - type: `scope`

- **Phase 3 zoom-tolerant merging wraps sub-filters with zoom guards**
  - source: `04_methods.tex:793-794`
  - type: `scope`

- **Synthezised sort key uses discriminator value as index for match, filters in reverse for case**
  - source: `04_methods.tex:796`
  - type: `scope`

- **Source zoom tightening: source "live" at zoom only if layer referencing it active**
  - source: `04_methods.tex:802`
  - type: `scope`

- **Tighter source bounds allow tile server to skip requests at unused zooms**
  - source: `04_methods.tex:803`
  - type: `scope`

### Data-Level Optimizations

- **Data passes listed in Table with 3 passes: tile shaving, transparent re-encoding, compression optimizations**
  - source: `04_methods.tex:893-895`
  - type: `scope`

- **Pipeline mirrors database optimizer: logical rewriting, physical strategy selection, cost-based competition**
  - source: `04_methods.tex:904`
  - type: `scope`

- **Stage 1: Style-driven tile shaving produces pruning advisory**
  - source: `04_methods.tex:906-908`
  - type: `scope`

- **Stage 2: Data transformations - string interning, feature reordering**
  - source: `04_methods.tex:909`
  - type: `scope`

- **Stage 3: Encoding strategy selection re-encodes to MLT via multi-strategy competition**
  - source: `04_methods.tex:910`
  - type: `scope`

- **Three stages compose: shaving narrows column set, determines distributions for Stage 3**
  - source: `04_methods.tex:914-916`
  - type: `scope`

- **Advisory computed from optimized style after all expression and structural passes**
  - source: `04_methods.tex:921`
  - type: `scope`

- **Dead layer elimination, metadata refinement, layer merging shrink live-layer set**
  - source: `04_methods.tex:922`
  - type: `scope`

- **Advisory captures 5 categories: property usage, geometry usage, zoom-level coverage, categorical-value usage, feature-ID usage**
  - source: `04_methods.tex:925-945`
  - type: `scope`

- **Property usage: each property name in get/has expressions with zoom range**
  - source: `04_methods.tex:928`
  - type: `scope`

- **Geometry usage: Point, LineString, Polygon types required at each zoom**
  - source: `04_methods.tex:931-933`
  - type: `scope`

- **Zoom-level coverage: zooms where at least one layer references source-layer**
  - source: `04_methods.tex:935-936`
  - type: `scope`

- **Categorical-value usage: property values from equality filters and match with zoom ranges**
  - source: `04_methods.tex:939-940`
  - type: `scope`

- **Feature-ID usage: whether any layer references id or feature-state**
  - source: `04_methods.tex:943-944`
  - type: `scope`

- **Tile shaving pruning operations in order: remove unreferenced source-layers, filter by geometry type, categorical values, strip unused properties, strip feature IDs**
  - source: `04_methods.tex:985-990`
  - type: `scope`

- **String interning replaces categorical string properties with frequency-ordered indices**
  - source: `04_methods.tex:1002`
  - type: `scope`

- **Interning table derived from tile statistics, sorted by descending frequency starting from 0**
  - source: `04_methods.tex:1003-1005`
  - type: `scope`

- **Interning reduces per-feature storage from variable-length string to small integer**
  - source: `04_methods.tex:1008`
  - type: `scope`

- **Frequency ordering means common values receive small indices, compress well under VarInt**
  - source: `04_methods.tex:1009`
  - type: `scope`

- **Optimizer rewrites style expressions to reference integer indices instead of strings**
  - source: `04_methods.tex:1011`
  - type: `scope`

- **Interned tiles encode property values as style-specific integer indices, only compatible with paired style**
  - source: `04_methods.tex:1014`
  - type: `scope`

- **Interning optional pipeline stage, can be disabled for multi-consumer deployments**
  - source: `04_methods.tex:1016`
  - type: `scope`

- **Feature reordering: spatial (Hilbert/Morton), ID-based, property-based orderings explored**
  - source: `04_methods.tex:1020`
  - type: `scope`

- **Encoder converts row-oriented MVT features into owned columnar representation**
  - source: `04_methods.tex:1029`
  - type: `scope`

- **Final wire format: three sections per layer - header, metadata, data**
  - source: `04_methods.tex:1032`
  - type: `scope`

- **Multi-strategy competition uses data distribution of each tile to try multiple strategies**
  - source: `04_methods.tex:1034-1035`
  - type: `scope`

- **Two nested competition levels: outer (sort orderings), inner (per-stream integer encoding)**
  - source: `04_methods.tex:1038-1039`
  - type: `scope`

- **Inner competition single-objective: smallest encoded size**
  - source: `04_methods.tex:1040`
  - type: `scope`

- **No-copy alternatives mechanism lets candidates write into encoder buffers, rolls losers back**
  - source: `04_methods.tex:1045`
  - type: `scope`

- **Nested competition kept near-additive via FSST warm-start caching, vertex-strategy decisions**
  - source: `04_methods.tex:1046`
  - type: `scope`

- **Sort strategies: unsorted, spatial Morton/Z-order, spatial Hilbert, ID-based**
  - source: `04_methods.tex:1147-1151`
  - type: `scope`

- **Morton/Z-order fast to compute, reasonable spatial locality**
  - source: `04_methods.tex:1148`
  - type: `scope`

- **Hilbert slower than Morton, superior spatial locality, avoids long jumps in Z-order**
  - source: `04_methods.tex:1149`
  - type: `scope`

- **Bounding-box heuristic skips spatial sorting on layers with 512+ features covering 80%+ tile extent on both axes**
  - source: `04_methods.tex:1229`
  - type: `number`

- **Thresholds derived experimentally from Germany-wide \ac{OMT}
  - source: `04_methods.tex:1231`
  - type: `scope`

- **Always tries small layers below threshold, cost of extra pass negligible**
  - source: `04_methods.tex:1230`
  - type: `scope`

- **Per-stream encoding pairs: logical (Plain, Delta, RLE, DeltaRle) × physical (VarInt, FastPFOR)**
  - source: `04_methods.tex:1234`
  - type: `scope`

- **Four logical encodings in general competition**
  - source: `04_methods.tex:1235`
  - type: `number`

- **Geometry-specific strategies: Morton-delta, componentwise-delta for coordinate data**
  - source: `04_methods.tex:1236`
  - type: `scope`

- **Data profiler samples contiguous block from middle of stream**
  - source: `04_methods.tex:1239`
  - type: `scope`

- **Profile streams with at most 512 values in full, longer streams over ⌊|s|/100⌋ values clamped to [512, 16384]**
  - source: `04_methods.tex:1240`
  - type: `number`

- **Profiler excludes RLE when average run length S̄ < 2.0**
  - source: `04_methods.tex:1243`
  - type: `number`

- **Profiler excludes Delta when non-monotonic and delta bit width exceeds raw values**
  - source: `04_methods.tex:1244`
  - type: `scope`

- **Profiler excludes DeltaRle when S̄_Δ < 2.0 and neither RLE nor Delta viable**
  - source: `04_methods.tex:1245`
  - type: `number`

- **FastPFOR only offered for 32-bit integer types**
  - source: `04_methods.tex:1246`
  - type: `scope`

- **Encoder fully encodes remaining candidates (typically 2-4) and commits smallest**
  - source: `04_methods.tex:1247`
  - type: `scope`

- **String strategies: Plain, Dictionary, FSST, FSST+Dictionary**
  - source: `04_methods.tex:1252-1260`
  - type: `scope`

- **FSST learns symbol table of up to 255 frequent byte sequences**
  - source: `04_methods.tex:1257`
  - type: `number`

- **FSST symbol table stored once per column**
  - source: `04_methods.tex:1258`
  - type: `scope`

- **FSST viability probe excludes columns below 2048 raw bytes**
  - source: `04_methods.tex:1264`
  - type: `number`

- **FSST sample trial compression on up to 256 strings before committing**
  - source: `04_methods.tex:1264`
  - type: `number`

- **FSST symbol table overhead up to 2040 bytes**
  - source: `04_methods.tex:1263`
  - type: `number`

- **FSST pruning variant drops symbols when inlining costs fewer bytes**
  - source: `04_methods.tex:1266`
  - type: `scope`

- **Shared dictionary grouping: MLT supports multiple string columns referencing common corpus**
  - source: `04_methods.tex:1269`
  - type: `scope`

- **Reference encoder groups by naming prefix, misses semantic overlaps**
  - source: `04_methods.tex:1270`
  - type: `scope`

- **Our encoder uses MinHash-based similarity clustering instead of prefix matching**
  - source: `04_methods.tex:1273`
  - type: `scope`

- **Two MinHash sketches per column: 128 permutations over exact strings and byte trigrams**
  - source: `04_methods.tex:1275`
  - type: `number`

- **Variance bound O(1/k) gives standard error ≈ 8.8% at k=128**
  - source: `04_methods.tex:1276`
  - type: `number`

- **Pairwise Jaccard similarity: Ĵ = |{i : h_i^(a) = h_i^(b)}| / 128**
  - source: `04_methods.tex:1278`
  - type: `scope`

- **Unifies columns exceeding 7.5% similarity threshold via Union-Find**
  - source: `04_methods.tex:1279`
  - type: `number`

- **Discards groups with fewer than two members**
  - source: `04_methods.tex:1281`
  - type: `scope`

- **Threshold selected via sweep over [2.5%, 20%] on Germany \ac{OMT}
  - source: `04_methods.tex:1282`
  - type: `scope`

- **Hybrid similarity mode (max of exact and trigram) wins at every threshold**
  - source: `04_methods.tex:1282`
  - type: `scope`

- **Curve nearly flat below 7.5%, empirical optimum at 2.5% saves additional 1.6 MB on 3.14 GB tileset**
  - source: `04_methods.tex:1283`
  - type: `number`

- **7.5% retained as conservative default**
  - source: `04_methods.tex:1284`
  - type: `number`

- **Geometry encoding: componentwise deltas (CWD), Hilbert-code dictionaries, Morton-code dictionaries, plain**
  - source: `04_methods.tex:1384-1386`
  - type: `scope`

- **CWD produces interleaved stream [x_0, y_0, Δx_1, Δy_1, ...] compressed via integer competition**
  - source: `04_methods.tex:1385`
  - type: `scope`

- **Morton/Hilbert dictionaries for unique vertices when coordinate range permits (both axes fit 16 bits)**
  - source: `04_methods.tex:1387`
  - type: `scope`

- **Feature ID encoding via per-stream integer competition, explicit tag for 32/64-bit**
  - source: `04_methods.tex:1391`
  - type: `scope`

- **Encoder narrows 64-bit ID columns to 32 bits when observed values fit**
  - source: `04_methods.tex:1392`
  - type: `scope`

- **Data profiler discovers structural patterns: sequential→DeltaRle, constant→RLE, irregular→VarInt**
  - source: `04_methods.tex:1395`
  - type: `scope`

- **Encoder correctness validated via property-based rounds per encoder, coverage-guided fuzzing, snapshot tests, pixel-exact end-to-end check**
  - source: `04_methods.tex:1398`
  - type: `scope`

### Tile Statistics Collection

- **Multiple passes require tile data knowledge: stats-driven constant folding, selectivity reordering, dead elimination, metadata refinement, tile pruning**
  - source: `04_methods.tex:1403`
  - type: `scope`

- **Statistics collection produces per-source, per-source-layer statistical profile**
  - source: `04_methods.tex:1404`
  - type: `scope`

- **Optimizer accepts MBTiles database or pre-computed statistics file**
  - source: `04_methods.tex:1405`
  - type: `scope`

- **Per-source-layer stats: feature count, features by zoom, geometry types, feature ID presence, per-property statistics**
  - source: `04_methods.tex:1407-1421`
  - type: `scope`

- **Boolean property stats: present count, true count**
  - source: `04_methods.tex:1417`
  - type: `scope`

- **Integer/unsigned property stats: present, min, max, cardinality, full value-frequency if cardinality ≤ 200**
  - source: `04_methods.tex:1418`
  - type: `number`

- **Double property stats: present, min, max, cardinality (no value-frequency)**
  - source: `04_methods.tex:1419`
  - type: `scope`

- **String property stats: present, cardinality, value-frequency if cardinality ≤ 200**
  - source: `04_methods.tex:1420`
  - type: `number`

- **Features appearing in multiple tiles counted multiple times, per-tile reasoning**
  - source: `04_methods.tex:1410-1411`
  - type: `scope`

- **Configurable sample rate for statistics collection**
  - source: `04_methods.tex:1424`
  - type: `scope`

- **Sample rate 1.0 (full census) required for irreversible decisions**
  - source: `04_methods.tex:1425`
  - type: `number`

- **Lower sample rates sufficient for selectivity estimation and reordering**
  - source: `04_methods.tex:1426`
  - type: `scope`

- **Sample-rate guard enforces distinction in optimizer**
  - source: `04_methods.tex:1427`
  - type: `scope`

### Preprocessing Cost Model

- **Total preprocessing cost: C_total(S, T) = C_style(S) + C_stats(T) + C_adv(S) + C_enc(S, T)**
  - source: `04_methods.tex:1435`
  - type: `scope`

- **Four additive terms: style passes, tile statistics, advisory computation, MLT re-encoding**
  - source: `04_methods.tex:1433`
  - type: `scope`

- **Bounding-box pruning, data profiling, FSST caching, scratch-buffer recycling, RAII keep C_enc bounded**
  - source: `04_methods.tex:1437`
  - type: `scope`

- **Cost reported on Germany \ac{OMT}eset**
  - source: `04_methods.tex:1438`
  - type: `scope`

## Gathering a Representative Sample

- **Deep evaluation: 15 styles against reproducible tile data and stratified scenario sample**
  - source: `04_methods.tex:1443`
  - type: `number`

- **Generalization corpus: 13 additional styles carry static-only checks**
  - source: `04_methods.tex:1444`
  - type: `number`

### Benchmarking Corpus

- **Corpus of 15 publicly available styles using \ac{OMT}BasemapDE schema**
  - source: `04_methods.tex:1448`
  - type: `number`

- **Four OpenFreeMap styles: liberty, bright, positron, fiord**
  - source: `04_methods.tex:1449`
  - type: `number`

- **Seven \ac{OMT}munity styles: dark-matter, osm-bright, klokan-basic, toner, osm-liberty, americana, stadia-outdoors**
  - source: `04_methods.tex:1450`
  - type: `number`

- **Four government/institutional styles: ICGC fosc, ICGC gris, BasemapDE topographic, BasemapDE color**
  - source: `04_methods.tex:1451`
  - type: `number`

- **Styles span complexity from <50 layers to several hundred layers**
  - source: `04_methods.tex:1453`
  - type: `scope`

### Generalisation Corpus

- **13 styles from Maputnik style editor catalog**
  - source: `04_methods.tex:1457`
  - type: `number`

- **Two additional catalog entries unavailable at measurement time**
  - source: `04_methods.tex:1457`
  - type: `number`

- **Static analysis only: style size, complexity metrics, pass applicability**
  - source: `04_methods.tex:1458`
  - type: `scope`

### Tile Data and Caching

- **Tile data from OSM via Planetiler or German government**
  - source: `04_methods.tex:1462`
  - type: `scope`

- **Web Mercator XYZ tiling scheme used by MapLibre**
  - source: `04_methods.tex:1463`
  - type: `scope`

- **BasemapDE accessed via XYZ-compatible endpoint instead of native WMTS**
  - source: `04_methods.tex:1464`
  - type: `scope`

- **OSM fully available, only source allowing sample rate 1.0**
  - source: `04_methods.tex:1465`
  - type: `scope`

- **Local caching proxy routes all tile requests, stores on first access, replays with 4G latency**
  - source: `04_methods.tex:1466`
  - type: `scope`

- **4G model: size/(30 MiB/s) + 25ms**
  - source: `04_methods.tex:1466`
  - type: `number`

- **Network model does not simulate packet loss, HTTP/2 multiplexing, TCP slow-start, HTTP/3**
  - source: `04_methods.tex:1468`
  - type: `scope`

- **Measured improvements conservative lower bound on real deployment**
  - source: `04_methods.tex:1469`
  - type: `scope`

- **Deterministic across runs via identical tile data**
  - source: `04_methods.tex:1470`
  - type: `scope`

### Geographic and Use-Case Scenarios

- **18 scenarios from matrix of 15 geographic locations and 5 camera animations**
  - source: `04_methods.tex:1475`
  - type: `number`

- **Locations: high-density cities Latin scripts (Munich, Berlin, Paris, New York, Rome)**
  - source: `04_methods.tex:1476`
  - type: `scope`

- **Locations: non-Latin scripts (Tokyo, Beijing, Seoul, Cairo)**
  - source: `04_methods.tex:1476`
  - type: `scope`

- **Locations: low-density/nature (Black Forest, Amazon, Swiss Alps, Sahara, Venice, Stockholm Archipelago)**
  - source: `04_methods.tex:1476`
  - type: `scope`

- **Animation types: zigzag, spiral, zoomdrill, pansweep, bearingspin**
  - source: `04_methods.tex:1477-1482`
  - type: `scope`

- **Full cross-product of 15×5 = 75 pairs too expensive**
  - source: `04_methods.tex:1486`
  - type: `number`

- **Selected 18 scenarios via stratified sampling: every location ≥1, every animation ≥3**
  - source: `04_methods.tex:1487`
  - type: `scope`

- **Sample biased against null hypothesis (no effect) toward densest style**
  - source: `04_methods.tex:1488`
  - type: `scope`

## Evaluation

- **Evaluation reports deployment metrics: data savings, rendering performance, optimization cost, efficiency**
  - source: `04_methods.tex:1498`
  - type: `scope`

- **Data savings: raw/gzip/Brotli style size, tile transfer volume**
  - source: `04_methods.tex:1501`
  - type: `scope`

- **Rendering: load time, FPS, frame time percentiles (p50, p95, p99), jank count, style parse time, time to first tile, time to first frame**
  - source: `04_methods.tex:1502`
  - type: `scope`

- **Optimization cost: preprocessing wall-clock time, offline amortised cost**
  - source: `04_methods.tex:1503-1504`
  - type: `scope`

- **Efficiency: qualitative energy discussion, no direct power/RAPL measurement**
  - source: `04_methods.tex:1505`
  - type: `scope`

### Metrics

- **Load time: wall-clock from request to completion of initial render**
  - source: `04_methods.tex:1514`
  - type: `scope`

- **Decoding latency embedded in loadMs (browser harness limitation)**
  - source: `04_methods.tex:1515`
  - type: `scope`

- **Isolated decoding throughput via Criterion micro-benchmarks**
  - source: `04_methods.tex:1516`
  - type: `scope`

- **Style parse time: time parsing/compiling style JSON into renderer representation**
  - source: `04_methods.tex:1517`
  - type: `scope`

- **Time to first tile: initialization until first tile decoded and ready**
  - source: `04_methods.tex:1518`
  - type: `scope`

- **Time to first frame: until first frame composited and presented**
  - source: `04_methods.tex:1519`
  - type: `scope`

- **FPS: average rendering throughput during animation**
  - source: `04_methods.tex:1520`
  - type: `scope`

- **Frame time percentiles: p50, p95, p99 distribution capturing typical/worst-case**
  - source: `04_methods.tex:1521`
  - type: `scope`

- **Jank count: frames exceeding 16.67ms (60 FPS budget)**
  - source: `04_methods.tex:1522`
  - type: `number`

- **Heap memory: JavaScript heap usage during benchmark**
  - source: `04_methods.tex:1523`
  - type: `scope`

- **Idle time: renderer waiting for tiles or GPU sync, indicating headroom**
  - source: `04_methods.tex:1524`
  - type: `scope`

- **Static metrics: style size (raw, gzip, Brotli), complexity metrics**
  - source: `04_methods.tex:1527-1529`
  - type: `scope`

- **Complexity metrics: total AST nodes, max depth, layer count, filter count, operator histogram**
  - source: `04_methods.tex:1529`
  - type: `scope`

### Ablation Methodology

- **Cumulative ablation: add passes one at a time in fixed order**
  - source: `04_methods.tex:1533-1534`
  - type: `scope`

- **19 cumulative steps: baseline + passes incrementally**
  - source: `04_methods.tex:1536`
  - type: `number`

- **Additional plain tile shaving configuration isolates style↔shaving interaction**
  - source: `04_methods.tex:1536`
  - type: `scope`

- **Each scenario/style combo executed 15 runs**
  - source: `04_methods.tex:1539`
  - type: `number`

- **Report median and standard deviation (right-skewed distribution)**
  - source: `04_methods.tex:1540-1541`
  - type: `scope`

- **Pin rendering to GPU via ANGLE/Vulkan not software rasteriser**
  - source: `04_methods.tex:1542`
  - type: `scope`

- **Puppeteer-driven headless browser loading MapLibre GL JS**
  - source: `04_methods.tex:1546`
  - type: `scope`

- **Performance counters via Performance API and custom renderer instrumentation**
  - source: `04_methods.tex:1546`
  - type: `scope`

## Chapter Summary

- **Three-level pipeline on (S,T)→(S',T') problem**
  - source: `04_methods.tex:1549-1550`
  - type: `scope`

- **Eight expression-level passes run to fixpoint**
  - source: `04_methods.tex:1550`
  - type: `number`

- **Six structural passes act on typed style document**
  - source: `04_methods.tex:1550`
  - type: `number`

- **Data-level passes re-encode shaved tiles into MLT via per-stream competition**
  - source: `04_methods.tex:1550`
  - type: `scope`

- **Pruning advisory ties levels together as projection-pushdown over tile data**
  - source: `04_methods.tex:1551`
  - type: `scope`

- **19-step cumulative ablation plus one plain-tile-shaving configuration**
  - source: `04_methods.tex:1552`
  - type: `number`

- **15 styles, 18 stratified scenarios, 15 repeat runs per cell**
  - source: `04_methods.tex:1552`
  - type: `number`

- **13-style generalization corpus**
  - source: `04_methods.tex:1552`
  - type: `number`

- **Preprocessing-cost model decomposes offline cost into four stages**
  - source: `04_methods.tex:1552`
  - type: `scope`
