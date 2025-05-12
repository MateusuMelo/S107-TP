pipeline {
    agent any

    environment {

        EMAIL_DESTINO = credentials('EMAIL_DESTINO')
        SMTP_USER = credentials('SMTP_USER')
        SMTP_PASS = credentials('SMTP_PASS')

        IMAGE_NAME = 'python-app'
        DOCKER_REGISTRY = 'seu-registro-docker'
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
                        error("Dockerfile não encontrado!")
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
                }
            }
        }

        stage('Notify') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}").inside("-e EMAIL_DESTINO=${env.EMAIL_DESTINO} -e SMTP_USER=${env.SMTP_USER} -e SMTP_PASS=${env.SMTP_PASS} -v ${WORKSPACE}:/app") {
                        sh 'python /app/email_notify.py'
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
            script {
                docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}").inside("-e EMAIL_DESTINO=${env.EMAIL_DESTINO} -e SMTP_USER=${env.SMTP_USER} -e SMTP_PASS=${env.SMTP_PASS} -v ${WORKSPACE}:/app") {
                    sh 'python /app/email_notify.py'
                }
            }
        }
        unstable {
            script {
                docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}").inside("-e EMAIL_DESTINO=${env.EMAIL_DESTINO} -e SMTP_USER=${env.SMTP_USER} -e SMTP_PASS=${env.SMTP_PASS} -v ${WORKSPACE}:/app") {
                    sh 'python /app/email_notify.py'
                }
            }
        }
    }
}