from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api import athletes, training, match, reports
import os

# Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa banco de dados com dados de referência (apenas se necessário)
try:
    from app.models.legend import Legend
    from app.database import SessionLocal
    db = SessionLocal()
    legend_count = db.query(Legend).count()
    db.close()
    
    if legend_count == 0:
        # Se não há jogadores históricos, inicializa o banco
        from init_db import init_database
        init_database()
except Exception as e:
    # Se houver erro, continua mesmo assim (banco pode já estar inicializado)
    print(f"Nota: {e}")

app = FastAPI(
    title="Plataforma Inteligente de Classificação de Atletas",
    description="Sistema completo para classificação, monitoramento e desenvolvimento de atletas de futebol",
    version="1.0.0"
)

# Configuração do CORS
# Permite configurar origens via variável de ambiente, ou usa "*" para permitir todas
cors_origins_env = os.getenv("CORS_ORIGINS")
if cors_origins_env:
    cors_origins = cors_origins_env.split(",")
else:
    # Em desenvolvimento permite todas, em produção configure CORS_ORIGINS
    cors_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
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
    # Railway fornece a porta via variável de ambiente PORT
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


