# 📁 Estrutura Completa do Projeto PhysioCapture

## 🎯 Visão Geral

Projeto migrado para:
- **Frontend**: Next.js 14 + TypeScript
- **Backend**: Django 5.0 + Django REST Framework
- **Banco de Dados**: PostgreSQL 15+

---

## 📂 Estrutura de Diretórios

```
physiocapture-migrado/
├── README.md                    # Documentação principal
├── install.sh                   # Script de instalação automática
│
├── backend/                     # 🐍 Backend Django
│   ├── config/                  # Configurações do Django
│   │   ├── __init__.py
│   │   ├── settings.py          # ⚙️ Configurações principais
│   │   ├── urls.py              # 🔌 URLs principais
│   │   ├── wsgi.py              # WSGI para deployment
│   │   └── asgi.py              # ASGI para deployment
│   │
│   ├── core/                    # 🔧 App Core (utilitários)
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py            # Models base (TimeStamped, SoftDelete)
│   │   ├── views.py             # Health check
│   │   └── urls.py
│   │
│   ├── clinics/                 # 🏥 App Clínicas
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py            # Model Clinic
│   │   ├── serializers.py       # Serializers Clinic
│   │   ├── views.py             # ViewSets Clinic
│   │   ├── urls.py
│   │   └── admin.py             # Admin Clinic
│   │
│   ├── users/                   # 👤 App Usuários
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py            # Model User customizado
│   │   ├── serializers.py       # Serializers User/Auth
│   │   ├── views.py             # ViewSets User/Auth
│   │   ├── permissions.py       # Permissões customizadas
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── patients/                # 🤕 App Pacientes
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py            # Model Patient
│   │   ├── serializers.py       # Serializers Patient
│   │   ├── views.py             # ViewSets Patient
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── consultations/           # 📋 App Consultas
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py            # Model Consultation
│   │   ├── serializers.py       # Serializers Consultation
│   │   ├── views.py             # ViewSets Consultation
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── documents/               # 📄 App Documentos
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py            # Model Document
│   │   ├── serializers.py       # Serializers Document
│   │   ├── views.py             # ViewSets Document
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── media/                   # 📁 Arquivos de upload
│   ├── staticfiles/             # 📦 Arquivos estáticos
│   ├── logs/                    # 📝 Logs da aplicação
│   │
│   ├── manage.py                # 🔧 CLI do Django
│   ├── requirements.txt         # 📦 Dependências Python
│   ├── .env.example             # 📝 Exemplo de variáveis de ambiente
│   ├── .gitignore               # 🚫 Git ignore
│   ├── setup.sh                 # 🚀 Script de setup
│   └── README.md                # 📖 Documentação do backend
│
└── frontend/                    # ⚛️ Frontend Next.js
    ├── src/
    │   ├── app/                 # 📄 Pages (App Router)
    │   │   ├── globals.css      # 🎨 Estilos globais
    │   │   ├── layout.tsx       # 📐 Layout principal
    │   │   └── page.tsx         # 🏠 Página inicial
    │   │
    │   ├── components/          # 🧩 Componentes React
    │   │   ├── ui/              # 🎨 Componentes UI
    │   │   │   └── button.tsx   # Botão reutilizável
    │   │   │
    │   │   └── providers/       # 🔌 Providers
    │   │       └── query-provider.tsx  # React Query Provider
    │   │
    │   ├── lib/                 # 🔧 Utilitários
    │   │   └── api.ts           # 🌐 Cliente Axios
    │   │
    │   ├── services/            # 🌐 Serviços de API
    │   │   └── auth.service.ts  # Serviço de autenticação
    │   │
    │   ├── types/               # 📝 TypeScript Types
    │   │   └── index.ts         # Types do sistema
    │   │
    │   └── hooks/               # 🎣 Custom Hooks
    │
    ├── public/                  # 📁 Arquivos públicos
    │
    ├── package.json             # 📦 Dependências Node
    ├── tsconfig.json            # ⚙️ Config TypeScript
    ├── next.config.js           # ⚙️ Config Next.js
    ├── tailwind.config.ts       # 🎨 Config Tailwind
    ├── postcss.config.js        # ⚙️ Config PostCSS
    ├── .env.example             # 📝 Exemplo de variáveis de ambiente
    ├── .gitignore               # 🚫 Git ignore
    └── README.md                # 📖 Documentação do frontend
```

---

## 🔑 Arquivos Principais

### Backend (Django)

#### ⚙️ Configuração
- `config/settings.py` - Configurações completas do Django (DB, CORS, JWT, etc)
- `config/urls.py` - URLs principais e rotas da API
- `.env.example` - Template de variáveis de ambiente
- `requirements.txt` - Todas as dependências Python

