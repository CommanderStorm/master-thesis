<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from "vue";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

interface Loc {
  name: string;
  center: [number, number];
  regime: string;
}
const locations: Loc[] = [
  { name: "New York", center: [-73.985, 40.748], regime: "urban US" },
  { name: "Amazon", center: [-60.025, -3.119], regime: "rainforest" },
  { name: "Sahara", center: [2.0, 24.0], regime: "sparse desert" },
  { name: "Paris", center: [2.349, 48.864], regime: "urban EU" },
  { name: "Black Forest", center: [8.2, 48.0], regime: "rural / forest" },
  { name: "Swiss Alps", center: [8.232, 46.818], regime: "alpine terrain" },
  { name: "Munich", center: [11.576, 48.137], regime: "urban EU" },
  { name: "Venice", center: [12.338, 45.434], regime: "island / water" },
  { name: "Rome", center: [12.496, 41.903], regime: "urban EU" },
  { name: "Berlin", center: [13.405, 52.52], regime: "urban EU" },
  { name: "Stockholm Archipelago", center: [18.52, 59.4], regime: "island / water" },
  { name: "Cairo", center: [31.236, 30.044], regime: "urban Africa" },
  { name: "Beijing", center: [116.397, 39.909], regime: "urban Asia" },
  { name: "Seoul", center: [126.978, 37.566], regime: "urban Asia" },
  { name: "Tokyo", center: [139.692, 35.69], regime: "urban Asia" },
];

const el = ref<HTMLDivElement>();
const current = ref(locations[0]);
const failed = ref(false);
let map: maplibregl.Map | undefined;
let cancelled = false;

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

// Great-circle distance in degrees of arc between two [lng, lat] points.
function arcDistance(a: [number, number], b: [number, number]): number {
  const toRad = Math.PI / 180;
  const lat1 = a[1] * toRad, lat2 = b[1] * toRad;
  const dLat = (b[1] - a[1]) * toRad, dLng = (b[0] - a[0]) * toRad;
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLng / 2) ** 2;
  return (2 * Math.atan2(Math.sqrt(h), Math.sqrt(1 - h)) * 180) / Math.PI;
}

// Closer the previous stop, the more we zoom in so the short hop is still visible;
// long hops stay pulled back so the whole jump fits and reads as extent.
function zoomForHop(deg: number): number {
  if (deg < 6) return 4.3;
  if (deg < 15) return 3.8;
  if (deg < 35) return 3.2;
  return 2.6;
}

async function runForever() {
  let i = 0;
  while (!cancelled && map) {
    const loc = locations[i % locations.length];
    const prev = locations[(i + locations.length - 1) % locations.length];
    current.value = loc;
    map.flyTo({ center: loc.center, zoom: zoomForHop(arcDistance(prev.center, loc.center)), duration: 4500, essential: true } as any);
    await sleep(6000);
    i++;
    if (i % locations.length === 0) {
      map.flyTo({ center: [15, 25], zoom: 1.4, duration: 4500, essential: true } as any);
      await sleep(6000);
    }
  }
}

onMounted(() => {
  try {
    map = new maplibregl.Map({
      container: el.value!,
      style: "/demo/style.json",
      transformRequest: (url) => (url.startsWith("/demo/") ? { url: location.origin + url } : { url }),
      center: [15, 25],
      zoom: 1.4,
      attributionControl: false,
      interactive: false,
    });
    map.on("style.load", () => {
      map!.setProjection({ type: "globe" });
    });
    map.on("load", () => {
      for (const loc of locations) {
        const dot = document.createElement("div");
        dot.className = "bench-marker";
        new maplibregl.Marker({ element: dot }).setLngLat(loc.center).addTo(map!);
      }
      runForever();
    });
  } catch (e) {
    console.warn("BenchExtent: map init failed, showing fallback", e);
    failed.value = true;
  }
});

onBeforeUnmount(() => {
  cancelled = true;
  map?.remove();
});
</script>

<template>
  <div class="extent-wrap">
    <div v-show="!failed" ref="el" class="extent" />
    <div v-show="!failed" class="caption">
      <span class="name">{{ current.name }}</span>
      <span class="desc">{{ current.regime }}</span>
    </div>
  </div>
</template>

<style scoped>
.extent-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: hidden;
}
.extent {
  width: 100%;
  height: 100%;
}
.caption {
  position: absolute;
  left: 10px;
  bottom: 10px;
  margin-right: 10px;
  display: flex;
  align-items: baseline;
  gap: 8px;
  background: rgba(17, 23, 37, 0.78);
  color: #fff;
  padding: 5px 10px;
  border-radius: 6px;
}
.name {
  font-size: 0.95rem;
  font-weight: 700;
  color: #95befa;
}
.desc {
  font-size: 0.72rem;
  opacity: 0.8;
}
:global(.bench-marker) {
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: #95befa;
  border: 2px solid #111725;
  box-shadow: 0 0 0 2px rgba(149, 190, 250, 0.5);
}
</style>
