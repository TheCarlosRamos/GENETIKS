@echo off
echo ========================================
echo Iniciando Frontend
echo ========================================
echo.

cd /d "%~dp0frontend"
if errorlevel 1 (
    echo ERRO: Pasta frontend nao encontrada!
    pause
    exit /b 1
)

echo Verificando dependencias...
if not exist "node_modules" (
    echo Instalando dependencias - pode demorar alguns minutos...
    call npm install
    if errorlevel 1 (
        echo ERRO ao instalar dependencias!
        pause
        exit /b 1
    )
) else (
    echo Dependencias ja instaladas
)

echo.
echo Iniciando servidor frontend...
echo.
echo Aguarde alguns segundos para compilar...
echo O navegador abrira automaticamente quando estiver pronto.
echo.
echo Para parar, pressione Ctrl+C
echo.

npm start

