## Map Rendering Approaches

- **ID Editor and Leaflet use SVG to render maps**
  - source: `03_theory.tex:14`
  - type: `name`

- **SVG is limited to 2D rendering approaches due to not having a camera**
  - source: `03_theory.tex:15`
  - type: `scope`

- **OpenLayers uses Canvas 2D as its primary renderer**
  - source: `03_theory.tex:18`
  - type: `name`

- **Canvas 2D rendering rasterises vector features on the CPU rather than submitting them to the GPU**
  - source: `03_theory.tex:18-19`
  - type: `qualitative`

- **Canvas 2D rendering throughput is CPU-bound and does not benefit from hardware-accelerated geometry processing**
  - source: `03_theory.tex:19`
  - type: `qualitative`

- **Canvas 2D is limited to 2D views without pitch or rotation**
  - source: `03_theory.tex:20`
  - type: `scope`

- **WebGL, WebGPU, OpenGL, Metal, Vulkan, DirectX are low-level 3D graphics APIs**
  - source: `03_theory.tex:22`
  - type: `name`

- **mapbox, maplibre, deck.gl, here use 3D graphics APIs for rendering**
  - source: `03_theory.tex:22`
  - type: `name`

- **3D graphics APIs allow more complex 3D-based rendering with pitch, yaw, and roll**
  - source: `03_theory.tex:23`
  - type: `scope`

- **3D graphics APIs can render more complex scenes with better performance due to having better hardware access**
  - source: `03_theory.tex:24`
  - type: `qualitative`

- **Renderers based on open-source 3D graphics APIs require data to be preprocessed and optimized specifically for rendering**
  - source: `03_theory.tex:28`
  - type: `scope`

- **3D graphics renderers cannot directly render high-level primitives such as shapes, text, or images**
  - source: `03_theory.tex:29`
  - type: `scope`

- **3D graphics renderers operate on lower-level graphics primitives such as textures, triangles, and quads**
  - source: `03_theory.tex:30`
  - type: `scope`

- **Low-level graphics building blocks are linked to map data through sprites, fonts, and styles**
  - source: `03_theory.tex:32`
  - type: `scope`

### Fonts

- **up to 131 megabyte of font data needs to be transferred for some fonts**
  - source: `03_theory.tex:122`
  - type: `number`

- **Harfbuzz text shaping engine is not exposed as a feature in native or web targets**
  - source: `03_theory.tex:121`
  - type: `scope`

- **Latin fonts usually have a clear 1:1 relationship between Unicode code point and rendered character**
  - source: `03_theory.tex:126`
  - type: `qualitative`

- **Fonts are cut into Unicode slices (start..end) and only the ranges that the client needs are served**
  - source: `03_theory.tex:129`
  - type: `scope`

- **MapLibre and Mapbox ship pre-rasterised glyph ranges as PBF encoded SDFs, indexed by Unicode range**
  - source: `03_theory.tex:132`
  - type: `name`

### Sprites

- **Sprite rendering is a well-established technique in computer graphics**
  - source: `03_theory.tex:136`
  - type: `scope`

- **MapLibre and Mapbox ship plain PNG or SDF-PNG sprite sheets together with a lookup table**
  - source: `03_theory.tex:140`
  - type: `name`

- **The lookup table records the location of each sprite, whether it is an SDF, and optional stretchable regions for symbols**
  - source: `03_theory.tex:141`
  - type: `scope`

### Tiles

- **At zoom level z, the world is subdivided into 2^z × 2^z tiles**
  - source: `03_theory.tex:148`
  - type: `number`

- **Each tile is identified by its column x, row y, and zoom level z**
  - source: `03_theory.tex:148`
  - type: `scope`

- **Lower zoom levels cover large geographic areas with simplified geometry; higher zoom levels cover smaller areas with greater detail**
  - source: `03_theory.tex:149`
  - type: `qualitative`

- **The client requests only the tiles intersecting the current viewport**
  - source: `03_theory.tex:150`
  - type: `scope`

- **When a client requests a tile at a zoom level beyond the source's maximum, the renderer overzooms it upscales the nearest available tile from the source's highest available zoom to fill the viewport**
  - source: `03_theory.tex:151`
  - type: `scope`

- **The layers sourced from that tile remain rendered at the overzoomed level even though no new tile is fetched**
  - source: `03_theory.tex:153`
  - type: `scope`

- **A layer's effective visibility at a given camera zoom is a function of both the layer's filter and the source's maxzoom, not the layer bounds alone**
  - source: `03_theory.tex:154-155`
  - type: `scope`

- **Removing a layer at zoom 14 will suppress its rendering at zoom 15 and beyond if the source's maxzoom is 14**
  - source: `03_theory.tex:156`
  - type: `qualitative`

- **The slicer performs two operations to synthesise a target tile from the source's maxzoom tile: rescale each coordinate by 2^(Δz) and clip to the target extent with a 128-unit overdraw buffer**
  - source: `03_theory.tex:159`
  - type: `number`

- **Both slicer operations consume the source's maxzoom tile as input**
  - source: `03_theory.tex:160`
  - type: `scope`

- **No symmetric underzoom behavior exists**
  - source: `03_theory.tex:162`
  - type: `scope`

- **If a source has no tile at a zoom lower than minzoom, the layer is not rendered there**
  - source: `03_theory.tex:163`
  - type: `scope`

- **A vector tile encodes map data in a compact binary format rather than in a pre-rendered image**
  - source: `03_theory.tex:165`
  - type: `scope`

- **Each tile is organized into source layers and each source layer contains a set of features**
  - source: `03_theory.tex:166`
  - type: `scope`

