#!/bin/bash

echo "🏥 PhysioCapture - Instalação Completa"
echo "======================================"
echo ""

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Função para verificar se comando existe
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Verificar pré-requisitos
echo "🔍 Verificando pré-requisitos..."

if ! command_exists python3; then
    echo -e "${RED}❌ Python 3 não encontrado. Instale Python 3.11+${NC}"
    exit 1
fi

if ! command_exists node; then
    echo -e "${RED}❌ Node.js não encontrado. Instale Node.js 18+${NC}"
    exit 1
fi

if ! command_exists psql; then
    echo -e "${YELLOW}⚠️  PostgreSQL não encontrado. Certifique-se de instalar PostgreSQL 15+${NC}"
fi

echo -e "${GREEN}✅ Pré-requisitos OK${NC}"
echo ""

# Instalar Backend
echo "📦 Instalando Backend Django..."
cd backend

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# Copiar .env
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${YELLOW}⚠️  Arquivo .env criado. Configure as variáveis antes de prosseguir.${NC}"
fi

# Criar diretório de logs
mkdir -p logs

echo -e "${GREEN}✅ Backend instalado${NC}"
echo ""

# Instalar Frontend
echo "📦 Instalando Frontend Next.js..."
cd ../frontend

npm install

# Copiar .env
if [ ! -f .env ]; then
    cp .env.example .env
fi

echo -e "${GREEN}✅ Frontend instalado${NC}"
echo ""

# Instruções finais
echo "======================================"
echo -e "${GREEN}✅ Instalação concluída!${NC}"
echo ""
echo "📝 Próximos passos:"
echo ""
echo "1. Configure o PostgreSQL:"
echo "   CREATE DATABASE physiocapture;"
echo "   CREATE USER postgres WITH PASSWORD 'postgres';"
echo "   GRANT ALL PRIVILEGES ON DATABASE physiocapture TO postgres;"
echo ""
echo "2. Configure os arquivos .env em backend/ e frontend/"
echo ""
echo "3. Execute as migrações do backend:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python manage.py migrate"
echo "   python manage.py createsuperuser"
echo ""
echo "4. Inicie os servidores:"
echo "   Backend:  cd backend && python manage.py runserver"
echo "   Frontend: cd frontend && npm run dev"
echo ""
echo "🌐 URLs:"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   Admin:    http://localhost:8000/admin"
echo ""
