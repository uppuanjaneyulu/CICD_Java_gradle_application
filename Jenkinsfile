pipeline{
    agent any
    stages{
        stage("sonar quality check") {
            steps{
                script{
                    withSonarQubeEnv(credentialsId: 'sonar-scaner') {
                            sh 'chmod +x app.py'
                            sh './app.py sonarqube'
                    }
                }
            }
        }
    }
}
