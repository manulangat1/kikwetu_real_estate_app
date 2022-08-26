pipeline { 
    agent any 
    enviroment{
        NEW_VERSION = "1.2.34"
    }
    stages { 
        stage('Build docker image') { 
            steps { 
                sh 'echo "Hello World"'
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
                echo "I am deploying version number ${NEW_VERSION}"
            }
        }

        stage ( 'Deploy prod') { 
            steps { 
                echo 'I am deploying to prod server'
                echo "I am deploying version number ${NEW_VERSION}"
            
            }
        }
    }
}
