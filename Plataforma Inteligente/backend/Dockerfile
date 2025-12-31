FROM python:3.9-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta que o servidor FastAPI está rodando
EXPOSE 8000

# Comando para rodar a aplicação
# Railway fornece a porta via variável de ambiente PORT
# Usa python main.py que já está configurado para ler a variável PORT
CMD ["python", "main.py"]
