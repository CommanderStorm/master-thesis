## Tile Data Optimization

- **Mapbox developed vtshaver, a C++/Node.js tool**
  - source: `02_related_work.tex:20`
  - type: `name`

- **vtshaver access date 2025-10-20**
  - source: `02_related_work.tex:20`
  - type: `url`

- **https://github.com/mapbox/vtshaver**
  - source: `02_related_work.tex:20`
  - type: `url`

- **Mapbox style-optimized vector tiles is a proprietary server-side feature**
  - source: `02_related_work.tex:25`
  - type: `citation`

- **Style-optimized vector tiles is cited as reference**
  - source: `02_related_work.tex:25`
  - type: `citation`

- **Reverse engineering prohibited by MapBox terms of service**
  - source: `02_related_work.tex:29`
  - type: `url`

- **https://media.ccc.de/v/36c3-11089-reflections_on_the_new_reverse_engineering_law access date 2026-05-21**
  - source: `02_related_work.tex:29`
  - type: `url`

- **Vilardaga built vt-optimizer**
  - source: `02_related_work.tex:31`
  - type: `name`

- **vt-optimizer access date 2025-10-20**
  - source: `02_related_work.tex:31`
  - type: `url`

- **https://github.com/ibesora/vt-optimizer**
  - source: `02_related_work.tex:31`
  - type: `url`

- **Mapbox recommended tile size limits 50 kB average, 500 kB maximum**
  - source: `02_related_work.tex:32`
  - type: `number`

- **https://docs.mapbox.com/mapbox-tiling-service/guides/frequentlyaskedquestions/ access date 2026-05-23**
  - source: `02_related_work.tex:32`
  - type: `url`

- **Tippecanoe access date 2026-04-21**
  - source: `02_related_work.tex:36`
  - type: `url`

- **https://github.com/felt/tippecanoe**
  - source: `02_related_work.tex:36`
  - type: `url`

- **Tippecanoe is standard open-source tool for building vector tilesets from GeoJSON or FlatGeobuf collections**
  - source: `02_related_work.tex:36`
  - type: `qualitative`

- **FlatGeobuf access date 2026-05-11**
  - source: `02_related_work.tex:36`
  - type: `url`

- **http://flatgeobuf.org/**
  - source: `02_related_work.tex:36`
  - type: `url`

- **Tippecanoe feature dropping based on density budgets (--drop-densest-as-needed)**
  - source: `02_related_work.tex:37`
  - type: `name`

- **Visvalingam line simplification**
  - source: `02_related_work.tex:37`
  - type: `citation`

- **Douglas-Peucker algorithm**
  - source: `02_related_work.tex:38`
  - type: `name`

- **Douglas-Peucker cited**
  - source: `02_related_work.tex:38`
  - type: `citation`

- **Visvalingam-Whyatt algorithm**
  - source: `02_related_work.tex:38`
  - type: `name`

- **Visvalingam-Whyatt cited**
  - source: `02_related_work.tex:38`
  - type: `citation`

- **model generalization cited**
  - source: `02_related_work.tex:44`
  - type: `citation`

- **\ac{OMT} schema**
  - source: `02_related_work.tex:49`
  - type: `name`

- **\ac{OMT} schema cited**
  - source: `02_related_work.tex:49`
  - type: `citation`

- **Wallner et al. describe PostGIS-based pipeline for dynamic vector tile creation**
  - source: `02_related_work.tex:50`
  - type: `citation`

- **Planetiler access date 2026-04-21**
  - source: `02_related_work.tex:51`
  - type: `url`

- **https://github.com/onthegomap/planetiler**
  - source: `02_related_work.tex:51`
  - type: `url`

- **Tilemaker access date 2026-04-21**
  - source: `02_related_work.tex:51`
  - type: `url`

- **https://tilemaker.org/**
  - source: `02_related_work.tex:51`
  - type: `url`

- **Protomaps basemap access date 2026-04-21**
  - source: `02_related_work.tex:51`
  - type: `url`

- **https://protomaps.com**
  - source: `02_related_work.tex:51`
  - type: `url`

