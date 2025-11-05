import api from '@/lib/api'
import type { LoginResponse, User } from '@/types'

export const authService = {
  async login(email: string, password: string): Promise<LoginResponse> {
    const { data } = await api.post('/auth/login/', { email, password })
    return data
  },

  async logout(refreshToken: string): Promise<void> {
    await api.post('/auth/logout/', { refresh: refreshToken })
  },

  async getProfile(): Promise<User> {
    const { data } = await api.get('/auth/users/me/')
    return data
  },
}
