#!/bin/bash

curl -o nginx.conf https://github.com/Kaiyrzhan01/TechOrda_fork/blob/main/docker/docker-bind/nginx.conf

docker run -d --name jusan-docker-bind -p 7777:80 \
  -v "$(pwd)/nginx.conf":/etc/nginx/nginx.conf \
  nginx:mainline

docker ps

docker logs jusan-docker-bind

