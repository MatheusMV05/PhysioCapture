# 🚀 PhysioCapture - Guia de Início Rápido

## ⚡ Instalação Rápida (5 minutos)

### Pré-requisitos Obrigatórios
- ✅ Python 3.11+
- ✅ Node.js 18+
- ✅ PostgreSQL 15+

### Passo 1: Configurar Banco de Dados (1 min)

```sql
-- Abra o PostgreSQL e execute:
CREATE DATABASE physiocapture;
CREATE USER postgres WITH PASSWORD 'capture123';
GRANT ALL PRIVILEGES ON DATABASE physiocapture TO postgres;
```

### Passo 2: Instalar e Rodar Backend (2 min)

```bash
cd backend

# Criar ambiente virtual e instalar
python -m venv venv

# Ativar ambiente virtual:
# Linux/Mac:
source venv/bin/activate
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat

pip install -r requirements.txt

# Configurar ambiente
cp .env.example .env
# Edite .env se necessário (os valores padrão já funcionam)

# Migrar banco e criar admin
python manage.py migrate
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver
```

✅ Backend rodando em: **http://localhost:8000**

### Passo 3: Instalar e Rodar Frontend (2 min)

```bash
# Em outro terminal:
cd frontend

# Instalar dependências
npm install

# Configurar ambiente
cp .env.example .env

# Rodar servidor
npm run dev
```

✅ Frontend rodando em: **http://localhost:3000**

---

## 🎯 URLs Importantes

| Serviço | URL |
|---------|-----|
| 🌐 Frontend | http://localhost:3000 |
| 🔌 API Backend | http://localhost:8000/api |
| 👤 Admin Django | http://localhost:8000/admin |
| 📋 Health Check | http://localhost:8000/api/health/ |

---

## 🔑 Primeiro Acesso

1. Acesse http://localhost:8000/admin
2. Faça login com o superusuário criado
3. Crie uma clínica
4. Crie um usuário vinculado à clínica
5. Acesse http://localhost:3000 e faça login

---

## 📝 Credenciais de Teste

### Superusuário Django Admin
- Email: (o que você criou no `createsuperuser`)
- Senha: (a que você definiu)

### Usuário do Sistema
Crie através do Admin Django em `/admin`

---

## 🧪 Testar a API

### Health Check
```bash
curl http://localhost:8000/api/health/
```

### Login
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"seu@email.com","password":"suasenha"}'
```

### Listar Pacientes (com token)
```bash
curl http://localhost:8000/api/patients/ \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

---

## 🔧 Comandos Úteis

### Backend
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Shell interativo
python manage.py shell

# Rodar testes
pytest
```

### Frontend
```bash
# Desenvolvimento
npm run dev

# Build de produção
npm run build

# Rodar build
npm start

# Lint
npm run lint
```

---

## 🐛 Problemas Comuns

### Erro de conexão com PostgreSQL
```bash
# Verifique se o PostgreSQL está rodando:
sudo systemctl status postgresql  # Linux
brew services list                 # Mac
# Services no Windows
```

### Porta 8000 já em uso
```bash
# Mate o processo na porta 8000:
lsof -ti:8000 | xargs kill -9     # Mac/Linux
# Use o Gerenciador de Tarefas no Windows
```

### Erro de migração
```bash
# Force a migração:
python manage.py migrate --run-syncdb
```

### Erro de dependências Node
```bash
# Limpe o cache e reinstale:
rm -rf node_modules package-lock.json
npm install
```

---

## 📚 Próximos Passos

1. ✅ Explore o Admin Django: http://localhost:8000/admin
2. ✅ Crie uma clínica de teste
3. ✅ Adicione usuários
4. ✅ Cadastre pacientes
5. ✅ Registre consultas
6. ✅ Faça upload de documentos

---

## 📖 Documentação Completa

- `README.md` - Documentação principal
- `ESTRUTURA_COMPLETA.md` - Estrutura detalhada do projeto
- `backend/README.md` - Documentação do backend
- `frontend/README.md` - Documentação do frontend

---

## 🆘 Ajuda

Se encontrar problemas:

1. Verifique os logs do console
2. Consulte a documentação completa
3. Revise as variáveis de ambiente (.env)
4. Certifique-se de que todos os serviços estão rodando

---

## 🎉 Pronto!

Seu sistema PhysioCapture está rodando!

Acesse: **http://localhost:3000** 🏥
