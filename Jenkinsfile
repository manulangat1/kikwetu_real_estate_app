pipeline{ 
    agent any 
    // enviroment {
    //     NEW_VERSION  = '1.3.0'
    // }
    stages { 
        stage('Build') { 
            steps { 
                sh 'echo "Hello World"'
            }
        }
        stage('Done'){
            steps {
                echo " WOw! I'm done!"
                echo "Building version ${NEW_VERSION}"
            }
        }
        stage('Deploy staging ') { 
            // when { 
            //     BRANCH_NAME == 'staging'
            // }
            steps { 
                echo 'I am deploying to staging server'
            }
        }

        stage ( 'Deploy prod') { 
            // when { 
            //     BRANCH_NAME == 'master'  
            // }
            steps { 
                echo 'I am deploying to prod server'
            
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
