# 1. Usar uma imagem oficial do Python 3.11
FROM python:3.11-slim

# 2. Definir a pasta de trabalho dentro do container
WORKDIR /app

# 3. Copiar o arquivo de requisitos para dentro do container
COPY requirements.txt .

# 4. Instalar as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo o seu código para dentro do container
COPY . .

# 6. Expor a porta que o Streamlit usa
EXPOSE 8501

# 7. Comando para rodar o app quando o container iniciar
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]