- **A feature consists of geometry (point, linestring, or polygon), optionally a set of key-value properties, optionally a set of IDs, and metadata**
  - source: `03_theory.tex:167`
  - type: `scope`

- **Raster tiles deliver pre-rendered images (PNG, JPEG, WebP, Avif, JPEGXL) rather than vector geometry**
  - source: `03_theory.tex:172`
  - type: `name`

- **Raster tiles require no client-side rendering logic but cannot be restyled, rotated at arbitrary angles, or queried interactively**
  - source: `03_theory.tex:173`
  - type: `qualitative`

- **FlatGeobuf, GeoParquet, and GeoArrow are analysis-focused formats optimized for analytical queries rather than tile-based rendering**
  - source: `03_theory.tex:175`
  - type: `name`

- **GeoParquet's row-group predicate pushdown and column pruning are analogous to the tile shaving applied to MLT**
  - source: `03_theory.tex:176-177`
  - type: `qualitative`

- **Parquet's row-group and column-chunk metadata would dominate at typical tile sizes (1 to 10 kilobyte)**
  - source: `03_theory.tex:177`
  - type: `number`

- **GeoJSON is a JSON-based geospatial interchange format**
  - source: `03_theory.tex:179`
  - type: `name`

- **GeoJSON verbosity (text-encoded coordinates and repeated property keys per feature) makes it impractical for continuous tile streaming**
  - source: `03_theory.tex:180`
  - type: `qualitative`

- **MVT is the dominant vector tile format, adopted as a de facto standard across open-source map renderers including MapLibre**
  - source: `03_theory.tex:182`
  - type: `name`

- **MVT uses the PBF as its wire format and stores features in a row-oriented layout**
  - source: `03_theory.tex:183`
  - type: `scope`

- **Each Feature carries its own list of property tags encoded as alternating key and value indices into per-layer string and value tables**
  - source: `03_theory.tex:185`
  - type: `scope`

- **Geometry is encoded as a sequence of MoveTo, LineTo, and ClosePath commands with delta-encoded integer coordinates**
  - source: `03_theory.tex:186`
  - type: `scope`

- **Delta-encoded integer coordinates are relative to the tile extent (typically 4096 units per tile edge)**
  - source: `03_theory.tex:186`
  - type: `number`

- **The row-oriented layout means accessing a single property column requires parsing past all other properties of the same Feature**
  - source: `03_theory.tex:188`
  - type: `qualitative`

- **Compression in row-oriented layout operates on the interleaved byte stream rather than on homogeneous data columns**
  - source: `03_theory.tex:188`
  - type: `qualitative`

- **MLT is a columnar vector tile format proposed by Tremmel et al.**
  - source: `03_theory.tex:192`
  - type: `name`

- **MLT stores each property as an independent column with type-specific encoding instead of row-major key-value-pair layout**
  - source: `03_theory.tex:193`
  - type: `scope`

- **MLT columnar layout enables per-column compression strategies (dictionary encoding, delta encoding, run-length encoding) and eliminates per-feature tag overhead**
  - source: `03_theory.tex:194`
  - type: `scope`

- **Tremmel et al. report up to 3× tile size reduction on encoded tilesets and up to 6× on certain large tiles**
  - source: `03_theory.tex:195`
  - type: `number`

- **approximately 14 kilobyte TCP slow-start window**
  - source: `03_theory.tex:199`
  - type: `number`

- **HTTP/2 multiplexing and HTTP/3 with QUIC-based successor for lossy mobile networks**
  - source: `03_theory.tex:199`
  - type: `name`

- **Zstandard and Brotli achieve higher compression ratios than gzip's LZ77 foundation**
  - source: `03_theory.tex:199`
  - type: `qualitative`

- **PMTiles and COMTiles are tile archive formats that enable serverless, cloud-native tile delivery from a single file in blob storage**
  - source: `03_theory.tex:200`
  - type: `name`

- **MVT is the established baseline and MLT aims to improve upon it**
  - source: `03_theory.tex:201`
  - type: `qualitative`

### Styles

- **A map style defines the complete visual appearance of a map, including which data is shown, how it is colored, sized, and labelled, and at which zoom levels each element appears**
  - source: `03_theory.tex:205`
  - type: `scope`

- **Server-side declarative styles, such as MapCSS, define rendering rules on the server**
  - source: `03_theory.tex:209`
  - type: `name`

- **Server-side declarative styles produce pre-rendered raster tiles that the client displays without further interpretation**
  - source: `03_theory.tex:210`
  - type: `scope`

- **Server-side declarative styles simplify the client's rendering logic but prevent client-side restyling**
  - source: `03_theory.tex:211`
  - type: `qualitative`

- **MapLibre and Mapbox use client-side declarative styles**
  - source: `03_theory.tex:213`
  - type: `name`

- **Client-side declarative styles transmit a machine-readable style document to the client, which interprets the style at render time**
  - source: `03_theory.tex:213-214`
  - type: `scope`

- **Client-side declarative styles enable dynamic restyling, data-driven visualization, and interactive features without regenerating tiles**
  - source: `03_theory.tex:215`
  - type: `scope`

- **Gleo and Navara use callback-based styling**
  - source: `03_theory.tex:217`
  - type: `name`

- **Callback-based styling offers maximum flexibility but makes static analysis and automatic optimizations impossible**
  - source: `03_theory.tex:218`
  - type: `qualitative`

- **Client-side declarative styles are amenable to static analysis and automatic optimizations**
  - source: `03_theory.tex:222`
  - type: `qualitative`

