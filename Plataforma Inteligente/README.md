# Plataforma Inteligente de Classificação de Atletas de Futebol

Plataforma completa para classificação, monitoramento e desenvolvimento de atletas baseada nas características dos maiores jogadores da história.

## 🏗️ Arquitetura

### Backend
- **FastAPI**: API REST moderna e rápida
- **SQLite/PostgreSQL**: Banco de dados (SQLite por padrão, PostgreSQL opcional)
- **SQLAlchemy**: ORM para gerenciamento de dados
- **NumPy/Scikit-learn**: Algoritmos de classificação e comparação

### Frontend
- **React.js**: Interface moderna e responsiva
- **Recharts**: Visualizações interativas (gráficos radar, linha)
- **React Router**: Navegação entre páginas

## 🚀 Início Rápido

### ⚡ Opção 1: Script Automático (Recomendado)

**Windows:**
```bash
# Duplo clique ou execute:
start.bat

# Ou via PowerShell:
.\run.ps1
```

**Linux/Mac (com Make):**
```bash
make run
```

O script irá:
- ✅ Verificar dependências
- ✅ Instalar pacotes necessários
- ✅ Inicializar banco de dados
- ✅ Iniciar backend e frontend
- ✅ Abrir navegador automaticamente

### 📋 Opção 2: Manual (2 Terminais)

#### Terminal 1 - Backend:
```bash
cd backend
pip install -r requirements.txt
python init_db.py
uvicorn main:app --reload
```

#### Terminal 2 - Frontend:
```bash
cd frontend
npm install
npm start
```

### ✅ Verificação

- **Backend**: `http://localhost:8000/docs` (documentação da API)
- **Frontend**: `http://localhost:3000` (interface web)

---

## 📋 Pré-requisitos

- **Python 3.8+**: `python --version`
- **Node.js 16+**: `node --version`
- **npm**: Vem com Node.js

## 🔧 Configuração Detalhada

### Backend

1. **Instalar dependências:**
```bash
cd backend
pip install -r requirements.txt
```

2. **Configurar variáveis de ambiente (opcional):**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. **Inicializar banco de dados:**
```bash
python init_db.py
```

4. **Iniciar servidor:**
```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://localhost:8000`
Documentação da API: `http://localhost:8000/docs`

### Frontend

1. **Instalar dependências:**
```bash
cd frontend
npm install
```

2. **Configurar URL da API (opcional):**
Crie um arquivo `.env` na pasta `frontend`:
```
REACT_APP_API_URL=http://localhost:8000
```

3. **Iniciar aplicação:**
```bash
npm start
```

A aplicação estará disponível em `http://localhost:3000`

> 💡 **Dica**: Consulte `COMANDOS.md` para um guia completo passo a passo!

## 📋 Funcionalidades

### 1. Cadastramento de Atletas
- Dados pessoais (nome, idade, nacionalidade)
- Características físicas (altura, peso, biotipo)
- Habilidades técnicas (16 habilidades avaliadas de 1-10)
- Deficiências/áreas de melhoria
- Posição primária e secundária

### 2. Classificação Inteligente
- Comparação automática com 20+ jogadores históricos
- Sugestão de posição ideal baseada em atributos
- Identificação de forças e fraquezas
- Score de compatibilidade por posição

### 3. Monitoramento de Desempenho
- Dashboard interativo com evolução temporal
- Gráficos radar de habilidades
- Alertas de estagnação e desequilíbrio
- Histórico completo de desempenho

### 4. Recomendações de Treinamento
- Exercícios específicos para cada deficiência
- Drills de treinamento personalizados
- Jogadores de referência para estudo
- Planos de desenvolvimento estruturados

### 5. Sistema de Match
- Compatibilidade com diferentes estilos de time
- Análise de adequação a múltiplas posições
- Sugestão de companheiros compatíveis
- Análise de complementaridade

