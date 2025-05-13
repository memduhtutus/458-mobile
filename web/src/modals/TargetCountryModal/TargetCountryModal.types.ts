import type { TParameter } from '@/api/parameter/parametersApi.types'

export type TTargetCountryModalProps = {
  parameter: TParameter
  fetchParameters: () => Promise<void>
}

export type TTargetCountryGlobalHeaderProps = {
  value: string
  parameterKey: string
}

export type TTargetCountryAddValueFormProps = {
  parameterId: string
  fetchParameters: () => Promise<void>
}

export type TTargetCountryValueItemProps = {
  country: string
  value: string
  parameterId: string
  targetValueId: string
  fetchParameters: () => Promise<void>
}