- **The MapLibre style specification is a JSON document with key components: Sources, Layers, Filters, Paint and layout properties, and Metadata bounds**
  - source: `03_theory.tex:224-241`
  - type: `scope`

- **Sources declare where tile data comes from and at which zoom levels tiles are available (minzoom, maxzoom)**
  - source: `03_theory.tex:227`
  - type: `scope`

- **Layers are the central rendering unit**
  - source: `03_theory.tex:229`
  - type: `scope`

- **Each layer references a source and a source-layer, specifies a type (fill, line, circle, symbol, fill-extrusion, raster, background or hillshade) and carries paint and layout properties**
  - source: `03_theory.tex:230`
  - type: `name`

- **Layers are drawn in declaration order from bottom to top**
  - source: `03_theory.tex:231`
  - type: `scope`

- **Filters are boolean expressions attached to layers that select which features from the source-layer are rendered**
  - source: `03_theory.tex:234-235`
  - type: `scope`

- **A feature is drawn by a layer only if the layer's filter evaluates true for that feature's properties and geometry type**
  - source: `03_theory.tex:235`
  - type: `scope`

- **Paint properties (colors, opacities, widths) can be changed without triggering a re-layout**
  - source: `03_theory.tex:238-239`
  - type: `scope`

- **Layout properties (text anchoring, icon rotation, symbol spacing) affect feature placement and require re-evaluation when modified**
  - source: `03_theory.tex:239`
  - type: `scope`

- **Metadata bounds (minzoom, maxzoom) restrict the zoom range in which a layer is active**
  - source: `03_theory.tex:241`
  - type: `scope`

- **The renderer can skip layers outside the zoom range before filter evaluation or geometry decoding**
  - source: `03_theory.tex:242`
  - type: `scope`

- **Filters and properties can be specified as literal constants, zoom-dependent expressions, data-driven expressions, or combinations**
  - source: `03_theory.tex:260`
  - type: `scope`

- **Expression trees can be deeply nested and may contain redundant or unreachable branches**
  - source: `03_theory.tex:261`
  - type: `scope`

- **Expression trees are amenable to simplification and optimization techniques used in compilers and database query planners**
  - source: `03_theory.tex:262`
  - type: `qualitative`

### Feature and Global State

- **Feature state is a per-feature map keyed by the (source, source-layer, feature ID) triple**
  - source: `03_theory.tex:276`
  - type: `scope`

- **Feature state is mutated from the host application via setFeatureState and removeFeatureState**
  - source: `03_theory.tex:276`
  - type: `scope`

- **Feature state is read from style expressions through the ["feature-state", key] operator**
  - source: `03_theory.tex:276`
  - type: `scope`

- **Feature state's canonical use is interactive UI such as hover highlighting or click-driven selection**
  - source: `03_theory.tex:277`
  - type: `scope`

- **Global state is a map-wide key-value store mutated via setGlobalStateProperty and read through the ["global-state", key] operator**
  - source: `03_theory.tex:278`
  - type: `scope`

- **Global state typically backs up application-wide toggles such as a day/night switch or a per-mode road-class filter**
  - source: `03_theory.tex:279`
  - type: `scope`

- **A state change re-evaluates the dependent paint expressions at render time, without re-parsing the tile or re-running bucket population**
  - source: `03_theory.tex:281`
  - type: `scope`

- **Feature state is cheap enough to drive hover effects**
  - source: `03_theory.tex:282`
  - type: `qualitative`

- **Both stores are mutated by the host application at runtime, after the style document and tile data have been loaded**
  - source: `03_theory.tex:283`
  - type: `scope`

- **A reference whose key is missing from the store, or whose stored value has a type the consuming expression cannot handle, raises a runtime evaluation error**
  - source: `03_theory.tex:284`
  - type: `scope`

- **Feature-state addressing requires stable feature IDs**
  - source: `03_theory.tex:285`
  - type: `scope`

## Compiler Optimization Techniques

- **Style expressions used by map renderers contain conditionals (case, match), boolean operators (all, any), arithmetic, and data access (get, has)**
  - source: `03_theory.tex:290`
  - type: `name`

- **Style expressions contain variables (lexical bindings via let/var, and runtime stores)**
  - source: `03_theory.tex:290`
  - type: `scope`

### Peephole Optimization

- **A peephole optimizer examines a small, fixed-size window of code and applies local pattern-matching rewrites**
  - source: `03_theory.tex:297`
  - type: `scope`

- **Each rewrite rule is independent, matching a local pattern and emitting a replacement without requiring knowledge of the surrounding program**
  - source: `03_theory.tex:298`
  - type: `scope`

- **Many small, local improvements accumulate into substantial global gains under repeated application**
  - source: `03_theory.tex:299`
  - type: `qualitative`

- **Machine-level peephole optimizers replace instruction sequences (e.g., replacing a multiply by a power of two with a shift)**
  - source: `03_theory.tex:303`
  - type: `qualitative`

- **IR-level peephole optimizers apply algebraic simplifications, identity eliminations, and strength reductions to expression trees**
  - source: `03_theory.tex:304`
  - type: `scope`

- **In the context of style expressions, the peephole window corresponds to a single expression node and its immediate children**
  - source: `03_theory.tex:305`
  - type: `scope`

- **A post-order visitor walks the expression tree and attempts to apply each rule at every node**
  - source: `03_theory.tex:306`
  - type: `scope`

### Constant Folding and Propagation

- **Constant folding evaluates expressions whose operands are all compile-time constants, replacing the expression with its result**
  - source: `03_theory.tex:310`
  - type: `scope`

