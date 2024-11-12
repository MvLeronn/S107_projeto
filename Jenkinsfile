pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                sh "python3 -m unittest"
            }
        }
    }
}