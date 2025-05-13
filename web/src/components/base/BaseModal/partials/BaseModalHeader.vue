<script setup lang="ts">
import { BaseText } from '@/components/base/BaseText'

defineProps<{
  title: string
  closeModal: () => void
}>()
</script>

<template>
  <div class="flex flex-row justify-between items-top">
    <BaseText v-if="title" variant="title" color="text-white" class="modal-title">{{
      title
    }}</BaseText>
    <button class="bg-none border-none font-size-24px cursor-pointer p-0 -mt-2" @click="closeModal">
      <BaseText v-if="title" variant="title" color="text-white" class="modal-title">
        &times;
      </BaseText>
    </button>
  </div>
</template>
