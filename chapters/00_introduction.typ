#heading(level: 1, "Background - Overview of Approaches to Map-Rendering")

As shown in @fig:basic-arch, there are four different aspects to how a map looks:
- #text(weight: "bold")[styles] define how a map looks and where to find the other items
- #text(weight: "bold")[tiles] deliver the geometry (points, lines, polygons) and associated data (for example building heights) that can be seen on maps
- #text(weight: "bold")[sprites] are the icons that can be seen on maps
- #text(weight: "bold")[fonts] are the text shown on the map

#figure(
  image("../figures/basic-architecture.png", width: 90%),
  caption: "Basic building blocks of a map rendering stack. Data is taken from a data source, converted into a simplified format (for example a spatial index) and served to a client. How a client renders this data is defined by a style and supported by fonts and sprites for the text and icons on a map."
) <fig:basic-arch>

There are several approaches to delivering clientside rendered vector maps.
For styles/sprites/fonts this is usually a file-server with little processing involved.

For tiles there are three different major approaches to storing/ accessing them:

- #text(weight: "bold")[Dynamic]: Store data in a database (for example #link("https://postgis.net/")[PostGIS]). Use a tile server to convert between stored/served data <access:dynamic>
- #text(weight: "bold")[Client-driven]: Store encoded tiles as one file in a blob store in a format that includes a header where a tile is (#link("https://protomaps.com/")[PMTiles], #link("https://versatiles.org/")[VersaTiles]). Requires multiple requests with appropriate #link("https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Range")[`Range`]s to know exact tile-location.
- #text(weight: "bold")[Semi-static]: Store encoded tiles on disk in a database (for example SQLite). Use a tile server to reach into the database and serve it to a client.

Dynamic can be synced minutely by applying diffs, while the other approaches need full rebuilding.
At larger scales, caching tiles in-memory via regional, CDN-type infrastructures and falling back to static data is important.

The data, sprites and fonts are then taken by a rendering engine, transformed into a GPU-capable representation and uploaded to the WebGL / WebGPU / Vulkan / ... buffer for rendering according to the style.

While all of these resources can be optimised, due to the continuous streaming nature and (usually) highest data load tiles are the most interesting.
Real world observations support this with the map performance Microsoft Bing Maps being siginficantly different from less optimised maps like #link("https://basemap.de/")[basemap.de/].

#heading(level: 1, "Proposed Work")

In this thesis, I propose to design and implement a #text(weight: "bold")[framework] and underlying benchmarks for #text(weight: "bold")[automatic data/style-driven optimisation of map rendering pipelines].
Currently, such optimisations are largely manual, ad hoc, and often style-specific — leaving significant performance potential untapped.
I hypothesize that a structured, automated approach can achieve nearly the same speed up one can achieve by manual optimisations.

#heading(level: 2, "Key Results / Research Questions")

- #text(weight: "bold")[R1]: This research investigates to what extent automatic data and style co-optimisation is able to reduce map tile size and improve rendering performance.
- #text(weight: "bold")[R2]: It further examines which techniques — such as simplification, query optimisation, query processing, and data management — are most relevant for achieving these improvements.
- #text(weight: "bold")[R3]: Finally, it evaluates how expensive such optimisations are in terms of latency, server- and client-side CPU, memory, and energy consumption.

#heading(level: 2, "Preliminary Structure")

1. Introduction
    1. Related work
    2. Research Goal
    3. Outline
2. Theoretical background
    1. Map rendering approaches
    2. Multi-objective optimisation
3. Methods
    1. System overview
    2. Gathering a representative sample
    3. Building optimisations
    4. Gathered metrics
4. Experiments
    1. Experiment one: Short description
        1. Evaluation details
        2. Results
        3. Discussion
5. Conclusion
6. Outlook
7. Appendix
8. Abbreviations
9. List of figures
10. List of tables
11. Biblography