- **Constant propagation extends constant folding by tracking known values of variables and substituting them at use sites**
  - source: `03_theory.tex:313-314`
  - type: `scope`

- **SCCP combines constant propagation with dead branch analysis in a single pass**
  - source: `03_theory.tex:316`
  - type: `scope`

- **SCCP simultaneously determines which values are constant and which branches are reachable**
  - source: `03_theory.tex:317`
  - type: `scope`

### Dead Code Elimination

- **DCE removes program statements whose results are never used or whose control-flow paths are unreachable**
  - source: `03_theory.tex:321`
  - type: `scope`

- **Unreachable code elimination removes code that can never be executed**
  - source: `03_theory.tex:322`
  - type: `scope`

- **Dead store elimination removes assignments to variables that are never subsequently read**
  - source: `03_theory.tex:322`
  - type: `scope`

- **Dead code elimination in map-style domain corresponds to removing style layers that can never produce visible output**
  - source: `03_theory.tex:324`
  - type: `scope`

### Algebraic Simplification

- **Algebraic simplification applies mathematical identities to reduce expression complexity without changing semantics**
  - source: `03_theory.tex:328`
  - type: `scope`

- **Identity elements: x ∧ true = x, x ∨ false = x, x + 0 = x, x · 1 = x**
  - source: `03_theory.tex:335-338`
  - type: `scope`

- **Annihilation: x ∧ false = false, x ∨ true = true, ∀x ∈ ℕ: x · 0 = 0**
  - source: `03_theory.tex:345-348`
  - type: `scope`

- **De Morgan's laws: ¬(a ∧ b) = ¬a ∨ ¬b, ¬(a ∨ b) = ¬a ∧ ¬b**
  - source: `03_theory.tex:354-355`
  - type: `scope`

- **Idempotence: x ∧ x = x, x ∨ x = x**
  - source: `03_theory.tex:362-363`
  - type: `scope`

- **Absorption: x ∧ (x ∨ y) = x, x ∨ (x ∧ y) = x**
  - source: `03_theory.tex:370-371`
  - type: `scope`

- **A filter ["all", ["all", a, b], c] is flattened to ["all", a, b, c] by associativity**
  - source: `03_theory.tex:377`
  - type: `qualitative`

- **A filter ["all", true, x] is simplified to x by identity elimination**
  - source: `03_theory.tex:378`
  - type: `qualitative`

### Fixpoint Iteration

- **Individual peephole rules may expose further opportunities**
  - source: `03_theory.tex:382`
  - type: `qualitative`

- **Constant folding a subexpression may create a new constant parent that enables dead branch elimination**
  - source: `03_theory.tex:383`
  - type: `qualitative`

- **A single traversal is generally insufficient**
  - source: `03_theory.tex:383`
  - type: `qualitative`

- **The remedy is to apply the entire rule set repeatedly until no rule fires**
  - source: `03_theory.tex:385`
  - type: `scope`

- **A term to which no rule applies is a fixpoint of the rewrite function**
  - source: `03_theory.tex:386`
  - type: `scope`

- **A term to which no rule applies is a normal form of the underlying rewrite system**
  - source: `03_theory.tex:386-387`
  - type: `scope`

- **In practice the loop reaches a normal form within a handful of iterations and is capped at eight as a safety bound**
  - source: `03_theory.tex:390`
  - type: `number`

- **Newcomb et al. reported similar confluence and termination concerns for Halide's hand-written rewrite optimizer**
  - source: `03_theory.tex:391`
  - type: `citation`

## Query Optimization

- **Style filters in map rendering are structurally equivalent to database query predicates**
  - source: `03_theory.tex:395-396`
  - type: `qualitative`

- **Both select a subset of records from a dataset based on attribute conditions**
  - source: `03_theory.tex:396`
  - type: `qualitative`

- **Techniques from relational query optimizations apply directly**
  - source: `03_theory.tex:397`
  - type: `qualitative`

### Cost-Based Query Optimization

- **A cost-based query optimizer selects among semantically equivalent query execution plans by estimating the cost of each plan**
  - source: `03_theory.tex:401`
  - type: `scope`

- **The order in which predicates are evaluated affects performance even when the final result is identical**
  - source: `03_theory.tex:403`
  - type: `qualitative`

- **Under short-circuit semantics, a conjunction p₁ ∧ p₂ ∧ ... ∧ pₙ is fastest when the most-likely-false predicate comes first**
  - source: `03_theory.tex:404`
  - type: `qualitative`

- **Under short-circuit semantics, a disjunction p₁ ∨ p₂ ∨ ... ∨ pₙ places the most-likely-true predicate first**
  - source: `03_theory.tex:404`
  - type: `qualitative`

### Selectivity Estimation

- **Estimating the expected fraction of records satisfying a predicate is known as selectivity estimation**
  - source: `03_theory.tex:408`
  - type: `scope`

- **Selinger et al. introduced foundational formulas for estimating selectivity under the independence assumption**
  - source: `03_theory.tex:409`
  - type: `citation`

- **The independence assumption is the assumption that attribute values in different columns are statistically independent**
  - source: `03_theory.tex:409`
  - type: `scope`

- **For a single equality predicate A = v on a column with d distinct values, the estimated selectivity is s = 1/d**
  - source: `03_theory.tex:411`
  - type: `scope`

- **When value-frequency histograms are available, the estimate improves to s = freq(v) / N**
  - source: `03_theory.tex:412`
  - type: `scope`

- **Compound selectivities: s(p₁ ∧ p₂) = s(p₁) · s(p₂), s(p₁ ∨ p₂) = 1 - (1 - s(p₁))(1 - s(p₂))**
  - source: `03_theory.tex:415-416`
  - type: `scope`

