<script setup lang="ts">
import { FlexBox } from '@/components/FlexBox'
import { BaseModal } from '@/components/base/BaseModal'
import { BaseText } from '@/components/base/BaseText'
import type { TTargetCountryModalProps } from './TargetCountryModal.types'
import TargetCountryAddValueForm from './partials/TargetCountryAddValueForm.vue'
import TargetCountryGlobalHeader from './partials/TargetCountryGlobalHeader.vue'
import TargetCountryValueItem from './partials/TargetCountryValueItem.vue'
const props = defineProps<TTargetCountryModalProps>()
</script>

<template>
  <BaseModal title="Value by Country" :model-value="true" :modal-height="'80vh'">
    <div class="flex flex-col justify-between items-center mb-4 gap-4">
      <TargetCountryGlobalHeader
        :value="props.parameter.value"
        :parameterKey="props.parameter.key"
      />
      <FlexBox class="justify-between items-center" v-if="props.parameter.targetValues?.length">
        <BaseText variant="bodyBold" color="text-white" class="self-start">Target Values</BaseText>
        <TargetCountryValueItem
          v-for="value in props.parameter.targetValues"
          :key="value.country"
          :country="value.country"
          :value="value.value"
          :parameter-id="props.parameter.id"
          :target-value-id="value.id"
          :fetch-parameters="props.fetchParameters"
        />
      </FlexBox>
      <TargetCountryAddValueForm
        :parameter-id="props.parameter.id"
        :fetch-parameters="props.fetchParameters"
      />
    </div>
  </BaseModal>
</template>
