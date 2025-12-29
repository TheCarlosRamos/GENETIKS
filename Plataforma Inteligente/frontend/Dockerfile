# Estágio de build
FROM node:16 AS build

WORKDIR /app

# Copia os arquivos de dependências
COPY frontend/package*.json ./

# Instala as dependências
RUN npm install

# Copia o restante da aplicação
COPY frontend/ .

# Constrói a aplicação
RUN npm run build

# Estágio de produção
FROM nginx:alpine

# Copia os arquivos construídos do estágio de build
COPY --from=build /app/build /usr/share/nginx/html

# Copia a configuração personalizada do Nginx
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
