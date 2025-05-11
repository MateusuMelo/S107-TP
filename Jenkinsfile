pipeline {
    agent any

    environment {
        // Configurações de email (configurar no Jenkins)
        EMAIL_DESTINO = credentials('EMAIL_DESTINO')
        SMTP_USER = credentials('SMTP_USER')
        SMTP_PASS = credentials('SMTP_PASS')

        // Nome da imagem Docker
        IMAGE_NAME = 'python-app'
    }

    stages {
        // Estágio 1: Obter o código-fonte
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Estágio 2: Construir a imagem Docker
        stage('Build Docker Image') {
            steps {
                script {
                    if (!fileExists('Dockerfile')) {
                        error("Dockerfile não encontrado! Por favor, verifique se o arquivo está na raiz do projeto.")
                    }
                    sh "docker build -t ${env.IMAGE_NAME} ."
                }
            }
        }

        // Estágio 3: Executar testes
        stage('Run Tests') {
            steps {
                script {
                    sh """
                    docker run --rm \
                    -v ${WORKSPACE}:/app \
                    ${env.IMAGE_NAME} \
                    sh -c 'pytest --junitxml=report.xml'
                    """
                    junit 'report.xml'
                }
            }
            post {
                always {
                    archiveArtifacts 'report.xml'
                }
            }
        }

        // Estágio 4: Criar pacote ZIP
        stage('Build Package') {
            steps {
                sh """
                docker run --rm \
                -v ${WORKSPACE}:/app \
                ${env.IMAGE_NAME} \
                sh -c 'zip -r /app/project.zip /app -x "*.git*"'
                """
                archiveArtifacts 'project.zip'
            }
        }

        // Estágio 5: Enviar notificação
        stage('Notify') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    sh """
                    docker run --rm \
                    -e EMAIL_DESTINO=${env.EMAIL_DESTINO} \
                    -e SMTP_USER=${env.SMTP_USER} \
                    -e SMTP_PASS=${env.SMTP_PASS} \
                    ${env.IMAGE_NAME} \
                    python email_notify.py
                    """
                }
            }
        }
    }

    // Ações pós-build
    post {
        failure {
            echo "A pipeline falhou. Por favor, verifique os logs para identificar o problema."
        }
        success {
            echo "Pipeline executada com sucesso!"
        }
    }
}