- **The independence assumption is known to be inaccurate when columns are correlated**
  - source: `03_theory.tex:419`
  - type: `qualitative`

- **The independence assumption provides a computationally cheap approximation that is effective in practice**
  - source: `03_theory.tex:419`
  - type: `qualitative`

- **More sophisticated estimators (multi-dimensional histograms, sampling-based methods, or lightweight graphical models) improve accuracy at higher computational cost**
  - source: `03_theory.tex:420`
  - type: `qualitative`

- **In \ac{OMT}ass and subclass are strongly correlated by schema design**
  - source: `03_theory.tex:423`
  - type: `qualitative`

- **In \ac{OMT}min_level and maritime are strongly correlated**
  - source: `03_theory.tex:423`
  - type: `qualitative`

### Partial Evaluation

- **Partial evaluation (also called program specialization) transforms a program with respect to known static inputs**
  - source: `03_theory.tex:429`
  - type: `scope`

- **Partial evaluation produces a residual program that depends only on the remaining dynamic inputs**
  - source: `03_theory.tex:429`
  - type: `scope`

- **The style optimizer performs partial evaluation of the rendering function**
  - source: `03_theory.tex:430`
  - type: `scope`

- **The style (static input) is known at optimization time, while tile data (dynamic input) varies at runtime**
  - source: `03_theory.tex:431`
  - type: `scope`

- **Filter-to-property constant propagation is a textbook instance of partial evaluation**
  - source: `03_theory.tex:432`
  - type: `qualitative`

- **MapLibre paints only features that pass the filter**
  - source: `03_theory.tex:433`
  - type: `scope`

- **Any equality constraint in the filter holds for every feature reaching the paint expression**
  - source: `03_theory.tex:433`
  - type: `scope`

- **The optimizer substitutes that constraint into the paint expression and folds away the branches it rules out**
  - source: `03_theory.tex:434-435`
  - type: `scope`

- **The filter itself stays unchanged and still runs at render time against dynamic feature data**
  - source: `03_theory.tex:434-435`
  - type: `scope`

- **The tile's value distribution (cardinalities, per-property frequencies, geometry-type counts) is the additional static input**
  - source: `03_theory.tex:435`
  - type: `scope`

- **Stats-driven folding uses tile value distribution to collapse match arms over absent values, tighten zoom bounds, and convert high-selectivity predicates into constants**
  - source: `03_theory.tex:435`
  - type: `scope`

- **Profile-guided optimization would require measuring per-expression hotness at render time**
  - source: `03_theory.tex:436-437`
  - type: `qualitative`

- **The style optimizer never observes render-time execution and therefore does not perform profile-guided specialization**
  - source: `03_theory.tex:437-438`
  - type: `scope`

- **The encoding strategy competition is a single-output search**
  - source: `03_theory.tex:439`
  - type: `scope`

- **Encoding strategy competition trials each candidate from a designer-specified set (sort orders × encoding schemes) on actual data and emits the smallest**
  - source: `03_theory.tex:440`
  - type: `scope`

- **A profiler prunes the encoding strategy search beforehand**
  - source: `03_theory.tex:440`
  - type: `scope`

- **Encoding strategy selection is exhaustive strategy selection over a bounded candidate space, optimal within that space but blind to strategies outside it**
  - source: `03_theory.tex:441`
  - type: `qualitative`

## Data Encoding and Compression

- **Efficient encoding of tile data is essential for interactive map performance**
  - source: `03_theory.tex:445`
  - type: `qualitative`

- **Tiles are fetched continuously during map interaction**
  - source: `03_theory.tex:445`
  - type: `scope`

- **A column has to be both represented as a value sequence and packed into bytes**
  - source: `03_theory.tex:446`
  - type: `scope`

- **Some named schemes only address the first step while relying on the second to actually shrink the byte count**
  - source: `03_theory.tex:446`
  - type: `scope`

- **A logical-level technique is the representation of a value sequence**
  - source: `03_theory.tex:448`
  - type: `scope`

- **A physical-level technique is the packing into bytes**
  - source: `03_theory.tex:448`
  - type: `scope`

- **A column applies zero or more logical techniques in chain and then exactly one physical technique**
  - source: `03_theory.tex:449`
  - type: `scope`

### Column-Oriented Storage

- **Traditional database systems store data in row-oriented layouts, where all attributes of a single record are stored contiguously**
  - source: `03_theory.tex:455`
  - type: `scope`

- **Row-oriented layout is efficient for transactional workloads that access entire records**
  - source: `03_theory.tex:456`
  - type: `qualitative`

- **Row-oriented layout is wasteful for analytical queries that access only a few columns**
  - source: `03_theory.tex:456`
  - type: `qualitative`

- **Column-oriented (columnar) storage transposes the layout, storing all values of a single attribute contiguously**
  - source: `03_theory.tex:458`
  - type: `scope`

- **Dremel introduced the record shredding and assembly algorithm for nested columnar data using definition and repetition levels**
  - source: `03_theory.tex:459`
  - type: `citation`

- **Dremel's representation pattern directly inspired Apache Parquet**
  - source: `03_theory.tex:459`
  - type: `citation`

- **Columnar layout inspired the columnar layout that MLT adapts for tile data**
  - source: `03_theory.tex:459-460`
  - type: `qualitative`

- **Columnar layout offers reduced I/O from reading or transferring only referenced columns**
  - source: `03_theory.tex:460`
  - type: `qualitative`

