@echo off
echo Instalando dependencias do backend...
echo.

echo [1/6] FastAPI...
pip install fastapi==0.104.1

echo [2/6] Uvicorn...
pip install "uvicorn[standard]==0.24.0"

echo [3/6] SQLAlchemy...
pip install sqlalchemy==2.0.23

echo [4/6] Pydantic...
pip install pydantic==2.5.0 pydantic-settings==2.1.0

echo [5/6] Outras dependencias...
pip install python-dotenv==1.0.0
pip install numpy
pip install pandas
pip install python-multipart==0.0.6
pip install alembic==1.12.1

echo.
echo [6/6] Verificando instalacao...
python -c "import fastapi; import sqlalchemy; import numpy; print('OK - Todas as dependencias instaladas!')"

echo.
echo Pronto!
pause

