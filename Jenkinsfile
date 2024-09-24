pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh 'pip3 install flask pytest pylint'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh ' python3 -m unittest discover'
            }
        }
        
        stage('Code Quality Check') {
            
            environment 
            {
                scannerHome = tool 'Sonar'
            }
            steps 
            {
                script {
                    withSonarQubeEnv('Sonar') {
                         sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=main"
                    }
                }
            }
            
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
                // Add your deployment steps here
                // For example, you might use scp to copy files to a server:
                // sh 'scp app.py user@server:/path/to/deployment/'
            }
        }
    }
    
    post {
        always {
            sh 'deactivate'
        }
    }
}
