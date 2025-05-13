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
      d="M12 4V20M12 20L18 14M12 20L6 14"
      :stroke="color"
      :stroke-width="strokeWidth"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>
