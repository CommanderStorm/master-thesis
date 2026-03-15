#set heading(numbering: "1.1")

#heading(level: 1)[Theoretical background] <ch_theoretical_background>

Discussing Performance improvements for slippy web maps requires understanding of the underlying architecture and technologies involved in rendering maps. 
First the Map Rendering Process will be discussed in @sec_map_rendering_approaches, then Multi objective optimization approaches will be discussed in @sec_multi_objective_optimisation and finally benchmarking approaches will be discussed in @sec_benchmarking.

#heading(level: 2)[Map rendering approaches] <sec_map_rendering_approaches>

When building a slippy map (i.e. a map with the modern pan, zoom, rotation, and interaction capabilities), the technology stack is fairly simple.

A user interacts with an input device (mouse, touch, keyboard) to control the map view.
The Map view is rendered using one of the following approaches:

- #text(weight: "bold")[SVG] is a vector graphics format that can be used to render maps as shown by the @IDEditor or @Leaflet.
  Using SVGs means one is limited to a 2D rendering approach due to not having a camera.
- #text(weight: "bold")[low level 3D Graphics APIs] like WebGL, WebGPU, OpenGL, Metal, Vulkan, DirectX, etc. for rendering 3D graphics as shown by @mapbox, @maplibre, @deck.gl, @here.
  This allows a more complex 3D based rendering with pitch, yaw and roll.
  Due to having better hardware access, these APIs can render more complex scenes with better performance.

Due to the need for low-level access, this research focuses exclusively on renderers based on open-source 3D graphics APIs. While these renderers are powerful, they require data to be preprocessed and optimized specifically for rendering. As a result, they cannot directly render high-level primitives such as shapes (polygons, lines, points), text, or images. Instead, they operate on lower-level graphics primitives such as textures, triangles, and quads.

These low-level graphics building blocks are linked to map data through sprites, fonts, and styles, which are then interpreted by a rendering engine.

As a lower-level representation layer for displaying map content, the following components are required, as shown in @fig:basic-arch:
- styles define the visual appearance of the map and reference the other required resources,
- tiles provide the geometry (points, lines, polygons) and associated attributes (for example, building heights) displayed on the map,
- sprites supply the icons shown on the map,
- fonts provide the glyphs used to render text labels.

#figure(
  image("../figures/basic-architecture.png", width: 90%),
  caption: "Basic building blocks of a map rendering stack. Data is taken from a data source, converted into a simplified format (for example a spatial index), and served to a client. The visual appearance is defined by a style and supported by fonts and sprites for text and icons."
) <fig:basic-arch>

There are several approaches to delivering client-side rendered vector maps.

Styles, sprites, and fonts are typically served from a file server or CDN and require little processing. In some cases, parts of these resources may be generated dynamically—for example, to support complex text shaping for Arabic, Hebrew, Indic, or Japanese scripts as described by @wilphli—but this processing is usually handled server-side.

Tiles, by contrast, can be stored and accessed using three major approaches:

- #text(weight: "bold")[Dynamic]: Store geospatial data in a database (for example, PostGIS) and use a tile server to generate and serve tiles on demand.
- #text(weight: "bold")[Client-driven]: Store encoded tiles as a single file in a blob store using a format that includes an internal tile index (for example, PMTiles or VersaTiles). Clients retrieve tiles using multiple HTTP requests with appropriate Range headers to locate the required data.
- #text(weight: "bold")[Semi-static]: Store encoded tiles in a database file on disk (for example, SQLite) and use a tile server to extract and serve tiles to clients.

Dynamic data sources can be updated frequently by applying incremental diffs, whereas the other approaches typically require a full rebuild when the underlying data changes. At larger scales, in-memory caching of tiles via regional or CDN-style infrastructure—combined with fallback to static data—is essential for performance.

Although all of these resources can be optimized, tiles are usually the most critical due to their continuous streaming nature and typically higher data volume.
Real-world observations support this: the performance of highly optimized systems such as Microsoft Bing Maps differs significantly from less optimized deployments, such as basemap.de.

Let's dive deeper into the specifics of each of the resources used to gain a better understanding of their performance characteristics and optimization strategies:

#heading(level: 3)[Fonts]

Fonts can be client rendered from a font file.
This requires shipping a font renderer to the client, as neither native nor web targets have for example @Harfbuzz as a feature.
This also means that for some fonts up to 30MB of Font data needs to be transfered.

For interactive usecases, this is prohibitive as the time to download this would be longer than acceptable.
Some fonts need this shaping, as they connect neatly, but latin fonts don't.
For these fonts, there is a clear 1:1 relationship between the Unicode Code point and a Rendered Character.

This is why a simpler way exists:
Cutting fonts up into Unicode slices (`start..end`) and serving only the ranges that are needed to the client.
This cutting of fonts has the implicit advantange of pruning the space of possible font data to just the data that is needed to render the map.

Common open source rednerers like @maplibre or source avaliable renders like @mapbox do this by shipping #todo how is the pbf format?

#heading(level: 3)[Sprites]

Sprites in comuter graphics are a fairly solved problem.
To avoid having to reques thousands of very small files or to have to render SVGs on a client, this work is shifted to the server and the server delivers spritesheets.


Common open source rednerers like @maplibre or source avaliable renders like @mapbox do this by shipping
- plain-Png or SDF-Png spritesheets, in combination with
- a lookup table of where on the spritesheet each sprite is located and if there are regions of the sprite that can be streched to account for placing text inside the sprite

#heading(level: 3)[Tiles]



#heading(level: 3)[Styles]

#heading(level: 2)[Multi-objective optimisation] <sec_multi_objective_optimisation>

#lorem(60)

#heading(level: 2)[Benchmarking] <sec_benchmarking>

#lorem(60)
