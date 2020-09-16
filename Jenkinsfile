pipeline {
  environment {
    imagename = "benspelledabc/djangosite"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/benspelledabc/djangosite.git', branch: 'develop', credentialsId: 'ben-github-global'])
        //git([url: 'https://github.com/benspelledabc/djangosite.git', branch: 'master', credentialsId: 'ben-github-global'])
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            //on develop branch, we are only going to push to latest
            //master will push to some other special sauce
            dockerImage.push("0.$BUILD_NUMBER")
            dockerImage.push('latest')
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        //we may not have pushed them all, but we're going to clean them all up
        sh "docker rmi $imagename:0.$BUILD_NUMBER"
        sh "docker rmi $imagename:latest"
      }
    }
  }
}
