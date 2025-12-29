@echo off
chcp 65001 >nul 2>&1
echo ========================================
echo Plataforma Inteligente de Atletas
echo ========================================
echo.

echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado! Instale Python 3.8+ primeiro.
    pause
    exit /b 1
)
python --version
echo OK - Python encontrado

echo.
echo [2/5] Verificando Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Node.js nao encontrado! Instale Node.js 16+ primeiro.
    pause
    exit /b 1
)
node --version
echo OK - Node.js encontrado

echo.
echo [3/5] Configurando Backend...
cd backend

echo Instalando dependencias Python...
if exist "install-deps.bat" (
    call install-deps.bat
    if errorlevel 1 (
        echo ERRO: Falha ao instalar dependencias!
        echo Tente manualmente: pip install -r requirements.txt
        cd ..
        pause
        exit /b 1
    )
) else (
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERRO: Falha ao instalar dependencias!
        echo Tente manualmente: pip install -r requirements.txt
        cd ..
        pause
        exit /b 1
    )
)
echo OK - Dependencias do backend instaladas

echo Inicializando banco de dados...
python init_db.py
if errorlevel 1 (
    echo ERRO: Falha ao inicializar banco de dados!
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo [4/5] Configurando Frontend...
cd frontend
if not exist "node_modules" (
    echo Instalando dependencias Node.js (pode demorar alguns minutos)...
    call npm install
    if errorlevel 1 (
        echo ERRO: Falha ao instalar dependencias do frontend!
        cd ..
        pause
        exit /b 1
    )
) else (
    echo OK - Dependencias do frontend ja instaladas
)
cd ..

echo.
echo [5/5] Iniciando servidores...
echo.
echo ========================================
echo Servidores iniciando...
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Pressione Ctrl+C nas janelas para parar os servidores
echo.

start "Backend - FastAPI" cmd /k "cd /d %~dp0backend && echo Backend rodando em http://localhost:8000 && uvicorn main:app --reload"
timeout /t 3 /nobreak >nul

start "Frontend - React" cmd /k "cd /d %~dp0frontend && echo Frontend rodando em http://localhost:3000 && npm start"
timeout /t 8 /nobreak >nul

echo Abrindo navegador...
start http://localhost:3000

echo.
echo OK - Plataforma iniciada com sucesso!
echo OK - Navegador aberto automaticamente!
echo.
echo Para parar os servidores, feche as janelas do CMD ou pressione Ctrl+C
echo.
pause
