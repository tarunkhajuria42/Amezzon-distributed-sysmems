#!/usr/bin/env bash
sudo java -jar DatabaseServer-2.0-jar-with-dependencies.jar -t http -l -d -p 8124
sudo docker start amezzon_db1
sudo docker start amezzon_db2
sudo docker start amezzon_db3
sudo docker start amezzon_token