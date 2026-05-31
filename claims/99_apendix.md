## Expression Rewrite Rules

- **Complete set of expression rewrite rules implemented in the optimizer, grouped by pass**
  - source: `99_apendix.tex:9`
  - type: `scope`

- **Rule 1: Negate comparison: [\mlop{"!"},[\mlop{op},a,b]] → [\mlop{neg(op)},a,b] when negated operator exists**
  - source: `99_apendix.tex:24`
  - type: `qualitative`

- **Rule 2: Boolean algebra: fold mlop{any}/ mlop{all} with literal operands; absorb mlval{true} from mlop{all}, mlval{false} from mlop{any}**
  - source: `99_apendix.tex:27`
  - type: `qualitative`

- **Rule 3: Fold negation: [\mlop{"!"}, \mlval{true}] → \mlval{false}**
  - source: `99_apendix.tex:28`
  - type: `qualitative`

- **Rule 4: Fold comparisons (mlop{==}, mlop{!=}, <, etc.) with two literal operands**
  - source: `99_apendix.tex:29`
  - type: `qualitative`

- **Rule 5: Evaluate pure operators when all arguments are literals**
  - source: `99_apendix.tex:30`
  - type: `qualitative`

- **Rule 6: Algebraic identity: x ^ mlval{0} → mlval{1}**
  - source: `99_apendix.tex:31`
  - type: `qualitative`

- **Rule 7: Strip redundant mlop{typeof} guards from migrated filters**
  - source: `99_apendix.tex:32`
  - type: `qualitative`

- **Rule 8: Resolve mlop{case} arms with known boolean conditions**
  - source: `99_apendix.tex:33`
  - type: `qualitative`

- **Rule 9: Resolve mlop{match} when input is a known literal**
  - source: `99_apendix.tex:34`
  - type: `qualitative`

- **Rule 10: SCCP: substitute equality bindings into mlop{case} arm bodies**
  - source: `99_apendix.tex:35`
  - type: `qualitative`

- **Rule 11: SCCP: substitute equality bindings into mlop{match} arm bodies**
  - source: `99_apendix.tex:36`
  - type: `qualitative`

- **Rule 12: Detect contradictory mlop{==}/ mlop{!=} predicates in mlop{all} → mlval{false}**
  - source: `99_apendix.tex:37`
  - type: `qualitative`

- **Rule 13: Substitute equality bindings into sibling predicates in mlop{all}**
  - source: `99_apendix.tex:38`
  - type: `qualitative`

- **Rule 14: Subsume weaker range bounds: keep tighter of two bounds on same variable**
  - source: `99_apendix.tex:39`
  - type: `qualitative`

- **Rule 15: Remove mlop{has} subsumed by comparison on the same property**
  - source: `99_apendix.tex:40`
  - type: `qualitative`

- **Rule 16: Boolean absorption: [\mlop{"all"},A,[\mlop{"any"},A,\ldots]] → [\mlop{"all"},A]**
  - source: `99_apendix.tex:41`
  - type: `qualitative`

- **Rule 17: Remove redundant type coercions on already-typed values**
  - source: `99_apendix.tex:42`
  - type: `qualitative`

- **Rule 18: Strip explicit [\mlop{"properties"}] argument from mlop{get}/ mlop{has}**
  - source: `99_apendix.tex:43`
  - type: `qualitative`

- **Rule 19: Fold [\mlop{"has"},p] → true/false when stats confirm property presence**
  - source: `99_apendix.tex:46`
  - type: `qualitative`

- **Rule 20: Fold [\mlop{"get"},p] to literal when property has a single value**
  - source: `99_apendix.tex:47`
  - type: `qualitative`

- **Rule 21: Fold geometry-type comparison from observed types in tile statistics**
  - source: `99_apendix.tex:48`
  - type: `qualitative`

- **Rule 22: Fold comparison to true/false when value distribution proves constant result**
  - source: `99_apendix.tex:49`
  - type: `qualitative`

- **Rule 23: Prune impossible labels from mlop{in} expression using value statistics**
  - source: `99_apendix.tex:50`
  - type: `qualitative`

- **Rule 24: Prune mlop{match} arms whose labels never appear in property value counts**
  - source: `99_apendix.tex:51`
  - type: `qualitative`

- **Rule 25: Reorder mlop{match} arms by descending value frequency**
  - source: `99_apendix.tex:52`
  - type: `qualitative`

