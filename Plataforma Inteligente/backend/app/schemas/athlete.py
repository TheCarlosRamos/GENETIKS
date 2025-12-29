from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from datetime import datetime

class TechnicalSkills(BaseModel):
    velocidade: float = Field(ge=1, le=10, default=5)
    resistencia: float = Field(ge=1, le=10, default=5)
    forca: float = Field(ge=1, le=10, default=5)
    agilidade: float = Field(ge=1, le=10, default=5)
    passe: float = Field(ge=1, le=10, default=5)
    drible: float = Field(ge=1, le=10, default=5)
    finalizacao: float = Field(ge=1, le=10, default=5)
    chute: float = Field(ge=1, le=10, default=5)
    jogo_aereo: float = Field(ge=1, le=10, default=5)
    visao_de_jogo: float = Field(ge=1, le=10, default=5)
    posicionamento: float = Field(ge=1, le=10, default=5)
    marcacao: float = Field(ge=1, le=10, default=5)
    interceptacao: float = Field(ge=1, le=10, default=5)
    reflexos: float = Field(ge=1, le=10, default=5)  # Para goleiros
    jogo_com_os_pes: float = Field(ge=1, le=10, default=5)  # Para goleiros
    disciplina_tatica: float = Field(ge=1, le=10, default=5)

class AthleteCreate(BaseModel):
    name: str
    age: int = Field(ge=10, le=50)
    nationality: Optional[str] = None
    height: Optional[float] = Field(None, ge=140, le=220)
    weight: Optional[float] = Field(None, ge=40, le=120)
    body_type: Optional[str] = Field(None, pattern="^(Ectomorfo|Mesomorfo|Endomorfo)$")
    dominant_foot: Optional[str] = Field(None, pattern="^(Destro|Canhoto|Ambidestro)$")
    primary_position: Optional[str] = None
    secondary_position: Optional[str] = None
    technical_skills: TechnicalSkills
    deficiencies: List[str] = []

class AthleteResponse(BaseModel):
    id: int
    name: str
    age: int
    nationality: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    body_type: Optional[str]
    dominant_foot: Optional[str]
    primary_position: Optional[str]
    secondary_position: Optional[str]
    technical_skills: Dict
    deficiencies: List[str]
    classification_data: Optional[Dict]
    created_at: datetime
    
    class Config:
        from_attributes = True

class ClassificationResult(BaseModel):
    recommended_position: str
    position_scores: Dict[str, float]
    similar_legends: List[Dict]
    strengths: List[str]
    development_areas: List[str]
    training_recommendations: List[Dict]
    compatibility_score: float

