<script setup lang="ts">
import { defineProps } from 'vue'
import type { TBaseTextInputProps } from '@/components/base/BaseTextInput/BaseTextInput.types'
import { BaseTextInput } from '@/components/base/BaseTextInput'
import { Field } from 'vee-validate'

const props = defineProps<TBaseTextInputProps>()

defineExpose({
  name: 'FieldPasswordInput',
})
</script>

<template>
  <Field name="password" :rules="{ required: true, min: 8 }" v-slot="{ field, errors }">
    <BaseTextInput
      v-model="field.value"
      @input="field.onChange"
      @blur="field.onBlur"
      :placeholder="props.placeholder"
      :sticky-state="props.stickyState"
      className="border-active-darker"
      type="password"
      :error="errors[0]"
    />
  </Field>
</template>
