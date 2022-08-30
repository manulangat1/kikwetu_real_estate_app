pipeline { 

    enviroment{ 
        NEW_VERSION = "3.4.5"
    }
    stages { 
        stage('Init') { 
            steps { 
                echo "Building version ${NEW_VERSION}"
                echo "Hello, this is build number ${BUILD_NUMBER}"
            }
        }
        // stage('Build docker image') { 
        //     steps { 
        //         sh 'echo "Hello World"'
        //         script{ 
        //         //    
        //         withCredentials([ 
        //             usernamePassword(credentials:'docker-hub-credentials', usernameVariable:USER, passwordVariable:PASSWORD)
        //         ]) { 
        //             sh "docker build . -t YOUR_IMAGE_NAME"
        //             sh "echo $PASSORD | docker login -u $USER --password-stdin"
        //             sh "docker push YOUR_IMAGE_NAME"
        //         }
        //         }
        //     }
        // }
    }
}