- **Rule 26: Fold mlop{coalesce} when mlop{get} arm is always or never present**
  - source: `99_apendix.tex:53`
  - type: `qualitative`

- **Rule 27: Prune unreachable mlop{interpolate}/ mlop{step} stops outside observed data range**
  - source: `99_apendix.tex:54`
  - type: `qualitative`

- **Rule 28: Factor common operands**
  - source: `99_apendix.tex:57`
  - type: `qualitative`

- **Rule 29: Canonicalise [\mlop{"exponential"},\mlval{1}] → [\mlop{"linear"}] in interpolate curves**
  - source: `99_apendix.tex:58`
  - type: `qualitative`

- **Rule 30: Collapse mlop{interpolate}/ mlop{step} when all output values are structurally equal**
  - source: `99_apendix.tex:59`
  - type: `qualitative`

- **Rule 31: Merge mlop{match} arms with identical outputs; drop arms that equal the fallback**
  - source: `99_apendix.tex:60`
  - type: `qualitative`

- **Rule 32: Strip mlop{coalesce} wrapper from comparison when default fails anyway**
  - source: `99_apendix.tex:61`
  - type: `qualitative`

- **Rule 33: Strip mlop{coalesce} from mlop{match} input when default not in any label**
  - source: `99_apendix.tex:62`
  - type: `qualitative`

- **Rule 34: Strip mlop{coalesce} from mlop{in} needle when default not in haystack**
  - source: `99_apendix.tex:63`
  - type: `qualitative`

- **Rule 35: Rewrite single-arm boolean mlop{match} to mlop{in}/ mlop{==}/ mlop{!=}**
  - source: `99_apendix.tex:64`
  - type: `qualitative`

- **Rule 36: Rewrite [\mlop{"any"},[\mlop{"=="},x,a],\ldots] → [\mlop{"in"},x,[\ldots]]**
  - source: `99_apendix.tex:65`
  - type: `qualitative`

- **Rule 37: Flatten nested mlop{case}: inline the fallback's arms**
  - source: `99_apendix.tex:66`
  - type: `qualitative`

- **Rule 38: Remove trailing mlop{case} arms whose output equals the fallback**
  - source: `99_apendix.tex:67`
  - type: `qualitative`

- **Rule 39: Rewrite mlop{case} to mlop{match} for O(1) dispatch when all arms test equality on the same expression**
  - source: `99_apendix.tex:68`
  - type: `qualitative`

- **Rule 40: Simplify mlop{coalesce}: remove null literals, truncate after first non-null literal**
  - source: `99_apendix.tex:69`
  - type: `qualitative`

- **Rule 41: Flatten nested mlop{coalesce} expressions**
  - source: `99_apendix.tex:70`
  - type: `qualitative`

- **Rule 42: Flatten nested mlop{all}/ mlop{any} operators**
  - source: `99_apendix.tex:71`
  - type: `qualitative`

- **Rule 43: De Morgan's laws: [\mlop{"!"},[\mlop{"any"},A,B]] → [\mlop{"all"},[\mlop{"!"},A],[\mlop{"!"},B]]**
  - source: `99_apendix.tex:72`
  - type: `qualitative`

- **Rule 44: Single-element mlop{in} → mlop{==}**
  - source: `99_apendix.tex:73`
  - type: `qualitative`

- **Rule 45: Merge adjacent mlop{in} expressions on the same variable inside mlop{any}**
  - source: `99_apendix.tex:74`
  - type: `qualitative`

- **Rule 46: Inline single-use mlop{let}/ mlop{var} bindings**
  - source: `99_apendix.tex:75`
  - type: `qualitative`

- **Rule 47: Reorder mlop{any}/ mlop{all} operands by estimated selectivity for short-circuit evaluation**
  - source: `99_apendix.tex:78`
  - type: `qualitative`

## MapLibre GL-JS Reference Excerpts

- **MapLibre performs two operations when synthesizing a tile at a zoom level beyond the source's maxzoom**
  - source: `99_apendix.tex:85`
  - type: `scope`

- **Listing overzoom implementation is from src/source/vector_tile_overzoomed.ts**
  - source: `99_apendix.tex:89`
  - type: `scope`

- **Listing worker_pipeline is from src/source/worker_tile.ts**
  - source: `99_apendix.tex:122`
  - type: `scope`

- **Layer-merging savings depend on two render-pass loops the painter runs over layerIds (opaque top-to-bottom, translucent bottom-to-top)**
  - source: `99_apendix.tex:162`
  - type: `qualitative`