- **Columnar layout offers better compression from higher local homogeneity of values of the same type and semantic domain**
  - source: `03_theory.tex:460`
  - type: `qualitative`

- **Columnar layout offers vectorised processing from natural fit for SIMD-style batch operations over arrays of the same type**
  - source: `03_theory.tex:460`
  - type: `qualitative`

- **The row-oriented MVT format stores all properties of a feature together**
  - source: `03_theory.tex:462`
  - type: `scope`

- **The columnar MLT format stores each property as an independent column**
  - source: `03_theory.tex:462`
  - type: `scope`

- **Columnar layout allows per-column encoding strategies**
  - source: `03_theory.tex:463`
  - type: `scope`

- **A column of road classes can use dictionary encoding, while a column of building heights can use a DeltaRLE logical chain handed to a physical technique such as FastPFOR**
  - source: `03_theory.tex:464`
  - type: `qualitative`

### Logical Integer Encodings

- **Integer columns appear throughout tile data as geometry coordinates, feature IDs, property values, and dictionary indices**
  - source: `03_theory.tex:468`
  - type: `scope`

- **Logical-level techniques rewrite the value sequence so that a downstream physical technique sees a distribution that packs to fewer bytes**
  - source: `03_theory.tex:469`
  - type: `scope`

- **Zigzag encoding maps signed integers to unsigned ones (n ↦ 2n for n ≥ 0, n ↦ -2n-1 for n < 0)**
  - source: `03_theory.tex:473`
  - type: `scope`

- **Zigzag encoding produces small unsigned codes for small-magnitude negative values**
  - source: `03_theory.tex:473`
  - type: `qualitative`

- **Zigzag encoding byte count is unchanged on its own and the saving comes from the downstream physical technique**
  - source: `03_theory.tex:474`
  - type: `scope`

- **Delta encoding replaces each value with the difference from its predecessor**
  - source: `03_theory.tex:476-477`
  - type: `scope`

- **Delta encoding does not shrink the column by itself**
  - source: `03_theory.tex:478`
  - type: `qualitative`

- **Delta produces the same number of values at (often) smaller magnitude, which then pack well under VarInt or FastPFOR**
  - source: `03_theory.tex:479`
  - type: `qualitative`

- **RLE replaces consecutive runs of identical values with (value, count) pairs**
  - source: `03_theory.tex:481`
  - type: `scope`

- **RLE reduces the symbol count on its own, unlike zigzag and delta**
  - source: `03_theory.tex:482`
  - type: `qualitative`

- **MLT classifies RLE as logical because it composes with other logical steps before a physical technique**
  - source: `03_theory.tex:483`
  - type: `scope`

- **RLE is most effective for low-cardinality, clustered columns, for example a road-class column sorted by class**
  - source: `03_theory.tex:484`
  - type: `qualitative`

- **Logical techniques chain freely**
  - source: `03_theory.tex:487`
  - type: `scope`

- **The canonical chain applies delta first and then RLE (written DeltaRLE)**
  - source: `03_theory.tex:488`
  - type: `scope`

- **DeltaRLE is effective for approximately sorted sequences where delta produces long runs of small (often zero) values that RLE then collapses**
  - source: `03_theory.tex:488`
  - type: `qualitative`

### Physical Integer Compressions

- **A physical-level technique packs a value sequence into bytes**
  - source: `03_theory.tex:492`
  - type: `scope`

- **Each integer column applies exactly one physical technique**
  - source: `03_theory.tex:492`
  - type: `scope`

- **VarInt represents each integer with a variable number of bytes, using 7 bits per byte for data and 1 bit as a continuation flag**
  - source: `03_theory.tex:496`
  - type: `scope`

- **VarInt: values in [0, 127] take 1 byte, [128, 16383] take 2 bytes**
  - source: `03_theory.tex:496`
  - type: `number`

- **VarInt expects unsigned values**
  - source: `03_theory.tex:497`
  - type: `scope`

- **A signed integer column is normally preceded by a zigzag remap for VarInt**
  - source: `03_theory.tex:497`
  - type: `scope`

- **FastPFOR partitions the input into fixed-size blocks (typically 128 or 256 values)**
  - source: `03_theory.tex:499`
  - type: `number`

- **FastPFOR computes the minimum bit width that fits most values in each block**
  - source: `03_theory.tex:499`
  - type: `scope`

- **FastPFOR packs at that width, with outliers in a separate patch list**
  - source: `03_theory.tex:499`
  - type: `scope`

- **FastPFOR achieves near-optimal bit packing when most values share a similar magnitude**
  - source: `03_theory.tex:500`
  - type: `qualitative`

- **Abadi et al. proposed property-based selection rules for choosing physical techniques**
  - source: `03_theory.tex:504`
  - type: `citation`

- **Damme et al. developed a cost-model-driven strategy that picks the lowest expected cost for a given data distribution**
  - source: `03_theory.tex:504`
  - type: `citation`

- **BtrBlocks trial-encodes candidate schemes on a sample of each column block and keeps the smallest result**
  - source: `03_theory.tex:506`
  - type: `name`

- **BtrBlocks argues that lightweight on-sample trials are both more accurate than a cost model and cheap enough to run at encode time**
  - source: `03_theory.tex:506`
  - type: `qualitative`

- **Encoding competition in sub:encoding_strategies sits in the same trial-based family as BtrBlocks**
  - source: `03_theory.tex:507`
  - type: `qualitative`

- **Encoding competition trials a pruned set of (logical chain, physical technique) pairs and retains the smallest output**
  - source: `03_theory.tex:508`
  - type: `scope`

