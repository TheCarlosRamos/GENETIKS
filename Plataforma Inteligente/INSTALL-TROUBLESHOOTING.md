# 🔧 Solução de Problemas de Instalação

## Problema: Erro ao instalar psycopg2-binary

**Sintoma:**
```
Error: pg_config executable not found.
```

**Solução:**
O `psycopg2-binary` é opcional (apenas necessário para PostgreSQL). Como usamos SQLite por padrão, você pode:

1. **Usar requirements-minimal.txt:**
```bash
cd backend
pip install -r requirements-minimal.txt
```

2. **Ou instalar manualmente sem psycopg2:**
```bash
cd backend
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv numpy python-multipart scikit-learn pandas alembic
```

## Problema: ModuleNotFoundError: No module named 'sqlalchemy'

**Sintoma:**
```
ModuleNotFoundError: No module named 'sqlalchemy'
```

**Solução:**
A instalação falhou silenciosamente. Instale manualmente:

```bash
cd backend
pip install -r requirements.txt
```

Se ainda falhar, use a versão minimalista:
```bash
pip install -r requirements-minimal.txt
```

## Problema: Erro ao instalar dependências do frontend

**Sintoma:**
```
npm ERR! ...
```

**Solução:**
```bash
cd frontend
# Limpe o cache
npm cache clean --force
# Delete node_modules se existir
rmdir /s /q node_modules
# Reinstale
npm install
```

## Problema: Python 3.13 e dependências antigas

**Sintoma:**
Erros de compatibilidade com Python 3.13

**Solução:**
Use Python 3.11 ou 3.12 (mais estável):
```bash
# Verifique sua versão
python --version

# Se for 3.13, considere usar 3.11 ou 3.12
# Ou atualize as versões no requirements.txt
```

## Instalação Manual Passo a Passo

Se os scripts automáticos falharem, faça manualmente:

### Backend:
```bash
cd backend
pip install fastapi==0.104.1
pip install uvicorn[standard]==0.24.0
pip install sqlalchemy==2.0.23
pip install pydantic==2.5.0
pip install python-dotenv==1.0.0
pip install numpy==1.24.3
pip install scikit-learn==1.3.2
pip install pandas==2.1.3
pip install python-multipart==0.0.6
pip install alembic==1.12.1

python init_db.py
```

### Frontend:
```bash
cd frontend
npm install react react-dom react-router-dom
npm install axios recharts
npm install react-scripts
```

## Verificar Instalação

### Backend:
```bash
cd backend
python -c "import fastapi; import sqlalchemy; print('OK')"
```

### Frontend:
```bash
cd frontend
npm list react
```

## Atualizar pip

Se houver problemas com pip:
```bash
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
```

