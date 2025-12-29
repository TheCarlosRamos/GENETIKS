#!/bin/bash

echo "========================================"
echo "Plataforma Inteligente de Atletas"
echo "========================================"
echo ""

echo "[1/4] Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python não encontrado! Instale Python 3.8+ primeiro."
    exit 1
fi
python3 --version

echo "[2/4] Verificando Node.js..."
if ! command -v node &> /dev/null; then
    echo "ERRO: Node.js não encontrado! Instale Node.js 16+ primeiro."
    exit 1
fi
node --version

echo ""
echo "[3/4] Configurando Backend..."
cd backend

echo "Instalando dependências Python..."
pip3 install -r requirements.txt --quiet

echo "Inicializando banco de dados..."
python3 init_db.py

echo ""
echo "[4/4] Iniciando servidores..."
echo ""
echo "========================================"
echo "IMPORTANTE: Mantenha este terminal aberto!"
echo "========================================"
echo ""
echo "Backend iniciando em http://localhost:8000"
echo "Frontend iniciando em http://localhost:3000"
echo ""
echo "Pressione Ctrl+C para parar os servidores"
echo ""

# Inicia backend em background
cd backend
uvicorn main:app --reload &
BACKEND_PID=$!

# Aguarda backend iniciar
sleep 3

# Inicia frontend
cd ../frontend
npm start &
FRONTEND_PID=$!

echo ""
echo "Servidores iniciados!"
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "Aguarde alguns segundos para o frontend carregar..."
echo ""

# Aguarda Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait


