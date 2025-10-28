#!/usr/bin/python

import RPi.GPIO as GPIO
from files import statusFile, tab, weatherFile

# Parse weather file
with open(weatherFile, "r") as inputfile:
    lines = inputfile.readlines()

    temp = float(lines[0].split("\t")[-1].replace("\n", ""))
    dew = float(lines[1].split("\t")[-1].replace("\n", ""))

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)

# Heater should turn on if ambient temperatur is below dew point (with a 10C threshold)
if temp <= (dew + 10):
    status = "ON"
    GPIO.output(23, GPIO.HIGH)
    print("Dew heater turned ON")
else:
    status = "OFF"
    GPIO.output(23, GPIO.LOW)
    print("Dew heater turned OFF")

# Write status file
with open(statusFile, "w") as outfile:
    outfile.write("data")
    outfile.write(tab)
    outfile.write("0")
    outfile.write(tab)
    outfile.write("Dew heater")
    outfile.write(tab)
    outfile.write(status)
