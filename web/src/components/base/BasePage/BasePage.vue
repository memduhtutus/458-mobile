<script setup lang="ts">
import { FlexBox } from '@/components/FlexBox'
import type { TBasePageProps } from './BasePage.types'
import { computed } from 'vue'
import { BaseHeader } from '@/components/base/BaseHeader'

const props = defineProps<TBasePageProps>()

defineOptions({
  name: 'BasePage',
})
defineExpose({
  name: 'BasePage',
})

const widthClass = computed(() => (props.fullWidth ? 'w-full' : 'max-w-[340px]'))
</script>

<template>
  <FlexBox>
    <BaseHeader v-if="props.header" />
    <div :class="widthClass" class="py-8">
      <slot />
    </div>
  </FlexBox>
</template>

<style scoped>
.header {
  background-color: blue;
  width: 100%;
  height: 60px;
}
</style>
