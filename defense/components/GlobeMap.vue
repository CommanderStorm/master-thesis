<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from "vue";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

const props = withDefaults(defineProps<{ height?: string; spin?: boolean; zoom?: number }>(), {
  height: "70vh",
  spin: true,
  zoom: 2.4,
});

const el = ref<HTMLDivElement>();
const failed = ref(false);
let map: maplibregl.Map | undefined;
let raf = 0;

// Fold Slidev's slide-scale transform into the pixel ratio so the WebGL buffer
// matches real screen pixels (otherwise it's rendered small, then stretched).
const effectivePixelRatio = () => {
  const layoutWidth = el.value?.clientWidth || 1;
  const renderedWidth = el.value?.getBoundingClientRect().width || layoutWidth;
  const slideScale = renderedWidth / layoutWidth;
  return Math.min((window.devicePixelRatio || 1) * slideScale, 4);
};

onMounted(() => {
  try {
    map = new maplibregl.Map({
      container: el.value!,
      style: "/demo/style.json",
      transformRequest: (url) => (url.startsWith("/demo/") ? { url: location.origin + url } : { url }),
      center: [10, 30],
      zoom: props.zoom,
      attributionControl: false,
      interactive: false,
      antialias: true,
      fadeDuration: 0,
      pixelRatio: effectivePixelRatio(),
    });
    map.on("style.load", () => {
      map!.setProjection({ type: "globe" });
    });

    if (props.spin) {
      const step = () => {
        if (!map) return;
        const c = map.getCenter();
        map.jumpTo({ center: [c.lng + 0.085, c.lat] });
        raf = requestAnimationFrame(step);
      };
      map.on("load", () => {
        raf = requestAnimationFrame(step);
      });
    }
    window.addEventListener("resize", onResize);
  } catch (e) {
    console.warn("GlobeMap: map init failed, showing fallback", e);
    failed.value = true;
  }
});

// Slide-scale changes on resize / fullscreen, so the buffer must follow.
const onResize = () => map?.setPixelRatio(effectivePixelRatio());

onBeforeUnmount(() => {
  cancelAnimationFrame(raf);
  window.removeEventListener("resize", onResize);
  map?.remove();
});
</script>

<template>
  <div class="globe-wrap" :style="{ height }">
    <div v-show="!failed" ref="el" class="globe" :style="{ height }" />
  </div>
</template>

<style scoped>
.globe {
  width: 100%;
  border-radius: 10px;
  overflow: hidden;
}
</style>
