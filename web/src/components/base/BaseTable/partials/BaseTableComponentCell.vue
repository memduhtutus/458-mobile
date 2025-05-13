<script setup lang="ts">
defineProps<{
  // Info: (serhat) Type any is a workaround to avoid type errors when the cell is a component
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  cell: any
  label: string
}>()
</script>

<template>
  <component class="flex-1" :is="cell" :label="label" />
</template>
