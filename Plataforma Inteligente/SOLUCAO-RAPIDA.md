# ⚡ Solução Rápida - Erro de Compilação

## Problema: Microsoft Visual C++ 14.0 required

O `scikit-learn` está tentando compilar e precisa do Visual C++ Build Tools.

## ✅ Solução: Removemos o scikit-learn

**Boa notícia:** O scikit-learn não é usado no código! Removemos ele do requirements.txt.

## 🚀 Instalação Rápida

### Opção 1: Script Automático (Recomendado)

```powershell
cd backend
.\install-deps.bat
```

### Opção 2: Manual

```powershell
cd backend

# Instale as dependências uma por uma
pip install fastapi==0.104.1
pip install "uvicorn[standard]==0.24.0"
pip install sqlalchemy==2.0.23
pip install pydantic==2.5.0 pydantic-settings==2.1.0
pip install python-dotenv==1.0.0
pip install numpy
pip install pandas
pip install python-multipart==0.0.6
pip install alembic==1.12.1

# Verifique
python -c "import fastapi; import sqlalchemy; import numpy; print('OK!')"
```

### Opção 3: Requirements Atualizado

```powershell
cd backend
pip install -r requirements.txt
```

Agora o requirements.txt não tem mais scikit-learn!

## ✅ Depois de Instalar

```powershell
# Inicialize o banco
python init_db.py

# Inicie o servidor
uvicorn main:app --reload
```

## 🔍 Verificar se Funcionou

```powershell
python -c "from app.database import engine; print('Banco OK!')"
```

Se não der erro, está funcionando! 🎉

