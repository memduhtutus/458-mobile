<script setup lang="ts">
import { computed } from 'vue'
import type { TBaseButtonProps } from './BaseButton.types'
import { getButtonStyle, getButtonSize } from './BaseButton.helpers'
import { BASE_BUTTON_DEFAULT_STYLES } from './BaseButton.constants'
import { VueSpinner } from 'vue3-spinners'

const props = withDefaults(defineProps<TBaseButtonProps>(), {
  variant: 'primary',
  size: 'medium',
  type: 'button',
  disabled: false,
  loading: false,
  block: false,
})

const emit = defineEmits<{
  (e: 'press'): void
}>()

const buttonClasses = computed(() => {
  const variantClasses = getButtonStyle(props.variant)
  const sizeClasses = getButtonSize(props.size)
  const blockClass = props.block ? 'w-full' : 'self-start'
  const disabledClass =
    props.disabled || props.loading ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'
  const defaultStyles = BASE_BUTTON_DEFAULT_STYLES.join(' ')

  return `${variantClasses} ${sizeClasses} ${blockClass} ${disabledClass} ${defaultStyles}`
})

const handleClick = () => {
  if (!props.disabled && !props.loading) {
    emit('press')
    props.onPress?.()
  }
}
</script>

<template>
  <button :type="type" :class="buttonClasses" :disabled="disabled" @click="handleClick">
    <div class="flex items-center justify-center gap-2 h-[20px]">
      <VueSpinner v-if="loading" color="white" size="16px" />
      <slot v-else />
    </div>
  </button>
</template>
