# ⚠️ Python 3.13 - Problemas Conhecidos

## Problema

Python 3.13 é muito novo e algumas bibliotecas ainda não são totalmente compatíveis, especialmente SQLAlchemy versões antigas.

## ✅ Solução Definitiva

Execute este script que corrige tudo:

```powershell
.\SOLUCAO-DEFINITIVA.bat
```

## 🔧 O que o script faz:

1. Atualiza pip, setuptools e wheel
2. Remove SQLAlchemy antigo
3. Instala SQLAlchemy >= 2.0.25 (compatível com Python 3.13)
4. Instala todas as outras dependências

## 📝 Alternativa: Usar Python 3.11 ou 3.12

Se os problemas persistirem, recomendo usar Python 3.11 ou 3.12 que são mais estáveis:

1. Instale Python 3.11 ou 3.12
2. Crie um ambiente virtual:
   ```powershell
   python3.11 -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências normalmente

## ✅ Verificar se Funcionou

```powershell
cd backend
python -c "import sqlalchemy; print('Versao:', sqlalchemy.__version__)"
python -c "from sqlalchemy import create_engine; print('OK!')"
```

Se não der erro, está funcionando!

## 🚀 Depois de Corrigir

```powershell
cd backend
python init_db.py
uvicorn main:app --reload
```

