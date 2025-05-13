export type TBaseButtonProps = {
  className?: string
  variant?: TBaseButtonVariants
  size?: TBaseButtonSize
  loading?: boolean
  block?: boolean
  disabled?: boolean
  onPress?: () => void
  type?: HTMLButtonElement['type']
}

export type TBaseButtonVariants = 'primary' | 'secondary' | 'ghost' | 'danger'
export type TBaseButtonSize = 'small' | 'medium' | 'large'
