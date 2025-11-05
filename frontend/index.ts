// Types para o sistema PhysioCapture

export interface User {
  id: string
  email: string
  name: string
  cpf?: string
  phone?: string
  crm?: string
  role: 'ADMIN' | 'MANAGER' | 'PHYSIOTHERAPIST' | 'RECEPTIONIST'
  clinic: string
  clinic_name?: string
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface Clinic {
  id: string
  name: string
  cnpj: string
  email: string
  phone: string
  phone_secondary?: string
  zip_code: string
  street: string
  number: string
  complement?: string
  neighborhood: string
  city: string
  state: string
  full_address?: string
  plan: 'BASIC' | 'PROFESSIONAL' | 'ENTERPRISE'
  plan_status: 'TRIAL' | 'ACTIVE' | 'SUSPENDED' | 'CANCELLED'
  max_users: number
  max_patients: number
  max_storage: number
  logo?: string
  website?: string
  description?: string
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface Patient {
  id: string
  full_name: string
  cpf: string
  date_of_birth: string
  age: number
  phone: string
  phone_secondary?: string
  email?: string
  zip_code?: string
  street?: string
  number?: string
  complement?: string
  neighborhood?: string
  city?: string
  state?: string
  full_address?: string
  occupation?: string
  insurance?: string
  insurance_number?: string
  status: 'ACTIVE' | 'INACTIVE' | 'EVALUATION' | 'DISCHARGED'
  general_notes?: string
  chief_complaint?: string
  current_illness?: string
  medical_history?: string
  medications?: string
  allergies?: string
  lifestyle?: string
  physical_assessment?: string
  clinic: string
  assigned_therapist?: string
  therapist_name?: string
  consultations_count?: number
  documents_count?: number
  last_visit_date?: string
  created_at: string
  updated_at: string
}

export interface Consultation {
  id: string
  date: string
  type: 'INITIAL_EVALUATION' | 'REASSESSMENT' | 'TREATMENT_SESSION' | 'DISCHARGE' | 'RETURN'
  subjective?: string
  objective?: string
  assessment?: string
  plan?: string
  exercises?: string
  next_visit?: string
  notes?: string
  clinic: string
  patient: string
  patient_name?: string
  performer: string
  performer_name?: string
  can_edit: boolean
  created_at: string
  updated_at: string
}

export interface Document {
  id: string
  file_name: string
  file_url: string
  file_size: number
  mime_type: string
  category: 'EXAME_IMAGEM' | 'EXAME_LABORATORIAL' | 'RECEITA' | 'ATESTADO' | 
            'CONSENTIMENTO' | 'ANAMNESE' | 'RELATORIO_EVOLUCAO' | 'OUTROS'
  title?: string
  description?: string
  clinic: string
  patient: string
  patient_name?: string
  uploader: string
  uploader_name?: string
  created_at: string
  updated_at: string
}

export interface AuthTokens {
  access: string
  refresh: string
}

export interface LoginResponse {
  user: User
  tokens: AuthTokens
}

export interface ApiError {
  message: string
  errors?: Record<string, string[]>
}
