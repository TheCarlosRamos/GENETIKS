# Guia de Deploy - GENETIKS

## Frontend (Vercel) ✅

O frontend já está configurado e funcionando no Vercel.

## Backend - Próximos Passos

### 1. Hospedar o Backend

Você precisa hospedar o backend FastAPI em algum serviço. Opções recomendadas:

#### Opção A: Railway (Recomendado - Mais Fácil)
1. Acesse [railway.app](https://railway.app)
2. Crie uma conta e conecte seu GitHub
3. Clique em "New Project" → "Deploy from GitHub repo"
4. Selecione o repositório `GENETIKS`
5. Configure:
   - **Root Directory**: `Plataforma Inteligente/backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Railway fornecerá uma URL como: `https://seu-projeto.railway.app`

#### Opção B: Render
1. Acesse [render.com](https://render.com)
2. Crie uma conta e conecte seu GitHub
3. Clique em "New" → "Web Service"
4. Selecione o repositório
5. Configure:
   - **Root Directory**: `Plataforma Inteligente/backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Render fornecerá uma URL como: `https://seu-projeto.onrender.com`

#### Opção C: PythonAnywhere
1. Acesse [pythonanywhere.com](https://www.pythonanywhere.com)
2. Crie uma conta gratuita
3. Faça upload dos arquivos do backend
4. Configure o WSGI file

### 2. Configurar Variável de Ambiente no Vercel

Após hospedar o backend e obter a URL:

1. Acesse o painel do Vercel
2. Vá em **Settings** → **Environment Variables**
3. Adicione uma nova variável:
   - **Name**: `REACT_APP_API_URL`
   - **Value**: `https://sua-url-do-backend.com` (URL completa do backend hospedado)
   - **Environments**: Marque todas (Production, Preview, Development)
4. Salve e faça um novo deploy

### 3. Configurar CORS no Backend (Opcional)

Se quiser restringir o CORS apenas para seu domínio do Vercel:

1. No serviço onde hospedou o backend, configure a variável de ambiente:
   - **Name**: `CORS_ORIGINS`
   - **Value**: `https://genetiks.vercel.app,https://genetiks-git-main-thecarlosramos.vercel.app`
   (adicione todos os domínios do Vercel que você usa)

### 4. Verificar se está funcionando

1. Acesse a URL do backend: `https://sua-url-do-backend.com/health`
   - Deve retornar: `{"status": "healthy"}`

2. Acesse a documentação: `https://sua-url-do-backend.com/docs`
   - Deve mostrar a interface Swagger

3. Teste o frontend no Vercel
   - Tente cadastrar um atleta
   - Deve funcionar sem erros de conexão

## Estrutura de URLs

- **Frontend**: `https://genetiks.vercel.app`
- **Backend**: `https://sua-url-do-backend.com` (você precisa configurar)

## Troubleshooting

### Erro: "Network Error" ou "Connection Refused"
- Verifique se a URL do backend está correta na variável `REACT_APP_API_URL`
- Verifique se o backend está rodando e acessível
- Verifique o CORS no backend

### Erro: "CORS policy"
- Configure a variável `CORS_ORIGINS` no backend com o domínio do Vercel
- Ou deixe como `["*"]` temporariamente para testes

### Backend não inicia
- Verifique os logs no serviço de hospedagem
- Certifique-se de que todas as dependências estão no `requirements.txt`
- Verifique se o comando de start está correto

