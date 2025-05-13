<script setup lang="ts">
import { onMounted, onUnmounted, watch } from 'vue'
import BaseModalHeader from './partials/BaseModalHeader.vue'
interface Props {
  modelValue: boolean
  title?: string
  modalHeight?: string
  closeOnClickOutside?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  title: '',
  closeOnClickOutside: true,
})

const emit = defineEmits<{
  (e: 'update:modelValue', value: boolean): void
  (e: 'close'): void
}>()

const closeModal = () => {
  emit('update:modelValue', false)
  emit('close')
}

const handleEscape = (e: KeyboardEvent) => {
  if (e.key === 'Escape') {
    closeModal()
  }
}

watch(
  () => props.modelValue,
  (newValue) => {
    if (newValue) {
      document.body.classList.add('no-scroll')
    } else {
      document.body.classList.remove('no-scroll')
    }
  },
)

onMounted(() => {
  document.addEventListener('keydown', handleEscape)
  if (props.modelValue) {
    document.body.classList.add('no-scroll')
  }
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleEscape)
  document.body.classList.remove('no-scroll')
})
</script>

<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="modelValue" class="modal-overlay" @click="closeOnClickOutside && closeModal()">
        <div
          class="flex flex-col bg-moon max-h-[90vh] overflow-y-auto rounded-lg p-4 relative w-[600px]"
          :style="{ height: modalHeight }"
          @click.stop
        >
          <BaseModalHeader :title="title" :closeModal="closeModal" />
          <div class="modal-body mt-8 flex-1 overflow-y-auto">
            <slot></slot>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style>
