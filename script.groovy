
def testApp() { 
    echo "Testing our application" 
    // you can now run your test command here, e.g if using pytest you run 
    // sh "pytest"
}

// def buildApp() { 
//     echo "Building app with build number #${env.BUILD_NUMBER}" // env variables are available and can be accesed in groovy files.
//     // withPassword([credentialsId:'dockerhub-id', passwordVariable: 'PASS', usernameVariable:'USER']){
//     //     sh "docker build . -t YOUR_REPO_NAME:YOUR_TAG" // replace YOU_REPO_NAME and YOUR_TAG with the respective repo name and tag.
//     //     sh "echo $PASS | docker login -u $USER --password-stdin"
//     //     sh " docker push YOUR_REPO_NAME:YOUR_TAG" // replace YOU_REPO_NAME and YOUR_TAG with the respective repo name and tag.
//     // }
// }
def deployApp() { 
    echo "We will handle this in the next article!"
}
return this