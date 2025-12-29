# 🔧 Solução: ERR_CONNECTION_REFUSED

## Problema

O navegador não consegue conectar ao localhost porque os servidores não estão rodando.

## ✅ Solução Passo a Passo

### 1. Verificar se os Servidores Estão Rodando

Execute:
```powershell
.\VERIFICAR-SERVIDORES.bat
```

Ou verifique manualmente:
```powershell
netstat -an | findstr ":8000"  # Backend
netstat -an | findstr ":3000"  # Frontend
```

### 2. Iniciar os Servidores Manualmente

**Terminal 1 - Backend:**
```powershell
cd backend

# Primeiro, inicialize o banco (só precisa fazer uma vez)
python init_db.py

# Depois, inicie o servidor
uvicorn main:app --reload
```

Você deve ver:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Terminal 2 - Frontend:**
```powershell
cd frontend

# Se ainda não instalou as dependências
npm install

# Inicie o servidor
npm start
```

Você deve ver:
```
Compiled successfully!
You can now view ... in the browser.
  Local:            http://localhost:3000
```

### 3. Aguardar os Servidores Iniciarem

- **Backend**: Aguarde 5-10 segundos após ver "Application startup complete"
- **Frontend**: Aguarde até ver "Compiled successfully!" (pode demorar 30-60 segundos na primeira vez)

### 4. Acessar no Navegador

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000/docs

## 🚀 Script Automático

Se preferir, use o script que abre tudo automaticamente:

```powershell
.\INICIAR-MANUAL.bat
```

Este script:
- Inicializa o banco de dados
- Abre o backend em uma janela
- Abre o frontend em outra janela
- Abre o navegador automaticamente

## ⚠️ Problemas Comuns

### Porta já em uso

Se a porta 8000 ou 3000 estiver em uso:

**Backend (porta diferente):**
```powershell
uvicorn main:app --reload --port 8001
```

**Frontend:**
O React perguntará automaticamente se deseja usar outra porta.

### Erro ao inicializar banco

```powershell
cd backend
python init_db.py
```

Se der erro, verifique se todas as dependências estão instaladas:
```powershell
python -c "import sqlalchemy; import fastapi; print('OK')"
```

### Frontend não compila

```powershell
cd frontend
rmdir /s /q node_modules
npm install
npm start
```

## ✅ Checklist

- [ ] Backend rodando na porta 8000
- [ ] Frontend rodando na porta 3000
- [ ] Banco de dados inicializado
- [ ] Aguardou tempo suficiente para os servidores iniciarem
- [ ] Navegador acessando http://localhost:3000

## 🆘 Ainda não funciona?

1. Verifique as janelas do CMD para ver erros
2. Certifique-se de que não há firewall bloqueando
3. Tente acessar http://localhost:8000/docs diretamente (backend)
4. Verifique se o antivírus não está bloqueando

