#!/usr/bin/python

import RPi.GPIO as GPIO
from files import heaterLogFile, statusFile, tab
from fetchWeatherInfo import fetchWeather
from datetime import datetime

from scripts.heater import canActivate, mustCoolDown, turnOff, turnOn

# Update weather info
weather = fetchWeather()
temp = weather[0]
dew = weather[1]

# Heater should turn on if ambient temperatur is below dew point (with a 10C threshold),
# and if it is allowed to activate (not in cooldown, and enough time since last activation)
if temp <= (dew + 10) and not mustCoolDown() and canActivate():
    turnOn()
    print("Dew heater turned ON")
else:
    turnOff()


if temp <= (dew + 10) and canActivate():
    turnOn()
    print("Dew heater turned ON")
elif mustCoolDown():
    turnOff()
    print("Dew heater turned OFF")