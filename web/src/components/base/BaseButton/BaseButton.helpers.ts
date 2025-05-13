import type { TBaseButtonSize, TBaseButtonVariants } from './BaseButton.types'
import { BUTTONS_VARIANT_STATE_MAP, BUTTON_SIZE_MAP } from './BaseButton.constants'

export function getButtonStyle(variant: TBaseButtonVariants): string {
  return BUTTONS_VARIANT_STATE_MAP[variant].join(' ')
}

export function getButtonSize(size: TBaseButtonSize): string {
  return BUTTON_SIZE_MAP[size].join(' ')
}
