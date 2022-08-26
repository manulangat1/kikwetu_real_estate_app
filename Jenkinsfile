pipeline { 
    agent any 
    stages { 
        stage('Build docker image') { 
            steps { 
                sh 'echo "Hello World"'
                script{ 
                   sh "docker build ./docker/local/django/Dockerfile -t manulangat/django-jenkins-pos:1.0"
                }
            }
        }
        stage('Done'){
            steps {
                echo " WOw! I'm done!"
            }
        }
        stage('Deploy staging ') { 
            steps { 
                echo 'I am deploying to staging server'
            }
        }

        stage ( 'Deploy prod') { 
            steps { 
                echo 'I am deploying to prod server'
            
            }
        }
    }
}
