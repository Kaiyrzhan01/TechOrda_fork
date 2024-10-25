#!/bin/bash

docker build -t nginx:jusan-dockerfile .

docker images

docker run -d --name jusan-dockerfile -p 6060:80 nginx:jusan-dockerfile

docker ps
