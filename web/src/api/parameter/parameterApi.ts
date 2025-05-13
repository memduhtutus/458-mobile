import API_ENDPOINT from '@/common/apiEndpoints'
import ApiClient from '@/config/requestConfig'
import type {
  TAddParameterRequstBody,
  TAddTargetValueRequstBody,
  TApiResponse,
  TEditParameterRequstBody,
  TParameter,
} from './parametersApi.types'
import replaceUrlParams from '@/common/replaceUrlParams'

export const requestParameters = async (): Promise<TParameter[]> => {
  const response = await ApiClient.get(API_ENDPOINT.PARAMETER)
  return response.data
}

export const requestAddParameter = async (
  parameter: TAddParameterRequstBody,
): Promise<TApiResponse<TParameter>> => {
  const response = await ApiClient.post(API_ENDPOINT.PARAMETER, parameter)
  return response
}

export const requestDeleteParameter = async (
  parameterId: string,
): Promise<TApiResponse<boolean>> => {
  const response = await ApiClient.delete(
    replaceUrlParams(API_ENDPOINT.PARAMETER_DETAIL, { id: parameterId }),
  )
  return response
}

export const requestEditParameter = async (
  parameterId: string,
  parameter: TEditParameterRequstBody,
): Promise<TApiResponse<TParameter>> => {
  const response = await ApiClient.put(
    replaceUrlParams(API_ENDPOINT.PARAMETER_DETAIL, { id: parameterId }),
    parameter,
  )
  return response
}

export const requestAddTargetValue = async (
  parameterId: string,
  targetValue: TAddTargetValueRequstBody,
): Promise<TApiResponse<TParameter>> => {
  const response = await ApiClient.post(
    replaceUrlParams(API_ENDPOINT.PARAMETER_TARGET_VALUES, { id: parameterId }),
    targetValue,
  )
  return response
}

export const requestDeleteTargetValue = async (
  parameterId: string,
  targetValueId: string,
): Promise<TApiResponse<TParameter>> => {
  const response = await ApiClient.delete(
    replaceUrlParams(API_ENDPOINT.PARAMETER_TARGET_VALUES_DETAIL, {
      id: parameterId,
      targetValueId,
    }),
  )
  return response
}
