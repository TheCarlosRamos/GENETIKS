# Exemplos de Uso da API

## Exemplo 1: Cadastrar um Atleta

```python
import requests

# Dados do atleta
athlete_data = {
    "name": "João Silva",
    "age": 22,
    "nationality": "Brasil",
    "height": 180.0,
    "weight": 75.0,
    "body_type": "Mesomorfo",
    "dominant_foot": "Destro",
    "primary_position": "Atacante",
    "secondary_position": "Meia",
    "technical_skills": {
        "velocidade": 8.5,
        "resistencia": 7.0,
        "forca": 7.5,
        "agilidade": 8.0,
        "passe": 6.5,
        "drible": 8.5,
        "finalizacao": 9.0,
        "chute": 8.5,
        "jogo_aereo": 7.0,
        "visao_de_jogo": 7.5,
        "posicionamento": 8.0,
        "marcacao": 4.0,
        "interceptacao": 3.5,
        "disciplina_tatica": 6.0
    },
    "deficiencies": ["Jogo aéreo", "Disciplina tática"]
}

# Cadastrar
response = requests.post("http://localhost:8000/athletes/", json=athlete_data)
athlete = response.json()
print(f"Atleta cadastrado: {athlete['name']}")
print(f"ID: {athlete['id']}")
print(f"Posição recomendada: {athlete['classification_data']['recommended_position']}")
```

## Exemplo 2: Obter Classificação

```python
import requests

athlete_id = 1

# Obter classificação atualizada
response = requests.get(f"http://localhost:8000/athletes/{athlete_id}/classification")
classification = response.json()

print(f"Posição Recomendada: {classification['recommended_position']}")
print(f"Score de Compatibilidade: {classification['compatibility_score'] * 100:.1f}%")

print("\nJogadores Similares:")
for legend in classification['similar_legends'][:3]:
    print(f"- {legend['name']} ({legend['similarity']}% similar)")
```

## Exemplo 3: Registrar Desempenho

```python
import requests

athlete_id = 1

# Novas habilidades após treinamento
new_skills = {
    "velocidade": 9.0,  # Melhorou!
    "resistencia": 7.5,
    "forca": 8.0,
    "agilidade": 8.5,
    "passe": 7.0,
    "drible": 9.0,
    "finalizacao": 9.5,
    "chute": 9.0,
    "jogo_aereo": 8.0,  # Melhorou muito!
    "visao_de_jogo": 8.0,
    "posicionamento": 8.5,
    "marcacao": 4.5,
    "interceptacao": 4.0,
    "disciplina_tatica": 7.0  # Melhorou!
}

# Métricas físicas (opcional)
physical_metrics = {
    "vo2_max": 55.0,
    "forca_maxima": 120.0
}

response = requests.post(
    f"http://localhost:8000/athletes/{athlete_id}/performance",
    json={
        "technical_skills": new_skills,
        "physical_metrics": physical_metrics
    }
)

print("Desempenho registrado com sucesso!")
```

## Exemplo 4: Obter Recomendações de Treinamento

```python
import requests

athlete_id = 1

response = requests.get(f"http://localhost:8000/training/{athlete_id}/recommendations")
recommendations = response.json()

print("Áreas de Desenvolvimento:")
for area in recommendations['development_areas']:
    print(f"- {area}")

print("\nRecomendações:")
for rec in recommendations['recommendations']:
    print(f"\n{rec['deficiency']}:")
    print("Exercícios:")
    for exercise in rec['exercises']:
        print(f"  - {exercise}")
    print("Jogadores de Referência:")
    for player in rec['reference_players']:
        print(f"  - {player}")
```

## Exemplo 5: Análise de Match

```python
import requests

athlete_id = 1

# Compatibilidade com posições
response = requests.get(f"http://localhost:8000/match/{athlete_id}/positions")
positions = response.json()

print(f"Posição Atual: {positions['current_position']}")
print(f"Posição Recomendada: {positions['recommended_position']}")
print("\nScores por Posição:")
for position, score in positions['position_scores'].items():
    print(f"{position}: {score}%")

# Compatibilidade com estilos de time
response = requests.get(f"http://localhost:8000/match/{athlete_id}/teams")
teams = response.json()

print("\nCompatibilidade com Estilos de Time:")
for style, data in teams['compatibility'].items():
    print(f"{style}: {data['score']}%")
```

## Exemplo 6: Relatório de Evolução

```python
import requests

athlete_id = 1

response = requests.get(f"http://localhost:8000/reports/{athlete_id}/evolution")
report = response.json()

if 'message' not in report:
    print(f"Período: {report['analysis_period']['days']} dias")
    print(f"\nMaiores Melhorias:")
    for improvement in report['top_improvements']:
        print(f"- {improvement['skill']}: +{improvement['change']:.2f} ({improvement['percentage']:.1f}%)")
    
    print(f"\nPrincipais Regressões:")
    for regression in report['top_regressions']:
        print(f"- {regression['skill']}: {regression['change']:.2f} ({regression['percentage']:.1f}%)")
```

## Exemplo 7: Usando JavaScript/Fetch

```javascript
// Cadastrar atleta
const athleteData = {
  name: "Maria Santos",
  age: 20,
  nationality: "Brasil",
  height: 165,
  weight: 60,
  body_type: "Ectomorfo",
  dominant_foot: "Canhoto",
  primary_position: "Meia",
  technical_skills: {
    velocidade: 7,
    resistencia: 8,
    forca: 5,
    agilidade: 9,
    passe: 9,
    drible: 9,
    finalizacao: 7,
    chute: 7,
    jogo_aereo: 4,
    visao_de_jogo: 9,
    posicionamento: 8,
    marcacao: 6,
    interceptacao: 5,
    disciplina_tatica: 7
  },
  deficiencies: []
};

fetch('http://localhost:8000/athletes/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(athleteData)
})
.then(response => response.json())
.then(data => {
  console.log('Atleta cadastrado:', data);
  console.log('Posição recomendada:', data.classification_data.recommended_position);
})
.catch(error => console.error('Erro:', error));
```

## Exemplo 8: Usando cURL

```bash
# Cadastrar atleta
curl -X POST "http://localhost:8000/athletes/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Pedro Costa",
    "age": 25,
    "height": 185,
    "weight": 80,
    "body_type": "Mesomorfo",
    "dominant_foot": "Destro",
    "primary_position": "Zagueiro",
    "technical_skills": {
      "velocidade": 6,
      "resistencia": 7,
      "forca": 8,
      "agilidade": 6,
      "passe": 7,
      "drible": 5,
      "finalizacao": 4,
      "chute": 5,
      "jogo_aereo": 8,
      "visao_de_jogo": 8,
      "posicionamento": 9,
      "marcacao": 9,
      "interceptacao": 9,
      "disciplina_tatica": 9
    },
    "deficiencies": []
  }'

# Obter classificação
curl "http://localhost:8000/athletes/1/classification"

# Obter recomendações
curl "http://localhost:8000/training/1/recommendations"
```


