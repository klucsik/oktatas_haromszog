pipeline {
  agent any
  stages {
    stage('build docker image') {
      steps {
        sh 'docker build --network=host -t klucsik.duckdns.org:5000/3szog_gyakorlo --dns=8.8.8.8 .'
        sh 'docker push klucsik.duckdns.org:5000/3szog_gyakorlo'
      }
    }

    stage('deploy on k8s') {
      steps {
        sh 'kubectl apply -f k8s/deploy_haromszog.yaml'
        sh 'kubectl rollout status deployment/oktatas_3szog --namespace=oktatas_3szog'
      }
    }

  }
}