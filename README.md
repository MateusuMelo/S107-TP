
# 📦 S107 - Prova 2 – CI/CD com Jenkins e Docker

Este repositório contém a implementação da prova 2 da disciplina **S107 – Gerência de Configuração e Evolução de Software**, incluindo:

- Sistema com testes automatizados
- Pipeline CI/CD usando Jenkins em container
- Docker Compose com 4 containers intercomunicando
- Armazenamento de artefatos e envio de e-mails automatizado

---

## 🚀 Como executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Variável de ambiente `EMAIL_DESTINO` configurada (pode ser via `.env`)

---

### 📁 Estrutura do projeto

```
.
├── docker-compose.yml
├── jenkins_image/
│   └── Dockerfile
├── Jenkinsfile
└── ...
```

---

### 🔧 Subir os containers

```bash
docker-compose up --build
```

---

## 🧪 Pipeline Jenkins

O Jenkins roda em: [http://localhost:8080](http://localhost:8080)

### Etapas do pipeline:

1. **Build**: Constrói a imagem da aplicação
2. **Testes**: Executa os testes com `pytest` e salva relatório JUnit
3. **Empacotamento**: Gera artefato `.zip`
4. **Notificação**: Envia e-mail ao final do pipeline (usando `EMAIL_DESTINO`)
5. **Armazenamento**: Relatórios e pacotes são salvos como artefatos no Jenkins

---

## 🐳 Containers usados

| Serviço    | Tipo de imagem        | Origem                |
|------------|------------------------|------------------------|
| Jenkins    | Customizada com Python | Dockerfile (`jenkins_image/`) |
| Backend    | Publicada no Docker Hub | [`mateus/c216-l1-backend`](https://hub.docker.com/r/mateus/c216-l1-backend) |
| Frontend   | Publicada no Docker Hub | [`mateus/c216-l1-frontend`](https://hub.docker.com/r/mateus/c216-l1-frontend) |
| PostgreSQL | Oficial do Docker Hub | `postgres:latest` |
| s107-pv2   | Imagem de testes       | [`mateusumelo/s107-pv2`](https://hub.docker.com/r/mateusumelo/s107-pv2) |

---

## 🔗 Links úteis

- 🔐 [Link da imagem Jenkins no Docker Hub](https://hub.docker.com/repository/docker/mateusumelo/jenkins/general)
- 🔐 [mateusumelo/s107-pv2 – imagem com `pytest`](https://hub.docker.com/repository/docker/mateusumelo/s107-pv2/general)


