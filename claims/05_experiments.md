## Experiment 1: Expression-Level Optimizations

- **Expression passes reduced per-style median load time by -2.0%**
  - source: `05_experiments.tex:32`
  - type: `number`

- **Per-style load reduction from expression passes spanned -58.8% to +12.3%**
  - source: `05_experiments.tex:52`
  - type: `number`

- **Default stripping accounted for -4.3% raw style size reduction**
  - source: `05_experiments.tex:57`
  - type: `number`

- **Default stripping accounted for -2.9% gzip style size reduction**
  - source: `05_experiments.tex:57`
  - type: `number`

- **Stats-driven folding delivered -1.6% raw-size reduction**
  - source: `05_experiments.tex:58`
  - type: `number`

- **Expression simplification delivered -1.4% raw-size reduction**
  - source: `05_experiments.tex:58`
  - type: `number`

- **Fiord raw style shrank by 20.3%**
  - source: `05_experiments.tex:59`
  - type: `number`

- **Fiord raw style size 22.2 KB to 17.7 KB**
  - source: `05_experiments.tex:59`
  - type: `number`

- **Liberty shrank by 7.0%**
  - source: `05_experiments.tex:59`
  - type: `number`

- **Liberty raw style size 43.1 KB to 40.1 KB**
  - source: `05_experiments.tex:59`
  - type: `number`

- **Fiord gzip reduction of 8.3%**
  - source: `05_experiments.tex:60`
  - type: `number`

- **Liberty gzip reduction of 5.9%**
  - source: `05_experiments.tex:60`
  - type: `number`

- **Aggregate load-time improvement across all expression passes was -2.0% per-style median**
  - source: `05_experiments.tex:72`
  - type: `number`

- **Evaluation on 18 scenarios and 15 benchmark styles**
  - source: `05_experiments.tex:70`
  - type: `scope`

- **Fiord fell by 36.8% in expression-tree node count**
  - source: `05_experiments.tex:166`
  - type: `number`

- **Fiord expression-tree node count 1610 to 1018**
  - source: `05_experiments.tex:166`
  - type: `number`

- **Liberty fell by 10.5% in expression-tree node count**
  - source: `05_experiments.tex:166`
  - type: `number`

- **Liberty expression-tree node count 3537 to 3167**
  - source: `05_experiments.tex:166`
  - type: `number`

## Experiment 2: Structural Optimizations

- **Fiord's 48-layer style shed two layers**
  - source: `05_experiments.tex:182`
  - type: `number`

- **Fiord shed 4.2% of layers**
  - source: `05_experiments.tex:182`
  - type: `number`

- **Fiord translation to 14.1% gzip transfer reduction**
  - source: `05_experiments.tex:183`
  - type: `number`

- **Fiord translation to 36.8% fewer expression-tree nodes**
  - source: `05_experiments.tex:183`
  - type: `number`

- **Liberty's 111 layers shed four**
  - source: `05_experiments.tex:184`
  - type: `number`

- **Liberty shed 3.6% of layers**
  - source: `05_experiments.tex:184`
  - type: `number`

- **Layer-merge step combined four pairs of adjacent layers**
  - source: `05_experiments.tex:184`
  - type: `number`

- **Layer-merge produced 4.9% gzip reduction**
  - source: `05_experiments.tex:184`
  - type: `number`

- **Layer merging produced 10.5% node reduction**
  - source: `05_experiments.tex:184`
  - type: `number`

- **Liberty expression-tree nodes 3537 to 3167**
  - source: `05_experiments.tex:184`
  - type: `number`

- **Layer merging added 36 bytes of gzip**
  - source: `05_experiments.tex:185`
  - type: `number`

- **Bright raw count 44.4 KB to 44.6 KB after layer merging**
  - source: `05_experiments.tex:198`
  - type: `number`

- **Bright layer count dropped by one (119 to 118)**
  - source: `05_experiments.tex:198`
  - type: `number`

## Experiment 3: Data-Level Optimizations

- **Tile shaving dominated with -66.1% pooled median load reduction (fiord+liberty)**
  - source: `05_experiments.tex:230`
  - type: `number`

- **Style-only contributed a modest -2.5%**
  - source: `05_experiments.tex:294`
  - type: `number`

- **Shaving-only dropped pooled median load time from 396 ms to 134 ms**
  - source: `05_experiments.tex:293`
  - type: `number`

- **Shaving-only achieved -66.1% pooled median load time reduction**
  - source: `05_experiments.tex:293`
  - type: `number`

