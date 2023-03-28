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
        'circle-color': ['get', 'color'],
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