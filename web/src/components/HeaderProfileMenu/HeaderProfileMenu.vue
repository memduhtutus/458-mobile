<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import HeaderProfileButton from './partials/HeaderProfileButton.vue'
import { BaseText } from '../base/BaseText'
import { BaseButton } from '../base/BaseButton'
import { logout } from '@/api/auth/authApi'
import { useRouter } from 'vue-router'
// import { getAuth } from 'firebase/auth'

const isOpen = ref(false)
const menuRef = ref<HTMLElement | null>(null)
const router = useRouter()
// const auth = getAuth()

const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

const handleClickOutside = (event: MouseEvent) => {
  if (menuRef.value && !menuRef.value.contains(event.target as Node)) {
    isOpen.value = false
  }
}

const onLogout = async () => {
  try {
    await logout()
    router.push('/signin')
  } catch (error) {
    console.error(error)
  }
}

const accountEmail = '' // auth.currentUser?.email || ''

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <div class="relative" ref="menuRef">
    <HeaderProfileButton :isOpen="isOpen" @toggleMenu="toggleMenu" />
    <div
      v-if="isOpen"
      class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-2 z-50 flex flex-col justify-center items-center gap-4 px-4"
    >
      <BaseText variant="bodyBold" color="text-moon">{{ accountEmail }}</BaseText>
      <BaseButton variant="primary" class="w-full" @click="onLogout"> Log out </BaseButton>
    </div>
  </div>
</template>
