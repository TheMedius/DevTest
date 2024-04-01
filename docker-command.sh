sudo docker stop $(sudo -S docker ps -q  --filter ancestor=testcelery)
sudo docker stop $(sudo -S docker ps -q  --filter ancestor=testcelery-beat)

# Build celery
sudo docker build -f DockerFileCelery . -t testcelery:latest

# Build celery beat
#sudo docker build -f DockerFileCeleryBeat . -t testcelery-beat:latest

sudo docker run -d --restart=on-failure:5 --network=host -v /var/lib/jenkins/workspace/DevTest/:/app/ -v /tmp/:/tmp/ --name celery testcelery
#sudo docker run -d --restart=on-failure:5 --network=host -v /var/lib/jenkins/workspace/Backend/:/app/ -v /tmp/:/tmp/ testcelery-beat
