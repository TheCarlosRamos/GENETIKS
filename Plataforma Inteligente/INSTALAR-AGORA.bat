@echo off
echo ========================================
echo Instalacao Rapida - Backend
echo ========================================
echo.

cd backend

echo Instalando dependencias (sem scikit-learn)...
echo.

pip install fastapi==0.104.1
pip install "uvicorn[standard]==0.24.0"
pip install sqlalchemy==2.0.23
pip install pydantic==2.5.0
pip install pydantic-settings==2.1.0
pip install python-dotenv==1.0.0
pip install numpy
pip install pandas
pip install python-multipart==0.0.6
pip install alembic==1.12.1

echo.
echo Verificando instalacao...
python -c "import fastapi; import sqlalchemy; import numpy; print('OK - Dependencias instaladas!')"

if errorlevel 1 (
    echo ERRO na verificacao!
    pause
    exit /b 1
)

echo.
echo Inicializando banco de dados...
python init_db.py

if errorlevel 1 (
    echo ERRO ao inicializar banco!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Backend configurado com sucesso!
echo ========================================
echo.
echo Para iniciar o servidor:
echo   uvicorn main:app --reload
echo.
pause