- **Style+shaving reached -67.2% pooled median load time reduction**
  - source: `05_experiments.tex:294`
  - type: `number`

- **MLT re-encoding matched plain-shaving load time within measurement noise (130 ms vs 130 ms)**
  - source: `05_experiments.tex:295`
  - type: `number`

- **Shaving-only lifted pooled median FPS from 837 to 1688**
  - source: `05_experiments.tex:297`
  - type: `number`

- **Shaving-only FPS improvement +101.7%**
  - source: `05_experiments.tex:297`
  - type: `number`

- **Style+shaving reached 1781 FPS**
  - source: `05_experiments.tex:297`
  - type: `number`

- **Style+shaving FPS improvement +112.8%**
  - source: `05_experiments.tex:297`
  - type: `number`

- **MLT variant FPS 2021**
  - source: `05_experiments.tex:297`
  - type: `number`

- **MLT variant FPS improvement +141.4%**
  - source: `05_experiments.tex:297`
  - type: `number`

- **Fiord per-style MLT FPS gain +148.1%**
  - source: `05_experiments.tex:306`
  - type: `number`

- **Liberty per-style MLT FPS gain +149.9%**
  - source: `05_experiments.tex:306`
  - type: `number`

- **Native Rust micro-benchmarks showed 4.6x to 8.3x decode throughput for MLT over MVT+gzip**
  - source: `05_experiments.tex:309`
  - type: `number`

- **Jangda et al measured 45-55% slowdown for WASM relative to native**
  - source: `05_experiments.tex:312`
  - type: `citation`

- **Fiord final load time 120.5 milliseconds (CI: [119.3, 121.5])**
  - source: `05_experiments.tex:317`
  - type: `number`

- **Liberty final load time 133.7 milliseconds (CI: [132.9, 134.2])**
  - source: `05_experiments.tex:317`
  - type: `number`

- **Fiord p-value < 10^-45, n = 270, Wilcoxon test**
  - source: `05_experiments.tex:317`
  - type: `number`

- **Liberty p-value < 10^-45, n = 254, Wilcoxon test**
  - source: `05_experiments.tex:317`
  - type: `number`

- **Fiord combined reduction 14.7% sat 0.2% above style-only 14.5%**
  - source: `05_experiments.tex:291`
  - type: `number`

- **Liberty combined reduction 4.8% matched style-only 4.8%**
  - source: `05_experiments.tex:291`
  - type: `number`

- **Per-scenario load-time synergy appeared in 17 of 36 style-scenario pairs**
  - source: `05_experiments.tex:296`
  - type: `number`

- **Our encoder achieved 28.3% smaller total size than reference baseline**
  - source: `05_experiments.tex:426`
  - type: `number`

- **Our encoder curves remained at 0.6-0.8x MVT throughout zoom range**
  - source: `05_experiments.tex:362`
  - type: `number`

- **Reference-encoder curves drifted above 1.0x at several zoom levels under Brotli/zstd**
  - source: `05_experiments.tex:362`
  - type: `number`

- **Germany \ac{OMT} tileset: MVT 4.24 GB plain**
  - source: `05_experiments.tex:406`
  - type: `number`

- **Germany \ac{OMT} tileset: MVT 3.08 GB gzip**
  - source: `05_experiments.tex:406`
  - type: `number`

- **Germany \ac{OMT} tileset: MVT 3.13 GB Brotli**
  - source: `05_experiments.tex:406`
  - type: `number`

- **Germany \ac{OMT} tileset: MVT 3.16 GB zstd**
  - source: `05_experiments.tex:406`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT reference 4.26 GB plain**
  - source: `05_experiments.tex:407`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT reference 3.54 GB gzip**
  - source: `05_experiments.tex:407`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT reference 3.57 GB Brotli**
  - source: `05_experiments.tex:407`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT reference 3.60 GB zstd**
  - source: `05_experiments.tex:407`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT this work 3.06 GB plain**
  - source: `05_experiments.tex:408`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT this work 2.70 GB gzip**
  - source: `05_experiments.tex:408`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT this work 2.72 GB Brotli**
  - source: `05_experiments.tex:408`
  - type: `number`

- **Germany \ac{OMT} tileset: MLT this work 2.75 GB zstd**
  - source: `05_experiments.tex:408`
  - type: `number`

- **Our encoder vs reference -28.3% plain**
  - source: `05_experiments.tex:410`
  - type: `number`

