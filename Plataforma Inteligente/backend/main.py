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

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


