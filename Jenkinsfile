pipeline { 
    agent any 
    stages { 
        stage('Build') { 
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
            }
        }

        stage ( 'Deploy prod') { 
            steps { 
                echo 'I am deploying to prod server'
            
            }
        }
    }
}
