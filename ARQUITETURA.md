# 🏗️ Arquitetura do PhysioCapture

## 📊 Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                      USUÁRIO FINAL                          │
│                      (Navegador Web)                        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP/HTTPS
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  FRONTEND - Next.js 14                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Pages (App Router)                                  │  │
│  │  - Login/Register                                    │  │
│  │  - Dashboard                                         │  │
│  │  - Pacientes, Consultas, Documentos                 │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Components                                          │  │
│  │  - UI Components (Button, Form, Modal, etc)         │  │
│  │  - Business Components                              │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  State Management                                    │  │
│  │  - React Query (cache, sync)                        │  │
│  │  - Zustand (auth state)                             │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Services                                            │  │
│  │  - API Client (Axios + Interceptors)                │  │
│  │  - Auth Service, Patients Service, etc              │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ REST API (JSON)
                         │ JWT Bearer Token
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  BACKEND - Django 5.0                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  API Layer (Django REST Framework)                  │  │
│  │  - ViewSets                                          │  │
│  │  - Serializers                                       │  │
│  │  - Authentication (JWT)                              │  │
│  │  - Permissions                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Business Logic Layer                                │  │
│  │  - Models (ORM)                                      │  │
│  │  - Validators                                        │  │
│  │  - Business Rules                                    │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Apps                                                │  │
│  │  - Core (utilities)                                  │  │
│  │  - Clinics                                           │  │
│  │  - Users (custom auth)                               │  │
│  │  - Patients                                          │  │
│  │  - Consultations                                     │  │
│  │  - Documents                                         │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ SQL Queries
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  DATABASE - PostgreSQL                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Tables                                              │  │
│  │  - clinics                                           │  │
│  │  - users (custom auth user)                          │  │
│  │  - patients                                          │  │
│  │  - consultations                                     │  │
│  │  - documents                                         │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  FILE STORAGE                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Opção 1: Local Storage (development)               │  │
│  │  /media/                                             │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Opção 2: AWS S3 (production)                       │  │
│  │  Bucket configurável                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Fluxo de Autenticação

```
┌─────────┐          ┌──────────┐          ┌─────────┐
│Frontend │          │ Backend  │          │Database │
└────┬────┘          └────┬─────┘          └────┬────┘
     │                    │                     │
     │ POST /auth/login/  │                     │
     │ {email, password}  │                     │
     ├───────────────────►│                     │
     │                    │ Validate credentials│
     │                    ├────────────────────►│
     │                    │                     │
     │                    │◄────────────────────┤
     │                    │ User found          │
     │                    │                     │
     │                    │ Generate JWT tokens │
     │                    │                     │
     │◄───────────────────┤                     │
     │ {access, refresh}  │                     │
     │                    │                     │
     │ Store tokens       │                     │
     │ in localStorage    │                     │
     │                    │                     │
     │ API Request        │                     │
     │ + Bearer Token     │                     │
     ├───────────────────►│                     │
     │                    │ Validate JWT        │
     │                    │                     │
     │                    │ Process request     │
     │                    │                     │
     │◄───────────────────┤                     │
     │ Response           │                     │
     │                    │                     │
```

---

## 📦 Estrutura de Dados

### Relacionamentos

```
┌─────────────┐
│   Clinic    │
│             │
│ - id        │
│ - name      │
│ - plan      │
└──────┬──────┘
       │
       │ 1:N
       │
       ├─────────────────────────────┐
       │                             │
       ▼                             ▼
┌─────────────┐              ┌─────────────┐
│    User     │              │   Patient   │
│             │              │             │
│ - id        │              │ - id        │
│ - email     │              │ - name      │
│ - role      │              │ - cpf       │
└──────┬──────┘              └──────┬──────┘
       │                            │
       │                            │ 1:N
       │                            │
       │                    ┌───────┴───────┐
       │                    │               │
       │                    ▼               ▼
       │            ┌──────────────┐ ┌─────────────┐
       │            │Consultation │ │  Document   │
       │            │             │ │             │
       │            │ - id        │ │ - id        │
       └───────────►│ - performer │ │ - uploader  │
                    │ - patient   │ │ - patient   │
                    └─────────────┘ └─────────────┘
```

---

## 🔐 Camadas de Segurança

