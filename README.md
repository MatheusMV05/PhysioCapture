# 🏥 PhysioCapture - Sistema de Gestão para Clínicas de Fisioterapia

Sistema completo de gestão para clínicas de fisioterapia com frontend Next.js, backend Django e banco de dados PostgreSQL.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Executando o Projeto](#executando-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades](#funcionalidades)
- [API Endpoints](#api-endpoints)
- [Deploy](#deploy)

## 🎯 Sobre o Projeto

PhysioCapture é um sistema completo para gestão de clínicas de fisioterapia que permite:

- ✅ Gerenciamento de pacientes
- ✅ Registro de consultas e evoluções
- ✅ Upload e organização de documentos médicos
- ✅ Controle de usuários e permissões
- ✅ Gestão de clínicas e planos
- ✅ Dashboard com estatísticas
- ✅ Sistema de autenticação JWT

## 🚀 Tecnologias

### Backend
- **Python 3.11+**
- **Django 5.0** - Framework web
- **Django REST Framework** - API REST
- **PostgreSQL 15+** - Banco de dados
- **JWT** - Autenticação
- **AWS S3** - Armazenamento de arquivos (opcional)

### Frontend
- **Next.js 14** - Framework React
- **TypeScript** - Tipagem estática
- **Tailwind CSS** - Estilização
- **React Query** - Gerenciamento de estado
- **Axios** - Cliente HTTP
- **React Hook Form** - Formulários
- **Zod** - Validação de schemas

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Node.js** 18+ e npm/yarn
- **Python** 3.11+ e pip
- **PostgreSQL** 15+
- **Git**

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd physiocapture-migrado
```

### 2. Instale o Backend

```bash
cd backend

# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Instale o Frontend

```bash
cd ../frontend

# Instale as dependências
npm install
# ou
yarn install
```

## ⚙️ Configuração

### Backend

1. **Configure o PostgreSQL**

```sql
CREATE DATABASE physiocapture;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE physiocapture TO postgres;
```

2. **Configure as variáveis de ambiente**

```bash
cd backend
cp .env.example .env
```

Edite o arquivo `.env`:

```env
SECRET_KEY=sua-chave-secreta-super-segura
DEBUG=True
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/physiocapture
CORS_ALLOWED_ORIGINS=http://localhost:3000
JWT_SECRET_KEY=sua-chave-jwt-secreta
```

3. **Execute as migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Crie um superusuário**

```bash
python manage.py createsuperuser
```

### Frontend

1. **Configure as variáveis de ambiente**

```bash
cd frontend
cp .env.example .env
```

Edite o arquivo `.env`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🚀 Executando o Projeto

### Backend

```bash
cd backend
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

python manage.py runserver
```

O backend estará rodando em: `http://localhost:8000`

### Frontend

```bash
cd frontend
npm run dev
# ou
yarn dev
```

O frontend estará rodando em: `http://localhost:3000`

### Acessando a Aplicação

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/api
- **Admin Django**: http://localhost:8000/admin

## 📁 Estrutura do Projeto

```
physiocapture-migrado/
├── backend/                 # Backend Django
│   ├── config/             # Configurações do Django
│   ├── core/               # App core (utilitários)
│   ├── clinics/            # App de clínicas
│   ├── users/              # App de usuários
│   ├── patients/           # App de pacientes
│   ├── consultations/      # App de consultas
│   ├── documents/          # App de documentos
│   ├── media/              # Arquivos de upload
│   ├── manage.py           # CLI do Django
│   └── requirements.txt    # Dependências Python
│
└── frontend/               # Frontend Next.js
    ├── src/
    │   ├── app/           # Pages do Next.js
    │   ├── components/    # Componentes React
    │   ├── lib/           # Utilitários
    │   ├── services/      # Serviços de API
    │   ├── types/         # TypeScript types
    │   └── hooks/         # React hooks
    ├── public/            # Arquivos públicos
    └── package.json       # Dependências Node
```

## ✨ Funcionalidades

### Gestão de Clínicas
- Cadastro completo de clínicas
- Controle de planos e limites
- Estatísticas da clínica

### Gestão de Usuários
- Sistema de autenticação JWT
- Múltiplos níveis de permissão (Admin, Manager, Fisioterapeuta, Recepcionista)
- Gestão de perfis

### Gestão de Pacientes
- Cadastro completo de pacientes
- Anamnese e histórico médico
- Acompanhamento de status
- Estatísticas por paciente

### Consultas/Evoluções
- Registro de consultas usando método SOAP
- Diferentes tipos de consultas
- Prescrição de exercícios
- Agendamento de retornos

### Documentos
- Upload de documentos médicos
- Categorização automática
- Armazenamento seguro
- Busca e filtros

## 🔌 API Endpoints

### Autenticação
```
POST   /api/auth/login/              - Login
POST   /api/auth/logout/             - Logout
POST   /api/auth/token/refresh/      - Refresh token
GET    /api/auth/users/me/           - Perfil do usuário
```

### Clínicas
```
GET    /api/clinics/                 - Listar clínicas
GET    /api/clinics/{id}/            - Detalhes da clínica
GET    /api/clinics/my_clinic/       - Minha clínica
GET    /api/clinics/{id}/stats/      - Estatísticas
```

### Pacientes
```
GET    /api/patients/                - Listar pacientes
POST   /api/patients/                - Criar paciente
GET    /api/patients/{id}/           - Detalhes do paciente
PATCH  /api/patients/{id}/           - Atualizar paciente
DELETE /api/patients/{id}/           - Deletar paciente
GET    /api/patients/{id}/stats/     - Estatísticas
```

### Consultas
```
GET    /api/consultations/           - Listar consultas
POST   /api/consultations/           - Criar consulta
GET    /api/consultations/{id}/      - Detalhes da consulta
PATCH  /api/consultations/{id}/      - Atualizar consulta
DELETE /api/consultations/{id}/      - Deletar consulta
```

### Documentos
```
GET    /api/documents/               - Listar documentos
POST   /api/documents/               - Upload documento
GET    /api/documents/{id}/          - Detalhes do documento
PATCH  /api/documents/{id}/          - Atualizar documento
DELETE /api/documents/{id}/          - Deletar documento
```

## 🚀 Deploy

### Backend (Django)

1. Configure as variáveis de ambiente para produção
2. Configure `DEBUG=False`
3. Execute `python manage.py collectstatic`
4. Use Gunicorn: `gunicorn config.wsgi:application`
5. Configure Nginx como proxy reverso

### Frontend (Next.js)

1. Execute `npm run build`
2. Deploy em Vercel, Netlify ou servidor próprio
3. Configure variáveis de ambiente no serviço de deploy

## 🔐 Segurança

- ✅ Autenticação JWT
- ✅ CORS configurado
- ✅ Validação de inputs
- ✅ Proteção CSRF
- ✅ Permissões por role
- ✅ Sanitização de dados

## 🧪 Testes

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm test
```

## 📝 Licença

Este projeto está sob a licença MIT.

## 👥 Autores

Sistema desenvolvido para gestão de clínicas de fisioterapia.

## 🆘 Suporte

Para suporte e dúvidas, abra uma issue no repositório.

---

**PhysioCapture** - Sistema completo de gestão para clínicas de fisioterapia 🏥
