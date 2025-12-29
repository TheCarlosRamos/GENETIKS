# Frontend - Plataforma Inteligente de Atletas

Interface React moderna e responsiva para a plataforma de classificação de atletas.

## Estrutura

```
frontend/
├── src/
│   ├── components/          # Componentes React
│   │   ├── AthleteList.js   # Lista de atletas
│   │   ├── AthleteForm.js   # Formulário de cadastro
│   │   ├── AthleteDetail.js # Detalhes do atleta
│   │   ├── Dashboard.js     # Dashboard de monitoramento
│   │   ├── MatchAnalysis.js # Análise de compatibilidade
│   │   ├── Reports.js       # Relatórios
│   │   └── ...              # Componentes auxiliares
│   ├── services/
│   │   └── api.js           # Cliente HTTP para API
│   ├── App.js               # Componente principal
│   └── index.js             # Entry point
└── package.json
```

## Instalação

```bash
npm install
```

## Configuração

Crie um arquivo `.env` na raiz do frontend:

```env
REACT_APP_API_URL=http://localhost:8000
```

## Execução

```bash
npm start
```

A aplicação estará disponível em `http://localhost:3000`

## Build para Produção

```bash
npm run build
```

Os arquivos otimizados estarão em `build/`

## Componentes Principais

### AthleteForm
Formulário completo para cadastro de atletas com:
- Dados pessoais e físicos
- Sliders para habilidades técnicas
- Gerenciamento de deficiências

### AthleteDetail
Visualização detalhada com abas:
- Visão Geral: Classificação e habilidades
- Classificação: Comparação com jogadores históricos
- Treinamento: Recomendações personalizadas
- Evolução: Gráficos de progresso

### Dashboard
Monitoramento em tempo real com:
- Seleção de atleta
- Alertas de estagnação
- Resumo de evolução

### MatchAnalysis
Análise de compatibilidade:
- Estilos de time
- Múltiplas posições
- Companheiros ideais

### Reports
Relatórios inteligentes:
- Evolução temporal
- Comparação com lendas
- Planos de desenvolvimento

## Visualizações

A plataforma utiliza **Recharts** para:
- **Radar Chart**: Habilidades do atleta
- **Line Chart**: Evolução temporal
- **Bar Charts**: Comparações e scores

## Estilização

CSS modular por componente com:
- Design responsivo
- Tema consistente (gradientes roxos)
- Animações suaves
- Cards e badges informativos


