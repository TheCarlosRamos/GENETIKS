@echo off
echo ========================================
echo Iniciando Plataforma - Modo Manual
echo ========================================
echo.

echo IMPORTANTE: Este script abrira 2 janelas separadas
echo Uma para o backend e outra para o frontend
echo.
echo Mantenha ambas as janelas abertas!
echo.
pause

echo.
echo [1/2] Inicializando banco de dados...
cd backend
if not exist "athlete_platform.db" (
    echo Criando banco de dados...
    python init_db.py
    if errorlevel 1 (
        echo ERRO ao criar banco de dados!
        cd ..
        pause
        exit /b 1
    )
) else (
    echo Banco de dados ja existe
)
cd ..

echo.
echo [2/2] Abrindo servidores em janelas separadas...
echo.

echo Abrindo Backend (aguarde alguns segundos)...
start "Backend - Porta 8000" cmd /k "cd /d %~dp0backend && echo ======================================== && echo BACKEND - Porta 8000 && echo ======================================== && echo. && echo Aguarde alguns segundos para iniciar... && echo. && uvicorn main:app --reload --host 0.0.0.0"

timeout /t 5 /nobreak >nul

echo Abrindo Frontend (aguarde alguns segundos)...
start "Frontend - Porta 3000" cmd /k "cd /d %~dp0frontend && echo ======================================== && echo FRONTEND - Porta 3000 && echo ======================================== && echo. && echo Aguarde alguns segundos para iniciar... && echo. && npm start"

timeout /t 10 /nobreak >nul

echo.
echo Abrindo navegador...
start http://localhost:3000

echo.
echo ========================================
echo Servidores iniciados!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo IMPORTANTE:
echo - Mantenha as 2 janelas do CMD abertas
echo - Aguarde alguns segundos para os servidores iniciarem
echo - Se der erro, verifique as janelas do CMD
echo.
pause

