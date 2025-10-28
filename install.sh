#!/usr/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install rpi.gpio

chmod +x ./heater_ON.py ./heater_OFF.py
chmod g+x ./heater_ON.py ./heater_OFF.py

chmod g+w ./status.txt
chgrp www-data ./status.txt

sudo  cp  ./sudoers.txt  /etc/sudoers.d/dew_heater
