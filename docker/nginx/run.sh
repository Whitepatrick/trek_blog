#!/bin/bash

sudo docker rm nginx
sudo docker build -t nginx $HOME/workspace/trek_blog/docker/nginx/. && \
sudo docker run --name nginx \
                       -p 80:80 \
                       -p 443:443 \
                       --net host \
                       nginx
