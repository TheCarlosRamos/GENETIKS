from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Athlete(Base):
    __tablename__ = "athletes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    nationality = Column(String)
    height = Column(Float)  # em cm
    weight = Column(Float)  # em kg
    body_type = Column(String)  # Ectomorfo, Mesomorfo, Endomorfo
    dominant_foot = Column(String)  # Destro, Canhoto, Ambidestro
    primary_position = Column(String)
    secondary_position = Column(String)
    
    # Habilidades técnicas (1-10)
    technical_skills = Column(JSON)  # Dict com habilidades e valores
    
    # Deficiencias/Áreas de melhoria
    deficiencies = Column(JSON)  # Lista de strings
    
    # Classificação e recomendações
    classification_data = Column(JSON)  # Resultado da classificação
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relacionamentos
    performance_records = relationship("PerformanceRecord", back_populates="athlete")
    training_recommendations = relationship("TrainingRecommendation", back_populates="athlete")

class PerformanceRecord(Base):
    __tablename__ = "performance_records"
    
    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"))
    record_date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Habilidades no momento do registro
    technical_skills = Column(JSON)
    physical_metrics = Column(JSON)  # VO2 máx, força, etc.
    
    athlete = relationship("Athlete", back_populates="performance_records")

class TrainingRecommendation(Base):
    __tablename__ = "training_recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer, ForeignKey("athletes.id"))
    deficiency = Column(String)
    exercises = Column(JSON)  # Lista de exercícios
    drills = Column(JSON)  # Lista de drills
    reference_players = Column(JSON)  # Lista de jogadores de referência
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    athlete = relationship("Athlete", back_populates="training_recommendations")

