<script setup lang="ts">
import IconProfile from '@/components/icons/IconProfile.vue'
import ChevronDownIcon from '@/components/icons/ChevronDownIcon.vue'
import ChevronUpIcon from '@/components/icons/ChevronUpIcon.vue'

defineProps<{
  isOpen: boolean
}>()

const emit = defineEmits<{
  (e: 'toggleMenu'): void
}>()
</script>

<template>
  <div class="flex flex-row items-center cursor-pointer" @click="emit('toggleMenu')">
    <IconProfile :width="32" :height="32" color="fill-white" />
    <div class="flex flex-col pointer-events-none">
      <ChevronDownIcon :width="16" :height="16" color="fill-white" v-if="!isOpen" />
      <ChevronUpIcon :width="16" :height="16" color="fill-white" v-else />
    </div>
  </div>
</template>
