#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
print("Heater ON")
GPIO.output(23, GPIO.HIGH)
# GPIO.cleanup()

tab = "\t"
status = "ON"
statusFile = "/home/adfr/allsky-dew-heater/status.txt"

with open(statusFile, "w") as outfile:
    outfile.write("data")
    outfile.write(tab)
    outfile.write("0")
    outfile.write(tab)
    outfile.write("Dew heater status")
    outfile.write(tab)
    outfile.write(status)
