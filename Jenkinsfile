pipeline {
    agent any

    stages {
        stage('Install') {
            steps{
                echo 'Installing requirements...'
                sh "pip install -r requirements.txt --break-system-packages"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                python3 -m unittest
                python3 tests.py
                '''
            }
        }
        stage('Build'){
            steps{
                echo 'Building and generating test report'
                sh "python3 -m build"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'dist/*tar.gz, test_report/*', fingerprint: true
        }
    }
}