pipeline {
    agent any
    
    environment {
        VENV_DIR = '.venv'  // Directory to create the virtual environment
        S3_BUCKET = 'mybucketjenkins'              // Replace with your S3 bucket name
        APPLICATION_NAME = 'my_app'             // AWS CodeDeploy application name
        DEPLOYMENT_GROUP = 'new_group'     // AWS CodeDeploy deployment group name
        REGION = 'ap-southeast-2'                         // e.g., us-east-1
    }

    stages {
        // Checkout the source code from the SCM (e.g., Git)
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Install python3-venv and set up Python virtual environment
        stage('Setup Python Environment') {
            steps {
                sh '''
                    
                    
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install flask pytest pylint
                '''
            }
        }

        // Build the application (optional, depends on project requirements)
        stage('Build') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate  # Activate virtual environment
                    pip check  # Verify dependencies
                '''
            }
        }
        
        // Run unit tests to verify functionality
        stage('Run Tests') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate  # Activate virtual environment
                    python3 -m unittest discover  # Run unit tests
                '''
            }
        }
        
        // Perform code quality checks using SonarQube
        stage('Code Quality Check') {
            environment {
                scannerHome = tool 'Sonar'
            }
            steps {
                script {
                    withSonarQubeEnv('Sonar') {
                        sh '''
                            echo "checking..."
                        '''
                    }
                }
            }
        }

        // Deploy to a test environment (e.g., Docker container)
        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploying to test environment..."
                    /usr/local/bin/docker build -t flask-app-test .  # Build Docker image
                    /usr/local/bin/docker run -d -p 5001:5000 flask-app-test  # Run container
                '''
            }
        }

        // Release to production (e.g., AWS CodeDeploy or Octopus)
        stage('Release') {
            steps {
                
                   sh """
                       /usr/local/bin/aws deploy create-deployment \
                        --application-name $APPLICATION_NAME \
                        --deployment-group-name $DEPLOYMENT_GROUP \
                        --s3-location bucket=$S3_BUCKET,key=Project.zip,bundleType=zip \
                        --region $REGION \
                        """

                
            }
        }

        // Monitoring and alerting setup (e.g., Datadog)
        stage('Monitoring and Alerting') {
            steps {
                sh '''
                    echo "Configuring monitoring and alerting..."
                    # Datadog Agent setup
                    DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=YOUR_DATADOG_API_KEY DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
                    datadog-agent status  # Check agent status
                '''
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment (deactivate) after the pipeline is finished
            sh '''
                if [ -f ${VENV_DIR}/bin/deactivate ]; then
                    source ${VENV_DIR}/bin/deactivate || true
                fi
            '''
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
