import RPi.GPIO as GPIO
from files import heaterLogFile, heaterLastActiveFile, statusFile, tab
from datetime import datetime

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)

def logStatus(status):
    with open(statusFile, "w") as outfile:
        outfile.write("data")
        outfile.write(tab)
        outfile.write("0")
        outfile.write(tab)
        outfile.write("Dew heater")
        outfile.write(tab)
        outfile.write(status)

    with open(heaterLogFile, "a") as logFile:
        logFile.write(f"${datetime.now().time()}: Heater turned {status}\n")

    if status == "ON":
        with open(heaterLastActiveFile, "w") as logFile:
            now = int(datetime.now().timestamp() * 1000)
            logFile.write(str(now))

def turnOn():
    setup()
    GPIO.output(23, GPIO.HIGH)
    logStatus("ON")

def turnOff():
    setup()
    GPIO.output(23, GPIO.LOW)
    logStatus("OFF")

cooldownAfterMs = 900000  # 15 minutes
allowActivationAfterMs = 3600000  # 1 hour

def mustCoolDown():
    try:
        with open(heaterLastActiveFile, "r") as logFile:
            lastActivatedStr = logFile.readline().strip()
            if lastActivatedStr:
                lastActivated = int(lastActivatedStr)
                now = int(datetime.now().timestamp() * 1000)
                diff = now - lastActivated
                if diff >= cooldownAfterMs and diff < allowActivationAfterMs:
                    return True
    except FileNotFoundError:
        pass
    return False

def canActivate():
    try:
        with open(heaterLastActiveFile, "r") as logFile:
            lastActivatedStr = logFile.readline().strip()
            if lastActivatedStr:
                lastActivated = int(lastActivatedStr)
                now = int(datetime.now().timestamp() * 1000)
                if (now - lastActivated) >= allowActivationAfterMs:
                    return True
    except FileNotFoundError:
        pass
    return False