from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.athlete import Athlete, PerformanceRecord
from app.services.classifier import AthleteClassifier
from datetime import datetime, timedelta
from typing import Dict

router = APIRouter(prefix="/reports", tags=["reports"])
classifier = AthleteClassifier()

@router.get("/{athlete_id}/evolution")
def get_evolution_report(athlete_id: int, period: str = "monthly", db: Session = Depends(get_db)):
    """Gera relatório de evolução do atleta"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Obtém registros de desempenho
    records = db.query(PerformanceRecord).filter(
        PerformanceRecord.athlete_id == athlete_id
    ).order_by(PerformanceRecord.record_date.asc()).all()
    
    if len(records) < 2:
        return {
            "message": "Dados insuficientes para análise de evolução",
            "records_count": len(records)
        }
    
    # Calcula evolução por habilidade
    first_record = records[0]
    last_record = records[-1]
    
    first_skills = first_record.technical_skills or {}
    last_skills = last_record.technical_skills or {}
    
    evolution = {}
    for skill in set(list(first_skills.keys()) + list(last_skills.keys())):
        old_value = first_skills.get(skill, 5)
        new_value = last_skills.get(skill, 5)
        change = new_value - old_value
        percentage = (change / old_value * 100) if old_value > 0 else 0
        
        evolution[skill] = {
            "initial": round(old_value, 2),
            "current": round(new_value, 2),
            "change": round(change, 2),
            "percentage": round(percentage, 2),
            "trend": "up" if change > 0 else "down" if change < 0 else "stable"
        }
    
    # Identifica maiores melhorias e regressões
    improvements = sorted(
        [(k, v) for k, v in evolution.items() if v["change"] > 0],
        key=lambda x: x[1]["change"],
        reverse=True
    )[:3]
    
    regressions = sorted(
        [(k, v) for k, v in evolution.items() if v["change"] < 0],
        key=lambda x: x[1]["change"]
    )[:3]
    
    return {
        "athlete_id": athlete_id,
        "athlete_name": athlete.name,
        "period": period,
        "analysis_period": {
            "start": first_record.record_date.isoformat(),
            "end": last_record.record_date.isoformat(),
            "days": (last_record.record_date - first_record.record_date).days
        },
        "evolution": evolution,
        "top_improvements": [
            {"skill": k, "change": v["change"], "percentage": v["percentage"]}
            for k, v in improvements
        ],
        "top_regressions": [
            {"skill": k, "change": v["change"], "percentage": v["percentage"]}
            for k, v in regressions
        ],
        "overall_trend": "positive" if len(improvements) > len(regressions) else "negative"
    }

@router.get("/{athlete_id}/comparative")
def get_comparative_report(athlete_id: int, db: Session = Depends(get_db)):
    """Gera relatório comparativo com jogadores históricos"""
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
    
    # Encontra jogadores similares
    similar_legends = classifier.find_closest_legends(athlete_data)
    
    # Comparação detalhada com top 3
    detailed_comparison = []
    athlete_skills = athlete_data["technical_skills"]
    
    for legend_data in similar_legends[:3]:
        # Busca dados completos da lenda
        from app.services.legend_database import LEGEND_DATABASE
        legend = next((l for l in LEGEND_DATABASE if l["name"] == legend_data["name"]), None)
        
        if legend:
            legend_skills = legend["technical_profile"]
            common_skills = set(athlete_skills.keys()) & set(legend_skills.keys())
            
            skill_comparison = {}
            for skill in common_skills:
                skill_comparison[skill] = {
                    "athlete": athlete_skills[skill],
                    "legend": legend_skills[skill],
                    "difference": round(athlete_skills[skill] - legend_skills[skill], 2)
                }
            
            detailed_comparison.append({
                "legend_name": legend["name"],
                "similarity": legend_data["similarity"],
                "position": legend["position"],
                "playing_style": legend["playing_style"],
                "skill_comparison": skill_comparison,
                "distinctive_traits": legend["distinctive_traits"]
            })
    
    return {
        "athlete_id": athlete_id,
        "athlete_name": athlete.name,
        "athlete_position": athlete.primary_position,
        "similar_legends": similar_legends[:5],
        "detailed_comparison": detailed_comparison,
        "insights": [
            f"O atleta tem {similar_legends[0]['similarity']:.1f}% de similaridade com {similar_legends[0]['name']}",
            f"Posição recomendada: {athlete.classification_data.get('recommended_position', 'N/A') if athlete.classification_data else 'N/A'}"
        ]
    }

@router.get("/{athlete_id}/development-plan")
def get_development_plan(athlete_id: int, db: Session = Depends(get_db)):
    """Gera plano de desenvolvimento personalizado"""
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
    
    # Obtém classificação
    classification = classifier.classify_athlete(athlete_data)
    
    # Identifica áreas de desenvolvimento
    development_areas = classifier.identify_development_areas(athlete_data)
    strengths = classifier.identify_strengths(athlete_data)
    
    # Gera recomendações
    training_recommendations = classifier.generate_training_recommendations(
        athlete_data, development_areas
    )
    
    # Projeção de potencial
    current_avg = sum(athlete_data["technical_skills"].values()) / len(athlete_data["technical_skills"]) if athlete_data["technical_skills"] else 5
    
    projection = {
        "short_term": {
            "period": "3 meses",
            "target_avg": min(10, round(current_avg + 0.5, 2)),
            "focus_areas": development_areas[:3]
        },
        "medium_term": {
            "period": "6 meses",
            "target_avg": min(10, round(current_avg + 1.0, 2)),
            "focus_areas": development_areas[:5]
        },
        "long_term": {
            "period": "12 meses",
            "target_avg": min(10, round(current_avg + 1.5, 2)),
            "focus_areas": development_areas
        }
    }
    
    return {
        "athlete_id": athlete_id,
        "athlete_name": athlete.name,
        "current_position": athlete.primary_position,
        "recommended_position": classification["recommended_position"],
        "current_level": {
            "average_skill": round(current_avg, 2),
            "strengths": strengths,
            "development_areas": development_areas
        },
        "training_recommendations": training_recommendations,
        "projection": projection,
        "reference_players": [
            {
                "name": legend["name"],
                "position": legend["position"],
                "similarity": legend["similarity"],
                "traits_to_emulate": legend["distinctive_traits"]
            }
            for legend in classification["similar_legends"][:3]
        ]
    }


