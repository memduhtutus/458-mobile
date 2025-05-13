<script setup lang="ts">
import type { TIconProps } from './icons.types'

withDefaults(defineProps<TIconProps>(), {
  width: 24,
  height: 24,
  color: 'stroke-white',
  strokeWidth: 2,
})
</script>

<template>
  <svg :width="width" :height="height" viewBox="0 0 24 24" fill="none" :class="color">
    <path
      d="M6 9L12 15L18 9"
      stroke-linecap="round"
      stroke-linejoin="round"
      :stroke-width="strokeWidth"
      vector-effect="non-scaling-stroke"
    />
  </svg>
</template>