- **Listing painter_loop is from src/render/painter.ts**
  - source: `99_apendix.tex:165`
  - type: `scope`

- **Per-layer placement loop justifies the exclusion of symbol layers from the merge candidate set**
  - source: `99_apendix.tex:186`
  - type: `qualitative`

- **Listing placement is from src/style/pauseable_placement.ts**
  - source: `99_apendix.tex:192`
  - type: `scope`

- **FillBucket.populate method witnesses the filter-first evaluation order**
  - source: `99_apendix.tex:216`
  - type: `qualitative`

- **Listing bucket_populate is from src/data/bucket/fill_bucket.ts**
  - source: `99_apendix.tex:222`
  - type: `scope`

## Camera Animation Patterns

- **Five synthetic camera animation patterns: zigzag, spiral, zoomdrill, pansweep, bearingspin**
  - source: `99_apendix.tex:245`
  - type: `scope`

- **Zigzag stresses zoom-triggered layer-visibility changes along tile loading**
  - source: `99_apendix.tex:330`
  - type: `qualitative`

- **Spiral camera orbits its target while pointing at it, isolates render cost from tile-load cost via a stable tile set**
  - source: `99_apendix.tex:387`
  - type: `qualitative`

- **Zoomdrill maximizes tile-cache churn**
  - source: `99_apendix.tex:435`
  - type: `qualitative`

- **Pansweep drives sustained unidirectional (thus predictable) tile cache misses in isolation**
  - source: `99_apendix.tex:491`
  - type: `qualitative`

- **Bearingspin exercises θ and high-φ-based GPU re-rendering cost without any non-LOD tile loading**
  - source: `99_apendix.tex:540`
  - type: `qualitative`

- **Zigzag pattern: 8 keyframes with xy, z, θ DOF and φ = 0°**
  - source: `99_apendix.tex:558`
  - type: `number`

- **Spiral pattern: 12 keyframes with xy, θ DOF and φ = 0°**
  - source: `99_apendix.tex:559`
  - type: `number`

- **Zoomdrill pattern: 7 keyframes with z DOF and φ = 0°**
  - source: `99_apendix.tex:560`
  - type: `number`

- **Pansweep pattern: 6 keyframes with xy DOF and φ = 0°**
  - source: `99_apendix.tex:561`
  - type: `number`

- **Bearingspin pattern: 8 keyframes with θ DOF and φ = 60°**
  - source: `99_apendix.tex:562`
  - type: `number`

## Per-Style Ablation Results

- **Per-style, per-ablation-step results include: size (raw bytes, gzip level 9, Brotli max), median load time, median FPS, and layer count**
  - source: `99_apendix.tex:581`
  - type: `qualitative`

- **Performance metrics are medians across all combinations of scenarios and animations**
  - source: `99_apendix.tex:582`
  - type: `qualitative`

- **Steps 16–19 (selectivity reorder, tile shaving, tile rewrite) require tile statistics and are only available for fiord and liberty, which were benchmarked with an .mbtiles source**
  - source: `99_apendix.tex:583`
  - type: `qualitative`

- **Americana excluded from per-style tables due to incomplete benchmark data (only 3 of 20 ablation steps completed)**
  - source: `99_apendix.tex:584`
  - type: `qualitative`

- **imports per-style ablation table for Liberty from per_style_liberty.csv**
  - source: `99_apendix.tex:586`
  - type: `scope`

- **imports per-style ablation table for Bright from per_style_bright.csv**
  - source: `99_apendix.tex:587`
  - type: `scope`

- **imports per-style ablation table for Positron from per_style_positron.csv**
  - source: `99_apendix.tex:588`
  - type: `scope`

- **imports per-style ablation table for Fiord from per_style_fiord.csv**
  - source: `99_apendix.tex:589`
  - type: `scope`

- **imports per-style ablation table for Dark Matter from per_style_dark_matter.csv**
  - source: `99_apendix.tex:590`
  - type: `scope`

- **imports per-style ablation table for OSM Bright from per_style_osm_bright.csv**
  - source: `99_apendix.tex:591`
  - type: `scope`

- **imports per-style ablation table for Klokan Basic from per_style_klokan_basic.csv**
  - source: `99_apendix.tex:592`
  - type: `scope`

- **imports per-style ablation table for Toner from per_style_toner.csv**
  - source: `99_apendix.tex:593`
  - type: `scope`

