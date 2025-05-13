export type TBaseTextInputProps = {
  modelValue?: string | number
  className?: string
  height?: number
  hasError?: boolean
  editable?: boolean
  stickyState?: TBaseTextInputStickyState
  placeholder?: string
  error?: string
  name?: string
  type?: 'text' | 'password' | 'email'
}

export type TBaseTextInputStickyState = 'default' | 'sticky-top' | 'sticky-bottom'
