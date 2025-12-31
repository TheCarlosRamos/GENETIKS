# Guia de Deploy no Railway - Backend GENETIKS

## Passo a Passo

### 1. Criar Conta no Railway

1. Acesse [railway.app](https://railway.app)
2. Clique em "Start a New Project"
3. Faça login com sua conta GitHub

### 2. Conectar o Repositório

1. Clique em "New Project"
2. Selecione "Deploy from GitHub repo"
3. Autorize o Railway a acessar seus repositórios
4. Selecione o repositório `TheCarlosRamos/GENETIKS`

### 3. Configurar o Serviço

1. Após o Railway detectar o repositório, clique no serviço criado
2. Vá em **Settings**
3. Configure o **Root Directory**: `Plataforma Inteligente/backend`
4. O Railway detectará automaticamente que é um projeto Python e usará o Dockerfile
5. **Importante**: Certifique-se de que o Root Directory está configurado corretamente, caso contrário o build falhará

### 4. Configurar Variáveis de Ambiente (Opcional)

No Railway, vá em **Variables** e adicione:

- **CORS_ORIGINS** (opcional): `https://genetiks.vercel.app,https://genetiks-git-main-thecarlosramos.vercel.app`
  - Isso restringe o CORS apenas para seu frontend
  - Se não configurar, aceitará requisições de qualquer origem

### 5. Deploy Automático

O Railway fará o deploy automaticamente. Você verá:
- Build logs
- Deploy logs
- URL do serviço (ex: `https://genetiks-backend-production.up.railway.app`)

### 6. Verificar se está Funcionando

1. Acesse a URL do Railway: `https://sua-url.railway.app/health`
   - Deve retornar: `{"status": "healthy"}`

2. Acesse a documentação: `https://sua-url.railway.app/docs`
   - Deve mostrar a interface Swagger do FastAPI

### 7. Configurar no Vercel

Após obter a URL do Railway:

1. Acesse o painel do Vercel
2. Vá em **Settings** → **Environment Variables**
3. Adicione:
   - **Name**: `REACT_APP_API_URL`
   - **Value**: `https://sua-url.railway.app` (URL completa do Railway)
   - **Environments**: Marque todas (Production, Preview, Development)
4. Salve e faça um novo deploy

### 8. Testar a Aplicação Completa

1. Acesse seu frontend no Vercel
2. Tente cadastrar um atleta
3. Deve funcionar sem erros de conexão!

## Troubleshooting

### Erro: "Module not found"
- Verifique se o `requirements.txt` está completo
- Verifique os logs de build no Railway

### Erro: "Port already in use"
- O Railway gerencia a porta automaticamente via variável `PORT`
- Não precisa configurar manualmente

### Banco de dados não inicializa
- O código inicializa automaticamente na primeira execução
- Verifique os logs no Railway para ver se há erros

### CORS ainda bloqueando
- Configure a variável `CORS_ORIGINS` no Railway com o domínio do Vercel
- Ou deixe como `["*"]` temporariamente para testes

## Estrutura de Arquivos Criados

- `railway.json` - Configuração do Railway
- `runtime.txt` - Versão do Python
- `main.py` - Atualizado para usar PORT do Railway e inicializar BD automaticamente

## Próximos Passos

Após o deploy bem-sucedido:
1. ✅ Backend rodando no Railway
2. ✅ Frontend configurado no Vercel com `REACT_APP_API_URL`
3. ✅ Aplicação completa funcionando!

