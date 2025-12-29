from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api import athletes, training, match, reports

# Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Plataforma Inteligente de Classificação de Atletas",
    description="Sistema completo para classificação, monitoramento e desenvolvimento de atletas de futebol",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080", "http://localhost:80", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Registra rotas
app.include_router(athletes.router)
app.include_router(training.router)
app.include_router(match.router)
app.include_router(reports.router)

@app.get("/")
def root():
    return {
        "message": "Plataforma Inteligente de Classificação de Atletas API",
        "version": "1.0.0",
        "endpoints": {
            "athletes": "/athletes",
            "training": "/training",
            "match": "/match",
            "reports": "/reports"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


