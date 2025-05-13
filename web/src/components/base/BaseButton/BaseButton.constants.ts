export const BUTTONS_VARIANT_STATE_MAP = {
  primary: [
    'bg-base-blue',
    'border-base-blue',
    'hover:bg-base-blue-lighter',
    'active:bg-base-blue-darker',
    'disabled:bg-passive',
    'disabled:border-gray-200',
    'disabled:text-gray-600',
  ],
  secondary: [
    'bg-base-navy',
    'border-base-navy',
    'hover:bg-base-navy-lighter',
    'active:bg-base-navy-darker',
    'disabled:bg-passive',
    'disabled:text-gray-600',
  ],
  ghost: [
    'bg-base-turquoise',
    'hover:bg-base-turquoise-lighter',
    'active:bg-base-turquoise-darker',
    'disabled:bg-passive',
    'disabled:border-transparent',
    'disabled:text-gray-600',
  ],
  danger: [
    'bg-base-red',
    'border-base-red',
    'hover:bg-base-red-lighter',
    'hover:border-base-coral',
    'active:bg-base-red-darker',
    'active:border-base-dark',
    'disabled:bg-passive',
    'disabled:border-gray-200',
    'disabled:text-gray-600',
  ],
}

export const BUTTON_SIZE_MAP = {
  small: ['py-1', 'px-4', 'text-sm', 'font-semibold'],
  medium: ['p-3', 'text-sm', 'font-semibold'],
  large: ['p-4', 'text-base', 'font-bold'],
}

export const BASE_BUTTON_DEFAULT_STYLES = [
  'transition-colors',
  'duration-200',
  'rounded-[4px]',
  'text-white',
]
