#!/usr/bin/python

from datetime import datetime
from heater import turnOff
from files import heaterLogFile

with open(heaterLogFile, "a") as logFile:
    logFile.write(f"{datetime.now().time()}: Heater mode set to OFF\n")

turnOff()