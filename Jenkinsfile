pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images for backend and frontend...'
                sh 'docker build -t backend ./backend'
                sh 'docker build -t frontend ./frontend'
            }
        }

        stage('Login to ECR') {
            steps {
                echo 'Logging in to Amazon ECR...'
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
                '''
            }
        }

        stage('Tag Docker Images') {
            steps {
                echo 'Tagging Docker images...'
                sh 'docker tag backend:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:backend-latest'
                sh 'docker tag frontend:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:frontend-latest'
            }
        }

        stage('Push Docker Images') {
            steps {
                echo 'Pushing Docker images to ECR...'
                sh 'docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:backend-latest'
                sh 'docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:frontend-latest'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (params.DEPLOY_TO_KUBERNETES) {
                        echo 'Deploying to Kubernetes...'
                        sh 'kubectl apply -f dev-deployment/'
                    } else {
                        echo 'Stopping existing containers and running new ones...'
                        sh 'docker stop backend || true'
                        sh 'docker stop frontend || true'
                        sh 'docker rm backend || true'
                        sh 'docker rm frontend || true'
                        sh 'docker run -d --name backend -p 5000:5000 backend'
                        sh 'docker run -d --name frontend -p 3000:3000 frontend'
                    }
                }
            }
        }
    }

    parameters {
        booleanParam(name: 'DEPLOY_TO_KUBERNETES', defaultValue: true, description: 'Deploy to Kubernetes (true) or run Docker containers (false)')
    }
}