#### 📊 Models (Banco de Dados)
- `core/models.py` - Models base (TimeStamped, SoftDelete)
- `clinics/models.py` - Model Clinic (clínicas)
- `users/models.py` - Model User customizado (usuários)
- `patients/models.py` - Model Patient (pacientes)
- `consultations/models.py` - Model Consultation (consultas)
- `documents/models.py` - Model Document (documentos)

#### 🔌 API (ViewSets e Serializers)
Cada app tem:
- `serializers.py` - Serialização dos dados
- `views.py` - ViewSets com a lógica da API
- `urls.py` - Rotas do app
- `admin.py` - Interface administrativa

#### 🔐 Autenticação e Permissões
- `users/permissions.py` - Permissões customizadas
- JWT configurado em `settings.py`
- Sistema de roles (Admin, Manager, Fisioterapeuta, Recepcionista)

---

### Frontend (Next.js)

#### ⚛️ Pages (App Router)
- `app/layout.tsx` - Layout principal com providers
- `app/page.tsx` - Página inicial
- `app/globals.css` - Estilos globais Tailwind

#### 🧩 Componentes
- `components/ui/button.tsx` - Componente Button reutilizável
- `components/providers/query-provider.tsx` - Provider do React Query

#### 🌐 Integração com API
- `lib/api.ts` - Cliente Axios configurado com interceptors JWT
- `services/auth.service.ts` - Serviço de autenticação
- `types/index.ts` - TypeScript types para toda a aplicação

#### ⚙️ Configuração
- `next.config.js` - Configuração do Next.js
- `tailwind.config.ts` - Configuração do Tailwind CSS
- `tsconfig.json` - Configuração do TypeScript
- `package.json` - Dependências e scripts

---

## 🚀 Como Usar

### Instalação Automática
```bash
chmod +x install.sh
./install.sh
```

### Instalação Manual

#### 1. Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Configure o .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

#### 2. Frontend
```bash
cd frontend
npm install
cp .env.example .env
# Configure o .env
npm run dev
```

---

## 📝 Modelos de Dados

### Clinic (Clínica)
- Dados da clínica
- Plano e limites
- Endereço completo
- Status de assinatura

### User (Usuário)
- Autenticação por email
- Roles e permissões
- Vínculo com clínica
- Dados profissionais (CRM)

### Patient (Paciente)
- Dados pessoais completos
- Endereço
- Anamnese
- Histórico médico
- Status do tratamento

### Consultation (Consulta)
- Método SOAP
- Tipos de consulta
- Prescrições
- Agendamentos

### Document (Documento)
- Upload de arquivos
- Categorização
- Metadados
- Vinculação com paciente

---

## 🔐 Autenticação JWT

O sistema usa JWT para autenticação:
- Token de acesso (60 minutos)
- Token de refresh (24 horas)
- Blacklist de tokens
- Refresh automático no frontend

---

## 📡 Endpoints Principais

### Auth
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/users/me/` - Perfil

### Clinics
- `GET /api/clinics/` - Listar
- `GET /api/clinics/my_clinic/` - Minha clínica
- `GET /api/clinics/{id}/stats/` - Estatísticas

### Patients
- CRUD completo em `/api/patients/`
- `GET /api/patients/{id}/stats/` - Estatísticas

### Consultations
- CRUD completo em `/api/consultations/`

### Documents
- CRUD completo em `/api/documents/`

---

## 🎨 UI Components

O frontend usa:
- Tailwind CSS para estilização
- Componentes reutilizáveis em `components/ui/`
- React Query para gerenciamento de estado
- React Hook Form + Zod para formulários
- Sonner para notificações

---

## 🔧 Ferramentas de Desenvolvimento

### Backend
- Django Debug Toolbar (dev)
- Django Extensions
- iPython
- Pytest para testes

### Frontend
- ESLint
- TypeScript
- Hot reload
- Fast Refresh

---

## 📦 Deploy

### Backend
- Gunicorn + Nginx
- PostgreSQL em produção
- AWS S3 para arquivos
- Variáveis de ambiente configuradas

### Frontend
- Vercel (recomendado)
- Build otimizado
- Variáveis de ambiente

---

## ✅ Checklist de Recursos

- ✅ Autenticação JWT
- ✅ CRUD completo de todas entidades
- ✅ Upload de arquivos
- ✅ Sistema de permissões
- ✅ API RESTful completa
- ✅ Frontend responsivo
- ✅ TypeScript type-safe
- ✅ Validação de formulários
- ✅ Gestão de estado com React Query
- ✅ Notificações toast
- ✅ Configuração de CORS
- ✅ Admin Django
- ✅ Documentação completa

---

## 📞 Suporte

Para dúvidas sobre a estrutura do projeto, consulte:
- `README.md` principal
- `backend/README.md` - Documentação do backend
- `frontend/README.md` - Documentação do frontend

---

**PhysioCapture** - Sistema completo e pronto para uso! 🏥
