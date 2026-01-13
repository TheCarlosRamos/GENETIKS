# Análise Técnica: Evolução da Metodologia de Coleta de Dados

## Contexto
Atualmente, a plataforma opera com um sistema de avaliação baseado em percepção subjetiva, onde o usuário atribui notas de 1 a 10 para as habilidades do atleta.

Embora funcional para um primeiro estágio, este documento visa levantar pontos de atenção sobre como essa metodologia impacta a precisão dos nossos algoritmos de Ciência de Dados e sugerir uma transição para métricas absolutas.

## O Desafio da Subjetividade (Por que mudar?)

### 1. A Variabilidade do Avaliador (Viés Humano)
O principal obstáculo de escalas 1-10 é a falta de um padrão universal. A nota "8" dada por um pai orgulhoso pode equivaler, tecnicamente, à nota "4" de um olheiro profissional exigente.
* **Impacto no Negócio:** Isso gera "ruído" no banco de dados. Sem um critério unificado, o algoritmo não consegue diferenciar com segurança um talento real de um dado superestimado, comprometendo a promessa de "classificação inteligente" do projeto.

### 2. Dificuldade de Cruzamento com o Futebol Profissional
Nosso objetivo é comparar atletas da base com estrelas do mercado (ex: Vinicius Jr., Haaland). O futebol profissional não utiliza notas subjetivas; ele utiliza métricas quantitativas (km/h, metros percorridos, percentual de acerto).
* **Impacto Técnico:** É estatisticamente impreciso cruzar uma "Nota 9 em Velocidade" (dado abstrato) com "36.5 km/h" (dado real). Para o "Padrão de Equivalência" funcionar, as unidades de medida precisam conversar entre si.

### 3. Tangibilidade da Evolução
Para o cliente (atleta/família), ver sua nota subir de "6" para "7" é vago.
* **Impacto no Produto:** Ao utilizarmos dados reais (ex: baixar o tempo de sprint de 5.2s para 4.8s), a evolução torna-se incontestável. Isso reforça a autoridade da plataforma como uma ferramenta de alta performance e mentoria baseada em fatos, não em opiniões.

## A Proposta: Adoção de Métricas Quantitativas (Sistema SI)

A sugestão é substituir gradualmente os inputs de opinião por inputs de fatos mensuráveis. O sistema (Backend) ficaria responsável por processar esse dado bruto e, internamente, calcular a nota de 1 a 10 para exibir nos gráficos.

Isso transfere a responsabilidade da avaliação do "olho humano" para o "algoritmo", garantindo imparcialidade.

## Exemplos de Transição

### Cenário 1: Avaliação de Velocidade
* **Modelo Atual:** Slider de 1 a 10.
* **Modelo Sugerido:** Tempo cronometrado em tiro de 30 metros (Input em Segundos).

### Cenário 2: Avaliação de Resistência
* **Modelo Atual:** Slider de 1 a 10.
* **Modelo Sugerido:** Distância percorrida em 12 minutos (Teste de Cooper) ou Nível atingido no Yo-Yo Test.

---

> "A precisão dos dados é o alicerce para construirmos o 'Centro Futurístico' que a Datta Genetiks propõe ser."
