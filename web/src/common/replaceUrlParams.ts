import { isUndefined, isEmpty } from 'lodash/fp'

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const replaceUrlParams = (urlParam: string, paramsObject: Record<string, any>): string => {
  let url = urlParam

  if (isUndefined(url)) {
    return ''
  }

  if (isEmpty(paramsObject)) {
    return url
  }

  Object.keys(paramsObject).forEach((key) => {
    const reg = new RegExp(`{${key}}`, 'g')
    url = url.replace(reg, paramsObject[key])
  })

  const areParamsMissing = /\{[a-zA-Z0-9.-_]+\}/gi.test(url)

  if (areParamsMissing) {
    throw new Error('Missing url params passed')
  }

  return url
}

export default replaceUrlParams
