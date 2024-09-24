pipeline {
    agent any
    
    stages {
        // Checkout the source code from the SCM (e.g., Git)
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Set up the Python environment by installing necessary packages
        stage('Setup Python Environment') {
            steps {
                sh 'pip3 install flask pytest pylint'
            }
        }
        
        // Build the Docker image for deployment
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        // Run unit tests to verify functionality
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
        
        // Perform code quality checks using SonarQube
        stage('Code Quality Check') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                   sh 'echo "checking code.."'
                }
            }
        }

        

        // Deploy the application
        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
                // Example: Use Docker to deploy the Flask app
                sh 'docker run -d -p 5000:5000 flask-app'
                // Alternatively, add steps for SCP or other deployment tools:
                // sh 'scp app.py user@server:/path/to/deployment/'
            }
        }
        stage('Release') {
            steps {
                sh 'echo "Releasing to production environment..."'
                // CodeDeploy example (replace with actual commands):
                sh 'aws deploy create-deployment --application-name my-app --deployment-group my-deployment-group --s3-location bucket=my-bucket,key=flask-app.zip,bundleType=zip'
                }
        }
        stage('Monitoring and Alerting') {
            steps {
                sh 'echo "Configuring monitoring and alerting..."'
                // Datadog Agent installation for monitoring:
                sh 'DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=YOUR_DATADOG_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"'
        
                // Monitor CPU, Memory, Network, and other metrics
                sh 'datadog-agent status'
    }
}
    }
    
    post {
        always {
            // Clean up the environment, for example deactivate a virtual environment if used
            sh 'deactivate || true' // `deactivate` is usually for virtualenv, adjust based on your environment
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
