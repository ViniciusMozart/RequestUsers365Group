# Usar uma imagem base do Python 3.8
FROM python:3.8

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o script python para o diretório de trabalho
COPY RequestUsers.py .
COPY requirements.txt .
COPY data /app/data
# Instalar os pacotes necessários usando o pip
RUN pip install requests msal
RUN pip install -r requirements.txt
# Definir as variáveis de ambiente usando os argumentos passados na construção da imagem
ARG TENANT_ID
ARG CLIENT_ID
ARG CLIENT_SECRET
ARG GROUP_ID

ENV TENANT_ID=$TENANT_ID
ENV CLIENT_ID=$CLIENT_ID
ENV CLIENT_SECRET=$CLIENT_SECRET
ENV GROUP_ID=$GROUP_ID

# Executar o script python quando o contêiner for iniciado
CMD ["python", "RequestUsers.py"]
