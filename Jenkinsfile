#!usr/bin/env groovy

@Library('jenkins-shared-library')
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
                    // gv.buildApp()
                    buildImage "image_name:1.0"
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
