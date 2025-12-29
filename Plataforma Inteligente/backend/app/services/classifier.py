"""
Sistema de Classificação Inteligente de Atletas
Compara características com jogadores históricos e sugere posições ideais
"""

import numpy as np
from typing import Dict, List, Tuple
from app.services.legend_database import LEGEND_DATABASE, POSITION_TEMPLATES

class AthleteClassifier:
    def __init__(self):
        self.legend_database = LEGEND_DATABASE
        self.position_templates = POSITION_TEMPLATES
    
    def classify_athlete(self, athlete_data: Dict) -> Dict:
        """
        Classifica atleta comparando com referências históricas
        """
        # 1. Análise de Posição Baseada em Atributos
        position_scores = self.calculate_position_suitability(athlete_data)
        
        # 2. Comparação com Jogadores Históricos
        legend_comparison = self.find_closest_legends(athlete_data)
        
        # 3. Identificação de Forças e Fraquezas
        strengths = self.identify_strengths(athlete_data)
        development_areas = self.identify_development_areas(athlete_data)
        
        # 4. Recomendações de Treinamento
        training_recommendations = self.generate_training_recommendations(
            athlete_data, development_areas
        )
        
        return {
            "recommended_position": max(position_scores, key=position_scores.get),
            "position_scores": position_scores,
            "similar_legends": legend_comparison[:5],
            "strengths": strengths,
            "development_areas": development_areas,
            "training_recommendations": training_recommendations,
            "compatibility_score": max(position_scores.values()) if position_scores else 0
        }
    
    def calculate_position_suitability(self, athlete_data: Dict) -> Dict[str, float]:
        """
        Calcula adequação do atleta para cada posição
        """
        position_scores = {}
        technical_skills = athlete_data.get("technical_skills", {})
        
        for position, template in self.position_templates.items():
            score = 0.0
            factors = []
            
            # 1. Análise de altura (se disponível)
            if athlete_data.get("height"):
                ideal_min, ideal_max = template["ideal_height"]
                height = athlete_data["height"]
                if ideal_min <= height <= ideal_max:
                    height_score = 1.0
                elif height < ideal_min:
                    height_score = max(0.3, 1 - (ideal_min - height) / 20)
                else:
                    height_score = max(0.3, 1 - (height - ideal_max) / 20)
                score += height_score * 0.15
                factors.append(f"Altura: {height_score:.2f}")
            
            # 2. Análise de habilidades-chave
            key_skills = template["key_skills"]
            skill_scores = []
            for skill in key_skills:
                skill_value = technical_skills.get(skill, 5)
                skill_scores.append(skill_value / 10.0)
            
            if skill_scores:
                avg_skill_score = np.mean(skill_scores)
                score += avg_skill_score * 0.70
                factors.append(f"Habilidades-chave: {avg_skill_score:.2f}")
            
            # 3. Análise de biotipo (se disponível)
            if athlete_data.get("body_type"):
                body_type = athlete_data["body_type"]
                preferred_types = template["preferred_body_types"]
                if body_type in preferred_types:
                    score += 0.15
                    factors.append(f"Biotipo: 1.0")
                else:
                    score += 0.05
                    factors.append(f"Biotipo: 0.33")
            
            position_scores[position] = min(1.0, score)
        
        return position_scores
    
    def find_closest_legends(self, athlete_data: Dict) -> List[Dict]:
        """
        Encontra jogadores históricos mais similares
        """
        athlete_skills = athlete_data.get("technical_skills", {})
        similarities = []
        
        for legend in self.legend_database:
            legend_skills = legend["technical_profile"]
            
            # Calcula similaridade usando distância euclidiana normalizada
            common_skills = set(athlete_skills.keys()) & set(legend_skills.keys())
            
            if not common_skills:
                continue
            
            # Normaliza valores para comparação
            athlete_vector = np.array([athlete_skills[skill] for skill in common_skills])
            legend_vector = np.array([legend_skills[skill] for skill in common_skills])
            
            # Distância euclidiana normalizada (menor = mais similar)
            distance = np.linalg.norm(athlete_vector - legend_vector) / len(common_skills)
            similarity = 1 / (1 + distance)  # Converte distância em similaridade
            
            # Bônus por posição similar
            if athlete_data.get("primary_position") == legend["position"]:
                similarity *= 1.2
            
            # Bônus por características físicas similares
            if athlete_data.get("height") and legend.get("height"):
                height_diff = abs(athlete_data["height"] - legend["height"])
                if height_diff < 10:
                    similarity *= 1.1
            
            similarities.append({
                "legend": legend,
                "similarity": similarity,
                "distance": distance
            })
        
        # Ordena por similaridade (maior primeiro)
        similarities.sort(key=lambda x: x["similarity"], reverse=True)
        
        return [
            {
                "name": item["legend"]["name"],
                "position": item["legend"]["position"],
                "similarity": round(item["similarity"] * 100, 2),
                "playing_style": item["legend"]["playing_style"],
                "distinctive_traits": item["legend"]["distinctive_traits"],
                "era": item["legend"]["era"]
            }
            for item in similarities
        ]
    
    def identify_strengths(self, athlete_data: Dict) -> List[str]:
        """
        Identifica principais forças do atleta
        """
        technical_skills = athlete_data.get("technical_skills", {})
        strengths = []
        
        # Habilidades acima de 8 são consideradas fortes
        for skill, value in technical_skills.items():
            if value >= 8:
                strengths.append(f"{skill.replace('_', ' ').title()}: {value}/10")
        
        # Ordena por valor (maior primeiro)
        strengths.sort(key=lambda x: float(x.split(": ")[1].split("/")[0]), reverse=True)
        
        return strengths[:5] if strengths else ["Nenhuma habilidade destacada identificada"]
    
    def identify_development_areas(self, athlete_data: Dict) -> List[str]:
        """
        Identifica áreas que precisam de desenvolvimento
        """
        technical_skills = athlete_data.get("technical_skills", {})
        deficiencies = athlete_data.get("deficiencies", [])
        development_areas = []
        
        # Adiciona deficiências explícitas
        development_areas.extend(deficiencies)
        
        # Identifica habilidades abaixo de 6
        for skill, value in technical_skills.items():
            if value < 6 and skill not in deficiencies:
                development_areas.append(skill.replace("_", " ").title())
        
        return list(set(development_areas))  # Remove duplicatas
    
    def generate_training_recommendations(
        self, athlete_data: Dict, development_areas: List[str]
    ) -> List[Dict]:
        """
        Gera recomendações de treinamento baseadas nas áreas de desenvolvimento
        """
        recommendations = []
        
        training_map = {
            "Jogo Aéreo": {
                "exercises": [
                    "Cabeceio com salto em diferentes alturas",
                    "Posicionamento em cruzamentos",
                    "Força de impulsão com exercícios pliométricos",
                    "Trabalho de timing em bolas aéreas"
                ],
                "drills": [
                    "2x2 em áreas pré-definidas com foco em jogo aéreo",
                    "Cruzamentos com marcação",
                    "Jogos aéreos 1x1",
                    "Treino de finalização de cabeça"
                ],
                "reference_players": ["Cristiano Ronaldo", "Marco van Basten", "Alessandro Nesta"]
            },
            "Jogo Com Os Pés": {
                "exercises": [
                    "Saída de bola curta sob pressão",
                    "Lançamentos longos precisos",
                    "Controle sob pressão",
                    "Passe com ambos os pés"
                ],
                "drills": [
                    "Posse de bola com numeração inferior",
                    "Transição rápida defesa-ataque",
                    "Jogo posicional com goleiro",
                    "Construção de jogo desde o gol"
                ],
                "reference_players": ["Manuel Neuer", "Ederson", "Alisson"]
            },
            "Disciplina Tática": {
                "exercises": [
                    "Estudos táticos com vídeos",
                    "Posicionamento em simulações de jogo",
                    "Tomada de decisão em situações táticas",
                    "Comunicação e organização"
                ],
                "drills": [
                    "Jogo com regras condicionantes",
                    "Transições defensivas organizadas",
                    "Marcação zonal vs individual",
                    "Sistemas de jogo variados"
                ],
                "reference_players": ["Philipp Lahm", "Cafu", "Franz Beckenbauer"]
            },
            "Finalização": {
                "exercises": [
                    "Chute em diferentes ângulos",
                    "Finalização sob pressão",
                    "Conclusão em velocidade",
                    "Chute de primeira"
                ],
                "drills": [
                    "1x1 com goleiro",
                    "Finalização em segunda jogada",
                    "Finalização após drible",
                    "Finalização em velocidade"
                ],
                "reference_players": ["Pelé", "Romário", "Ronaldo Fenômeno"]
            },
            "Drible": {
                "exercises": [
                    "Drible em espaços reduzidos",
                    "Mudanças de direção",
                    "Drible em velocidade",
                    "Proteção de bola"
                ],
                "drills": [
                    "1x1 em diferentes áreas",
                    "Drible em circuito",
                    "Drible em situações de jogo",
                    "Drible com finalização"
                ],
                "reference_players": ["Lionel Messi", "Diego Maradona", "Andrés Iniesta"]
            },
            "Passe": {
                "exercises": [
                    "Passe curto de precisão",
                    "Passe longo",
                    "Passe em movimento",
                    "Passe de primeira"
                ],
                "drills": [
                    "Rondos com diferentes números",
                    "Passe em triangulações",
                    "Transições rápidas",
                    "Construção de jogadas"
                ],
                "reference_players": ["Xavi Hernández", "Andrea Pirlo", "Zinedine Zidane"]
            },
            "Marcação": {
                "exercises": [
                    "Marcação individual",
                    "Marcação zonal",
                    "Antecipação",
                    "Combate físico"
                ],
                "drills": [
                    "1x1 defensivo",
                    "Marcação em diferentes zonas",
                    "Transições defensivas",
                    "Jogo posicional defensivo"
                ],
                "reference_players": ["Franco Baresi", "Lothar Matthäus", "Frank Rijkaard"]
            },
            "Velocidade": {
                "exercises": [
                    "Sprints de diferentes distâncias",
                    "Aceleração",
                    "Velocidade com mudança de direção",
                    "Velocidade com bola"
                ],
                "drills": [
                    "Corridas de velocidade",
                    "Transições rápidas",
                    "Contra-ataques",
                    "Jogo em velocidade"
                ],
                "reference_players": ["Ronaldo Fenômeno", "Cafu", "Cristiano Ronaldo"]
            },
            "Resistência": {
                "exercises": [
                    "Corrida contínua",
                    "Intervalos de alta intensidade",
                    "Resistência com bola",
                    "Recuperação ativa"
                ],
                "drills": [
                    "Jogos de posse prolongada",
                    "Transições contínuas",
                    "Pressionamento alto",
                    "Jogo em espaços amplos"
                ],
                "reference_players": ["Cafu", "Xavi Hernández", "Andrés Iniesta"]
            }
        }
        
        for area in development_areas:
            area_normalized = area.lower()
            # Tenta encontrar correspondência
            for key, value in training_map.items():
                if key.lower() in area_normalized or area_normalized in key.lower():
                    recommendations.append({
                        "deficiency": area,
                        "exercises": value["exercises"],
                        "drills": value["drills"],
                        "reference_players": value["reference_players"]
                    })
                    break
            else:
                # Recomendação genérica se não encontrar correspondência específica
                recommendations.append({
                    "deficiency": area,
                    "exercises": [
                        f"Trabalho específico em {area.lower()}",
                        "Exercícios técnicos direcionados",
                        "Drills de jogo real"
                    ],
                    "drills": [
                        "Aplicação em situações de jogo",
                        "Treino posicional",
                        "Jogos condicionados"
                    ],
                    "reference_players": ["Estudar jogadores de referência na posição"]
                })
        
        return recommendations

