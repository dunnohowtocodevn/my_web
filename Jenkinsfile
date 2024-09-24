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
            steps {
                sh '''
                    #!/bin/bash
                    export PATH=$PATH:/Users/macbook/Library/Python/3.9/bin
                    pyflint your_script.py
                    '''
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
