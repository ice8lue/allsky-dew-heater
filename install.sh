#!/usr/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install rpi.gpio

chmod +x ./scripts/heater_ON.py ./scripts/heater_OFF.py fetchWeatherInfo.py
chmod g+x ./scripts/heater_ON.py ./scripts/heater_OFF.py fetchWeatherInfo.py

chmod g+w ./status.txt weather.txt
chgrp www-data ./status.txt weather.txt

sudo  cp  ./sudoers.txt  /etc/sudoers.d/dew_heater

pip install -r ./requirements.txt
