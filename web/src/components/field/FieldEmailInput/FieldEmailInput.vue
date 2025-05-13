<script setup lang="ts">
import { defineProps } from 'vue'
import type { TBaseTextInputProps } from '@/components/base/BaseTextInput/BaseTextInput.types'
import { BaseTextInput } from '@/components/base/BaseTextInput'
import { Field } from 'vee-validate'

const props = defineProps<TBaseTextInputProps>()

defineExpose({
  name: 'FieldEmailInput',
})
</script>

<template>
  <Field name="email" rules="required|email" v-slot="{ field, errors }">
    <BaseTextInput
      v-model="field.value"
      @input="field.onChange"
      @blur="field.onBlur"
      :placeholder="props.placeholder"
      :sticky-state="props.stickyState"
      className="border-active-darker"
      type="email"
      :error="errors[0]"
    />
  </Field>
</template>
