pipeline {
    agent any
    statges{
        satge("sonar quality check") {
            steps{
                script{
                    withSonarQubeEnv(credentialsId: 'sonar-token') {
                            sh 'chmod +x gradlew'
                            sh './gradlew sonarqube'
                }
            }
        }
    }
}
