"""
Script para inicializar o banco de dados com dados de referência
"""
from app.database import engine, Base, SessionLocal
from app.models.legend import Legend
from app.services.legend_database import LEGEND_DATABASE

def init_database():
    """Cria tabelas e popula com dados de referência"""
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Verifica se já existem dados
        existing_count = db.query(Legend).count()
        if existing_count > 0:
            print(f"Banco de dados já possui {existing_count} jogadores históricos.")
            return
        
        # Insere jogadores históricos
        for legend_data in LEGEND_DATABASE:
            legend = Legend(
                name=legend_data["name"],
                nationality=legend_data.get("nationality"),
                position=legend_data.get("position"),
                height=legend_data.get("height"),
                weight=legend_data.get("weight"),
                body_type=legend_data.get("body_type"),
                dominant_foot=legend_data.get("dominant_foot"),
                technical_profile=legend_data.get("technical_profile", {}),
                distinctive_traits=legend_data.get("distinctive_traits", []),
                playing_style=legend_data.get("playing_style"),
                era=legend_data.get("era"),
                description=legend_data.get("description", "")
            )
            db.add(legend)
        
        db.commit()
        print(f"✅ {len(LEGEND_DATABASE)} jogadores históricos inseridos com sucesso!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao inicializar banco de dados: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Inicializando banco de dados...")
    init_database()
    print("✅ Banco de dados inicializado!")


