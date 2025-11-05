# PhysioCapture Frontend

Frontend do sistema PhysioCapture desenvolvido com Next.js 14 e TypeScript.

## 🚀 Tecnologias

- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- React Query
- Axios
- React Hook Form + Zod
- Sonner (Toast notifications)

## 📦 Instalação

```bash
npm install
# ou
yarn install
```

## ⚙️ Configuração

Crie um arquivo `.env` baseado no `.env.example`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🏃 Executando

### Desenvolvimento
```bash
npm run dev
```

### Build
```bash
npm run build
npm start
```

### Lint
```bash
npm run lint
```

## 📁 Estrutura

```
src/
├── app/              # App Router (pages)
├── components/       # Componentes React
│   ├── ui/          # Componentes UI reutilizáveis
│   └── providers/   # Providers (Query, Auth, etc)
├── lib/             # Utilitários e configurações
├── services/        # Serviços de API
├── types/           # TypeScript types
└── hooks/           # Custom hooks
```

## 🔌 Conectando ao Backend

O frontend se conecta ao backend Django através da variável `NEXT_PUBLIC_API_URL`.

Certifique-se de que o backend está rodando em `http://localhost:8000` antes de iniciar o frontend.

## 📝 Licença

MIT