- **Encoding competition operates on each whole tile rather than on a sample, since per-tile data volumes are modest**
  - source: `03_theory.tex:508`
  - type: `scope`

### String Compression

- **String data in vector tiles includes feature names, road classes, land-use categories, and administrative identifiers**
  - source: `03_theory.tex:512`
  - type: `scope`

- **Dictionary encoding is the logical-level string technique**
  - source: `03_theory.tex:515`
  - type: `scope`

- **Dictionary encoding stores each unique string once and replaces occurrences with integer indices**
  - source: `03_theory.tex:516`
  - type: `scope`

- **Dictionary encoding is effective when many features share the same value**
  - source: `03_theory.tex:516`
  - type: `qualitative`

- **The resulting index column is handed to the integer techniques of sub:logical_integer_encodings and sub:physical_integer_compressions**
  - source: `03_theory.tex:517`
  - type: `scope`

- **FSST is the physical-level string technique**
  - source: `03_theory.tex:519`
  - type: `scope`

- **FSST is a lightweight, block-oriented compressor**
  - source: `03_theory.tex:520`
  - type: `scope`

- **FSST learns a symbol table of up to 255 frequent byte sequences from the input corpus**
  - source: `03_theory.tex:520`
  - type: `number`

- **FSST replaces occurrences of frequent byte sequences with single-byte codes**
  - source: `03_theory.tex:520-521`
  - type: `scope`

- **FSST preserves random access, so each compressed string can be decompressed independently**
  - source: `03_theory.tex:521`
  - type: `qualitative`

- **FSST is unlike general-purpose compressors such as LZ77 or Zstandard**
  - source: `03_theory.tex:521`
  - type: `qualitative`

- **FSST symbol table is stored once and amortised over all strings in the column**
  - source: `03_theory.tex:522`
  - type: `scope`

- **Dictionary encoding and FSST compose in the same logical-then-physical pattern**
  - source: `03_theory.tex:524`
  - type: `scope`

- **Applying FSST to deduplicated dictionary strings compresses both unique values and byte-level redundancy within them**
  - source: `03_theory.tex:525`
  - type: `qualitative`

### Space-Filling Curves

- **Space-filling curves map multi-dimensional points to a one-dimensional ordering while preserving spatial locality**
  - source: `03_theory.tex:529`
  - type: `scope`

- **Points that are close in two-dimensional space tend to receive nearby positions on the curve**
  - source: `03_theory.tex:530`
  - type: `qualitative`

- **Space-filling curves serve as a logical encoding that maps a 2D coordinate to a single integer column**
  - source: `03_theory.tex:531`
  - type: `scope`

- **Space-filling curves serve as a feature ordering that sorts features before per-column encoding**
  - source: `03_theory.tex:531`
  - type: `scope`

- **Feature ordering improves the effectiveness of delta and RLE on geometry and property columns**
  - source: `03_theory.tex:531`
  - type: `qualitative`

- **Z-order (Morton) curve interleaves the binary representations of the x and y coordinates to form a single index**
  - source: `03_theory.tex:536`
  - type: `scope`

- **Morton code is M(x, y) = Σ(i=0 to b-1) (xᵢ · 2^(2i) + yᵢ · 2^(2i+1))**
  - source: `03_theory.tex:539-540`
  - type: `scope`

- **Morton codes are fast to compute via bit-interleaving instructions**
  - source: `03_theory.tex:542`
  - type: `qualitative`

- **The Z-order curve exhibits jumps between quadrants that break spatial continuity**
  - source: `03_theory.tex:542`
  - type: `qualitative`

- **The Hilbert curve traces a continuous path through the grid without the inter-quadrant jumps of the Z-order curve**
  - source: `03_theory.tex:544`
  - type: `qualitative`

- **The Hilbert curve achieves better locality preservation at the cost of a more complex index computation**
  - source: `03_theory.tex:544`
  - type: `qualitative`

- **The Hilbert R-tree orders rectangles along the Hilbert curve to achieve tighter node packing than conventional R-trees**
  - source: `03_theory.tex:545`
  - type: `name`

- **FlatGeobuf uses a packed Hilbert R-tree for spatial indexing of its features**
  - source: `03_theory.tex:546`
  - type: `name`

- **The Hilbert index is computed recursively by dividing the unit square into four quadrants**
  - source: `03_theory.tex:547-548`
  - type: `scope`

- **Each quadrant is mapped to a sub-range of the curve**
  - source: `03_theory.tex:548`
  - type: `scope`

- **The quadrant containing the point determines the high-order bits of the index**
  - source: `03_theory.tex:549`
  - type: `scope`

- **The process recurses on the sub-quadrant**
  - source: `03_theory.tex:549`
  - type: `scope`

- **Each feature is assigned a curve index based on its first vertex coordinate**
  - source: `03_theory.tex:551`
  - type: `scope`

- **Encoding competition selects the feature ordering that produces the smallest encoded output (across Morton, Hilbert, and non-spatial orderings)**
  - source: `03_theory.tex:551`
  - type: `scope`

### Locality-Sensitive Hashing

- **When multiple string columns share overlapping vocabularies, storing a single shared dictionary can reduce overhead**
  - source: `03_theory.tex:555-556`
  - type: `scope`

- **Identifying which columns share sufficient overlap is a set similarity problem**
  - source: `03_theory.tex:556`
  - type: `scope`

- **MinHash is a locality-sensitive hashing technique**
  - source: `03_theory.tex:558`
  - type: `scope`

- **MinHash estimates the Jaccard similarity between two sets A and B**
  - source: `03_theory.tex:558`
  - type: `scope`