### 6. Relatórios Inteligentes
- Relatório de evolução mensal/trimestral
- Análise comparativa com jogadores históricos
- Plano de desenvolvimento personalizado
- Projeção de potencial (curto/médio/longo prazo)

## 📊 Estrutura do Projeto

```
Plataforma Inteligente/
├── backend/
│   ├── app/
│   │   ├── models/          # Modelos de banco de dados
│   │   ├── schemas/          # Schemas Pydantic
│   │   ├── api/              # Endpoints da API
│   │   ├── services/         # Lógica de negócio
│   │   └── database.py       # Configuração do banco
│   ├── main.py               # Aplicação FastAPI
│   ├── init_db.py            # Script de inicialização
│   └── requirements.txt      # Dependências Python
├── frontend/
│   ├── src/
│   │   ├── components/       # Componentes React
│   │   ├── services/         # Serviços de API
│   │   └── App.js            # Componente principal
│   └── package.json          # Dependências Node
└── README.md
```

## 🎯 Uso da Plataforma

### Cadastrar um Atleta
1. Acesse "Cadastrar" no menu
2. Preencha os dados pessoais e físicos
3. Ajuste as habilidades técnicas (sliders de 1-10)
4. Adicione deficiências/áreas de melhoria
5. Clique em "Cadastrar e Classificar"

### Visualizar Classificação
1. Acesse a lista de atletas
2. Clique em um atleta para ver detalhes
3. Veja a aba "Classificação" para:
   - Jogadores históricos similares
   - Scores por posição
   - Forças e áreas de desenvolvimento

### Monitorar Evolução
1. Acesse "Dashboard" no menu
2. Selecione um atleta
3. Visualize:
   - Alertas de estagnação
   - Evolução de habilidades
   - Comparativos temporais

### Gerar Relatórios
1. Acesse "Relatórios" no menu
2. Selecione um atleta
3. Escolha o tipo de relatório:
   - **Evolução**: Análise temporal de progresso
   - **Comparativo**: Comparação com jogadores históricos
   - **Desenvolvimento**: Plano personalizado de crescimento

## 🔧 Tecnologias Utilizadas

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Frontend**: React, React Router, Recharts
- **Banco de Dados**: SQLite (padrão) ou PostgreSQL
- **Algoritmos**: NumPy para cálculos de similaridade

## 📝 API Endpoints

### Atletas
- `GET /athletes/` - Lista todos os atletas
- `POST /athletes/` - Cadastra novo atleta
- `GET /athletes/{id}` - Detalhes do atleta
- `GET /athletes/{id}/classification` - Classificação atualizada
- `GET /athletes/{id}/monitoring` - Dados de monitoramento
- `POST /athletes/{id}/performance` - Registra desempenho

### Treinamento
- `GET /training/{id}/recommendations` - Recomendações de treino
- `GET /training/{id}/plans` - Planos de treinamento

### Match
- `GET /match/{id}/teams` - Compatibilidade com estilos de time
- `GET /match/{id}/positions` - Compatibilidade com posições
- `GET /match/{id}/teammates` - Companheiros compatíveis

### Relatórios
- `GET /reports/{id}/evolution` - Relatório de evolução
- `GET /reports/{id}/comparative` - Relatório comparativo
- `GET /reports/{id}/development-plan` - Plano de desenvolvimento

## 🎓 Jogadores Históricos no Banco de Dados

A plataforma inclui dados de 20+ jogadores históricos:
- **Atacantes**: Pelé, Maradona, Messi, Ronaldo Fenômeno, Cristiano Ronaldo, Romário, Van Basten
- **Meias**: Zidane, Xavi, Iniesta
- **Volantes**: Matthäus, Rijkaard, Pirlo
- **Defensores**: Beckenbauer, Baresi, Nesta, Lahm, Cafu
- **Goleiros**: Neuer

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Adicionar novos jogadores históricos ao banco de dados

## 📄 Licença

Este projeto é open source e está disponível para uso educacional e comercial.

