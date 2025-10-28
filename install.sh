#!/usr/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install rpi.gpio

chgrp www-data ./status.txt weather.txt

sudo  cp  ./sudoers.txt  /etc/sudoers.d/dew_heater

pip install -r ./requirements.txt
