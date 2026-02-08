#set heading(numbering: "1.1")

#heading(level: 1)[Theoretical background] <ch_theoretical_background>

#lorem(60)

#heading(level: 2)[Map rendering approaches] <sec_map_rendering_approaches>
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



#heading(level: 4, "Dynamic") <access:dynamic>

Store data in a database (for example #link("https://postgis.net/")[PostGIS]). Use a tile server to convert between stored/served data.

- #text(weight: "bold")[Client-driven]: Store encoded tiles as one file in a blob store in a format that includes a header where a tile is (#link("https://protomaps.com/")[PMTiles], #link("https://versatiles.org/")[VersaTiles]). Requires multiple requests with appropriate #link("https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Range")[`Range`]s to know exact tile-location.
- #text(weight: "bold")[Semi-static]: Store encoded tiles on disk in a database (for example SQLite). Use a tile server to reach into the database and serve it to a client.

Dynamic can be synced minutely by applying diffs, while the other approaches need full rebuilding.
At larger scales, caching tiles in-memory via regional, CDN-type infrastructures and falling back to static data is important.

The data, sprites and fonts are then taken by a rendering engine, transformed into a GPU-capable representation and uploaded to the WebGL / WebGPU / Vulkan / ... buffer for rendering according to the style.

While all of these resources can be optimised, due to the continuous streaming nature and (usually) highest data load tiles are the most interesting.
Real world observations support this with the map performance Microsoft Bing Maps being siginficantly different from less optimised maps like #link("https://basemap.de/")[basemap.de/].

#heading(level: 2)[Multi-objective optimisation] <sec_multi_objective_optimisation>

#lorem(60)

#heading(level: 2)[Benchmarking] <sec_benchmarking>

#lorem(60)
