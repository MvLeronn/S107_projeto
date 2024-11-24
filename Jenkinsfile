pipeline {
    agent any
    environment {
        FROM_EMAIL = credentials('FROM_EMAIL')  // Credenciais do e-mail remetente
        EMAIL_PASSWORD = credentials('EMAIL_PASSWORD') // Senha do e-mail remetente
    }
    stages {
        stage('Debug Workspace') {
            steps {
                echo 'Verificando o repositório...'
                sh 'git status'
                sh 'git log -1 --pretty=format:"%ae"'
            }
        }
        stage('Install') {
            steps {
                echo 'Instalando dependências...'
                sh "pip install -r requirements.txt --break-system-packages"
            }
        }
        stage('Test') {
            steps {
                echo 'Executando testes...'
                sh '''
                python3 -m unittest
                python3 tests.py
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Construindo a aplicação...'
                sh "python3 -m build"
            }
        }
        stage('Send Email Notification') {
            steps {
                echo 'Enviando notificação por e-mail...'
                script {
                    // Capturar o e-mail do autor do commit
                    def commitAuthorEmail = sh(
                        script: "git log -1 --pretty=format:'%ae'",
                        returnStdout: true
                    ).trim()

                    echo "E-mail capturado do commit: ${commitAuthorEmail}"

                    // Validar e substituir e-mail inválido
                    if (commitAuthorEmail.contains('noreply.github.com') || commitAuthorEmail.isEmpty()) {
                        echo "E-mail inválido capturado (${commitAuthorEmail}), utilizando e-mail padrão."
                        commitAuthorEmail = 'admin@domain.com' // Substitua pelo e-mail padrão correto
                    }

                    echo "E-mail final do autor do commit: ${commitAuthorEmail}"

                    // Passar o e-mail como variável de ambiente
                    withEnv([
                        'FROM_EMAIL=' + env.FROM_EMAIL,
                        'EMAIL_PASSWORD=' + env.EMAIL_PASSWORD,
                        'COMMIT_AUTHOR_EMAIL=' + commitAuthorEmail
                    ]) {
                        sh 'python3 scripts/send_email.py'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Execução do pipeline concluída.'
            archiveArtifacts artifacts: 'dist/*.tar.gz, test_report/*', fingerprint: true
        }
    }
}
