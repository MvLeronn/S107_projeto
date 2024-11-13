pipeline {
    agent any

    stages {
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
}