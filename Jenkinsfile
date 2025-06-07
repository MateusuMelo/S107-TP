pipeline {
    agent any

    environment {
        IMAGE_NAME = 'python-app'
        SMTP_USER = credentials('SMTP_USER')
        SMTP_PASSWORD = credentials('SMTP_PASS')
        EMAIL_TO = credentials('EMAIL_DESTINO')
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
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}").inside('-v ${WORKSPACE}:/app') {
                            sh 'pytest'
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
    }

    post {
        always {
            sh 'docker system prune -f || true'
        }
        success {
            emailext (
                subject: "✅ SUCCESS - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2>Pipeline concluído com sucesso!</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Console:</b> <a href="${env.BUILD_URL}console">Link</a></p>
                """,
                to: "${env.EMAIL_TO}",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "❌ FAILED - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2 style="color:red">Falha no pipeline!</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Erro:</b> Verifique o <a href="${env.BUILD_URL}console">log</a></p>
                """,
                to: "${env.EMAIL_TO}",
                mimeType: 'text/html'
            )
        }
        unstable {
            emailext (
                subject: "⚠️ UNSTABLE - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2 style="color:orange">Testes falharam (build instável)</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Detalhes:</b> <a href="${env.BUILD_URL}testReport">Relatório</a></p>
                """,
                to: "${env.EMAIL_TO}",
                mimeType: 'text/html'
            )
        }
    }
}