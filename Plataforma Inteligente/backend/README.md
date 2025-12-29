# Backend - Plataforma Inteligente de Atletas

API REST desenvolvida com FastAPI para classificação e monitoramento de atletas.

## Estrutura

```
backend/
├── app/
│   ├── models/          # Modelos SQLAlchemy
│   │   ├── athlete.py   # Modelo de atleta
│   │   └── legend.py    # Modelo de jogador histórico
│   ├── schemas/         # Schemas Pydantic para validação
│   ├── api/             # Endpoints da API
│   │   ├── athletes.py  # CRUD de atletas
│   │   ├── training.py  # Recomendações de treino
│   │   ├── match.py     # Sistema de match
│   │   └── reports.py   # Relatórios
│   ├── services/        # Lógica de negócio
│   │   ├── classifier.py        # Classificador de atletas
│   │   └── legend_database.py   # Banco de dados de referência
│   └── database.py      # Configuração do banco
├── main.py              # Aplicação FastAPI principal
├── init_db.py           # Script de inicialização
└── requirements.txt     # Dependências
```

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

Por padrão, o sistema usa SQLite. Para usar PostgreSQL:

1. Crie um arquivo `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/athlete_platform
```

2. Instale o driver PostgreSQL:
```bash
pip install psycopg2-binary
```

## Inicialização

```bash
# Criar banco de dados e popular com jogadores históricos
python init_db.py

# Iniciar servidor
uvicorn main:app --reload
```

## Documentação da API

Após iniciar o servidor, acesse:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Algoritmo de Classificação

O sistema utiliza:
1. **Análise de Posição**: Calcula adequação baseada em altura, habilidades-chave e biotipo
2. **Comparação com Lendas**: Usa distância euclidiana normalizada para encontrar jogadores similares
3. **Identificação de Padrões**: Analisa forças e fraquezas baseado em thresholds

## Adicionar Novos Jogadores Históricos

Edite `app/services/legend_database.py` e adicione novos jogadores ao array `LEGEND_DATABASE`.


