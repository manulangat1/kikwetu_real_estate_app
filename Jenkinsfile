pipeline { 

    agent any
    parameters { 
        choice(name: 'Version', choices:['1.1.0', '1.2.0', '1.3.0'], description:'')
    }
    stages { 

        stage('Init') { 
            
            steps { 
                // echo "Building version ${NEW_VERSION}"
                echo "Hello, this is build number ${BUILD_NUMBER}"
            }
        }
        stage("deploy"){ 
            steps{
                echo "Deploying Version ${VERSION}"
            }
        }
    }
}
