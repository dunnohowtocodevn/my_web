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
               
            }
        }
        
        stage('Build') {
            steps {
            
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
        
        stage('Code Quality Check') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    withSonarQubeEnv('Sonar') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        // Deploy to a test environment
        stage('Deploy') {
            steps {
                sh 'echo "Deploying to test environment..."'
                sh 'docker build -t flask-app-test .'
                sh 'docker run -d -p 5000:5000 flask-app-test'
            }
        }

        // Release to production
        stage('Release') {
            steps {
                sh 'echo "Releasing to production..."'
                sh 'aws deploy create-deployment --application-name my-app --deployment-group my-deployment-group --s3-location bucket=my-bucket,key=flask-app.zip,bundleType=zip'
            }
        }

        // Configure monitoring and alerting for the production environment
        stage('Monitoring and Alerting') {
            steps {
                sh 'echo "Configuring monitoring and alerting..."'
                sh 'DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=YOUR_DATADOG_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"'
                sh 'datadog-agent status'
            }
        }
    }
    
    post {
        always {
            sh 'deactivate || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
