<script setup lang="ts">
import { ref, computed } from 'vue'
import ChevronDownIcon from '@/components/icons/ChevronDownIcon.vue'
import ChevronUpIcon from '@/components/icons/ChevronUpIcon.vue'
import { BaseButton } from '@/components/base/BaseButton'
import { FlexBox } from '@/components/FlexBox'
import { BaseTextInput } from '../BaseTextInput'

const props = defineProps<{
  label?: string
  items?: string[]
  modelValue?: string
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
  (e: 'select', value: string): void
}>()

const isOpen = ref(false)
const searchQuery = ref('')

const filteredItems = computed(() => {
  if (!props.items) return []
  if (!searchQuery.value) return props.items

  return props.items.filter((item) => item.toLowerCase().includes(searchQuery.value.toLowerCase()))
})

const close = () => {
  isOpen.value = false
  searchQuery.value = ''
}

const selectItem = (item: string) => {
  emit('update:modelValue', item)
  emit('select', item)
  close()
}

defineExpose({
  close,
})
</script>

<template>
  <FlexBox class="relative" ref="dropdownRef">
    <BaseButton :label="label" @click="isOpen = !isOpen" :block="true">
      {{ modelValue || label }}
      <ChevronDownIcon v-if="!isOpen" />
      <ChevronUpIcon v-else />
    </BaseButton>

    <FlexBox
      v-if="isOpen"
      class="z-10 mt-2 p-4 rounded-md focus:outline-none bg-moon-lighter absolute top-1/1 left-0 w-full"
    >
      <BaseTextInput type="text" v-model="searchQuery" placeholder="Search..." />
      <FlexBox class="py-1 justify-start overflow-y-auto">
        <slot :filtered-items="filteredItems" :select-item="selectItem">
          <button
            v-for="item in filteredItems"
            :key="item"
            @click="selectItem(item)"
            class="w-full text-left px-4 py-2 text-sm text-passive hover:bg-moon hover:text-white rounded-md"
          >
            {{ item }}
          </button>
        </slot>
      </FlexBox>
    </FlexBox>
  </FlexBox>
</template>
