<script setup lang="ts">
import { BasePage } from '@/components/base/BasePage'
import { BaseText } from '@/components/base/BaseText'
import { FlexBox } from '@/components/FlexBox'
import IMAGES from '@/common/images'
import { BaseButton } from '@/components/base/BaseButton'
import { Form } from 'vee-validate'
import type { SubmissionContext } from 'vee-validate'
import { FieldEmailInput } from '@/components/field/FieldEmailInput'
import { FieldPasswordInput } from '@/components/field/FieldPasswordInput'
import { BaseFieldError } from '@/components/base/BaseFieldError'
import { ref } from 'vue'
import { login } from '@/api/auth/authApi'
import { useRouter } from 'vue-router'
interface SignInFormValues {
  email: string
  password: string
}

interface FirebaseError {
  code: string
  message: string
}

const router = useRouter()
const loading = ref(false)

const onSubmit = async (values: unknown, { setFieldError }: SubmissionContext) => {
  const formValues = values as SignInFormValues
  try {
    loading.value = true
    const user = await login(formValues.email, formValues.password)
    console.log(user)
    router.push('/')
  } catch (error: unknown) {
    const firebaseError = error as FirebaseError
    if (firebaseError.code === 'auth/invalid-credential') {
      setFieldError('email', 'Invalid email address or password')
    } else {
      setFieldError('email', 'An error occurred during sign in')
    }
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <BasePage>
    <img :src="IMAGES.icon" alt="logo" class="p-8" />
    <FlexBox className="p-4">
      <BaseText variant="title" color="text-active-darker">Please sign in</BaseText>
    </FlexBox>
    <Form @submit="onSubmit" v-slot="{ errors }">
      <FieldEmailInput placeholder="Enter your email" sticky-state="sticky-top" />
      <FieldPasswordInput placeholder="Enter your password" sticky-state="sticky-bottom" />
      <FlexBox className="gap-2 mt-2">
        <BaseFieldError :error="errors.email" />
        <BaseFieldError :error="errors.password" />
      </FlexBox>
      <FlexBox className="py-4">
        <BaseButton variant="secondary" type="submit" :loading="loading" block>Sign in</BaseButton>
        <BaseText variant="bodySmall" color="text-passive" class="mt-16">AIWAI © 2021</BaseText>
      </FlexBox>
    </Form>
  </BasePage>
</template>
