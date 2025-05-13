export type TBaseTextProps = {
  variant?: TBaseTextVariants
  color?: string
  tag?: string
  text?: string
}

export type TBaseTextVariants =
  | 'body'
  | 'bodyBold'
  | 'subtitle'
  | 'subtitleBold'
  | 'title'
  | 'titleBold'
  | 'bodySmall'
