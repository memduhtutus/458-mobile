<script setup lang="ts">
import { FlexBox } from '@/components/FlexBox'
import IMAGES from '@/common/images'
import { HeaderProfileMenu } from '@/components/HeaderProfileMenu'
</script>

<template>
  <FlexBox class="h-[64px] px-4 items-center flex-row justify-between">
    <img :src="IMAGES.icon" alt="Logo" class="h-8" />
    <div class="flex-1" />
    <HeaderProfileMenu />
  </FlexBox>
</template>
