#!/usr/bin/env bash
sudo docker container rm -f appserver
sudo docker image rm -f appserver
sudo docker build -t appserver .