- **Starburst system established rule-based query rewriting**
  - source: `02_related_work.tex:56`
  - type: `citation`

- **Pirahesh et al.'s Starburst system cited**
  - source: `02_related_work.tex:56`
  - type: `citation`

- **Projection and predicate pushdown cited**
  - source: `02_related_work.tex:56`
  - type: `citation`

- **Spark SQL cited**
  - source: `02_related_work.tex:56`
  - type: `citation`

- **Parquet nested representation originates in Dremel's record shredding and assembly**
  - source: `02_related_work.tex:57`
  - type: `citation`

- **Abadi et al. characterised early versus late materialisation trade-off**
  - source: `02_related_work.tex:57`
  - type: `citation`

## Tile Encoding and Format Innovation

- **MVT uses Protocol Buffers**
  - source: `02_related_work.tex:62`
  - type: `name`

- **MVT wire format specification access date 2026-04-21**
  - source: `02_related_work.tex:62`
  - type: `url`

- **https://github.com/mapbox/vector-tile-spec/tree/master/2.1**
  - source: `02_related_work.tex:62`
  - type: `url`

- **Protocol Buffers access date 2026-04-21**
  - source: `02_related_work.tex:62`
  - type: `url`

- **https://protobuf.dev/**
  - source: `02_related_work.tex:62`
  - type: `url`

- **MVT adopted as conformance class in OGC API-Tiles standard**
  - source: `02_related_work.tex:63`
  - type: `citation`

- **Tremmel & Zink introduced MapLibre Tile (MLT) format**
  - source: `02_related_work.tex:66`
  - type: `name`

- **MapLibre Tile (MLT) achieves up to 3× tile size reduction on encoded tilesets**
  - source: `02_related_work.tex:66`
  - type: `number`

- **MapLibre Tile (MLT) achieves up to 6× on certain large tiles relative to MVT**
  - source: `02_related_work.tex:66`
  - type: `number`

- **MLT uses FSST compression**
  - source: `02_related_work.tex:67`
  - type: `citation`

- **Tremmel proposed COMTiles, cloud-optimized tile archive format**
  - source: `02_related_work.tex:68`
  - type: `name`

- **Lemire and Boytsov introduced SIMD-vectorised integer compression FastPFOR**
  - source: `02_related_work.tex:75`
  - type: `citation`

- **FastPFOR achieves billions of integers per second in decompression throughput**
  - source: `02_related_work.tex:75`
  - type: `number`

- **Boncz et al. developed FSST string compression scheme**
  - source: `02_related_work.tex:76`
  - type: `citation`

- **Kuschewski et al. demonstrated with BtrBlocks that cascading multiple encoding schemes achieves 2.2× faster scans than Parquet**
  - source: `02_related_work.tex:77`
  - type: `number`

- **Abadi et al. introduced decision rules for choosing among RLE, dictionary, and bit-packing in C-Store system**
  - source: `02_related_work.tex:81`
  - type: `citation`

- **Damme et al. evaluated dozens of lightweight integer encodings**
  - source: `02_related_work.tex:82`
  - type: `citation`

- **Boissier formulated encoding selection as budget-constrained optimization problem**
  - source: `02_related_work.tex:83`
  - type: `citation`

- **Zeng et al. empirically evaluated Parquet and ORC internals**
  - source: `02_related_work.tex:84`
  - type: `citation`

- **Tile granularity 10-100 kB**
  - source: `02_related_work.tex:86`
  - type: `number`

- **SageDB vision cited**
  - source: `02_related_work.tex:88`
  - type: `citation`

- **Kraska cited for instance-optimized system design**
  - source: `02_related_work.tex:88`
  - type: `citation`

- **SageDB vision cited again**
  - source: `02_related_work.tex:90`
  - type: `citation`

- **Ding et al. showed instance-optimized data layouts reduce blocks accessed by 93% on cloud analytics workloads**
  - source: `02_related_work.tex:90`
  - type: `number`

- **BtrBlocks reduces blocks by column-block level by 93%**
  - source: `02_related_work.tex:90`
  - type: `citation`

