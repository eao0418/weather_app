#!/usr/bin/python
import argparse
import getpass
import re

from urllib.error import HTTPError
from modules.response import WeatherResponse
from modules.handler import ApiHandler
from modules.tools import Util
from modules.console import Console


def main():

    parser = argparse.ArgumentParser()

    # Help output
    system_help = "The measurement system to get results in.  Valid arguments are: imperial, metric, or kelvin"
    mode_help = "The mode to run the program in.  Valid arguments are: single, console"

    parser.add_argument("--mode", required=True, help=mode_help)
    parser.add_argument("--system", required=True, help=system_help)

    key = getpass.getpass(
        "Please provide your API key for openweathermap.org: ")

    args = parser.parse_args()

    mode = args.mode
    system = args.system

    acceptable_units = ["imperial", "kelvin", "metric"]

    if system.lower() not in acceptable_units:
        raise ValueError("The provided system is not an acceptable value.")

    if key == None or len(key.strip()) == 0:
        raise ValueError("They key cannot be None or empty string")

    if mode.lower() == "single":
        single_mode(key, system)
    elif mode.lower() == "console":
        console_mode(key, system)
    else:
        print("A valid mode was not selected, exiting!")
        key = ""
        exit(1)


def single_mode(key: str, system: str):
    """Runs the weather API in single mode. 

    Keyword Arguments: 
    key -- The API key to openweathermap
    system -- The measurement system to use.
    """

    Util.print_help("single")

    city = input("City >")
    state = input("State >")
    country = input("Country >")
    #state = args.state
    #country = args.country
    Util.validate_weather_params(city, state, country)
    handler = ApiHandler(key)

    try:
        output = handler.get_current_weather_by_city_and_state(
            city, state, country, system)
    except HTTPError as he:
        if he.getcode() == 404:
            print("The requested city, state, and country combination was not found in the weather api system, please try again")
        if he.getcode() == 401:
            print("The provided API key value did not provide access to the weather API.  Please provide a valid API key and try again.")
            exit(1)

    if output != None:

        weather_output = f"""
        Requested City:         |       {output.get_requested_city()}
        -                           -
        Visibility:             |       {output.get_visibility()}
        Visibility Desc         |       {output.get_visibility_description()}
        -
        Actual Temp (degrees)   |       {output.get_actual_temp()} {output.get_temp_system()}
        Feels Like (degrees)    |       {output.get_feels_like()} {output.get_temp_system()}
        High Temp (degrees)     |       {output.get_high_temp()} {output.get_temp_system()}
        Low Temp (degrees)      |       {output.get_low_temp()} {output.get_temp_system()}
        -
        Wind Speed              |       {output.get_wind_speed()} {output.get_wind_speed_system()}
        Wind Direction          |       {output.get_wind_direction()}
        """

        print(str(weather_output))
    else:
        print("No valid output was retrieved from the API")

    key = ""


def console_mode(key: str, system: str):

    Console.run(key, system)
    key = ""


if __name__ == "__main__":
    main()
