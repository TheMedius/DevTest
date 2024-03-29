#!/bin/bash
echo "----------------------------------------------NGINX------------------------------------------------------------------------"
sudo systemctl start nginx
sudo systemctl status nginx
#echo "----------------------------------------------CELERY------------------------------------------------------------------------"
#sudo docker start celery
#celery=$(sudo -S docker ps -q  --filter ancestor=devtest)
#sudo docker update --restart unless-stopped $celery
#sudo docker update --restart unless-stopped $voicebot
#sudo docker ps
#echo "----------------------------------------------DAPHNE------------------------------------------------------------------------"
#sudo systemctl start daphne
#sudo systemctl status daphne
echo "----------------------------------------------GUNICORN----------------------------------------------------------------------"
sudo systemctl start gunicorn
sudo systemctl status gunicorn
#echo "----------------------------------------------CELERY-----------------------------------------------------------------------"
#sudo docker exec celerymain celery -A medius.celery_app purge -f
#sudo docker restart $(sudo -S docker ps -q  --filter ancestor=devtest)
#sudo docker ps
#echo "----------------------------------------------CLEAR QUEUE------------------------------------------------------------------"
#sudo docker exec celerymain celery -A medius.celery_app purge -f
