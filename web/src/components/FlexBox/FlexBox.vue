<script setup lang="ts">
import { withDefaults, defineProps } from 'vue'

withDefaults(
  defineProps<{
    className?: string
  }>(),
  {
    className: '',
  },
)

defineExpose({
  name: 'FlexBox',
})
</script>

<template>
  <div :class="['flex flex-col justify-center items-center w-full', className]">
    <slot></slot>
  </div>
</template>
