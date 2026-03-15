#heading(level: 1, "Methods")

In this thesis, I propose to design and implement a #text(weight: "bold")[framework] and underlying benchmarks for #text(weight: "bold")[automatic data/style-driven optimisation of map rendering pipelines].
Currently, such optimisations are largely manual, ad hoc, and often style-specific — leaving significant performance potential untapped.
I hypothesize that a structured, automated approach can achieve nearly the same speed up one can achieve by manual optimisations.

#heading(level: 2, "Approach")

For building on a performance relevant topic, gathering a solid baseline and benchmarking against it is the planned approach.

The framework should be integrated into one of the highest performance tile servers for evaluation purposes to reduce measurement bias.
According to public benchmarks #footnote[#link("https://github.com/FabianRechsteiner/vector-tiles-benchmark")]: #link("https://maplibre.org/martin")[`Martin`] or #link("https://www.bbox.earth/")[`BBox`].

#heading(level: 3, "Gathering a Representative Sample")

To ensure that the work is representative effective of optimisations on real-world data a corpus of publicly available styles is gathered.
Sampling a good variety of tiles should enable comparing most optimisations.
Some, like constant folding, require a full table scan, though.
Since OpenStreetMap (OSM) is the most widely used source for vector tile generation, its data will serve as the baseline for most experiments requring table scan data access.
Given the recent deployment of publicly available minutely updating vector tiles, this seems realistic.

If the optimisations provide tangible benefit, I suspect that it should be doable to get in touch with data providers in the later stages, once the implementation is solid and evaluated under real world conditions.

For some of the optimisations - such as the proposed operator rewriting - building out a benchmark will be sensible.

#heading(level: 3, "Building Optimisations")

A few of the optimisations that I envision can be applied to all, others only to some data sources mentioned in @sec_map_rendering_approaches.
When optimising performance, a holistic approach is assumed to be nessesary.
Thus, we will look into the different componets that make up a map: data, resources, styles and metadata-glue.
Specifically, during this research, we will be looking into
- Making the data simpler, more effecitve, or otherwise serving friendly (see @tab:optimisations-serving). We assume that networkign speed and clients CPU is finite, thus using this less would be benefitial.
- Investigating the effect of supporting resources (see @tab:optimisations-resources). We assume that the supprting resources (fonts, sprites) are not zero-cost for clients.
- Making the style simpler to render (see @tab:optimisations-styles). We assume that some style optimisations are more expensive than others. By reducing expensive operations, better performance should be possible.
- Providing better metadata to clients (see @tab:optimisations-metadata). We assume that clients can skip work if the metadata is more accurate.

Most of the optimisations are similar to how databases optimize queries or compilers code.
During evaluation / implementation this list will change as new opportunities become apparent or are found to be ineffective in practice.

These optimisations can be split by topic, but also by data requirement:
- #text(style: "italic")[full scan] means that this optimisation would require executing one operation over the whole table at minimum.
- #text(style: "italic")[sampling] means that this data can be gathered by sampling approaches, but evaluating if a full scan could add context will have to be looked at.
  For sampling based approaches, the resampling frequency for the dynamic sources noted in @sec_map_rendering_approaches needs to be determined via statistical approaches.
- #text(style: "italic")[-] is the case where no scan is necessary.
  This does not mean that it might not still be beneficial, for example for parameter tuning.

#heading(level: 2, "Evaluation")

Many of the optimisations are novel, meaning there is no literature on their effectiveness.

The following might aspects of the suspected multi-objective optimisation
- #text(weight: "bold")[Data savings]: Reduction in data transferred
- #text(weight: "bold")[Rendering performance]: Load time and frame rate on client devices
- #text(weight: "bold")[Optimisation cost]: Preprocessing time and complexity
- #text(weight: "bold")[Energy consumption]: On the client, server, and the network

Benchmarks comparing the different goals on real-world data and environments (native vs web and mobile vs desktop) are necessary.
The baseline will always be the unaltered version and the comparison is a matrix / combination of optimisation passes.