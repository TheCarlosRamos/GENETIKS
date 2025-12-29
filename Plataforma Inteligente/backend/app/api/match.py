from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.athlete import Athlete
from app.services.classifier import AthleteClassifier
from typing import List, Dict
import numpy as np

router = APIRouter(prefix="/match", tags=["match"])
classifier = AthleteClassifier()

@router.get("/{athlete_id}/teams")
def match_with_teams(
    athlete_id: int,
    team_style: str = None,
    system: str = None,
    db: Session = Depends(get_db)
):
    """Analisa compatibilidade do atleta com diferentes estilos de time"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Estilos de jogo e suas características
    team_styles = {
        "posse_bola": {
            "required_skills": ["passe", "visao_de_jogo", "disciplina_tatica", "resistencia"],
            "description": "Time que prioriza posse de bola e construção de jogadas"
        },
        "contra_ataque": {
            "required_skills": ["velocidade", "finalizacao", "drible", "agilidade"],
            "description": "Time que joga em transições rápidas"
        },
        "pressionamento_alto": {
            "required_skills": ["resistencia", "velocidade", "marcacao", "disciplina_tatica"],
            "description": "Time que pressiona alto e busca recuperação rápida"
        },
        "defensivo": {
            "required_skills": ["marcacao", "posicionamento", "disciplina_tatica", "interceptacao"],
            "description": "Time que prioriza organização defensiva"
        },
        "ofensivo": {
            "required_skills": ["finalizacao", "drible", "velocidade", "jogo_aereo"],
            "description": "Time que prioriza criação de chances e finalização"
        }
    }
    
    athlete_skills = athlete.technical_skills or {}
    compatibility_scores = {}
    
    for style_name, style_data in team_styles.items():
        required_skills = style_data["required_skills"]
        scores = []
        
        for skill in required_skills:
            skill_value = athlete_skills.get(skill, 5)
            scores.append(skill_value / 10.0)
        
        avg_score = np.mean(scores) if scores else 0
        compatibility_scores[style_name] = {
            "score": round(avg_score * 100, 2),
            "description": style_data["description"],
            "required_skills": required_skills
        }
    
    # Ordena por compatibilidade
    sorted_compatibility = sorted(
        compatibility_scores.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    )
    
    return {
        "athlete_id": athlete_id,
        "athlete_name": athlete.name,
        "position": athlete.primary_position,
        "compatibility": dict(sorted_compatibility),
        "recommended_style": sorted_compatibility[0][0] if sorted_compatibility else None
    }

@router.get("/{athlete_id}/positions")
def match_with_positions(athlete_id: int, db: Session = Depends(get_db)):
    """Analisa compatibilidade do atleta com diferentes posições"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Prepara dados para classificação
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
    
    # Calcula adequação para cada posição
    position_scores = classifier.calculate_position_suitability(athlete_data)
    
    # Ordena posições por score
    sorted_positions = sorted(
        position_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    return {
        "athlete_id": athlete_id,
        "athlete_name": athlete.name,
        "current_position": athlete.primary_position,
        "position_scores": {
            pos: round(score * 100, 2)
            for pos, score in sorted_positions
        },
        "recommended_position": sorted_positions[0][0] if sorted_positions else None,
        "alternative_positions": [
            {"position": pos, "score": round(score * 100, 2)}
            for pos, score in sorted_positions[1:4]
        ]
    }

@router.get("/{athlete_id}/teammates")
def match_with_teammates(
    athlete_id: int,
    position: str = None,
    db: Session = Depends(get_db)
):
    """Analisa compatibilidade com outros atletas (para formação de equipes)"""
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    
    # Busca outros atletas
    query = db.query(Athlete).filter(Athlete.id != athlete_id)
    if position:
        query = query.filter(
            (Athlete.primary_position == position) |
            (Athlete.secondary_position == position)
        )
    
    other_athletes = query.all()
    
    athlete_skills = athlete.technical_skills or {}
    compatibility_list = []
    
    for other in other_athletes:
        other_skills = other.technical_skills or {}
        
        # Calcula complementaridade (atletas com habilidades diferentes se complementam)
        common_skills = set(athlete_skills.keys()) & set(other_skills.keys())
        if not common_skills:
            continue
        
        # Score de complementaridade (diferentes mas não opostos)
        complementarity = 0
        for skill in common_skills:
            diff = abs(athlete_skills[skill] - other_skills[skill])
            # Ideal: diferença moderada (2-4 pontos)
            if 2 <= diff <= 4:
                complementarity += 1
            elif diff < 2:
                complementarity += 0.5  # Muito similares
            else:
                complementarity += 0.2  # Muito diferentes
        
        complementarity_score = complementarity / len(common_skills) if common_skills else 0
        
        compatibility_list.append({
            "athlete_id": other.id,
            "name": other.name,
            "position": other.primary_position,
            "complementarity_score": round(complementarity_score * 100, 2),
            "skills": other_skills
        })
    
    # Ordena por complementaridade
    compatibility_list.sort(key=lambda x: x["complementarity_score"], reverse=True)
    
    return {
        "athlete_id": athlete_id,
        "athlete_name": athlete.name,
        "compatible_teammates": compatibility_list[:10]  # Top 10
    }


