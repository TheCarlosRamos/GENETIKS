# Justificativa Técnica: Expansão da Base de Dados de Atletas

## Visão Geral
A plataforma Genetiks foi concebida com um banco de dados de referência histórica (ex: Pelé, Maradona). Embora fundamentais para o marketing, esses perfis não refletem a totalidade das exigências físicas do futebol contemporâneo. Este documento detalha a estratégia de incorporação de jogadores em atividade (Séries A/B e Elite Europeia) para aumentar a precisão dos algoritmos de similaridade.

## Por que incluir jogadores atuais?

### 1. Modernização dos Padrões de Performance
O futebol moderno sofreu uma drástica evolução atlética. Comparar um jovem atleta de hoje com jogadores de décadas passadas pode gerar distorções na avaliação de potencial físico.
* **Impacto:** A inclusão de atletas atuais fornece parâmetros reais de VO2 Max, intensidade de sprint e recuperação, alinhando o "Teste Genético" às demandas biológicas do esporte atual.

### 2. Granularidade de Dados para Machine Learning
A disponibilidade de dados estatísticos detalhados para lendas históricas é limitada. Já para atletas em atividade, é possível extrair centenas de pontos de dados (xG, mapas de calor, eficiência de pressão).
* **Impacto:** Transforma a avaliação subjetiva em uma análise quantitativa robusta, permitindo cruzamentos de dados de alta precisão e evitando erros de escolha.

### 3. Validação de Mercado
Clubes e agentes buscam atletas que supram demandas táticas vigentes.
* **Impacto:** Oferecer um comparativo com um jogador "funcional" do mercado atual (ex: um volante com métricas similares às de Casemiro ou Rodri) entrega um valor tangível imediato para a tomada de decisão de contratação.

## Arquétipos Modernos para o Dataset

Para cobrir as principais demandas do futebol de alto nível, focaremos na inclusão dos seguintes perfis estratégicos:

### Extremos de Alta Intensidade
* **Referências:** Vinicius Jr, Kylian Mbappé, Phil Foden.
* **Valor no Modelo:** Estabelecem o limite superior para testes de velocidade e aceleração, calibrando a régua de avaliação para atacantes de lado de campo.

### O "Motor" Moderno
* **Referências:** Rodri, Kevin De Bruyne, Jude Bellingham, Pedri.
* **Valor no Modelo:** Essenciais para avaliar a combinação de resistência cardiovascular e inteligência tática, identificando atletas capazes de performar em alta rotação durante os 90 minutos.

### Potência Física e Finalização
* **Referências:** Erling Haaland, Viktor Gyökeres, Victor Osimhen.
* **Valor no Modelo:** Validam o cruzamento entre dados antropométricos (altura/peso/massa) e eficiência técnica. Fundamental para projetar o teto de desenvolvimento físico do atleta e montar o catálogo muscular.

### Referências de Potencial (Jovens Talentos)
* **Referências:** Lamine Yamal, Endrick, Estêvão.
* **Valor no Modelo:** Oferecem uma comparação justa por faixa etária. Permitem projetar se o desempenho atual do atleta em formação é compatível com a curva de evolução apresentada por talentos globais na mesma idade.

### Laterais Ofensivos e Físicos
* **Referências:** Trent Alexander-Arnold, Achraf Hakimi, Alphonso Davies.
* **Valor no Modelo:** Essenciais para testar a dualidade do atleta moderno: capacidade de recomposição defensiva somada à criação de jogadas no terço final (cruzamentos e assistências).

### Zagueiros Construtores (Ball-Playing Defenders)
* **Referências:** William Saliba, Rúben Dias, Virgil van Dijk.
* **Valor no Modelo:** Validam a capacidade do defensor de iniciar jogadas. Cruzam dados de imposição física com técnica refinada.

### Goleiros Líberos
* **Referências:** Manuel Neuer, Alisson Becker, Mike Maignan.
* **Valor no Modelo:** Diferenciam o goleiro tradicional do goleiro moderno. Adicionam métricas de qualidade de passe e controle de bola com os pés, fundamentais para clubes que priorizam a construção desde a defesa.
