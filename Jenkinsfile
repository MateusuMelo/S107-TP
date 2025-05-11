pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10-slim'
    }

    tools {
        // Configura a instalação do Docker que você definiu nas Global Tools Configuration do Jenkins
        docker 'default-docker'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run in Docker') {
            steps {
                script {
                    docker.withRegistry('', '') { // Opcional: configura credenciais para registry
                        docker.image(env.DOCKER_IMAGE).inside('-v ${WORKSPACE}:/app') {
                            sh '''
                                cd /app
                                pip install --upgrade pip
                                pip install -r requirements.txt pytest
                                pytest --junitxml=report.xml
                            '''
                        }
                    }
                    junit 'report.xml'
                }
            }
        }

        stage('Build Package') {
            steps {
                script {
                    docker.withRegistry('', '') {
                        docker.image(env.DOCKER_IMAGE).inside('-v ${WORKSPACE}:/app') {
                            sh '''
                                cd /app
                                apt-get update && apt-get install -y zip
                                zip -r project.zip . -x "*.git*"
                            '''
                        }
                    }
                    archiveArtifacts 'project.zip'
                }
            }
        }
    }
}