<script setup lang="ts">
import BaseText from '../../BaseText/BaseText.vue'
import type { TBaseTableColumn } from '../BaseTable.types'

defineProps<{
  columns: TBaseTableColumn[]
}>()
</script>

<template>
  <div
    class="grid w-full"
    :style="{
      gridTemplateColumns: columns.map((col) => (col.flex ? `${col.flex}fr` : '1fr')).join(' '),
    }"
  >
    <div v-for="column in columns" :key="column.key" class="px-4 py-2">
      <div class="flex flex-row items-center gap-2">
        <BaseText variant="subtitle" color="text-active">{{ column.label }}</BaseText>
        <component :is="column.extra" />
      </div>
    </div>
  </div>
</template>
