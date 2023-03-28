<template>
  <div class="h-full w-full">
    <h1>Hello World</h1>
<!--    <div id="map" class="h-full" />-->
  </div>
</template>

<script setup>
// https://github.com/nuxt/framework/issues/3587
definePageMeta({
  pageTransition: false,
  layout: 'fullscreen'
})
</script>