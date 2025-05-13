<script setup lang="ts">
import { BaseText } from '@/components/base/BaseText'
defineProps<{
  cell: string | boolean | number
  label: string
}>()
</script>

<template>
  <BaseText variant="bodySmall" color="text-muted-white">
    <BaseText tag="span" variant="bodyBold" color="text-white" class="md:hidden"
      >{{ label }}:
    </BaseText>
    {{ cell }}</BaseText
  >
</template>
