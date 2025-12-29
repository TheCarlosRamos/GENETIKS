# ⚡ Início Rápido - 3 Passos

## 🎯 Forma Mais Rápida

### Windows:
```bash
# Duplo clique em:
start.bat

# Ou execute no terminal:
.\run.ps1
```

### Linux/Mac:
```bash
make run
```

**Pronto!** O navegador abrirá automaticamente em `http://localhost:3000`

---

## 📝 O que o script faz automaticamente:

1. ✅ Verifica Python e Node.js
2. ✅ Instala dependências do backend
3. ✅ Instala dependências do frontend
4. ✅ Inicializa banco de dados
5. ✅ Inicia backend (porta 8000)
6. ✅ Inicia frontend (porta 3000)
7. ✅ Abre navegador automaticamente

---

## 🔧 Se preferir fazer manualmente:

### Terminal 1:
```bash
cd backend
pip install -r requirements.txt
python init_db.py
uvicorn main:app --reload
```

### Terminal 2:
```bash
cd frontend
npm install
npm start
```

---

## ✅ Verificar se está funcionando:

- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000

**Pronto para usar! 🎉**


