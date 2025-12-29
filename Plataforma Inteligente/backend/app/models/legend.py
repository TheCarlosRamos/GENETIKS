from sqlalchemy import Column, Integer, String, Float, JSON
from app.database import Base

class Legend(Base):
    __tablename__ = "legends"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    nationality = Column(String)
    position = Column(String)
    height = Column(Float)
    weight = Column(Float)
    body_type = Column(String)
    dominant_foot = Column(String)
    
    # Perfil de habilidades (1-10)
    technical_profile = Column(JSON)
    
    # Características distintivas
    distinctive_traits = Column(JSON)  # Lista de características
    playing_style = Column(String)
    era = Column(String)  # Década/era em que jogou
    
    # Metadados
    description = Column(String)

