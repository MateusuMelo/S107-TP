pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10-slim'
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
                    // Usando a sintaxe correta para o Docker Tool
                    docker.withTool('docker') {
                        docker.withRegistry('', '') {
                            docker.image(env.DOCKER_IMAGE).inside('-v ${WORKSPACE}:/app') {
                                sh '''
                                    cd /app
                                    pip install --upgrade pip
                                    pip install -r requirements.txt pytest
                                    pytest --junitxml=report.xml
                                '''
                            }
                        }
                    }
                    junit 'report.xml'
                }
            }
        }

        stage('Build Package') {
            steps {
                script {
                    docker.withTool('docker') {
                        docker.withRegistry('', '') {
                            docker.image(env.DOCKER_IMAGE).inside('-v ${WORKSPACE}:/app') {
                                sh '''
                                    cd /app
                                    apt-get update && apt-get install -y zip
                                    zip -r project.zip . -x "*.git*"
                                '''
                            }
                        }
                    }
                    archiveArtifacts 'project.zip'
                }
            }
        }
    }
}