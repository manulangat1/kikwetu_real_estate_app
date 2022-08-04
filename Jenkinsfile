pipeline{ 
    agent any 
    enviroments {
        NEW_VERSION  = '1.3.0'
    }
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
            when { 
                BRANCH_NAME == 'staging'
            }
            steps { 
                echo 'I am deploying to staging server'
            }
        }

        stage ( 'Deploy prod') { 
            when { 
                BRANCH_NAME == 'master'  && CODE_CHANGES == true
            }
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
