export type TParameter = {
  id: string
  key: string
  value: string
  description: string
  createdAt: number
  updatedAt: number
  targetValues?: TargetValue[]
}

export interface TargetValue {
  id: string
  country: string
  value: string
  createdAt?: number
  createdBy?: string
}

export type TAddParameterRequstBody = {
  key: string
  value: string
  description: string
}

export type TEditParameterRequstBody = TAddParameterRequstBody & { lastUpdatedAt?: number }

export type TApiError = {
  message: string
  errorCode: string
}

export type TApiResponse<T> = {
  data: T
  error?: TApiError
}

export type TAddTargetValueRequstBody = {
  country: string
  value: string
}
