pipeline {
    agent any

    environment {
        EMAIL_DESTINO = credentials('EMAIL_DESTINO')
        SMTP_USER = credentials('SMTP_USER')
        SMTP_PASS = credentials('SMTP_PASS')
    }

    stages {
        stage('📥 Checkout code') {
            steps {
                checkout scm
            }
        }

        stage('🐳 Build Docker image') {
            steps {
                script {
                    // Build da imagem Docker local (Dockerfile na raiz)
                    dockerImage = docker.build("custom-python-image")
                }
            }
        }

        stage('🧪 Run Tests') {
            agent {
                docker {
                    image "custom-python-image"
                    args "-u root"
                }
            }
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install pytest
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                pytest --junitxml=report.xml
                '''
            }
            post {
                always {
                    junit 'report.xml'
                    archiveArtifacts artifacts: 'report.xml', fingerprint: true
                }
            }
        }

        stage('📦 Build Project') {
            agent {
                docker {
                    image "custom-python-image"
                    args "-u root"
                }
            }
            steps {
                sh '''
                apt-get update && apt-get install -y zip
                zip -r project.zip . -x '*.git*'
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'project.zip', fingerprint: true
                }
            }
        }

        stage('✉️ Send Notification') {
            when {
                expression { currentBuild.currentResult ==~ /SUCCESS|FAILURE|UNSTABLE/ }
            }
            agent {
                docker {
                    image "custom-python-image"
                    args "-u root"
                }
            }
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install secure-smtplib
                python3 email_notify.py
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed.'
        }
        success {
            echo '✅ Build succeeded.'
        }
    }
}
