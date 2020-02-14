#!/usr/bin/python
import argparse
import getpass
import re

from urllib.error import HTTPError
from handler import ApiHandler

parser = argparse.ArgumentParser()

# Help output
city_help = "The name of the city to get the weather for."
state_help = "The two-character abbreviation for the state to search for the city"
country_help = "The ISO 3166 Alpha-2 country code that goes with the city and state."
system_help = "The measurement system to get results in.  Valid arguments are: imperial, metric, or kelvin"

parser.add_argument("--city", required = True, help = city_help)
parser.add_argument("--state", required = True, help = state_help)
parser.add_argument("--country", required = True, help = country_help)
parser.add_argument("--system", required = True, help = system_help)
key = getpass.getpass("Please provide your API key for openweathermap.org: ")

args = parser.parse_args()

p = re.compile('[A-Za-z]')

city = args.city
state = args.state
country = args.country
system = args.system
acceptable_units = ["imperial", "kelvin", "metric"]

if not city.isalpha():
    raise ValueError("The provided value does not match the pattern of a valid city")
if not state.isalpha():
    raise ValueError("The provided value does not match the pattern of a valid state")
if not country.isalpha():
    raise ValueError("The provided value does not match the pattern of a valid country code")
if system.lower() not in acceptable_units:
    raise ValueError("The provided system is not an acceptable value.")

if key == None or len(key.strip()) <= 0:
    raise ValueError("They key cannot be None or empty string")

#measurement_system = "imperial"
handler = ApiHandler(key)
output = {}
try:
    output = handler.get_current_weather_by_city_and_state(city, state, country, system)
except HTTPError as he:
    if he.getcode() == 404:
        print("The requested city, state, and country combination was not found in the weather api system, please try again")
    if he.getcode() == 401:
        print("The provided API key value did not provide access to the weather API.  Please provide a valid API key and try again.")
        exit(1)

if output != {}:

    requested_city = output.get("name")
    visibility = output.get("weather")[0].get("main")
    visibility_description = output.get("weather")[0].get("description")
    #
    actual_temp = output.get("main").get("temp")
    feels_like = output.get("main").get("feels_like")
    high_temp = output.get("main").get("temp_max")
    low_temp = output.get("main").get("temp_min")
    temp_system = ""
    #
    wind_speed = output.get("wind").get("speed")
    wind_angle = output.get("wind").get("deg")
    wind_direction = ""
    wind_speed_system = ""

    if system.lower() == "imperial":
        temp_system = "F"
        wind_speed_system = "miles/hour"
    elif system.lower() == "metric":
        temp_system = "C"
        wind_speed_system = "meters/second"
    elif system.lower() == "kelvin":
        temp_system = "K"
        wind_speed_system = "meters/second"
    #
    if (wind_angle == None):
        wind_direction = "UNK"
    elif (wind_angle >= 348.75 and wind_angle <= 359.99) or (wind_angle >= 0 and wind_angle <= 11.25):
        wind_direction = "N"
    elif (wind_angle >= 11.25 and wind_angle <= 33.75):
        wind_direction = "NNE"
    elif (wind_angle >= 33.75 and wind_angle <= 56.25):
        wind_direction = "NE"
    elif (wind_angle >= 56.25 and wind_angle <= 78.75):
        wind_direction = "ENE"
    elif (wind_angle >= 78.75 and wind_angle <= 101.25):
        wind_direction = "E"
    elif (wind_angle >= 101.25 and wind_angle <= 123.75):
        wind_direction = "ESE"
    elif (wind_angle >= 123.75 and wind_angle <= 146.25):
        wind_direction = "SE"
    elif (wind_angle >= 146.25 and wind_angle <= 168.75):
        wind_direction = "SSE"
    elif (wind_angle >= 168.75 and wind_angle <= 191.25):
        wind_direction = "S"
    elif (wind_angle >= 191.25 and wind_angle <= 213.75):
        wind_direction = "SSW"
    elif (wind_angle >= 213.75 and wind_angle <= 236.25):
        wind_direction = "SW"
    elif (wind_angle >= 236.25 and wind_angle <= 258.75):
        wind_direction = "WSW"
    elif (wind_angle >= 258.75 and wind_angle <= 281.25):
        wind_direction = "W"
    elif (wind_angle >= 281.25 and wind_angle <= 303.75):
        wind_direction = "WNW"
    elif (wind_angle >= 303.75 and wind_angle <= 326.25):
        wind_direction = "NW"
    elif (wind_angle >= 326.25 and wind_angle <= 348.75):
        wind_direction = "NNW"
    else:
        wind_direction = "UNK"
    """
    N       348.75 - 11.25
    NNE     11.25 - 33.75
    NE      33.75 - 56.25
    ENE     56.25 - 78.75
    E       78.75 - 101.25
    ESE     101.25 - 123.75
    SE      123.75 - 146.25
    SSE     146.25 - 168.75
    S       168.75 - 191.25
    SSW     191.25 - 213.75
    SW      213.75 - 236.25
    WSW     236.25 - 258.75
    W       258.75 - 281.25
    WNW     281.25 - 303.75
    NW      303.75 - 326.25
    NNW     326.25 - 348.75
    """


    weather_output = f"""
    Requested City:         |       {requested_city}
    -                           -
    Visibility:             |       {visibility}
    Visibility Desc         |       {visibility_description}
    -
    Actual Temp (degrees)   |       {actual_temp} {temp_system}
    Feels Like (degrees)    |       {feels_like} {temp_system}
    High Temp (degrees)     |       {high_temp} {temp_system}
    Low Temp (degrees)      |       {low_temp} {temp_system}
    -
    Wind Speed              |       {wind_speed} {wind_speed_system}
    Wind Direction          |       {wind_direction}
    """

    print(str(weather_output))
else:
    print("No valid output was retrieved from the API")

key = ""