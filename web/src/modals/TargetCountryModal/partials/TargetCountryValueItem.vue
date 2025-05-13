<script setup lang="ts">
import { FlexBox } from '@/components/FlexBox'
import { InfoItem } from '@/components/InfoItem'
import { BaseButton } from '@/components/base/BaseButton'
import { requestDeleteTargetValue } from '@/api/parameter/parameterApi'
import { useToast } from 'vue-toastification'
import { computed, ref } from 'vue'

import type { TTargetCountryValueItemProps } from '../TargetCountryModal.types'
import { getCountryName } from '@/common/countries'

const props = defineProps<TTargetCountryValueItemProps>()

const isLoading = ref(false)

const toast = useToast()

const handleDelete = async () => {
  try {
    isLoading.value = true
    const response = await requestDeleteTargetValue(props.parameterId, props.targetValueId)

    if (response.error) {
      toast.error(response.error.message)
      return
    }
    //success case
    await props.fetchParameters()
    toast.success('Target value deleted successfully')
  } catch (error) {
    console.error(error)
    toast.error('Unexpected error')
  } finally {
    isLoading.value = false
  }
}

const countryName = computed(() => {
  return getCountryName(props.country) as string
})
</script>

<template>
  <FlexBox class="flex-row justify-between items-center p-2 rounded-md bg-moon-lighter my-2">
    <InfoItem class="flex-1" :title="countryName" :value="value" />
    <BaseButton variant="danger" size="small" @click="handleDelete" :loading="isLoading">
      Delete
    </BaseButton>
  </FlexBox>
</template>
