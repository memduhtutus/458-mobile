import type { TBaseTextInputProps } from '@/components/base/BaseTextInput/BaseTextInput.types'

export type TFieldTextInputProps = TBaseTextInputProps & {
  rules?: string
  name: string
  type?: 'text' | 'password' | 'email'
}
