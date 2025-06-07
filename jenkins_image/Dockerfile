FROM jenkins/jenkins:lts

USER root

# Atualiza os pacotes e instala dependências
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean

# Cria um link simbólico para chamar 'python' diretamente
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copia a pasta de configs do Jenkins para dentro da imagem
# Atenção: essa pasta deve estar disponível no contexto do build
COPY --chown=jenkins:jenkins jenkins_home/ /var/jenkins_home/

# Retorna ao usuário padrão do Jenkins
USER jenkins