- **imports per-style ablation table for OSM Liberty from per_style_osm_liberty.csv**
  - source: `99_apendix.tex:594`
  - type: `scope`

- **imports per-style ablation table for BasemapDE Colour from per_style_basemap_col.csv**
  - source: `99_apendix.tex:595`
  - type: `scope`

- **imports per-style ablation table for BasemapDE Topo from per_style_basemap_top.csv**
  - source: `99_apendix.tex:596`
  - type: `scope`

- **imports per-style ablation table for ICGC Fosc from per_style_icgc_fosc.csv**
  - source: `99_apendix.tex:597`
  - type: `scope`

- **imports per-style ablation table for ICGC Gris from per_style_icgc_gris.csv**
  - source: `99_apendix.tex:598`
  - type: `scope`

- **imports per-style ablation table for Stadia Outdoors from per_style_stadia_outdoors.csv**
  - source: `99_apendix.tex:599`
  - type: `scope`

## Per-Zoom Tile Size Breakdown

- **Per-zoom-level tile size (gzip) for the Germany \ac{OMT} tileset across four encoding configurations: MVT baseline, reference MLT encoder (Tremmel & Zink), MLT encoder (this work, without shaving), and full pipeline (style optimizations + tile shaving + encoder)**
  - source: `99_apendix.tex:604`
  - type: `scope`

- **For the shaved configuration, advisory generated from the fiord style is used**
  - source: `99_apendix.tex:605`
  - type: `qualitative`

- **imports tile_sizes_per_zoom.csv for per-zoom tile size comparison**
  - source: `99_apendix.tex:621`
  - type: `scope`

## Maputnik Generalisation Corpus

- **13 styles from the Maputnik editor catalog used in the cross-style generalization study**
  - source: `99_apendix.tex:638`
  - type: `number`

- **Two catalog entries were unavailable at the time of measurement (HTTP 403)**
  - source: `99_apendix.tex:639`
  - type: `qualitative`

- **Optimizer run with all static passes enabled (no tile statistics)**
  - source: `99_apendix.tex:640`
  - type: `qualitative`

- **Empty Style: 0 layers, baseline 197 B, optimised 153 B, -22.3% raw, -12.0% Brotli**
  - source: `99_apendix.tex:649`
  - type: `number`

- **Americana: 353 layers, baseline 1103650 B, optimised 450242 B, -59.2% raw, -2.2% Brotli**
  - source: `99_apendix.tex:650`
  - type: `number`

- **AWS Hybrid: 125 layers, baseline 122022 B, optimised 109088 B, -10.6% raw, -3.6% Brotli**
  - source: `99_apendix.tex:651`
  - type: `number`

- **AWS Standard: 160 layers, baseline 143294 B, optimised 128055 B, -10.6% raw, -3.1% Brotli**
  - source: `99_apendix.tex:652`
  - type: `number`

- **Dark Matter: 47 layers, baseline 29642 B, optimised 18894 B, -36.3% raw, -9.8% Brotli**
  - source: `99_apendix.tex:653`
  - type: `number`

- **LocationIQ Streets: 119 layers, baseline 127889 B, optimised 41253 B, -67.7% raw, -17.0% Brotli**
  - source: `99_apendix.tex:654`
  - type: `number`

- **MapTiler Basic: 48 layers, baseline 23277 B, optimised 15966 B, -31.4% raw, -2.1% Brotli**
  - source: `99_apendix.tex:655`
  - type: `number`

- **Toner: 37 layers, baseline 31608 B, optimised 13435 B, -57.5% raw, -13.9% Brotli**
  - source: `99_apendix.tex:656`
  - type: `number`

- **OSM Bright: 128 layers, baseline 74188 B, optimised 49762 B, -32.9% raw, -11.9% Brotli**
  - source: `99_apendix.tex:657`
  - type: `number`

- **OSM Liberty: 105 layers, baseline 48300 B, optimised 33675 B, -30.3% raw, -11.7% Brotli**
  - source: `99_apendix.tex:658`
  - type: `number`

- **Positron: 50 layers, baseline 32736 B, optimised 20232 B, -38.2% raw, -11.5% Brotli**
  - source: `99_apendix.tex:659`
  - type: `number`

- **Stadia Outdoors: 110 layers, baseline 43208 B, optimised 41837 B, -3.2% raw, -3.1% Brotli**
  - source: `99_apendix.tex:660`
  - type: `number`

- **Versatiles Colorful: 309 layers, baseline 151692 B, optimised 114549 B, -24.5% raw, -0.7% Brotli**
  - source: `99_apendix.tex:661`
  - type: `number`

