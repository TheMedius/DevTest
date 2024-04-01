#!/bin/bash

sudo cp -rf app.conf /etc/nginx/conf.d

sudo usermod -a -G root www-data

chmod 755 /var/lib/jenkins/workspace/DevTest

sudo nginx -t

sudo systemctl reload nginx

sudo systemctl restart nginx

sudo systemctl status nginx
