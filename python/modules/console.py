#!/usr/bin/python

from modules.handler import ApiHandler
from modules.tools import Util
from urllib.error import HTTPError
import argparse


class Console:

    @staticmethod
    def run(key: str, measurement_system: str):
        """Runs the weather_app in console mode

        Keyword Arguments: 
        measurement_system -- The system to use to in the requests.
        key -- The API key for openweathermap
        """
        Util.print_help("console")

        counter = 0

        while True:

            if counter > 0:
                check_continue()

            print("Select a location to query weather data for")

            city = input("City >")
            state = input("State >")
            country = input("Country >")

            output = None

            try:
                Util.validate_weather_params(city, state, country)
                
                handler = ApiHandler(key)
                try:
                    output = handler.get_current_weather_by_city_and_state(city, state, country, measurement_system)
                except HTTPError as he:
                    if he.getcode() == 404:
                        print("The requested city, state, and country combination was not found in the weather api system, please try again")
                    if he.getcode() == 401:
                        print("The provided API key value did not provide access to the weather API.  Please provide a valid API key and try again.")
                        key = ""
                        exit(1)
            except ValueError as ve:
                print(ve)

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
                print("")
            else:
                print("No valid output was retrieved from the API")
                print("")
            
            counter += 1
                
def check_continue():
    retry = input("Try again y/n:")

    if (retry.lower() == "n"):
        print("exiting")
        exit(0)
