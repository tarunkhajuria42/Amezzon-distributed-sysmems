#!/usr/bin/env bash
sudo docker container prune
sudo docker run -d -p 3331:3306 --name amezzon_db1 cdedonder/amezzon_db:latest --bind-address=*
sudo docker run -d -p 3332:3306 --name amezzon_db2 cdedonder/amezzon_db:latest --bind-address=*
sudo docker run -d -p 3333:3306 --name amezzon_db3 cdedonder/amezzon_db:latest --bind-address=*
sudo docker run -d -p 4444:3306 --name amezzon_token cdedonder/amezzon_token:latest --bind-address=*