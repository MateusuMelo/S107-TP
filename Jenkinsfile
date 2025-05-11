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

        stage('🧪 Run Tests') {
            steps {
                script {
                    withEnv(['PYTHONUNBUFFERED=1']) {
                        sh '''
                        python3 -m pip install --upgrade pip
                        pip install pytest
                        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                        pytest --junitxml=report.xml
                        '''
                    }
                }
            }
            post {
                always {
                    junit 'report.xml'
                    archiveArtifacts artifacts: 'report.xml', fingerprint: true
                }
            }
        }

        stage('📦 Build Project') {
            steps {
                sh '''
                sudo apt-get update
                sudo apt-get install -y zip
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
