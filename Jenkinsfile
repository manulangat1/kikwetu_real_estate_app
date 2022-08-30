def gv 
pipeline { 

    agent any
    // parameters { 
    //     choice(name: 'Version', choices:['1.1.0', '1.2.0', '1.3.0'], description:'')
    // }
    stages { 

        stage('Init') { 
            
            steps { 
                script { 
                    gv = load "script.groovy"
                }
            }
        }

        stage('build') { 
            steps{
                scripts { 
                    gv.buildApp()
                }
            }
        }

        stage("deploy"){ 
            steps{
                echo "Deploying Version ${VERSION}"
            }
        }
    }
}
