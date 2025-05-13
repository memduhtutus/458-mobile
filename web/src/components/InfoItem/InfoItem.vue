<script setup lang="ts">
import { BaseText } from '@/components/base/BaseText'

defineProps<{
  title: string
  value: string
}>()
</script>

<template>
  <BaseText variant="body" color="text-passive">
    <BaseText variant="bodyBold" color="text-white" tag="span">{{ title }}: </BaseText>
    {{ value }}
  </BaseText>
</template>
