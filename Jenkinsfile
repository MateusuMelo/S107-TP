pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.10'
                    reuseNode true
                }
            }
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install pytest'
                sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
                sh 'pytest --junitxml=report.xml'
                junit 'report.xml'
                archiveArtifacts artifacts: 'report.xml', fingerprint: true
            }
            post {
                always {
                    echo 'Testing stage completed'
                }
            }
        }

        stage('Build') {
            steps {
                sh 'sudo apt update && sudo apt install -y zip || true'
                sh 'zip -r project.zip . -x "*.git*"'
                archiveArtifacts artifacts: 'project.zip', fingerprint: true
            }
            post {
                always {
                    echo 'Build stage completed'
                }
            }
        }

        stage('Notify') {
            steps {
                script {
                    // Assuming you have Python available on the Jenkins agent
                    // If not, you would need to use a Docker container here too
                    sh 'python -m pip install --upgrade pip'
                    sh 'pip install secure-smtplib'

                    // You'll need to set these credentials in Jenkins
                    withCredentials([
                        usernamePassword(
                            credentialsId: 'SMTP_CREDENTIALS',
                            usernameVariable: 'SMTP_USER',
                            passwordVariable: 'SMTP_PASS'
                        )
                    ]) {
                        sh '''
                            export EMAIL_DESTINO=${env.EMAIL_DESTINO}
                            export SMTP_USER=${SMTP_USER}
                            export SMTP_PASS=${SMTP_PASS}
                            python email_notify.py
                        '''
                    }
                }
            }
            post {
                always {
                    echo 'Notification stage completed'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
    }
}