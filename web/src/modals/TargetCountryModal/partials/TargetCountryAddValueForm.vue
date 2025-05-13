<script setup lang="ts">
import { useToast } from 'vue-toastification'
import { ref } from 'vue'

import { FlexBox } from '@/components/FlexBox'
import { BaseDropdownMenu } from '@/components/base/BaseDropdownMenu'
import { BaseTextInput } from '@/components/base/BaseTextInput'
import { BaseButton } from '@/components/base/BaseButton'
import { BaseText } from '@/components/base/BaseText'
import { requestAddTargetValue } from '@/api/parameter/parameterApi'
import countries, { getCountryCode } from '@/common/countries'

import type { TTargetCountryAddValueFormProps } from '../TargetCountryModal.types'
const props = defineProps<TTargetCountryAddValueFormProps>()

const selectedCountry = ref('')
const targetValue = ref('')
const isLoading = ref(false)

const toast = useToast()

const isOpen = ref(false)
const dropdownRef = ref()

const updateSelectedCountry = (country: string) => {
  selectedCountry.value = country
  isOpen.value = false
  dropdownRef.value?.close()
}

const saveTargetValue = async () => {
  try {
    isLoading.value = true
    console.log('saveTargetValue', selectedCountry.value, targetValue.value)
    const countryCode = getCountryCode(selectedCountry.value) as string
    const response = await requestAddTargetValue(props.parameterId, {
      country: countryCode,
      value: targetValue.value,
    })
    if (response.error) {
      toast.error(response.error.message)
      return
    }
    //success case
    await props.fetchParameters()
    toast.success('Target value added successfully')
    selectedCountry.value = ''
    targetValue.value = ''
  } catch (error) {
    console.error('unexpected', error)
    toast.error('Unexpected error')
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <FlexBox class="gap-4">
    <BaseText variant="bodyBold" color="text-white" class="self-start">Add Target Value</BaseText>
    <FlexBox class="items-start gap-2 md:flex-row">
      <BaseDropdownMenu
        label="Select Country"
        class="flex-1"
        :items="countries.map((country) => country.name)"
        ref="dropdownRef"
        v-model="selectedCountry"
        @update:model-value="updateSelectedCountry"
      />
      <FlexBox v-if="selectedCountry" class="flex-1">
        <BaseTextInput v-model="targetValue" :placeholder="`Enter value for ${selectedCountry}`" />
      </FlexBox>
    </FlexBox>
    <div class="px-12 w-full md:px-4 md:w-3/5 flex">
      <BaseButton
        :block="true"
        :loading="isLoading"
        variant="ghost"
        :disabled="!targetValue"
        v-if="selectedCountry"
        @click="saveTargetValue"
      >
        Set Value for {{ selectedCountry }}
      </BaseButton>
    </div>
  </FlexBox>
</template>
