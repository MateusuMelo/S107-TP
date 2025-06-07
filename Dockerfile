FROM python:3.10-slim

WORKDIR /app

# Instala dependências do sistema (zip pra build e libs essenciais)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    zip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia tudo pro container (exceto o que tá no .dockerignore)
COPY . .

# Instala dependências do Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt pytest
