<template>
  <div class="relative h-full w-full">
    <div id="map" class="h-full" />
    <button type="button" class="absolute bottom-2 md:bottom-4 right-2 md:right-4 inline-flex items-center p-2 border border-transparent rounded-full shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500" @click="displayFilters">
      <Icon name="mdi:tune" size="1.5em" />
    </button>
  </div>
</template>

<script setup>
import maplibregl from 'maplibre-gl'
import style from '@/assets/style.json'
import sample from '@/assets/big-sample.json'
import 'maplibre-gl/dist/maplibre-gl.css'

// https://github.com/nuxt/framework/issues/3587
definePageMeta({
  pageTransition: false,
  layout: 'fullscreen'
})

function displayFilters () {
  console.log('displayFilters')
}

onMounted(() => {
  const map = new maplibregl.Map({
    container: 'map',
    style,
    center: [4.8312188, 45.757198],
    zoom: 13,
    attributionControl: false
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
        'circle-color': ['get', 'color']
      }
    })
    map.on('click', 'poi', (e) => {
      const { properties } = e.features[0]
      new maplibregl.Popup({ closeButton: false, closeOnClick: true })
        .setLngLat(e.lngLat)
        .setHTML(`
            <h3>${properties.type_signalement}</h3>
            <div>${properties.description}</div>
          `)
        .addTo(map)
    })
    map.on('mouseenter', 'poi', () => map.getCanvas().style.cursor = 'pointer')
    map.on('mouseleave', 'poi', () => map.getCanvas().style.cursor = '')
  })
})
</script>

<style>
.mapboxgl-popup-content {
  font: 400 15px/22px 'Source Sans Pro', 'Helvetica Neue', sans-serif;
  padding: 0;
  width: 180px;
}
.mapboxgl-popup-content h3 {
  background: #94a3b8;
  color: #fff;
  margin: 0;
  padding: 10px;
  border-radius: 3px 3px 0 0;
  font-weight: 700;
  margin-top: -15px;
}

.mapboxgl-popup-content div {
  padding: 10px;
}

.mapboxgl-popup-anchor-top > .mapboxgl-popup-content {
  margin-top: 15px;
}

.mapboxgl-popup-anchor-top > .mapboxgl-popup-tip {
  border-bottom-color: #91c949;
}
</style>
