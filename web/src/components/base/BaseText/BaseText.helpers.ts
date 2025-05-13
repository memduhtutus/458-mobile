import { BASE_TEXT_VARIANT_MAP } from './BaseText.constants'
import type { TBaseTextVariants } from './BaseText.types'

export function getTextStyle(variant: TBaseTextVariants): string {
  return BASE_TEXT_VARIANT_MAP[variant].join(' ')
}
