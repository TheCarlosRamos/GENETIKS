.PHONY: help install backend frontend run stop clean

help:
	@echo "========================================"
	@echo "Plataforma Inteligente de Atletas"
	@echo "========================================"
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make install    - Instala todas as dependências"
	@echo "  make backend    - Inicia apenas o backend"
	@echo "  make frontend   - Inicia apenas o frontend"
	@echo "  make run        - Inicia backend e frontend"
	@echo "  make init-db    - Inicializa o banco de dados"
	@echo "  make clean      - Limpa arquivos temporários"
	@echo ""

install:
	@echo "📦 Instalando dependências..."
	@echo "Backend..."
	cd backend && pip install -r requirements.txt
	@echo "Frontend..."
	cd frontend && npm install
	@echo "✅ Dependências instaladas!"

init-db:
	@echo "🗄️  Inicializando banco de dados..."
	cd backend && python init_db.py
	@echo "✅ Banco de dados inicializado!"

backend:
	@echo "🚀 Iniciando backend..."
	cd backend && uvicorn main:app --reload

frontend:
	@echo "🚀 Iniciando frontend..."
	cd frontend && npm start

run: init-db
	@echo "🚀 Iniciando plataforma completa..."
	@echo ""
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:3000"
	@echo ""
	@echo "Pressione Ctrl+C para parar"
	@echo ""
ifeq ($(OS),Windows_NT)
	@start cmd /k "cd backend && uvicorn main:app --reload"
	@timeout /t 3 /nobreak >nul
	@start cmd /k "cd frontend && npm start"
	@timeout /t 5 /nobreak >nul
	@start http://localhost:3000
	@echo "✅ Plataforma iniciada! Navegador aberto."
else
	@cd backend && uvicorn main:app --reload &
	@sleep 3
	@cd frontend && npm start &
	@sleep 5
	@xdg-open http://localhost:3000 2>/dev/null || open http://localhost:3000 2>/dev/null || echo "Abra http://localhost:3000 no navegador"
	@echo "✅ Plataforma iniciada!"
	@echo "Pressione Ctrl+C para parar"
	@wait
endif

clean:
	@echo "🧹 Limpando arquivos temporários..."
	@rmdir /s /q backend\__pycache__ 2>nul || true
	@rmdir /s /q backend\*.pyc 2>nul || true
	@rmdir /s /q frontend\node_modules 2>nul || true
	@echo "✅ Limpeza concluída!"

