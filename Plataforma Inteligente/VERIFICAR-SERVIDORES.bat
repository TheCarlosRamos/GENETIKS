@echo off
echo ========================================
echo Verificando Status dos Servidores
echo ========================================
echo.

echo [1/3] Verificando Backend (porta 8000)...
netstat -an | findstr ":8000" >nul
if errorlevel 1 (
    echo ERRO: Backend nao esta rodando na porta 8000
    echo.
    echo Para iniciar o backend:
    echo   cd backend
    echo   uvicorn main:app --reload
) else (
    echo OK - Backend esta rodando na porta 8000
)

echo.
echo [2/3] Verificando Frontend (porta 3000)...
netstat -an | findstr ":3000" >nul
if errorlevel 1 (
    echo ERRO: Frontend nao esta rodando na porta 3000
    echo.
    echo Para iniciar o frontend:
    echo   cd frontend
    echo   npm start
) else (
    echo OK - Frontend esta rodando na porta 3000
)

echo.
echo [3/3] Testando conexao...
curl http://localhost:8000/docs >nul 2>&1
if errorlevel 1 (
    echo AVISO: Nao foi possivel conectar ao backend
) else (
    echo OK - Backend respondendo
)

echo.
echo ========================================
echo Diagnostico concluido
echo ========================================
echo.
pause