```
┌─────────────────────────────────────────────────────┐
│              Layer 1: Network                       │
│  - HTTPS (Production)                               │
│  - CORS Configuration                               │
└─────────────────────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│              Layer 2: Authentication                │
│  - JWT Tokens                                       │
│  - Token Refresh                                    │
│  - Token Blacklist                                  │
└─────────────────────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│              Layer 3: Authorization                 │
│  - Role-based Permissions                           │
│  - Clinic Isolation                                 │
│  - Resource-level Permissions                       │
└─────────────────────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│              Layer 4: Data Validation               │
│  - Django Validators                                │
│  - Zod Schemas (Frontend)                           │
│  - SQL Injection Prevention (ORM)                   │
└─────────────────────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│              Layer 5: Data Protection               │
│  - Password Hashing (bcrypt)                        │
│  - CSRF Protection                                  │
│  - XSS Prevention                                   │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Fluxo de Deploy

### Development
```
┌────────────┐    ┌────────────┐    ┌────────────┐
│  Git Repo  │───►│ Local Dev  │───►│   Tests    │
└────────────┘    └────────────┘    └────────────┘
```

### Production (Sugerido)
```
┌────────────┐    ┌────────────┐    ┌────────────┐
│  Git Repo  │───►│   CI/CD    │───►│   Tests    │
└────────────┘    └────────────┘    └────────────┘
                                           │
                                           ▼
                    ┌──────────────────────────────┐
                    │      Build & Deploy          │
                    └──────────────────────────────┘
                            │           │
                            ▼           ▼
                    ┌─────────┐  ┌─────────┐
                    │ Vercel  │  │  AWS    │
                    │(Frontend)│  │(Backend)│
                    └─────────┘  └─────────┘
```

---

## 📊 Fluxo de Dados

### Criação de Paciente

```
Frontend                Backend                  Database
   │                       │                        │
   │ 1. Submit Form        │                        │
   ├──────────────────────►│                        │
   │                       │ 2. Validate Data       │
   │                       │ 3. Check Permissions   │
   │                       │ 4. Check Clinic Limits │
   │                       │                        │
   │                       │ 5. Create Patient      │
   │                       ├───────────────────────►│
   │                       │                        │
   │                       │◄───────────────────────┤
   │                       │ 6. Patient Created     │
   │                       │                        │
   │◄──────────────────────┤                        │
   │ 7. Return Patient Data│                        │
   │                       │                        │
   │ 8. Update UI          │                        │
   │ 9. Show Success Toast │                        │
```

---

## 🔄 Sistema Multi-Tenant

```
                    ┌─────────────────┐
                    │  PhysioCapture  │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
    ┌──────────┐       ┌──────────┐      ┌──────────┐
    │ Clínica A│       │ Clínica B│      │ Clínica C│
    └────┬─────┘       └────┬─────┘      └────┬─────┘
         │                  │                  │
    ┌────┴────┐        ┌────┴────┐       ┌────┴────┐
    │ Users   │        │ Users   │       │ Users   │
    │ Patients│        │ Patients│       │ Patients│
    │ Docs    │        │ Docs    │       │ Docs    │
    └─────────┘        └─────────┘       └─────────┘

    ✅ Isolamento completo de dados
    ✅ Cada clínica vê apenas seus próprios dados
    ✅ Administradores têm acesso total
```

---

## 📈 Escalabilidade

### Atual (Monolítico)
```
Frontend ──► Backend ──► Database
```

### Futuro (Microserviços - Opcional)
```
Frontend ──┬──► Auth Service ──► Database
           ├──► Patients Service ──► Database
           ├──► Consultations Service ──► Database
           └──► Documents Service ──► S3
```

---

## 🛠️ Stack Tecnológica

```
┌─────────────────────────────────────────┐
│           Frontend Stack                │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Next.js 14 (React Framework)    │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ TypeScript (Type Safety)        │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ Tailwind CSS (Styling)          │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ React Query (State Management)  │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ Axios (HTTP Client)             │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│           Backend Stack                 │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Django 5.0 (Web Framework)      │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ DRF (REST Framework)            │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ PostgreSQL (Database)           │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ JWT (Authentication)            │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ AWS S3 (File Storage)           │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

## 🎯 Próximos Passos para Produção

1. **Containerização**
   - Criar Dockerfiles
   - Docker Compose para desenvolvimento
   - Kubernetes para produção (opcional)

2. **CI/CD**
   - GitHub Actions
   - Testes automáticos
   - Deploy automático

3. **Monitoramento**
   - Sentry (error tracking)
   - New Relic (performance)
   - CloudWatch (AWS logs)

4. **Segurança**
   - SSL/TLS certificates
   - Rate limiting
   - Security headers
   - Regular security audits

5. **Performance**
   - Redis cache
   - CDN para assets
   - Database indexing
   - Query optimization

---

**PhysioCapture** - Arquitetura robusta e escalável 🏗️
