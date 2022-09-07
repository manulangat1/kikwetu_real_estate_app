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
                    // def newVersion =  version.split('.')[0]  
                    // echo "$newVersion"
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

        stage('Commit version update') { 
            steps {
                script { 
                    withCredentials([usernamePassword(credentialsId:'github-credentials', passwordVariable:'PASS', usernameVariable:'USER')]) {
                        sh 'git config --global user.name  "emmanuelthedeveloper@gmail.com"'
                        sh 'git config --global user.email "manulangat1" '
                        sh "git status"
                        sh "git branch"
                        sh "git config --list"
                        sh "git remote set-url https://${USER}:${$PASS}@github.com/manulangat1/kikwetu_real_estate_app.git" 
                        sh "git add ."
                        sh 'git commit -m "ci-version bump" '
                        sh "git push origin HEAD:${BRANCH_NAME} "
                        echo "Done pushing to github"
                    }
                }
            }
        }
    }
}
