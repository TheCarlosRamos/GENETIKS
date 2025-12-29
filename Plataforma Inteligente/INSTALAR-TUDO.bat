@echo off
echo ========================================
echo Instalacao Completa da Plataforma
echo ========================================
echo.

echo [1/3] Instalando Backend...
cd backend
if not exist "requirements.txt" (
    echo ERRO: Arquivo requirements.txt nao encontrado!
    echo Certifique-se de estar na pasta correta.
    pause
    exit /b 1
)

echo Instalando dependencias Python...
echo Atualizando pip primeiro...
python -m pip install --upgrade pip

echo Instalando pacotes...
pip install fastapi==0.104.1
pip install "uvicorn[standard]==0.24.0"
pip install "sqlalchemy>=2.0.25"
pip install pydantic==2.5.0
pip install pydantic-settings==2.1.0
pip install python-dotenv==1.0.0
pip install numpy
pip install pandas
pip install python-multipart==0.0.6
pip install "alembic>=1.13.0"

echo.
echo Verificando instalacao...
python test-install.py
if errorlevel 1 (
    echo.
    echo AVISO: Algumas dependencias podem estar faltando.
    echo Tentando continuar mesmo assim...
    echo.
)

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
echo [2/3] Instalando Frontend...
cd frontend
if not exist "package.json" (
    echo ERRO: Arquivo package.json nao encontrado!
    cd ..
    pause
    exit /b 1
)

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
    echo Dependencias do frontend ja instaladas
)
cd ..

echo.
echo [3/3] Iniciando servidores...
echo.
echo ========================================
echo Instalacao concluida!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Iniciando servidores...
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

