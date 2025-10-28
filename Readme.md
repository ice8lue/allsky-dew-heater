# AllskyCamera Dew Heater Control

## Installation

1. Clone this repo to your user root: `$ git clone https://github.com/ice8lue/allsky-dew-heater`
2. Run install: `$ cd allsky-dew-heater; ./install.sh`
3. Add [WeatherAPI](https://www.weatherapi.com) key and location info to `.env`
4. Add the following to your Allsky settings > WebUI Configuration > System Page Additions: `/home/adfr/allsky-dew-heater/buttons.txt:/home/adfr/allsky-dew-heater/status.txt:/home/adfr/allsky-dew-heater/weather.txt`
5. Setup a custom script for `/home/adfr/allsky-dew-heater/scripts/heater_AUTO.py` in Module Manager > Periodic Jobs