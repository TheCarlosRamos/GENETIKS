@echo off
echo ========================================
echo Plataforma Inteligente de Atletas
echo ========================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    pause
    exit /b 1
)

echo Verificando Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Node.js nao encontrado!
    pause
    exit /b 1
)

echo.
echo Configurando Backend...
cd backend
pip install -r requirements.txt --quiet
python init_db.py
cd ..

echo.
echo Configurando Frontend...
cd frontend
if not exist "node_modules" (
    echo Instalando dependencias (aguarde)...
    call npm install
)
cd ..

echo.
echo Iniciando servidores...
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.

start "Backend" cmd /k "cd /d %~dp0backend && uvicorn main:app --reload"
timeout /t 3 /nobreak >nul

start "Frontend" cmd /k "cd /d %~dp0frontend && npm start"
timeout /t 8 /nobreak >nul

start http://localhost:3000

echo.
echo Pronto! Navegador aberto.
echo.
pause

