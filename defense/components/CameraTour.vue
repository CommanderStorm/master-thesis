<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from "vue";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

// Auto-cycling camera tour illustrating the five benchmark camera paths
interface Keyframe {
  center?: [number, number];
  zoom?: number;
  bearing?: number;
  pitch?: number;
  duration: number;
}
const D = 1600;

// Munich
const base: [number, number] = [11.576, 48.137];

const animations: { name: string; desc: string; frames: Keyframe[] }[] = [
  {
    name: "zigzag",
    desc: "alternating zoom along a bearing",
    frames: Array.from({ length: 8 }, (_, i) => ({
      center: [base[0] + (i + 1) * 1.5, base[1] + (i % 2 ? -1.5 : 1.5)],
      zoom: i % 2 ? 4 : 2.5,
      bearing: i * 15,
      pitch: 0,
      duration: D,
    })),
  },
  {
    name: "spiral",
    desc: "orbit a location, camera always pointing at it",
    frames: Array.from({ length: 12 }, (_, i) => {
      const a = (i / 12) * 2 * Math.PI,
        r = 4;
      const lng = base[0] + r * Math.cos(a),
        lat = base[1] + r * Math.sin(a);
      const bearing = ((Math.atan2(base[0] - lng, base[1] - lat) * 180) / Math.PI + 360) % 360;
      return { center: [lng, lat], zoom: 3.2, bearing, pitch: 45, duration: D };
    }),
  },
  {
    name: "zoomdrill",
    desc: "zoom in then out, stationary",
    frames: [1, 2, 3, 4, 3, 2, 1].map((z) => ({ center: base, zoom: z, bearing: 0, pitch: 0, duration: D })),
  },
  {
    name: "pansweep",
    desc: "sweep across a region at constant zoom",
    frames: Array.from({ length: 6 }, (_, i) => ({
      center: [base[0] + (i - 3) * 4, base[1] + (i % 2 ? -1.5 : 1.5)],
      zoom: 3.2,
      bearing: 0,
      pitch: 0,
      duration: D,
    })),
  },
  {
    name: "bearingspin",
    desc: "stationary, full bearing sweep at high pitch",
    frames: Array.from({ length: 8 }, (_, i) => ({ center: base, zoom: 3.2, bearing: (i / 8) * 360, pitch: 60, duration: D })),
  },
];

const el = ref<HTMLDivElement>();
const current = ref(animations[0]);
const failed = ref(false);
let map: maplibregl.Map | undefined;
let cancelled = false;

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

async function runForever() {
  let ai = 0;
  while (!cancelled && map) {
    const anim = animations[ai % animations.length];
    current.value = anim;
    map.jumpTo({ ...anim.frames[0], duration: 0 } as any);
    for (const f of anim.frames) {
      if (cancelled) return;
      map.easeTo({ ...f, essential: true } as any);
      await sleep(f.duration + 120);
    }
    await sleep(500);
    ai++;
  }
}

onMounted(() => {
  try {
    map = new maplibregl.Map({
      container: el.value!,
      style: "/demo/style.json",
      transformRequest: (url) => (url.startsWith("/demo/") ? { url: location.origin + url } : { url }),
      center: base,
      zoom: 3.2,
      attributionControl: false,
      interactive: false,
    });
    map.on("load", () => {
      runForever();
    });
  } catch (e) {
    console.warn("CameraTour: map init failed, showing fallback", e);
    failed.value = true;
  }
});

onBeforeUnmount(() => {
  cancelled = true;
  map?.remove();
});
</script>

<template>
  <div class="tour-wrap">
    <div v-show="!failed" ref="el" class="tour" />
    <div v-show="!failed" class="caption">
      <span class="name">{{ current.name }}</span>
      <span class="desc">{{ current.desc }}</span>
    </div>
  </div>
</template>

<style scoped>
.tour-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: hidden;
}
.tour {
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
</style>
