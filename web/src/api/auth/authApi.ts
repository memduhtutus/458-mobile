// import { signInWithEmailAndPassword, signOut } from 'firebase/auth'
// import type { AuthError } from 'firebase/auth'
// import { auth } from '@/config/firebase'

import API_ENDPOINT from '@/common/apiEndpoints'
import ApiClient from '@/config/requestConfig'

export const login = async (email: string, password: string) => {
  const formData = new FormData()
  formData.append('username', email)
  formData.append('password', password)
  const response = await ApiClient.post(API_ENDPOINT.LOGIN, formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  })
  return response.data
}

export const logout = async () => {
  // try {
  //   await signOut(auth)
  // } catch (error) {
  //   const authError = error as AuthError
  //   throw authError
  // }
}