- **Our encoder vs reference -23.8% gzip**
  - source: `05_experiments.tex:410`
  - type: `number`

- **Our encoder vs reference -23.7% Brotli**
  - source: `05_experiments.tex:410`
  - type: `number`

- **Our encoder vs reference -23.6% zstd**
  - source: `05_experiments.tex:410`
  - type: `number`

- **Our encoder vs MVT -27.9% plain**
  - source: `05_experiments.tex:411`
  - type: `number`

- **Our encoder vs MVT -12.3% gzip**
  - source: `05_experiments.tex:411`
  - type: `number`

- **Our encoder vs MVT -13.1% Brotli**
  - source: `05_experiments.tex:411`
  - type: `number`

- **Our encoder vs MVT -12.9% zstd**
  - source: `05_experiments.tex:411`
  - type: `number`

- **MLT (reference) incorporation included correct delta-zigzag sequencing, RLE viability checks, FSST thresholds**
  - source: `05_experiments.tex:416`
  - type: `qualitative`

- **Germany \ac{OMT} tileset zoom 0-14, 256588 kilo tiles**
  - source: `05_experiments.tex:420`
  - type: `number`

- **Reference encoder worse than gzip-compressed MVT (3.54 GB vs 3.08 GB)**
  - source: `05_experiments.tex:429`
  - type: `number`

- **Our encoder under no compression 3.06 GB already smaller than MVT+gzip 3.08 GB**
  - source: `05_experiments.tex:435`
  - type: `number`

- **MVT under zstd-22 yielded 3.16 GB**
  - source: `05_experiments.tex:440`
  - type: `number`

- **Our encoder under zstd-22 yielded 2.75 GB**
  - source: `05_experiments.tex:440`
  - type: `number`

- **Our encoder reduction -12.9% versus zstd-22 MVT**
  - source: `05_experiments.tex:440`
  - type: `number`

- **MLT decoder achieved 5.73 milliseconds at Zoom 4**
  - source: `05_experiments.tex:464`
  - type: `number`

- **MLT decoder achieved 19.4 milliseconds at Zoom 7**
  - source: `05_experiments.tex:464`
  - type: `number`

- **MLT decoder achieved 4.09 milliseconds at Zoom 13**
  - source: `05_experiments.tex:464`
  - type: `number`

- **MVT+gzip 47.6 milliseconds at Zoom 4**
  - source: `05_experiments.tex:465`
  - type: `number`

- **MVT+gzip 103 milliseconds at Zoom 7**
  - source: `05_experiments.tex:465`
  - type: `number`

- **MVT+gzip 18.7 milliseconds at Zoom 13**
  - source: `05_experiments.tex:465`
  - type: `number`

- **MVT uncompressed 44.2 milliseconds at Zoom 4**
  - source: `05_experiments.tex:466`
  - type: `number`

- **MVT uncompressed 90.6 milliseconds at Zoom 7**
  - source: `05_experiments.tex:466`
  - type: `number`

- **MVT uncompressed 16.5 milliseconds at Zoom 13**
  - source: `05_experiments.tex:466`
  - type: `number`

- **MLT speedup vs gzip at Zoom 4: 8.3x**
  - source: `05_experiments.tex:468`
  - type: `number`

- **MLT speedup vs gzip at Zoom 7: 5.3x**
  - source: `05_experiments.tex:468`
  - type: `number`

- **MLT speedup vs gzip at Zoom 13: 4.6x**
  - source: `05_experiments.tex:468`
  - type: `number`

- **MLT decoder achieved 96-134 MiB/s decode throughput**
  - source: `05_experiments.tex:473`
  - type: `number`

- **MVT+gzip achieved 15-23 MiB/s decode throughput**
  - source: `05_experiments.tex:473`
  - type: `number`

- **Our decoder 4.0-7.7x faster than uncompressed MVT**
  - source: `05_experiments.tex:478`
  - type: `number`

- **28% reduction reported on unshaved Germany tileset**
  - source: `05_experiments.tex:379`
  - type: `number`

- **Germany tileset 3.07 GB \ac{OMT} schema zoom levels 0-14**
  - source: `05_experiments.tex:496`
  - type: `number`

- **Tile-data reductions ranged from 19.8% (Bright) to 46.3% (Toner)**
  - source: `05_experiments.tex:498`
  - type: `number`

- **Median tile-data reduction 29.0%**
  - source: `05_experiments.tex:498`
  - type: `number`

