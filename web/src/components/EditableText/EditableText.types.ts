import type { TBaseTextInputProps } from '@/components/base/BaseTextInput/BaseTextInput.types'
import type { TBaseTextProps } from '@/components/base/BaseText/BaseText.types'

export type TEditableTextProps = {
  textFieldProps: TBaseTextInputProps
  textProps: TBaseTextProps
  isEditing: boolean
  label?: string
}
