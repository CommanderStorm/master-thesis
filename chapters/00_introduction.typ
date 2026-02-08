#heading(level: 1, "Introduction")

#heading(level: 2, "Related Work")

The research in this area has been fairly specific in the different subcategories, but has not been put together into a cohesive big picture framework.

#heading(level: 2, "Data Level Optimisations")

#heading(level: 2, "Style Level Optimisations")

- #link("https://github.com/mapbox/vtshaver/")[Mapbox] built #raw("vtshaver") #footnote[#link("https://github.com/mapbox/vtshaver/")], a tool to shave tiles.
  It looks at the style and performs optimisations to tile size and tile decoding speed.
  It does not look at the data to optimize the style.
- #link("https://github.com/ibesora/vt-optimizer")[Isaac Vilardaga] built #raw("vt-optimizer") #footnote[#link("https://github.com/ibesora/vt-optimizer")], a tool to optimise styles based on the data.
  The optimisation implemented is dropping invisible/unused layers/fields both in the style and data.
  It does not go as deep into this direction as #raw("vtshaver"), and does not use the data to optimize the style.
- Tremmel et al. #footnote[Preprint at #link("https://www.arxiv.org/pdf/2508.10791")] reduces tile size by wire format innovation.
  They discovered that there is 2-6x tile size reduction possible, mainly using more modern ideas (like row vs. column, server-side tessellation, ....).
  They propose that on the fly reencoding might be possible.
  Their work does not consider styles which leaves avenues for performance improvements.
- #link("https://github.com/FabianRechsteiner/vector-tiles-benchmark")[Universität Salzburg] recently published a benchmark comparing different server implementations.
  Since the systems considered offer different features, the evaluation partly compares incomparable aspects.
  It does not go into the optimisation aspects.
- #link("https://github.com/bdon/OSMExpress/")[OSMExpress] is fairly efficient queries of OSM data, including the application of minutely diffs.
  Much of the existing optimisation work is motivated by the scale of OSM data, whose continuous growth and high update frequency place significant demands on analytical systems.
  The underlying architecture being postgres based limits its applicability.
  OSMExpress can also only answer raw spatial queries and does therefore not touch maps.

As shown, existing tools optimise either data or style, but not both.
Furthermore, the existing tools only apply a subset of optimisations or focus on compression rather than data/style-based filtering or style rewriting.
They do not evaluate multi-objective tradeoffs suchs as latency vs. energy consumption.
This thesis will fill this gap.

#figure(
  table(
    columns: (1fr, 1fr, 3fr), // Approximation for p{3cm}|p{2cm}|p{11cm} - will adjust if needed
    align: (start, start, start),
    [*optimisation*], [*data*], [*description [technique]*],
    table.hline(),
    [transparent reencoding], [-], [reencode tiles into a different tile specification on the fly [storage format]],
    [compression optimisation], [-], [compress tiles more aggressively or with a different compression algorithm [no exact match]],
    [data layout optimisation], [-], [for dynamic databases, reorganise tile data for access pattern [storage layout]],
    [overlap reduction], [-], [for some layers like roads or pois at the higher zoom levels overlap is common. If one knows the style redundant data can be removed [storage layout]],
    [static generation], [-], [(only some styles) extract semantics and generate a new, optimal #link("https://github.com/onthegomap/planetiler/tree/main/planetiler-custommap")[static instruction set for constructing the tile database]],
    [tile shaving], [-], [only encodes the exact data that a style would actually look at [no exact match]],
  ),
  caption: "Overview of data-serving level optimisation techniques targeting improved tile storage, retrieval, and transmission efficiency."
) <tab:optimisations-serving>

#figure(
  table(
    columns: (1fr, 1fr, 3fr), // Approximation for p{3cm}|p{2cm}|p{11cm}
    align: (start, start, start),
    [*optimisation*], [*data*], [*description [technique]*],
    table.hline(),
    [prewarming caches], [-], [make sure that sprites and fonts are in an in-memory cache [prefetching]],
    [minimum sprite-set mining], "- / full scan", [some styles may permit to statically know which sprites will be used. For others, one might need to do a full table scan to gather this statistic. [no exact match]],
    [server side layouting], "- / full scan", [Layouting of labels and sprites is a performance intensive task for clients. Pulling this work to the server side might have advantages [no exact match]],
  ),
  caption: "Overview of optimisation strategies for supporting resources such as sprites and fonts, focusing on reducing client-side load and improving rendering responsiveness."
) <tab:optimisations-resources>

#figure(
  table(
    columns: (1fr, 1fr, 3fr), // Approximation for p{3cm}|p{2cm}|p{11em}
    align: (start, start, start),
    [*optimisation*], [*data*], [*description [technique]*],
    table.hline(),
    [filter reordering], [sampling], [optimize style filter order (like #raw("any"), #raw("all"), #raw("match"), #raw("case")) [selectivity analysis]],
    [expression order optimisation], [sampling], [optimise the order of reorderable-expressions (like #raw("match")) [selectivity analysis]],
    [expression kind optimisation], [-], [rewrite expensive operators with more performant forms [operator selection]],
    [constant folding], [full scan], [replace constant style expressions or predicates with literal values [constant folding]],
  ),
  caption: "Overview of style-level optimisation techniques designed to reduce rendering complexity through expression rewriting, filter reordering, and related strategies."
) <tab:optimisations-styles>

#figure(
  table(
    columns: (1fr, 1fr, 3fr), // Approximation for p{3cm}|p{2cm}|p{11em}
    align: (start, start, start),
    [*optimisation*], [*data*], [*description [technique]*],
    table.hline(),
    [dead source elimination], [-], [remove impossible or hidden data-sources or style-layers [dead code elimination]],
    [metadata refinement], [full scan], [more accurate #raw("{min,max}_zoom") metadata based on the data, filters, and impossible styling conditions (think: #raw("opacity=0") after zooming out) [no exact match]],
  ),
  caption: "Overview of metadata-level optimisation techniques aimed at improving client-side rendering performance through more accurate and efficient metadata representation"
) <tab:optimisations-metadata>

#heading(level: 2, "Research Goal")
- #text(weight: "bold")[R1]: This research investigates to what extent automatic data and style co-optimisation is able to reduce map tile size and improve rendering performance.
- #text(weight: "bold")[R2]: It further examines which techniques — such as simplification, query optimisation, query processing, and data management — are most relevant for achieving these improvements.
- #text(weight: "bold")[R3]: Finally, it evaluates how expensive such optimisations are in terms of latency, server- and client-side CPU, memory, and energy consumption.

#heading(level: 2, "Outline")
// Briefly describe the structure of the thesis here.