## Benchmark Environment

- **All measurements collected on a single workstation**
  - source: `99_apendix.tex:674`
  - type: `qualitative`

- **Preprocessing (MVT pruning, MLT encoding) and browser-based rendering used the same host**
  - source: `99_apendix.tex:675`
  - type: `qualitative`

### Hardware

- **CPU: AMD Ryzen 7 3700X (Zen 2, 8 cores / 16 threads, base 3.6 GHz / boost 4.4 GHz)**
  - source: `99_apendix.tex:687`
  - type: `name`

- **RAM: 46 GiB usable (3×16 GiB DDR4-3200 UDIMM, 1.2 V; configured at 1600 MT/s, 2 of 4 channels populated)**
  - source: `99_apendix.tex:688`
  - type: `name`

- **GPU: NVIDIA GeForce GTX 1660 SUPER (Turing TU116, 6 GB GDDR6, discrete)**
  - source: `99_apendix.tex:689`
  - type: `name`

- **Storage: Corsair Force MP600 1 TB NVMe M.2 SSD (PCIe Gen 4 x4, 931.5 GiB usable)**
  - source: `99_apendix.tex:690`
  - type: `name`

- **Form factor: Desktop workstation**
  - source: `99_apendix.tex:691`
  - type: `name`

### Operating System and Graphics Stack

- **Distribution: Manjaro Linux (rolling, x86_64)**
  - source: `99_apendix.tex:707`
  - type: `name`

- **Kernel: Linux 6.6.126-1-MANJARO (SMP PREEMPT_DYNAMIC, built 2026-02-16)**
  - source: `99_apendix.tex:708`
  - type: `name`

- **glibc: GNU libc 2.43**
  - source: `99_apendix.tex:709`
  - type: `name`

- **GPU driver: NVIDIA proprietary 590.48.01**
  - source: `99_apendix.tex:710`
  - type: `name`

- **Vulkan loader: API 1.4.325, conformance 1.4.3.0, driver NVIDIA 590.48.1.0**
  - source: `99_apendix.tex:711`
  - type: `name`

- **ANGLE backend: Vulkan**
  - source: `99_apendix.tex:712`
  - type: `name`

### Language Toolchains

- **Rust (rustc): 1.94.1 (2026-03-25)**
  - source: `99_apendix.tex:731`
  - type: `name`

- **Cargo: 1.94.1 (2026-03-24)**
  - source: `99_apendix.tex:732`
  - type: `name`

- **JDK: Eclipse Temurin 22.0.2+9**
  - source: `99_apendix.tex:733`
  - type: `name`

- **Gradle: uses gradlew**
  - source: `99_apendix.tex:734`
  - type: `name`

- **Node.js: v25.8.1**
  - source: `99_apendix.tex:735`
  - type: `name`

- **npm: 11.12.1**
  - source: `99_apendix.tex:736`
  - type: `name`

- **Python: 3.13.2**
  - source: `99_apendix.tex:737`
  - type: `name`

### Browser and Headless Render Harness

- **Rendering scenarios drive a headless Chromium instance via Puppeteer**
  - source: `99_apendix.tex:749`
  - type: `qualitative`

- **Visual-correctness check uses MapLibre GL JS's Node-side software rasteriser with pixelmatch**
  - source: `99_apendix.tex:750`
  - type: `qualitative`

- **Chrome launch flags: --enable-gpu, --ignore-gpu-blocklist, --enable-unsafe-swiftshader, --use-angle=vulkan, --enable-features=Vulkan,UseSkiaRenderer, --disable-frame-rate-limit, --enable-webgl, --disable-gpu-vsync, --renderer-process-limit=8, --disable-background-networking, --disable-background-timer-throttling, --disable-backgrounding-occluded-windows**
  - source: `99_apendix.tex:751-760`
  - type: `qualitative`

- **Browser engine: Google Chrome 137.0.7151.68 (headless)**
  - source: `99_apendix.tex:769`
  - type: `name`

- **Puppeteer: ^24.0.0**
  - source: `99_apendix.tex:770`
  - type: `name`

- **MapLibre GL JS: ^6.0.0-9**
  - source: `99_apendix.tex:771`
  - type: `name`

- **pixelmatch: ^7.1.0**
  - source: `99_apendix.tex:772`
  - type: `name`

- **pngjs: ^7.0.0**
  - source: `99_apendix.tex:773`
  - type: `name`