- **Jaccard similarity J(A, B) = |A ∩ B| / |A ∪ B|**
  - source: `03_theory.tex:560`
  - type: `scope`

- **Constructing a MinHash signature requires examining every element of A and B**
  - source: `03_theory.tex:562`
  - type: `scope`

- **Construction time remains O(|A|+|B|) and the input sets must be retained throughout construction**
  - source: `03_theory.tex:562`
  - type: `number`

- **MinHash yields a constant-factor reduction in persistent representation**
  - source: `03_theory.tex:563`
  - type: `qualitative`

- **Exact computation stores all O(|A|+|B|) elements, MinHash stores only k hash values per set**
  - source: `03_theory.tex:564`
  - type: `number`

- **For fixed k, the saving in persistent storage grows without bound as |A| and |B| increase**
  - source: `03_theory.tex:565`
  - type: `qualitative`

- **For each of k independent hash functions h₁, ..., hₖ, the minimum hash value over all elements is recorded: sigᵢ(A) = minₐ∈A hᵢ(a)**
  - source: `03_theory.tex:566`
  - type: `scope`

- **Jaccard similarity is estimated as Ĵ(A, B) = (1/k) Σ(i=1 to k) 1[sigᵢ(A) = sigᵢ(B)]**
  - source: `03_theory.tex:569`
  - type: `scope`

- **The MinHash estimate is unbiased with variance O(1/k)**
  - source: `03_theory.tex:572`
  - type: `qualitative`

- **MinHash accuracy is fine-tunable**
  - source: `03_theory.tex:572`
  - type: `qualitative`

## Benchmarking

- **Benchmarking is the systematic measurement of system performance under controlled workloads and standardized metrics**
  - source: `03_theory.tex:577`
  - type: `scope`

- **Benchmarking is used to evaluate system behavior, compare alternative implementations, and quantify the effects of optimizations**
  - source: `03_theory.tex:577-578`
  - type: `scope`

- **According to Jain, a good evaluation must start with selecting relevant metrics**
  - source: `03_theory.tex:579`
  - type: `citation`

- **Georges et al. demonstrated that naive averaging of execution times on managed runtimes leads to unreliable conclusions**
  - source: `03_theory.tex:580`
  - type: `citation`

- **Georges et al. advocate for confidence intervals computed over multiple independent JVM/engine invocations**
  - source: `03_theory.tex:580`
  - type: `citation`

- **The bootstrap itself is a resampling method for constructing confidence intervals without distributional assumptions**
  - source: `03_theory.tex:582`
  - type: `scope`

- **The bootstrap was formalised by Efron and Tibshirani**
  - source: `03_theory.tex:582`
  - type: `citation`

- **Hoefler and Belli codified twelve common pitfalls in reporting performance results**
  - source: `03_theory.tex:583`
  - type: `citation`

- **Evaluation in ch:experiments follows Hoefler and Belli's guidelines by reporting per-metric confidence intervals and separating throughput from latency measurements**
  - source: `03_theory.tex:584`
  - type: `scope`

- **Resource utilisation metrics include CPU load, GPU utilisation, and memory consumption**
  - source: `03_theory.tex:588`
  - type: `scope`

- **Latency and responsiveness measure the time between initiating an operation and the first visible result**
  - source: `03_theory.tex:589-590`
  - type: `scope`

- **Throughput is typically measured in FPS or frame time**
  - source: `03_theory.tex:590`
  - type: `scope`

- **Frame stability captures variations in frame time and identifies dropped frames or rendering stutters**
  - source: `03_theory.tex:591`
  - type: `scope`

- **Network utilisation includes transferred bytes, tile request rates, and bandwidth consumption**
  - source: `03_theory.tex:592`
  - type: `scope`

- **Power consumption is relevant for mobile devices and battery-powered systems**
  - source: `03_theory.tex:593`
  - type: `scope`

- **Cellular radio energy is proportional to data volume**
  - source: `03_theory.tex:595`
  - type: `qualitative`

- **GPU active time scales with draw-call count**
  - source: `03_theory.tex:595`
  - type: `qualitative`

- **Micro-benchmarks isolate a single operation and measure its cost in isolation**
  - source: `03_theory.tex:601-602`
  - type: `scope`

- **Micro-benchmarks are useful for identifying bottlenecks but may not reflect real-world performance**
  - source: `03_theory.tex:602-603`
  - type: `qualitative`

- **Macro-benchmarks measure the performance of a complete subsystem under controlled conditions**
  - source: `03_theory.tex:603-604`
  - type: `scope`

- **Macro-benchmarks capture interactions between components but require careful setup to ensure reproducibility**
  - source: `03_theory.tex:604`
  - type: `qualitative`

- **Application-level benchmarks measure end-to-end user-perceived performance in a realistic deployment**
  - source: `03_theory.tex:605-606`
  - type: `scope`

- **Application-level benchmarks are the most representative but also the noisiest due to network variability, browser behavior, and hardware differences**
  - source: `03_theory.tex:606-607`
  - type: `qualitative`

- **Macro-benchmarks are primarily used**
  - source: `03_theory.tex:609`
  - type: `scope`

- **Full style is loaded, tiles are fetched and decoded, and the renderer is exercised with a scripted camera animation**
  - source: `03_theory.tex:610-611`
  - type: `scope`

- **Benchmark harness controls for network variability via a caching proxy**
  - source: `03_theory.tex:611`
  - type: `scope`

- **Benchmark harness controls for GPU variability via hardware-accelerated rendering with ANGLE/Vulkan**
  - source: `03_theory.tex:611`
  - type: `name`
