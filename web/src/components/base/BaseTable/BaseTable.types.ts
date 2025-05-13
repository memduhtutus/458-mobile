import type { Component } from 'vue'

export type TBaseTableProps = {
  columns: TBaseTableColumn[]
  values: TCellType[][]
}
export type TBaseTableColumn = {
  label: string
  extra?: Component
  key: string
  flex?: number
}

export type TPrintableCellType = string | number | boolean
export type TComponentCellType = Component
export type TCellType = TPrintableCellType | TComponentCellType
