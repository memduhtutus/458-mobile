<script setup lang="ts">
import { BaseText } from '@/components/base/BaseText'
import { FlexBox } from '@/components/FlexBox'
import IconAlertOctagon from '@/components/icons/IconAlertOctagon.vue'
import type { TBaseFieldErrorProps } from './BaseFieldError.types'

defineProps<TBaseFieldErrorProps>()
</script>

<template>
  <FlexBox v-if="error" className="flex-row items-center justify-start gap-2">
    <IconAlertOctagon color="stroke-error" />
    <BaseText variant="bodySmall" color="text-error">
      {{ error }}
    </BaseText>
  </FlexBox>
</template>
