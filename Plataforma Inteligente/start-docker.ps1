# Script para iniciar a aplicação com Docker Compose
# Uso: .\start-docker.ps1 [--build]

param (
    [switch]$build = $false
)

# Verifica se o Docker está instalado
try {
    $dockerVersion = docker --version
    Write-Host "Docker encontrado: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "Erro: Docker não encontrado. Por favor, instale o Docker antes de continuar." -ForegroundColor Red
    exit 1
}

# Verifica se o Docker Compose está disponível
try {
    $composeVersion = docker-compose --version
    Write-Host "Docker Compose encontrado: $composeVersion" -ForegroundColor Green
} catch {
    # Tenta com o novo comando docker compose (com espaço)
    try {
        $composeVersion = docker compose version
        Write-Host "Docker Compose (novo formato) encontrado: $composeVersion" -ForegroundColor Green
    } catch {
        Write-Host "Erro: Docker Compose não encontrado. Por favor, instale o Docker Compose antes de continuar." -ForegroundColor Red
        exit 1
    }
}

# Verifica se o parâmetro --build foi passado
$buildFlag = ""
if ($build) {
    $buildFlag = "--build"
    Write-Host "Modo de reconstrução ativado. Os containers serão reconstruídos." -ForegroundColor Yellow
}

# Navega até o diretório do script
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptPath

# Inicia os serviços com Docker Compose
Write-Host "Iniciando os serviços com Docker Compose..." -ForegroundColor Cyan

try {
    # Tenta usar o comando docker-compose
    docker-compose -f docker-compose.yml up -d $buildFlag
} catch {
    # Se falhar, tenta com o novo comando docker compose (com espaço)
    try {
        docker compose -f docker-compose.yml up -d $buildFlag
    } catch {
        Write-Host "Erro ao iniciar os serviços com Docker Compose." -ForegroundColor Red
        Write-Host "Erro detalhado: $_" -ForegroundColor Red
        exit 1
    }
}

# Mostra os containers em execução
Write-Host "`nContainers em execução:" -ForegroundColor Green
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Mostra as URLs de acesso
Write-Host "`nAplicação disponível em:" -ForegroundColor Green
Write-Host "- Frontend: http://localhost:8080" -ForegroundColor Cyan
Write-Host "- Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "- Backend Docs: http://localhost:8000/docs" -ForegroundColor Cyan

Write-Host "`nPara parar os containers, execute: docker-compose down" -ForegroundColor Yellow
