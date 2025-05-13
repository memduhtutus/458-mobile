<script setup lang="ts">
import { withDefaults, defineProps, computed, defineEmits } from 'vue'
import { BaseFieldError } from '@/components/base/BaseFieldError'
import type { TBaseTextInputProps } from './BaseTextInput.types'
const props = withDefaults(defineProps<TBaseTextInputProps>(), {
  modelValue: undefined,
  className: '',
  height: 48,
  hasError: false,
  editable: true,
  stickyState: undefined,
  placeholder: undefined,
  type: 'text',
  name: undefined,
  error: undefined,
})

const emit = defineEmits(['update:modelValue', 'input', 'blur'])

const getBorderRadiusClasses = () => {
  switch (props.stickyState) {
    case 'sticky-bottom':
      return 'relative rounded-tr-none rounded-tl-none -mt-px'
    case 'sticky-top':
      return 'relative rounded-br-none rounded-bl-none focus:z-3'
    default:
      return ''
  }
}

const getErrorClasses = () => {
  return props.error ? 'border-error z-2 text-error' : 'text-white'
}

const getExtraClasses = computed(() => {
  const borderRadiusClasses = getBorderRadiusClasses()
  const errorClasses = getErrorClasses()

  return `${borderRadiusClasses} ${errorClasses} ${props.className}`
})

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  emit('update:modelValue', target.value)
  emit('input', event)
}

const handleBlur = (event: Event) => {
  emit('blur', event)
}

defineExpose({
  name: 'BaseTextInput',
})
</script>

<template>
  <div class="relative w-full">
    <input
      :value="modelValue"
      @input="handleInput"
      @blur="handleBlur"
      class="outline-none bg-moon border border-active text-sm font-normal focus:border-base-purple block w-full p-2.5 rounded-lg focus:text-white placeholder-passive"
      :class="getExtraClasses"
      :placeholder="placeholder"
      :type="type"
      :name="name"
      required
    />
  </div>
  <BaseFieldError v-if="error && !stickyState" :error="error" />
</template>