- **Graphics backend: ANGLE on Vulkan**
  - source: `99_apendix.tex:774`
  - type: `name`

- **Device pixel ratio: 1.0**
  - source: `99_apendix.tex:775`
  - type: `number`

### Key Library Versions

- **MLT-Rust: mlt-core 0.9.0**
  - source: `99_apendix.tex:797`
  - type: `name`

- **MLT-Rust: mvt-reader 2.3.0**
  - source: `99_apendix.tex:798`
  - type: `name`

- **MLT-Rust: fastpfor 0.9**
  - source: `99_apendix.tex:799`
  - type: `name`

- **MLT-Rust: fsst-rs git @pruning**
  - source: `99_apendix.tex:800`
  - type: `name`

- **MLT-Rust: brotli 8**
  - source: `99_apendix.tex:801`
  - type: `name`

- **MLT-Rust: zstd 0.13**
  - source: `99_apendix.tex:802`
  - type: `name`

- **MLT-Rust: flate2 1**
  - source: `99_apendix.tex:803`
  - type: `name`

- **MLT-Rust: criterion 0.8**
  - source: `99_apendix.tex:804`
  - type: `name`

- **Optimiser: mlt-core 0.9**
  - source: `99_apendix.tex:806`
  - type: `name`

- **Optimiser: prost 0.13**
  - source: `99_apendix.tex:807`
  - type: `name`

- **MLT-Java: protobuf-java 4.34.0**
  - source: `99_apendix.tex:809`
  - type: `name`

- **MLT-Java: JavaFastPFOR 0.3.10**
  - source: `99_apendix.tex:810`
  - type: `name`

- **MLT-Java: jts-core 1.20.0**
  - source: `99_apendix.tex:811`
  - type: `name`

- **MLT-Java: mapbox-vector-tile-java 25.1.0**
  - source: `99_apendix.tex:812`
  - type: `name`

- **MLT-Java: earcut4j 3.0.0**
  - source: `99_apendix.tex:813`
  - type: `name`

- **MLT-Java: guava 33.5.0-jre**
  - source: `99_apendix.tex:814`
  - type: `name`

- **MLT-Java: hppc 0.10.0**
  - source: `99_apendix.tex:815`
  - type: `name`

- **MLT-Java: jmh-core 1.37**
  - source: `99_apendix.tex:816`
  - type: `name`

## Shared-Dictionary Threshold Sweep

- **Chosen threshold of 0.075 captures the majority of the achievable size reduction for MinHash-based shared-dictionary grouping**
  - source: `99_apendix.tex:828`
  - type: `number`

- **Marginal improvement from finer thresholds is modest**
  - source: `99_apendix.tex:828`
  - type: `qualitative`

- **Total encoded mbtiles size of the Germany \ac{OMT} tileset ranges approximately 6 MB out of 3.14 GB total across different MinHash similarity modes and Jaccard thresholds**
  - source: `99_apendix.tex:837`
  - type: `number`

- **Hybrid mode (teal) produces the smallest output at every threshold**
  - source: `99_apendix.tex:834`
  - type: `qualitative`

- **All modes increase monotonically with threshold as fewer column pairs qualify for shared-dictionary grouping**
  - source: `99_apendix.tex:835`
  - type: `qualitative`

## Use of Generative AI and Writing Assistance Tools

- **Anthropic Claude and Google Gemini used as a sounding board on author-written material**
  - source: `99_apendix.tex:847`
  - type: `qualitative`

- **Claude used for reviewing code in the thesis software artefact, suggesting rephrasings of paragraphs the author had already drafted, and discussing how to present or improve specific figures**
  - source: `99_apendix.tex:849`
  - type: `qualitative`

- **Claude not used to draft sections, summarize literature, or do other dumb things**
  - source: `99_apendix.tex:850`
  - type: `qualitative`

- **Grammarly used for grammar, spelling, wording, and punctuation correction of author-written text**
  - source: `99_apendix.tex:852`
  - type: `qualitative`

- **Zeta (Zed editor) provided inline code completions in the thesis software, comparable to other editor completion engines**
  - source: `99_apendix.tex:855`
  - type: `qualitative`

- **Zeta (Zed editor) not used on the LaTeX source**
  - source: `99_apendix.tex:857`
  - type: `qualitative`

- **No prose, figures, tables, results, citations, or scientific claims were generated by generative AI tools**
  - source: `99_apendix.tex:845`
  - type: `qualitative`
