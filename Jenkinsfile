pipeline {
    agent any

    environment {
        IMAGE_NAME = 'python-app'
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
                    junit 'reports/report.xml'
                    archiveArtifacts artifacts: 'reports/report.xml', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f || true'
            // Limpeza adicional
            sh 'docker container prune -f || true'
            sh 'docker image prune -f || true'
        }
        success {
            emailext (
                subject: "✅ Pipeline SUCCESS - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2>Pipeline executado com sucesso!</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Número do Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Console:</b> <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></p>
                """,
                to: 'seu-email@dominio.com',  // Substitua pelo e-mail real
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "❌ Pipeline FAILED - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2 style="color:red">Falha no pipeline!</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Número do Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Console:</b> <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></p>
                <p><b>Cause:</b> Verifique os logs para detalhes</p>
                """,
                to: 'seu-email@dominio.com',  // Substitua pelo e-mail real
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                mimeType: 'text/html'
            )
        }
        unstable {
            emailext (
                subject: "⚠️ Pipeline UNSTABLE - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2 style="color:orange">Pipeline instável!</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Número do Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Console:</b> <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></p>
                <p><b>Possível causa:</b> Testes falharam, mas não quebraram o build</p>
                """,
                to: 'seu-email@dominio.com',  // Substitua pelo e-mail real
                recipientProviders: [[$class: 'DevelopersRecipientProvider']],
                mimeType: 'text/html'
            )
        }
    }
}