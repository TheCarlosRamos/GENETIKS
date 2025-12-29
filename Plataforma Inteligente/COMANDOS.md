# 🚀 Guia Rápido - Como Rodar a Plataforma

## ⚡ Início Rápido (2 Terminais)

### Terminal 1 - Backend (API)

```powershell
# 1. Entre na pasta do backend
cd backend

# 2. Instale as dependências Python
pip install -r requirements.txt

# 3. Inicialize o banco de dados (só precisa fazer uma vez)
python init_db.py

# 4. Inicie o servidor
uvicorn main:app --reload
```

✅ **Backend rodando em:** `http://localhost:8000`  
📚 **Documentação da API:** `http://localhost:8000/docs`

---

### Terminal 2 - Frontend (Interface Web)

```powershell
# 1. Entre na pasta do frontend
cd frontend

# 2. Instale as dependências Node.js
npm install

# 3. Inicie a aplicação
npm start
```

✅ **Frontend rodando em:** `http://localhost:3000`

---

## 📋 Passo a Passo Detalhado

### Pré-requisitos

Verifique se você tem instalado:
- **Python 3.8+**: `python --version`
- **Node.js 16+**: `node --version`
- **npm**: `npm --version`

### 1️⃣ Configurar o Backend

```powershell
# Navegue até a pasta do projeto
cd "C:\Users\User\OneDrive - unb.br\Área de Trabalho\Plataforma Inteligente"

# Entre no backend
cd backend

# Instale as dependências
pip install -r requirements.txt

# Crie e popule o banco de dados
python init_db.py
```

**Saída esperada:**
```
✅ 20 jogadores históricos inseridos com sucesso!
✅ Banco de dados inicializado!
```

### 2️⃣ Iniciar o Backend

```powershell
# Ainda na pasta backend
uvicorn main:app --reload
```

**Saída esperada:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Deixe este terminal aberto!** ⚠️

### 3️⃣ Configurar o Frontend

Abra um **NOVO TERMINAL** (mantenha o backend rodando):

```powershell
# Navegue até a pasta do projeto
cd "C:\Users\User\OneDrive - unb.br\Área de Trabalho\Plataforma Inteligente"

# Entre no frontend
cd frontend

# Instale as dependências (pode demorar alguns minutos)
npm install
```

### 4️⃣ Iniciar o Frontend

```powershell
# Ainda na pasta frontend
npm start
```

O navegador abrirá automaticamente em `http://localhost:3000`

---

## ✅ Verificação

### Backend está funcionando?
- Acesse: `http://localhost:8000/docs`
- Você deve ver a documentação interativa da API (Swagger)

### Frontend está funcionando?
- Acesse: `http://localhost:3000`
- Você deve ver a tela inicial com o menu de navegação

---

## 🎯 Primeiro Uso

1. **Cadastrar um Atleta:**
   - Clique em "Cadastrar" no menu
   - Preencha os dados
   - Ajuste as habilidades com os sliders (1-10)
   - Clique em "Cadastrar e Classificar"

2. **Ver Classificação:**
   - Clique no atleta cadastrado
   - Veja a aba "Classificação" para comparar com jogadores históricos

3. **Explorar Funcionalidades:**
   - **Dashboard**: Monitoramento de evolução
   - **Match**: Análise de compatibilidade
   - **Relatórios**: Análises detalhadas

---

## 🔧 Solução de Problemas Comuns

### Erro: "pip não é reconhecido"
```powershell
# Use python -m pip
python -m pip install -r requirements.txt
```

### Erro: "uvicorn não é reconhecido"
```powershell
# Instale o uvicorn globalmente ou use python -m
python -m uvicorn main:app --reload
```

### Erro: "npm não é reconhecido"
- Instale o Node.js: https://nodejs.org/
- Reinicie o terminal após instalar

### Erro: Porta 8000 já em uso
```powershell
# Use outra porta
uvicorn main:app --reload --port 8001
```
E atualize o arquivo `frontend/.env` (crie se não existir):
```
REACT_APP_API_URL=http://localhost:8001
```

### Erro: Porta 3000 já em uso
- O React perguntará automaticamente se deseja usar outra porta
- Apenas confirme (Y)

### Erro ao instalar dependências Python
```powershell
# Atualize o pip primeiro
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Erro ao instalar dependências Node
```powershell
# Limpe o cache e reinstale
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

---

## 📝 Comandos Úteis

### Parar os servidores
- **Backend**: Pressione `Ctrl + C` no terminal do backend
- **Frontend**: Pressione `Ctrl + C` no terminal do frontend

### Reiniciar o banco de dados
```powershell
cd backend
python init_db.py
```

### Ver logs do backend
- Os logs aparecem automaticamente no terminal onde o uvicorn está rodando

### Ver logs do frontend
- Os logs aparecem automaticamente no terminal onde o npm start está rodando

---

## 🎓 Próximos Passos

1. ✅ Backend rodando em `http://localhost:8000`
2. ✅ Frontend rodando em `http://localhost:3000`
3. 📝 Cadastre seu primeiro atleta
4. 📊 Explore as funcionalidades da plataforma

**Pronto! A plataforma está funcionando! 🎉**


