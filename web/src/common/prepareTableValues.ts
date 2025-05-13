import type { Component } from 'vue'

export const prepareTableValues = (values: object[], extra?: Component) => {
  return values.map((value) => {
    return [...Object.values(value), ...(extra ? [extra] : [])]
  })
}
