<script setup lang="ts">
import { defineProps } from 'vue'
import { Field } from 'vee-validate'
import { BaseTextInput } from '@/components/base/BaseTextInput'
import type { TFieldTextInputProps } from './FieldTextInput.types'

const props = defineProps<TFieldTextInputProps>()

defineExpose({
  name: 'FieldTextInput',
})
</script>

<template>
  <Field :name="props.name" :rules="props.rules" v-slot="{ field, errors }">
    <BaseTextInput
      v-model="field.value"
      @input="field.onChange"
      @blur="field.onBlur"
      :placeholder="props.placeholder"
      :sticky-state="props.stickyState"
      :error="errors[0]"
      :type="props.type"
    />
  </Field>
</template>
