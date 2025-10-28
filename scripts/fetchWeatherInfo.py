#!/usr/bin/python

import urllib.request
import json
import os
from dotenv import load_dotenv


load_dotenv()

apiUrl = f"https://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={os.getenv('LOCATION')}&aqi=no"

with urllib.request.urlopen(apiUrl) as url:
    data = json.loads(url.read().decode())

temp = data["current"]["temp_c"]
dewpoint = data["current"]["dewpoint_c"]

# Write output file
tab = "\t"
newline = "\n"
weatherFile = "/home/adfr/allsky-dew-heater/weather.txt"

with open(weatherFile, "w") as outfile:
    outfile.write("data")
    outfile.write(tab)
    outfile.write("0")
    outfile.write(tab)
    outfile.write("Temperature Outside")
    outfile.write(tab)
    outfile.write(str(temp))
    outfile.write(newline)

    outfile.write("data")
    outfile.write(tab)
    outfile.write("0")
    outfile.write(tab)
    outfile.write("Dew Point")
    outfile.write(tab)
    outfile.write(str(dewpoint))
