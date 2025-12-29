# Guia de Instalação Completo

## Requisitos do Sistema

- **Python**: 3.8 ou superior
- **Node.js**: 16.x ou superior
- **npm**: 8.x ou superior (vem com Node.js)

## Passo a Passo

### 1. Clone ou baixe o projeto

```bash
cd "Plataforma Inteligente"
```

### 2. Configuração do Backend

```bash
# Entre na pasta do backend
cd backend

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Inicialize o banco de dados
python init_db.py

# Inicie o servidor
uvicorn main:app --reload
```

O backend estará rodando em `http://localhost:8000`

### 3. Configuração do Frontend

Abra um novo terminal:

```bash
# Entre na pasta do frontend
cd frontend

# Instale as dependências
npm install

# Inicie a aplicação
npm start
```

O frontend estará rodando em `http://localhost:3000`

## Verificação

1. **Backend**: Acesse `http://localhost:8000/docs` para ver a documentação interativa da API
2. **Frontend**: Acesse `http://localhost:3000` para usar a aplicação

## Solução de Problemas

### Erro ao instalar dependências Python

```bash
# Atualize o pip
python -m pip install --upgrade pip

# Tente novamente
pip install -r requirements.txt
```

### Erro ao instalar dependências Node

```bash
# Limpe o cache
npm cache clean --force

# Delete node_modules e package-lock.json
rm -rf node_modules package-lock.json

# Reinstale
npm install
```

### Erro de conexão com o banco de dados

- Por padrão, o sistema usa SQLite (não requer configuração)
- Se quiser usar PostgreSQL, configure o arquivo `.env` no backend

### Porta já em uso

- Backend: Altere a porta no comando `uvicorn main:app --reload --port 8001`
- Frontend: O React perguntará se deseja usar outra porta automaticamente

## Próximos Passos

1. Cadastre seu primeiro atleta
2. Explore a classificação automática
3. Visualize os relatórios e recomendações
4. Use o sistema de match para análise de compatibilidade

