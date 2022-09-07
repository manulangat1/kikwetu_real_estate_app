#!usr/bin/env groovy

@Library('jenkins-shared-library')
def gv 
// env.WORKSPACE = pwd()
def version
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
        stage("Read version file"){
            steps { 
                script  { 
                    echo "$env.WORKSPACE"
                    // def filePath = 
                    def matcher = readFile("version.txt") =~ '<version>(.+)</version>'
                    version = matcher[0][1]
                    def newVersion =  version.split('.')[2] +1 
                    echo "$newVersion"
                    env.IMAGE_NAME = "$version-$BUILD_NUMBER"
                    
                    // echo "$imageTag"
                    echo "$IMAGE_NAME"
                }
            }
        }
        stage ('test') { 
            steps  { 
                script {
                    gv.testApp()
                }
            }
        }
        stage('build') { 
            // when { 
            //     expression { 
            //         BRANCH_NAME == 'staging'
            //     }
            //     // now
            // }
            steps{
                script { 
                    echo "Building the apps"
                    // gv.buildApp()
                    // buildImage "image_name:1.0"
                }
            }
        }

        stage("deploy"){ 
            steps{
                script { 
                    gv.deployApp()
                }
                
            }
        }
    }
}
