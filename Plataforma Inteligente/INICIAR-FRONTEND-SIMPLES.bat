@echo off
cd /d "%~dp0frontend"
if not exist "node_modules" (
    echo Instalando dependencias...
    call npm install
)
echo Iniciando frontend...
call npm start

