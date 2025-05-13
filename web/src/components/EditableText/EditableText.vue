<script setup lang="ts">
import { FlexBox } from '@/components/FlexBox'
import { BaseTextInput } from '@/components/base/BaseTextInput'
import { BaseText } from '@/components/base/BaseText'
import type { TEditableTextProps } from './EditableText.types'

defineProps<TEditableTextProps>()
const emit = defineEmits(['update:modelValue'])

const handleValueChange = (value: string) => {
  emit('update:modelValue', value)
}
</script>

<template>
  <FlexBox>
    <FlexBox v-if="isEditing" class="gap-2 md:ml-[-22px]">
      <BaseText class="md:hidden self-start" tag="span" variant="bodyBold" color="text-white"
        >{{ label }}:
      </BaseText>
      <BaseTextInput v-bind="textFieldProps" @update:modelValue="handleValueChange" />
    </FlexBox>
    <FlexBox v-else class="self-start md:bg-moon md:h-[42px] md:pb-[0px]">
      <BaseText class="self-start" v-bind="textProps" color="text-muted-white">
        <BaseText class="md:hidden" tag="span" variant="bodyBold" color="text-white"
          >{{ label }}:
        </BaseText>
      </BaseText>
    </FlexBox>
  </FlexBox>
</template>
