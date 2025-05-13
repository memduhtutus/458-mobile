import type { TApiError } from '@/api/parameter/parametersApi.types'
import axios from 'axios'
// import { getAuth } from 'firebase/auth'

const ApiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

ApiClient.interceptors.request.use(
  async (config) => {
    // const currentUser = getAuth().currentUser
    // if (currentUser) {
    //   const token = await currentUser.getIdToken()
    //   config.headers.Authorization = `Bearer ${token}`
    // }
    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)

ApiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.data) {
      const apiError = error.response.data as TApiError
      return Promise.resolve({ data: null, error: apiError })
    }
    return Promise.resolve({ data: null, error: error })
  },
)

export default ApiClient
