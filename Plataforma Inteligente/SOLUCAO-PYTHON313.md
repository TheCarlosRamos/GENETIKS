# 🔧 Solução: Python 3.13 e SQLAlchemy

## Problema

Python 3.13 tem incompatibilidade com SQLAlchemy 2.0.23.

**Erro:**
```
AssertionError: Class <class 'sqlalchemy.sql.elements.SQLCoreOperations'> directly inherits TypingOnly...
```

## ✅ Solução Rápida

Execute:
```powershell
.\CORRIGIR-SQLALCHEMY.bat
```

Ou manualmente:
```powershell
pip install --upgrade sqlalchemy alembic
```

## 🔄 Solução Completa

Atualize o SQLAlchemy para versão mais recente:

```powershell
cd backend

# Atualize pip primeiro
python -m pip install --upgrade pip

# Instale/atualize SQLAlchemy
pip install --upgrade sqlalchemy alembic

# Instale outras dependências
pip install fastapi==0.104.1
pip install "uvicorn[standard]==0.24.0"
pip install pydantic==2.5.0 pydantic-settings==2.1.0
pip install python-dotenv==1.0.0
pip install numpy pandas
pip install python-multipart==0.0.6
```

## ✅ Verificar

```powershell
python -c "import sqlalchemy; print('SQLAlchemy:', sqlalchemy.__version__)"
python -c "import fastapi; import sqlalchemy; import numpy; print('Tudo OK!')"
```

## 📝 Nota

O `requirements.txt` foi atualizado para usar `sqlalchemy>=2.0.25` que é compatível com Python 3.13.

