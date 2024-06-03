#!/usr/bin/env bash

# Instl Nginx if not exisit
if ! command -v nginx &>/dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Make directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

# touch HTML file
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

# Update Nginx config
config='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}'
sed -i "38i $config" /etc/nginx/sites-available/default

service nginx restart

exit 0

