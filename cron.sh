#!/bin/bash

pipenv shell
flask importers import 

#echo "my cronjob is working!" >> /home/vid/WWW/lotoes-master/cron.txt