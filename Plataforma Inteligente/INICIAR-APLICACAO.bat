@echo off
echo ========================================
echo Iniciando Plataforma Inteligente
echo ========================================
echo.

echo [1/2] Inicializando banco de dados...
cd backend
python init_db.py
if errorlevel 1 (
    echo ERRO ao inicializar banco de dados!
    cd ..
    pause
    exit /b 1
)
echo OK - Banco de dados inicializado!

echo.
echo [2/2] Iniciando servidores...
echo.
echo ========================================
echo Servidores iniciando...
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Pressione Ctrl+C nas janelas para parar
echo.

cd ..
start "Backend - FastAPI" cmd /k "cd /d %~dp0backend && echo Backend rodando em http://localhost:8000 && uvicorn main:app --reload"
timeout /t 3 /nobreak >nul

start "Frontend - React" cmd /k "cd /d %~dp0frontend && echo Frontend rodando em http://localhost:3000 && npm start"
timeout /t 8 /nobreak >nul

start http://localhost:3000

echo.
echo ========================================
echo Plataforma iniciada!
echo ========================================
echo.
echo Navegador aberto automaticamente.
echo Para parar, feche as janelas do CMD.
echo.
pause

