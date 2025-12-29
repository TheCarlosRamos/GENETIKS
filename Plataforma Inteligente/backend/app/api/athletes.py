from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.athlete import Athlete, PerformanceRecord
from app.schemas.athlete import AthleteCreate, AthleteResponse, ClassificationResult
from app.services.classifier import AthleteClassifier
from datetime import datetime

router = APIRouter(prefix="/athletes", tags=["athletes"])
classifier = AthleteClassifier()

@router.post("/", response_model=AthleteResponse)
def create_athlete(athlete: AthleteCreate, db: Session = Depends(get_db)):
    """Cadastra um novo atleta e realiza classificação automática"""
    # Converte TechnicalSkills para dict
    technical_skills_dict = athlete.technical_skills.dict()
    
    # Prepara dados do atleta para classificação
    athlete_data = {
        "name": athlete.name,
        "age": athlete.age,
        "height": athlete.height,
        "weight": athlete.weight,
        "body_type": athlete.body_type,
        "dominant_foot": athlete.dominant_foot,
        "primary_position": athlete.primary_position,
        "technical_skills": technical_skills_dict,
        "deficiencies": athlete.deficiencies
    }
    
    # Realiza classificação
    classification = classifier.classify_athlete(athlete_data)
    
    # Cria registro do atleta
    db_athlete = Athlete(
        name=athlete.name,
        age=athlete.age,
        nationality=athlete.nationality,
        height=athlete.height,
        weight=athlete.weight,
        body_type=athlete.body_type,
        dominant_foot=athlete.dominant_foot,
        primary_position=athlete.primary_position,
        secondary_position=athlete.secondary_position,
        technical_skills=technical_skills_dict,
        deficiencies=athlete.deficiencies,
        classification_data=classification
    )
    
    db.add(db_athlete)
    db.commit()
    db.refresh(db_athlete)
    
    # Cria registro inicial de desempenho
    initial_record = PerformanceRecord(
        athlete_id=db_athlete.id,
        technical_skills=technical_skills_dict,
        physical_metrics={}
    )
    db.add(initial_record)
    db.commit()
    
    return db_athlete

@router.get("/", response_model=List[AthleteResponse])
def get_athletes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista todos os atletas cadastrados"""
    athletes = db.query(Athlete).offset(skip).limit(limit).all()
    return athletes

@router.get("/{athlete_id}", response_model=AthleteResponse)
def get_athlete(athlete_id: int, db: Session = Depends(get_db)):
    """Obtém detalhes de um atleta específico"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return athlete

@router.get("/{athlete_id}/classification", response_model=ClassificationResult)
def get_classification(athlete_id: int, db: Session = Depends(get_db)):
    """Obtém classificação atualizada do atleta"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Prepara dados para reclassificação
    athlete_data = {
        "name": athlete.name,
        "age": athlete.age,
        "height": athlete.height,
        "weight": athlete.weight,
        "body_type": athlete.body_type,
        "dominant_foot": athlete.dominant_foot,
        "primary_position": athlete.primary_position,
        "technical_skills": athlete.technical_skills or {},
        "deficiencies": athlete.deficiencies or []
    }
    
    # Realiza classificação
    classification = classifier.classify_athlete(athlete_data)
    
    # Atualiza dados de classificação no banco
    athlete.classification_data = classification
    db.commit()
    
    return classification

@router.post("/{athlete_id}/performance")
def record_performance(
    athlete_id: int,
    technical_skills: dict,
    physical_metrics: dict = {},
    db: Session = Depends(get_db)
):
    """Registra novo desempenho do atleta"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Cria novo registro de desempenho
    record = PerformanceRecord(
        athlete_id=athlete_id,
        technical_skills=technical_skills,
        physical_metrics=physical_metrics
    )
    
    db.add(record)
    
    # Atualiza habilidades do atleta
    athlete.technical_skills = technical_skills
    db.commit()
    db.refresh(record)
    
    return {"message": "Desempenho registrado com sucesso", "record_id": record.id}

@router.get("/{athlete_id}/performance")
def get_performance_history(athlete_id: int, db: Session = Depends(get_db)):
    """Obtém histórico de desempenho do atleta"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    records = db.query(PerformanceRecord).filter(
        PerformanceRecord.athlete_id == athlete_id
    ).order_by(PerformanceRecord.record_date.desc()).all()
    
    return [
        {
            "id": record.id,
            "date": record.record_date.isoformat(),
            "technical_skills": record.technical_skills,
            "physical_metrics": record.physical_metrics
        }
        for record in records
    ]

@router.get("/{athlete_id}/monitoring")
def get_monitoring_dashboard(athlete_id: int, db: Session = Depends(get_db)):
    """Obtém dados para dashboard de monitoramento"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Obtém histórico de desempenho
    records = db.query(PerformanceRecord).filter(
        PerformanceRecord.athlete_id == athlete_id
    ).order_by(PerformanceRecord.record_date.asc()).all()
    
    # Calcula evolução
    evolution_data = []
    if len(records) >= 2:
        first_record = records[0]
        last_record = records[-1]
        
        first_skills = first_record.technical_skills or {}
        last_skills = last_record.technical_skills or {}
        
        evolution = {}
        for skill in set(list(first_skills.keys()) + list(last_skills.keys())):
            old_value = first_skills.get(skill, 5)
            new_value = last_skills.get(skill, 5)
            evolution[skill] = {
                "old": old_value,
                "new": new_value,
                "change": round(new_value - old_value, 2),
                "percentage": round(((new_value - old_value) / old_value * 100) if old_value > 0 else 0, 2)
            }
        
        evolution_data = evolution
    
    # Identifica alertas
    alerts = []
    current_skills = athlete.technical_skills or {}
    
    # Alerta de estagnação
    if len(records) >= 3:
        recent_records = records[-3:]
        for skill in current_skills.keys():
            values = [r.technical_skills.get(skill, 5) for r in recent_records if r.technical_skills]
            if len(values) == 3 and len(set(values)) == 1:
                alerts.append({
                    "type": "stagnation",
                    "skill": skill,
                    "message": f"Estagnação detectada em {skill}"
                })
    
    # Alerta de desequilíbrio
    physical_skills = ["velocidade", "resistencia", "forca", "agilidade"]
    technical_skills_list = ["passe", "drible", "finalizacao", "chute"]
    
    physical_avg = sum([current_skills.get(s, 5) for s in physical_skills]) / len(physical_skills)
    technical_avg = sum([current_skills.get(s, 5) for s in technical_skills_list]) / len(technical_skills_list)
    
    if abs(physical_avg - technical_avg) > 2:
        alerts.append({
            "type": "imbalance",
            "message": "Desequilíbrio entre habilidades físicas e técnicas detectado"
        })
    
    return {
        "athlete": {
            "id": athlete.id,
            "name": athlete.name,
            "position": athlete.primary_position,
            "current_skills": current_skills
        },
        "classification": athlete.classification_data,
        "evolution": evolution_data,
        "alerts": alerts,
        "performance_history": [
            {
                "date": r.record_date.isoformat(),
                "skills": r.technical_skills
            }
            for r in records
        ]
    }

