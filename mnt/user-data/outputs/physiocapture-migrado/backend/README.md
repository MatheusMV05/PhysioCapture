# PhysioCapture Backend - Django REST API

Backend do sistema PhysioCapture desenvolvido com Django e Django REST Framework.

## 🚀 Tecnologias

- Python 3.11+
- Django 5.0
- Django REST Framework
- PostgreSQL 15+
- JWT Authentication
- AWS S3 (opcional)

## 📋 Pré-requisitos

- Python 3.11 ou superior
- PostgreSQL 15 ou superior
- pip (gerenciador de pacotes Python)
- virtualenv (recomendado)

## 🔧 Instalação

### 1. Clone o repositório e entre no diretório do backend

```bash
cd physiocapture-migrado/backend
```

### 2. Crie e ative um ambiente virtual

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados PostgreSQL

Crie um banco de dados PostgreSQL:

```sql
CREATE DATABASE physiocapture;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE physiocapture TO postgres;
```

### 5. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e configure:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/physiocapture
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### 6. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 8. Execute o servidor

```bash
python manage.py runserver
```

O servidor estará rodando em `http://localhost:8000`

## 📁 Estrutura do Projeto

```
backend/
├── config/              # Configurações do Django
│   ├── settings.py     # Configurações principais
│   ├── urls.py         # URLs principais
│   ├── wsgi.py         # WSGI para deployment
│   └── asgi.py         # ASGI para deployment
├── core/               # App core (utilitários)
├── clinics/            # App de clínicas
├── users/              # App de usuários
├── patients/           # App de pacientes
├── consultations/      # App de consultas
├── documents/          # App de documentos
├── media/              # Arquivos de mídia (uploads)
├── staticfiles/        # Arquivos estáticos
├── logs/               # Logs da aplicação
├── manage.py           # Gerenciador Django
├── requirements.txt    # Dependências
└── .env               # Variáveis de ambiente
```

## 🔑 Autenticação

A API usa JWT (JSON Web Tokens) para autenticação.

### Login

```bash
POST /api/auth/login/
Content-Type: application/json

{
  "email": "usuario@exemplo.com",
  "password": "senha123"
}
```

Resposta:

```json
{
  "user": {...},
  "tokens": {
    "access": "eyJ0eXAiOiJKV1...",
    "refresh": "eyJ0eXAiOiJKV1..."
  }
}
```

### Usando o token

Inclua o token de acesso no header:

```
Authorization: Bearer eyJ0eXAiOiJKV1...
```

## 📚 Endpoints da API

### Health Check
- `GET /api/health/` - Status da API

### Autenticação
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `POST /api/auth/register/` - Registro
- `POST /api/auth/token/refresh/` - Refresh token
- `GET /api/auth/users/me/` - Perfil do usuário
- `POST /api/auth/users/change_password/` - Trocar senha

### Clínicas
- `GET /api/clinics/` - Listar clínicas
- `GET /api/clinics/{id}/` - Detalhes da clínica
- `GET /api/clinics/my_clinic/` - Minha clínica
- `GET /api/clinics/{id}/stats/` - Estatísticas da clínica
- `POST /api/clinics/` - Criar clínica
- `PUT /api/clinics/{id}/` - Atualizar clínica
- `DELETE /api/clinics/{id}/` - Deletar clínica

### Pacientes
- `GET /api/patients/` - Listar pacientes
- `GET /api/patients/{id}/` - Detalhes do paciente
- `GET /api/patients/{id}/stats/` - Estatísticas do paciente
- `POST /api/patients/` - Criar paciente
- `PUT /api/patients/{id}/` - Atualizar paciente
- `DELETE /api/patients/{id}/` - Deletar paciente
- `POST /api/patients/{id}/toggle_status/` - Alternar status

### Consultas
- `GET /api/consultations/` - Listar consultas
- `GET /api/consultations/{id}/` - Detalhes da consulta
- `POST /api/consultations/` - Criar consulta
- `PUT /api/consultations/{id}/` - Atualizar consulta
- `DELETE /api/consultations/{id}/` - Deletar consulta

### Documentos
- `GET /api/documents/` - Listar documentos
- `GET /api/documents/{id}/` - Detalhes do documento
- `POST /api/documents/` - Upload de documento
- `PUT /api/documents/{id}/` - Atualizar documento
- `DELETE /api/documents/{id}/` - Deletar documento

## 🧪 Testes

Execute os testes com:

```bash
pytest
```

Para testes com cobertura:

```bash
pytest --cov=. --cov-report=html
```

## 🚀 Deploy

### Usando Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Com Docker (opcional)

```dockerfile
# Dockerfile exemplo
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🔐 Segurança

- Use HTTPS em produção
- Altere o `SECRET_KEY` em produção
- Configure `DEBUG=False` em produção
- Use variáveis de ambiente para dados sensíveis
- Mantenha as dependências atualizadas

## 📝 Comandos Úteis

```bash
# Criar novas migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Iniciar shell do Django
python manage.py shell

# Ver rotas disponíveis
python manage.py show_urls

# Limpar banco de dados
python manage.py flush
```

## 🐛 Troubleshooting

### Erro de conexão com o banco de dados

Verifique se:
- PostgreSQL está rodando
- As credenciais no `.env` estão corretas
- O banco de dados foi criado

### Erro de migração

```bash
python manage.py migrate --run-syncdb
```

### Erro de permissão

```bash
# Linux/Mac
chmod +x manage.py
```

## 📄 Licença

Este projeto está sob a licença MIT.
