import type { Component } from 'vue'

export type TBasePageProps = {
  header?: TBaseHeaderProps
  fullWidth?: boolean
}

export type TBaseHeaderProps = {
  left?: Component
  right?: Component
}
