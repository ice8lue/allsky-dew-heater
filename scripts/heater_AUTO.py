#!/usr/bin/python

import RPi.GPIO as GPIO
from files import heaterLogFile, statusFile, tab
from fetchWeatherInfo import fetchWeather
from datetime import datetime

from heater import canActivate, mustCoolDown, turnOff, turnOn

# Update weather info
weather = fetchWeather()
temp = weather[0]
dew = weather[1]

# Heater should turn ON if temperature is within 10 degrees of dew point
# and last activation was more than an hour ago.
if temp <= (dew + 10) and canActivate():
    turnOn()
    print("Dew heater turned ON")

# Heater should turn OFF if it has been ON for more than 15 minutes
# or temperature is more than 10 degrees above dew point.
elif mustCoolDown() or temp > (dew + 10):
    turnOff()
    print("Dew heater turned OFF")

# Otherwise, keeo heater state unchanged