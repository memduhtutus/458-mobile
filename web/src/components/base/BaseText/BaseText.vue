<script setup lang="ts">
import { computed } from 'vue'
import { getTextStyle } from './BaseText.helpers'
import type { TBaseTextProps } from './BaseText.types'

const props = withDefaults(defineProps<TBaseTextProps>(), {
  variant: 'body',
  color: 'text-white',
  tag: 'p',
  text: undefined,
})

const classes = computed(() => {
  return [getTextStyle(props.variant), props.color].join(' ')
})

defineExpose({
  name: 'BaseText',
})
</script>

<template>
  <component :is="tag" :class="classes">
    <span>
      <slot />
      <span>{{ text }}</span>
    </span>
  </component>
</template>
