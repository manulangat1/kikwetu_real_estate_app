def gv 
pipeline { 

    agent any
    parameters { 
        choice(name: 'Version', choices:['1.1.0', '1.2.0', '1.3.0'], description:'')
    }
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
            when { 
                BRANCH_NAME == 'staging'
            }
            steps{
                script { 
                    gv.buildApp()
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
