pipeline {
    agent any

    environment {
        // Set these variables in Jenkins configuration
        EMAIL_DESTINO = credentials('EMAIL_DESTINO')
        SMTP_USER = credentials('SMTP_USER')
        SMTP_PASS = credentials('SMTP_PASS')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                script {
                    // Assuming you have a container image available in your workspace
                    // that contains Python and can be executed directly
                    sh '''
                        # Use the container image you have in your project root
                        # This is a placeholder - adjust to how your container should be run
                        ./python-container/run.sh install-dependencies
                        ./python-container/run.sh run-tests
                    '''
                    junit 'report.xml' // Assuming your tests generate this file
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.xml', fingerprint: true
                }
            }
        }

        stage('Build') {
            steps {
                sh '''
                    # Install zip if not present
                    if ! command -v zip &> /dev/null; then
                        echo "zip not found, attempting to install..."
                        sudo apt-get update && sudo apt-get install -y zip || true
                    fi
                    zip -r project.zip . -x "*.git*"
                '''
                archiveArtifacts artifacts: 'project.zip', fingerprint: true
            }
        }

        stage('Notify') {
            steps {
                script {
                    // Run the notification inside your Python container
                    sh '''
                        ./python-container/run.sh install-email-deps
                        ./python-container/run.sh send-notification
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
        failure {
            echo 'Pipeline failed'
        }
        success {
            echo 'Pipeline succeeded'
        }
    }
}