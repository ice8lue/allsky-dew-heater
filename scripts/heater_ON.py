#!/usr/bin/python

from datetime import datetime
from heater import turnOn
from files import heaterLogFile

with open(heaterLogFile, "a") as logFile:
    logFile.write(f"{datetime.now().time()}: Heater mode set to ON\n")

turnOn()