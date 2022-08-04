pipeline{ 
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
    }
    post { 
        success { 
            echo "I'm always!"
        }

        failure { 
            echo "Build failed"
        }
    }
    }
