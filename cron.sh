#!/bin/bash

cd /home/vid/WWW/lotoes-master
pipenv run flask importers import > /home/vid/WWW/lotoes-master/cron.txt

#ls -l >> /home/vid/WWW/lotoes-master/cron.txt
