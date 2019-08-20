#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if [ ! -x /usr/sbin/nginx ]
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello holberton" | sudo tee  /data/web_static/releases/test/index.html > /dev/null
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "51i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart 
