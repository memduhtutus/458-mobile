<script setup lang="ts">
import BaseTableComponentCell from './partials/BaseTableComponentCell.vue'
import BaseTableHeader from './partials/BaseTableHeader.vue'
import BaseTablePrintableCell from './partials/BaseTablePrintableCell.vue'
import type { TBaseTableProps, TPrintableCellType } from './BaseTable.types'
import { FlexBox } from '@/components/FlexBox'

defineProps<TBaseTableProps>()
</script>

<template>
  <FlexBox class="w-full">
    <BaseTableHeader :columns="columns" class="hidden md:grid" />
    <template v-for="(rows, rowIndex) in values" :key="rowIndex">
      <div
        class="block md:grid w-full"
        :style="{
          gridTemplateColumns: columns.map((col) => (col.flex ? `${col.flex}fr` : '1fr')).join(' '),
        }"
      >
        <div class="md:contents border-1 border-white flex-1 mx-8 my-2 pt-2 rounded-2xl">
          <div v-for="(cell, columnIndex) in rows" :key="columnIndex" class="contents">
            <BaseTablePrintableCell
              v-if="['string', 'boolean', 'number'].includes(typeof cell)"
              :cell="cell as TPrintableCellType"
              :label="columns[columnIndex].label"
              class="flex-1 px-4 mb-2"
            />
            <BaseTableComponentCell
              v-else
              :cell="cell"
              class="px-4 mb-2 overflow-hidden"
              :label="columns[columnIndex].label"
            />
          </div>
        </div>
      </div>
    </template>
  </FlexBox>
</template>
