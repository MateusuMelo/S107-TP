pipeline {
    agent any

    environment {
        // Configurações de email (usando as credenciais exatas que você tem)
        EMAIL_DESTINO = credentials('EMAIL_DESTINO')
        SMTP_USER = credentials('SMTP_USER')
        SMTP_PASS = credentials('SMTP_PASS')

        // Nome da imagem Docker
        IMAGE_NAME = 'python-app'
        DOCKER_REGISTRY = 'seu-registro-docker' // Opcional para deploy
    }

    options {
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    if (!fileExists('Dockerfile')) {
                        error("Dockerfile não encontrado! Por favor, verifique se o arquivo está na raiz do projeto.")
                    }
                    docker.build("${env.IMAGE_NAME}:${env.BUILD_ID}")
                    sh "docker tag ${env.IMAGE_NAME}:${env.BUILD_ID} ${env.IMAGE_NAME}:latest"
                }
            }
            post {
                success { echo "Imagem Docker construída com sucesso!" }
                failure { echo "Falha ao construir a imagem Docker" }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}").inside('-v ${WORKSPACE}:/app') {
                            sh 'pytest --junitxml=report.xml || true'
                        }
                        junit 'report.xml'
                    } catch (Exception e) {
                        echo "Erro nos testes: ${e}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
                    script {
                        if (currentBuild.result == 'UNSTABLE') {
                            emailext (
                                subject: "⚠️ Pipeline ${env.JOB_NAME} - Testes instáveis (Build #${env.BUILD_NUMBER})",
                                body: "Alguns testes falharam. Verifique o relatório: ${env.BUILD_URL}testReport/",
                                to: env.EMAIL_DESTINO,
                                from: env.SMTP_USER,
                                replyTo: env.SMTP_USER,
                                smtpUser: env.SMTP_USER,
                                smtpPassword: env.SMTP_PASS
                            )
                        }
                    }
                }
            }
        }

        stage('Notify') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    emailext (
                        subject: "✅ Pipeline ${env.JOB_NAME} - Sucesso (Build #${env.BUILD_NUMBER})",
                        body: "Pipeline executada com sucesso!\n\nDetalhes: ${env.BUILD_URL}",
                        to: env.EMAIL_DESTINO,
                        from: env.SMTP_USER,
                        replyTo: env.SMTP_USER,
                        smtpUser: env.SMTP_USER,
                        smtpPassword: env.SMTP_PASS
                    )
                }
            }
        }

        stage('Push to Registry') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry("https://${env.DOCKER_REGISTRY}", 'docker-registry-creds') {
                        docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}").push()
                        docker.image("${env.IMAGE_NAME}:latest").push()
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f || true'
        }
        failure {
            emailext (
                subject: "❌ Pipeline ${env.JOB_NAME} - Falhou (Build #${env.BUILD_NUMBER})",
                body: "A pipeline falhou. Por favor, verifique os logs.\n\nDetalhes: ${env.BUILD_URL}",
                to: env.EMAIL_DESTINO,
                from: env.SMTP_USER,
                replyTo: env.SMTP_USER,
                smtpUser: env.SMTP_USER,
                smtpPassword: env.SMTP_PASS
            )
        }
        unstable {
            emailext (
                subject: "⚠️ Pipeline ${env.JOB_NAME} - Instável (Build #${env.BUILD_NUMBER})",
                body: "A pipeline está instável (alguns testes falharam).\n\nDetalhes: ${env.BUILD_URL}testReport/",
                to: env.EMAIL_DESTINO,
                from: env.SMTP_USER,
                replyTo: env.SMTP_USER,
                smtpUser: env.SMTP_USER,
                smtpPassword: env.SMTP_PASS
            )
        }
    }
}