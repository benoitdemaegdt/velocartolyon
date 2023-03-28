<template>
  <div class="h-full w-full">
    <div id="map" class="h-full" />
  </div>
</template>

<script setup>
import style from '@/assets/style.json'
import sample from '@/assets/sample.json'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'

// https://github.com/nuxt/framework/issues/3587
definePageMeta({
  pageTransition: false,
  layout: 'fullscreen'
})

onMounted(() => {
  const map = new maplibregl.Map({
    container: 'map',
    style,
    center: [4.8312188, 45.757198],
    zoom: 13
  })
  map.addControl(new maplibregl.NavigationControl({ showCompass: false }), 'top-left')
  map.addControl(new maplibregl.FullscreenControl(), 'top-right')

  map.on('load', () => {
    map.addSource('poi', { type: 'geojson', data: sample })
    map.addLayer({
      id: 'poi',
      type: 'circle',
      source: 'poi',
      paint: {
        'circle-radius': 5,
        'circle-color': '#ef4444'
      }
    })
  })
})
</script>