- **11 OMT-compatible styles in benchmark corpus evaluated for tile shaving**
  - source: `05_experiments.tex:496`
  - type: `scope`

- **Rendering-time saving from shaving r is defined per tile**
  - source: `05_experiments.tex:522`
  - type: `qualitative`

- **Rusan et al calculation: tile size / 30 Mbit/s + 25 ms / 2**
  - source: `05_experiments.tex:536`
  - type: `citation`

- **Benchmark values r ≈ 3 milliseconds per tile**
  - source: `05_experiments.tex:536`
  - type: `number`

- **Benchmark values Cf ≈ 25.8 milliseconds**
  - source: `05_experiments.tex:536`
  - type: `number`

- **Benchmark values 50 kilobyte average tile**
  - source: `05_experiments.tex:536`
  - type: `number`

- **Pooled hit rate h(ΛM/N) ≈ 0.9**
  - source: `05_experiments.tex:536`
  - type: `number`

- **Maximum tolerable hit-rate gap r/Cf ≈ 11.6%**
  - source: `05_experiments.tex:536`
  - type: `number`

- **Tippecanoe URL: https://github.com/felt/tippecanoe accessed 2026-04-21**
  - source: `05_experiments.tex:546`
  - type: `url`

- **Planetiler URL: https://github.com/onthegomap/planetiler accessed 2026-04-21**
  - source: `05_experiments.tex:546`
  - type: `url`

## Cross-Style Generalisation

- **Static-only passes median 31.4% raw reduction across 13 unseen styles**
  - source: `05_experiments.tex:554`
  - type: `number`

- **No style regressed in generalization corpus**
  - source: `05_experiments.tex:554`
  - type: `qualitative`

- **Initial style size and complexity correlation r = 0.35, n = 13, p = 0.24**
  - source: `05_experiments.tex:554`
  - type: `number`

- **13 styles from Maputnik generalization corpus**
  - source: `05_experiments.tex:560`
  - type: `scope`

- **10 deep-corpus styles benchmarked end-to-end with tile data**
  - source: `05_experiments.tex:562`
  - type: `scope`

- **11 OMT-compatible styles evaluated at tile-shaving level**
  - source: `05_experiments.tex:562`
  - type: `scope`

- **13 additional styles evaluated with static analysis only**
  - source: `05_experiments.tex:562`
  - type: `scope`

- **Raw reductions ranged from 3.2% (Stadia Outdoors) to 67.7% (LocationIQ Streets)**
  - source: `05_experiments.tex:577`
  - type: `number`

- **No style regressed in cross-style evaluation**
  - source: `05_experiments.tex:577`
  - type: `qualitative`

- **Under gzip compression range narrowed to 3.9-22.4%**
  - source: `05_experiments.tex:578`
  - type: `number`

- **Under gzip compression median 11.4%**
  - source: `05_experiments.tex:578`
  - type: `number`

- **LocationIQ Streets 67.7% raw reduction**
  - source: `05_experiments.tex:579`
  - type: `number`

- **Americana 59.2% raw reduction**
  - source: `05_experiments.tex:579`
  - type: `number`

- **MapTiler Toner 57.5% raw reduction**
  - source: `05_experiments.tex:579`
  - type: `number`

- **Stadia Outdoors 3.2% reduction**
  - source: `05_experiments.tex:580`
  - type: `number`

- **AWS styles both at 10.6% reduction**
  - source: `05_experiments.tex:580`
  - type: `number`

- **Americana 48510 nodes initial complexity**
  - source: `05_experiments.tex:583`
  - type: `number`

- **Correlation r = 0.35, n = 13, p = 0.24 for complexity vs reduction**
  - source: `05_experiments.tex:582`
  - type: `number`

- **Dropping Americana flipped correlation sign to r = -0.54**
  - source: `05_experiments.tex:584`
  - type: `number`

- **Median raw reduction 31.4% across 13 unseen styles**
  - source: `05_experiments.tex:634`
  - type: `number`

- **Range 3.2% to 67.7% across Maputnik styles**
  - source: `05_experiments.tex:634`
  - type: `number`

- **No style regressed**
  - source: `05_experiments.tex:634`
  - type: `qualitative`

- **Weak link between initial complexity and achievable reduction r = 0.35, p = 0.24**
  - source: `05_experiments.tex:634`
  - type: `number`

- **Stats-driven passes added 10-20% additional reduction on top of static passes**
  - source: `05_experiments.tex:649`
  - type: `number`

## Combined Results

