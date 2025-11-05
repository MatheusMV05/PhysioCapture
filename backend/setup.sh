#!/bin/bash

echo "🚀 Iniciando setup do backend PhysioCapture..."

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Criar ambiente virtual
echo -e "${YELLOW}📦 Criando ambiente virtual...${NC}"
python3 -m venv venv

# Ativar ambiente virtual
echo -e "${YELLOW}🔧 Ativando ambiente virtual...${NC}"
source venv/bin/activate

# Instalar dependências
echo -e "${YELLOW}📥 Instalando dependências...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# Copiar .env.example para .env se não existir
if [ ! -f .env ]; then
    echo -e "${YELLOW}📝 Criando arquivo .env...${NC}"
    cp .env.example .env
    echo -e "${GREEN}✅ Arquivo .env criado! Edite com suas configurações.${NC}"
fi

# Criar diretório de logs
mkdir -p logs

# Executar migrações
echo -e "${YELLOW}🗄️  Executando migrações...${NC}"
python manage.py makemigrations
python manage.py migrate

# Coletar arquivos estáticos
echo -e "${YELLOW}📦 Coletando arquivos estáticos...${NC}"
python manage.py collectstatic --noinput

echo -e "${GREEN}✅ Setup concluído com sucesso!${NC}"
echo -e "${YELLOW}Para criar um superusuário, execute: python manage.py createsuperuser${NC}"
echo -e "${YELLOW}Para iniciar o servidor, execute: python manage.py runserver${NC}"
