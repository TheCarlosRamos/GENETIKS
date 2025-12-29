from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.athlete import Athlete, TrainingRecommendation
from app.services.classifier import AthleteClassifier
from typing import List, Dict

router = APIRouter(prefix="/training", tags=["training"])
classifier = AthleteClassifier()

@router.get("/{athlete_id}/recommendations")
def get_training_recommendations(athlete_id: int, db: Session = Depends(get_db)):
    """Obtém recomendações de treinamento para o atleta"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Prepara dados do atleta
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
    
    # Identifica áreas de desenvolvimento
    development_areas = classifier.identify_development_areas(athlete_data)
    
    # Gera recomendações
    recommendations = classifier.generate_training_recommendations(
        athlete_data, development_areas
    )
    
    return {
        "athlete_id": athlete_id,
        "development_areas": development_areas,
        "recommendations": recommendations
    }

@router.post("/{athlete_id}/recommendations/{deficiency}")
def create_training_plan(
    athlete_id: int,
    deficiency: str,
    plan: Dict,
    db: Session = Depends(get_db)
):
    """Cria plano de treinamento específico para uma deficiência"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    training_plan = TrainingRecommendation(
        athlete_id=athlete_id,
        deficiency=deficiency,
        exercises=plan.get("exercises", []),
        drills=plan.get("drills", []),
        reference_players=plan.get("reference_players", [])
    )
    
    db.add(training_plan)
    db.commit()
    db.refresh(training_plan)
    
    return training_plan

@router.get("/{athlete_id}/plans")
def get_training_plans(athlete_id: int, db: Session = Depends(get_db)):
    """Obtém todos os planos de treinamento do atleta"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    plans = db.query(TrainingRecommendation).filter(
        TrainingRecommendation.athlete_id == athlete_id
    ).order_by(TrainingRecommendation.created_at.desc()).all()
    
    return [
        {
            "id": plan.id,
            "deficiency": plan.deficiency,
            "exercises": plan.exercises,
            "drills": plan.drills,
            "reference_players": plan.reference_players,
            "created_at": plan.created_at.isoformat()
        }
        for plan in plans
    ]


