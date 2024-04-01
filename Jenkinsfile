pipeline {
    agent any
    stages {
         stage('Setup Python Virtual Environment'){
            steps {
                sh '''
                    chmod +x envsetup.sh
                    ./envsetup.sh
                    '''
            }
        }
        stage('Setup gunicorn service'){
            steps {
                sh '''
                    chmod +x gunicorn.sh
                    ./gunicorn.sh
                    '''
            }
        }
        stage('Setup Nginx'){
            steps {
                sh '''
                    chmod +x nginx.sh
                    ./nginx.sh
                    '''
            }
        }
        stage('Permissions'){
            steps {
                sh '''
                    sudo chmod -R 777 /var/lib/jenkins/workspace/DevTest
                    '''
            }
        }
        stage('System Services'){
            steps {
                sh '''
                    chmod +x services.sh
                    ./services.sh
                    '''
            }
        }
    }
}
