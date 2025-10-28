#!/usr/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install rpi.gpio

chmod g+x ./heater_ON.py
chmod g+x ./heater_OFF.py

chmod g+w ./status.txt
chgrp www-data ./status.txt

sudo  cp  ./dew-heater-sudoers.txt  /etc/sudoers.d
