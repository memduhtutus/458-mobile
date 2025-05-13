<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { BasePage } from '@/components/base/BasePage'
import { requestParameters } from '@/api/parameter/parameterApi'
import type { TParameter } from '@/api/parameter/parametersApi.types'
import { FlexBox } from '@/components/FlexBox'
import { VueSpinner } from 'vue3-spinners'

const loading = ref(true)
const parameters = ref<TParameter[]>([])

const fetchParameters = async () => {
  const parametersResponse = await requestParameters()
  parameters.value = parametersResponse
  loading.value = false
}

onMounted(async () => {
  await fetchParameters()
})
</script>
<template>
  <BasePage fullWidth :header="{}">
    <FlexBox className="justify-center items-center mt-24" v-if="loading">
      <VueSpinner size="32" color="white" />
    </FlexBox>
    <HomeConfigTable :parameters="parameters" :fetchParameters="fetchParameters" v-else />
  </BasePage>
</template>
