#!/usr/bin/python

import RPi.GPIO as GPIO
from scripts.files import statusFile, tab

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
# print("Heater OFF")
GPIO.output(23, GPIO.LOW)
# GPIO.cleanup()

status = "OFF"

with open(statusFile, "w") as outfile:
    outfile.write("data")
    outfile.write(tab)
    outfile.write("0")
    outfile.write(tab)
    outfile.write("Dew heater")
    outfile.write(tab)
    outfile.write(status)
