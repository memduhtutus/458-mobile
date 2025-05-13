<script setup lang="ts">
import { FlexBox } from '@/components/FlexBox'
import { InfoItem } from '@/components/InfoItem'
import type { TTargetCountryGlobalHeaderProps } from '../TargetCountryModal.types'
const props = defineProps<TTargetCountryGlobalHeaderProps>()
</script>

<template>
  <FlexBox class="gap-2 items-center mb-2">
    <InfoItem title="Parameter Key" :value="props.parameterKey" />
    <InfoItem title="Global Value" :value="props.value" />
  </FlexBox>
</template>