- **Three optimization channels composed additively, not synergistically**
  - source: `05_experiments.tex:662`
  - type: `qualitative`

- **Data-level passes did almost nothing for sustained frame rate**
  - source: `05_experiments.tex:663`
  - type: `qualitative`

- **19 cumulative ablation steps**
  - source: `05_experiments.tex:669`
  - type: `scope`

- **Urban tile-dense scenarios showed larger absolute improvements than sparse scenarios**
  - source: `05_experiments.tex:676`
  - type: `qualitative`

- **Expression passes produced diffuse moderate improvement across scenarios**
  - source: `05_experiments.tex:677`
  - type: `qualitative`

- **Structural passes improvement concentrated where dead elimination or layer merging applied**
  - source: `05_experiments.tex:677`
  - type: `qualitative`

- **Sustained frame rates above 2000 FPS exposed small GC-pauses**
  - source: `05_experiments.tex:707`
  - type: `number`

- **Style-parse component shrank monotonically with each expression pass**
  - source: `05_experiments.tex:742`
  - type: `qualitative`

- **First-tile and remaining-load unchanged by style-only steps**
  - source: `05_experiments.tex:742`
  - type: `qualitative`

- **Baseline browser heap 86.0 MB**
  - source: `05_experiments.tex:745`
  - type: `number`

- **Heap at step 15: 82.9 MB**
  - source: `05_experiments.tex:745`
  - type: `number`

- **Style-level passes reduced heap -3.6%**
  - source: `05_experiments.tex:745`
  - type: `number`

- **Tile shaving step 17 dropped heap to 63.7 MB**
  - source: `05_experiments.tex:746`
  - type: `number`

- **Full pipeline reached 55.3 MB at step 19**
  - source: `05_experiments.tex:746`
  - type: `number`

- **Cumulative heap reduction -35.7%**
  - source: `05_experiments.tex:746`
  - type: `number`

- **Style-level passes reduced heap by 3.1 MB**
  - source: `05_experiments.tex:763`
  - type: `number`

- **Marginal contribution table covers 12 styles and 18 scenarios**
  - source: `05_experiments.tex:829`
  - type: `scope`

- **Liberty's 111-layer style completed all passes in 7.5 milliseconds**
  - source: `05_experiments.tex:866`
  - type: `number`

- **Advisory computation 1.1 milliseconds**
  - source: `05_experiments.tex:866`
  - type: `number`

- **Tile-statistics collection 57.4 seconds for 256588 source tiles**
  - source: `05_experiments.tex:867`
  - type: `number`

- **Tile pruning and MVT re-encoding 15.6 seconds with Rayon parallelism**
  - source: `05_experiments.tex:868`
  - type: `number`

- **MLT encoding single-threaded 5 minutes 42 seconds**
  - source: `05_experiments.tex:869`
  - type: `number`

- **MLT encoding with 16 threads 47 seconds**
  - source: `05_experiments.tex:869`
  - type: `number`

- **MLT encoding without competition single-threaded 2 minutes 55 seconds**
  - source: `05_experiments.tex:870`
  - type: `number`

- **Overhead ratio of full competition 1.95x**
  - source: `05_experiments.tex:871`
  - type: `number`

- **Analytical estimate 3-5x overhead**
  - source: `05_experiments.tex:871`
  - type: `number`

- **Germany tileset single-threaded pipeline time under 7 minutes**
  - source: `05_experiments.tex:900`
  - type: `number`

- **Germany tileset 16-thread parallelism approximately 2 minutes**
  - source: `05_experiments.tex:901`
  - type: `number`

- **Expression passes drove largest reductions in AST node count**
  - source: `05_experiments.tex:907`
  - type: `qualitative`

- **Full pipeline cut per-style median load time by 71%**
  - source: `05_experiments.tex:915`
  - type: `number`

- **Full pipeline lifted FPS by 152%**
  - source: `05_experiments.tex:915`
  - type: `number`

- **Full pipeline load time reductions 63-74% per-style**
  - source: `05_experiments.tex:1011`
  - type: `number`

- **Full pipeline per-style median load reduction 71%**
  - source: `05_experiments.tex:1011`
  - type: `number`

- **Full pipeline FPS improvements 100-200%**
  - source: `05_experiments.tex:1011`
  - type: `number`

- **Full pipeline per-style median FPS improvement 152%**
  - source: `05_experiments.tex:1011`
  - type: `number`