- **Fehér et al.'s adaptive compression family selects encodings at runtime**
  - source: `02_related_work.tex:91`
  - type: `citation`

- **Cen et al.'s LEA learned encoding advisor achieves 19% lower latency and 26% less space than heuristic selection on TPC-H**
  - source: `02_related_work.tex:91`
  - type: `number`

- **Gaffuri presented one of earliest academic treatments of vector tile architecture**
  - source: `02_related_work.tex:94`
  - type: `citation`

- **GeoParquet uses per-page encoding competition (dictionary, RLE, delta, bit-packing)**
  - source: `02_related_work.tex:98`
  - type: `qualitative`

- **Parquet per-column-chunk metadata amortised over large row groups**
  - source: `02_related_work.tex:100`
  - type: `qualitative`

- **Tile sizes 10-100 kB**
  - source: `02_related_work.tex:100`
  - type: `number`

## Style Optimization

- **MapLibre style specification utilities gl-style-validate and gl-style-migrate**
  - source: `02_related_work.tex:109`
  - type: `name`

- **MapLibre style specification access date 2025-10-24**
  - source: `02_related_work.tex:109`
  - type: `url`

- **https://www.maplibre.org/maplibre-style-spec/**
  - source: `02_related_work.tex:109`
  - type: `url`

- **Stamen Design published mapbox-gl-style-remove-defaults**
  - source: `02_related_work.tex:118`
  - type: `name`

- **mapbox-gl-style-remove-defaults access date 2026-5-27**
  - source: `02_related_work.tex:118`
  - type: `url`

- **https://github.com/stamen/mapbox-gl-style-remove-defaults**
  - source: `02_related_work.tex:118`
  - type: `url`

- **Hague et al. formalise CSS rule merging as Max-SAT problem**
  - source: `02_related_work.tex:123`
  - type: `citation`

- **SatCSS tool beats six production CSS minifiers on real benchmarks**
  - source: `02_related_work.tex:123`
  - type: `qualitative`

- **Pirahesh et al. established rule-based query rewriting as distinct optimization phase in Starburst system**
  - source: `02_related_work.tex:127`
  - type: `citation`

- **Equality saturation cited**
  - source: `02_related_work.tex:128`
  - type: `citation`

- **Egg cited for equality saturation**
  - source: `02_related_work.tex:128`
  - type: `citation`

## Rendering Performance Benchmarking

- **Netek et al. compared vector and raster tile performance across eight scenarios**
  - source: `02_related_work.tex:135`
  - type: `number`

- **Balla and Gede benchmarked GeoJSON rendering performance across Leaflet, OpenLayers, MapLibre GL JS, and Mapbox GL JS**
  - source: `02_related_work.tex:138`
  - type: `scope`

- **Below 10,000 features, SVG-based renderers (Leaflet, OpenLayers) are faster**
  - source: `02_related_work.tex:139`
  - type: `qualitative`

- **Above 50,000 features, WebGL-based renderers (Mapbox GL JS, MapLibre GL JS) dominate due to GPU acceleration**
  - source: `02_related_work.tex:140`
  - type: `qualitative`

- **Rechsteiner compared open-source vector tile server implementations**
  - source: `02_related_work.tex:143`
  - type: `citation`

- **Georges et al. and Hoefler and Belli established methodological foundations for statistically rigorous performance evaluation**
  - source: `02_related_work.tex:147`
  - type: `citation`

- **Bootstrap confidence intervals, warm-up handling, and metric separation used in benchmarking**
  - source: `02_related_work.tex:148`
  - type: `scope`

## Positioning

- **Mapbox's closed-source style-optimized tiles service is only precedent that couples style and data**
  - source: `02_related_work.tex:157`
  - type: `qualitative`

- **Mapbox terms of service explicitly preclude independent evaluation**
  - source: `02_related_work.tex:157`
  - type: `qualitative`

- **Tremmel and Zink's MLT format advances encoding layer but picks strategies without consulting style**
  - source: `02_related_work.tex:160`
  - type: `qualitative`
