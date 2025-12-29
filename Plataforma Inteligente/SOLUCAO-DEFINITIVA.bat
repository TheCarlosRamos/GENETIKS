@echo off
echo ========================================
echo Solucao Definitiva - Python 3.13
echo ========================================
echo.

echo Python 3.13 e muito novo e tem problemas com algumas bibliotecas.
echo Vamos instalar versoes compativeis...
echo.

cd backend

echo [1/4] Atualizando pip...
python -m pip install --upgrade pip setuptools wheel

echo.
echo [2/4] Desinstalando SQLAlchemy antigo...
pip uninstall sqlalchemy alembic -y

echo.
echo [3/4] Instalando versoes compativeis...
pip install "sqlalchemy>=2.0.25"
pip install "alembic>=1.13.0"

echo.
echo [4/4] Instalando outras dependencias...
pip install fastapi==0.104.1
pip install "uvicorn[standard]==0.24.0"
pip install pydantic==2.5.0
pip install pydantic-settings==2.1.0
pip install python-dotenv==1.0.0
pip install numpy
pip install pandas
pip install python-multipart==0.0.6

echo.
echo Testando...
python -c "import fastapi; print('FastAPI OK')" 2>nul
python -c "import sqlalchemy; print('SQLAlchemy versao:', sqlalchemy.__version__)" 2>nul
python -c "import numpy; print('NumPy OK')" 2>nul

echo.
echo Se nao houver erros acima, tente inicializar o banco:
echo   python init_db.py
echo.
pause