- **Pooled Fiord+Liberty aggregate +141.4% FPS**
  - source: `05_experiments.tex:999`
  - type: `number`

- **Static passes median 31.4% raw style reduction across 13 unseen styles**
  - source: `05_experiments.tex:1013`
  - type: `number`

- **Tile shaving 66.1% pooled median load reduction (fiord+liberty)**
  - source: `05_experiments.tex:997`
  - type: `number`

- **MLT encoder 28% tile-volume cut over Java reference**
  - source: `05_experiments.tex:1010`
  - type: `number`

- **MLT encoder 12% reduction over gzip-compressed MVT**
  - source: `05_experiments.tex:1010`
  - type: `number`

## Visual Correctness Validation

- **Pixelmatch evaluation across all 15 benchmark styles at zoom levels 0-14**
  - source: `05_experiments.tex:947`
  - type: `scope`

- **18 scenarios evaluated for visual correctness**
  - source: `05_experiments.tex:947`
  - type: `scope`

- **Pixelmatch allowed tolerance 0.00025**
  - source: `05_experiments.tex:948`
  - type: `number`

- **Pixelmatch threshold 0.1285 YIQ-perceptual**
  - source: `05_experiments.tex:948`
  - type: `number`

- **MapLibre GL JS Node-side software rasteriser used for correctness validation**
  - source: `05_experiments.tex:947`
  - type: `name`

## Threats to Validity

- **Single hardware configuration GPU model CPU memory**
  - source: `05_experiments.tex:955`
  - type: `scope`

- **Specific browser version with ANGLE/Vulkan graphics backend**
  - source: `05_experiments.tex:955`
  - type: `scope`

- **15-run median used to reduce measurement noise**
  - source: `05_experiments.tex:958`
  - type: `number`

- **Evaluation limited to MapLibre GL JS**
  - source: `05_experiments.tex:962`
  - type: `scope`

- **Tile data limited to \ac{OMT} and BasemapDE schemas**
  - source: `05_experiments.tex:964`
  - type: `scope`

- **15 benchmark styles evaluated**
  - source: `05_experiments.tex:966`
  - type: `scope`

- **10 of 15 deep-corpus styles benchmarked end-to-end**
  - source: `05_experiments.tex:969`
  - type: `scope`

- **ICGC Fosc and ICGC Gris excluded due to text-field handling**
  - source: `05_experiments.tex:970`
  - type: `name`

- **BasemapDE pair excluded not OMT-compatible**
  - source: `05_experiments.tex:971`
  - type: `name`

- **Tile statistics at sample rate 1.0**
  - source: `05_experiments.tex:973`
  - type: `number`

- **11 OMT-compatible deep-corpus styles tile-shaving verified**
  - source: `05_experiments.tex:972`
  - type: `scope`

- **Tile-shaving reductions 19.8% to 46.3%**
  - source: `05_experiments.tex:972`
  - type: `number`

- **All 15 styles style-only results cover**
  - source: `05_experiments.tex:974`
  - type: `scope`

- **Fixed bandwidth throttle simulation**
  - source: `05_experiments.tex:977`
  - type: `qualitative`

- **Synthetic camera animations zigzag spiral zoomdrill pansweep bearingspin**
  - source: `05_experiments.tex:978`
  - type: `name`

- **Tile statistics count feature occurrences across tiles**
  - source: `05_experiments.tex:981`
  - type: `qualitative`

- **Selectivity estimation model assumes independence between filter predicates**
  - source: `05_experiments.tex:985`
  - type: `qualitative`

- **Bootstrap 95% confidence intervals 10000 resamples percentile method**
  - source: `05_experiments.tex:989`
  - type: `number`

- **Wilcoxon signed-rank tests confirmed load-time reductions**
  - source: `05_experiments.tex:991`
  - type: `qualitative`

- **Fiord baseline 370.9 ms to 120.5 ms, p < 10^-45, n = 270**
  - source: `05_experiments.tex:991`
  - type: `number`

- **Liberty baseline 466.5 ms to 133.7 ms, p < 10^-74, n = 254**
  - source: `05_experiments.tex:991`
  - type: `number`

- **Fiord 18 scenarios × 15 runs measurement pool**
  - source: `05_experiments.tex:992`
  - type: `scope`

- **Liberty 17 of 18 scenarios full-pipeline pool**
  - source: `05_experiments.tex:993`
  - type: `scope`

- **No multiple-comparisons correction applied**
  - source: `05_experiments.tex:1004`
  - type: `qualitative`
