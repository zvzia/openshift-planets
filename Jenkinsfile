pipeline {
    agent any

    stages {
        stage('Begin') {
            steps {
                echo 'Rozpoczęcie budowania'
            }
        }
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
        stage("Docker Build") {
            steps {
              sh '''
                  oc start-build -F openshift-planets --from-dir=.
              '''
            }
        }
    }
}