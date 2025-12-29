# Script PowerShell para iniciar a plataforma completa
# Uso: .\run.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Plataforma Inteligente de Atletas" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica Python
Write-Host "[1/5] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERRO: Python não encontrado!" -ForegroundColor Red
    Write-Host "Instale Python 3.8+ de https://www.python.org/" -ForegroundColor Red
    exit 1
}

# Verifica Node.js
Write-Host "[2/5] Verificando Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version
    Write-Host "✅ Node.js $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERRO: Node.js não encontrado!" -ForegroundColor Red
    Write-Host "Instale Node.js 16+ de https://nodejs.org/" -ForegroundColor Red
    exit 1
}

# Instala dependências do backend
Write-Host "[3/5] Instalando dependências do backend..." -ForegroundColor Yellow
Set-Location backend
$pipResult = & pip install -r requirements.txt 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ ERRO: Falha ao instalar dependências do backend!" -ForegroundColor Red
    Write-Host "Tente manualmente: pip install -r requirements.txt" -ForegroundColor Yellow
    Set-Location ..
    exit 1
}
Write-Host "✅ Dependências do backend instaladas!" -ForegroundColor Green

# Inicializa banco de dados
Write-Host "[4/5] Inicializando banco de dados..." -ForegroundColor Yellow
$dbResult = & python init_db.py 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ ERRO: Falha ao inicializar banco de dados!" -ForegroundColor Red
    Set-Location ..
    exit 1
}
Write-Host "✅ Banco de dados inicializado!" -ForegroundColor Green

Set-Location ..

# Instala dependências do frontend
Write-Host "[5/5] Instalando dependências do frontend..." -ForegroundColor Yellow
Set-Location frontend
if (-not (Test-Path "node_modules")) {
    Write-Host "Instalando pacotes npm (pode demorar alguns minutos)..." -ForegroundColor Yellow
    npm install
    Write-Host "✅ Dependências do frontend instaladas!" -ForegroundColor Green
} else {
    Write-Host "✅ Dependências do frontend já instaladas!" -ForegroundColor Green
}
Set-Location ..

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🚀 Iniciando servidores..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Green
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Green
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""
Write-Host "Pressione Ctrl+C para parar os servidores" -ForegroundColor Yellow
Write-Host ""

# Inicia backend em nova janela
Write-Host "Iniciando backend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\backend'; Write-Host 'Backend rodando em http://localhost:8000' -ForegroundColor Green; uvicorn main:app --reload"

# Aguarda backend iniciar
Start-Sleep -Seconds 3

# Inicia frontend em nova janela
Write-Host "Iniciando frontend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\frontend'; Write-Host 'Frontend rodando em http://localhost:3000' -ForegroundColor Green; npm start"

# Aguarda frontend iniciar
Start-Sleep -Seconds 8

# Abre navegador
Write-Host "Abrindo navegador..." -ForegroundColor Yellow
Start-Process "http://localhost:3000"

Write-Host ""
Write-Host "✅ Plataforma iniciada com sucesso!" -ForegroundColor Green
Write-Host "✅ Navegador aberto automaticamente!" -ForegroundColor Green
Write-Host ""
Write-Host "Para parar os servidores, feche as janelas do PowerShell ou pressione Ctrl+C" -ForegroundColor Yellow
Write-Host ""


