pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'  // Directory to create the virtual environment
    }

    stages {
        // Checkout the source code from the SCM (e.g., Git)
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Set up Python virtual environment and install dependencies
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}  # Create virtual environment
                    source ${VENV_DIR}/bin/activate  # Activate the virtual environment
                    pip install --upgrade pip  # Upgrade pip
                    pip install flask pytest pylint  # Install required dependencies
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
                            source ${VENV_DIR}/bin/activate  # Activate virtual environment
                            ${scannerHome}/bin/sonar-scanner  # Run SonarQube scan
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
                    docker build -t flask-app-test .  # Build Docker image
                    docker run -d -p 5000:5000 flask-app-test  # Run container
                '''
            }
        }

        // Release to production (e.g., AWS CodeDeploy or Octopus)
        stage('Release') {
            steps {
                sh '''
                    echo "Releasing to production..."
                    # Example: AWS CodeDeploy (adjust to your environment)
                    aws deploy create-deployment --application-name my-app --deployment-group my-deployment-group --s3-location bucket=my-bucket,key=flask-app.zip,bundleType=zip
                '''
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
