#!/usr/bin/python
import urllib.request
import urllib.parse
from urllib.error import HTTPError
import json
from modules.response import WeatherResponse


class ApiHandler:

    host_name = ""
    api_key = ""

    def __init__(self, key):
        """Creates a new instance of ApiHandler

        Keyword Arguments: 
        key -- The API key for openweathermap.org

        returns -- A new instance of ApiHandler
        """
        self.host_name = "api.openweathermap.org"
        self.api_key = key

    def make_api_request(self, url: str, method: str, headers: dict):
        """Makes an API request to the specified URL

        Keyword Arguments: 
        url -- The full URL to make the request to.
        method -- The HTTP method to use in the request.
        headers -- A dictionary of headers to use in the request; can be None.

        returns -- The decoded JSON object
        """

        req = urllib.request.Request(url, method=method)

        # Headers should be allowed to be None.
        if headers is not None or headers != {}:
            for key in headers.keys():
                req.add_header(key, headers.get(key, ""))

        result = json.load(urllib.request.urlopen(req))

        return result

    def get_current_weather_by_city(self, city_name: str, units):
        """Gets the current weather for the requested city name

        Keyword Arguments: 
        city_name -- The name of the city to get the weather for.
        units -- Sets the return data type in metric, imperial, or kelvin. 

        returns -- The data
        """

        acceptable_units = ["imperial", "kelvin", "metric"]
        if units.lower() not in acceptable_units:

            raise AttributeError("The value provided for units was not valid")

        url = "https://" + self.host_name + "/data/2.5/weather?q="
        url += city_name + "&appid=" + self.api_key
        url += "&units=" + units

        result = self.make_api_request(url, "GET", {})

        weather_response = WeatherResponse(result, units)

        return weather_response

    def get_current_weather_by_city_and_state(self, city_name: str, state_name: str, country_code: str, units: str):
        """Gets the current weather for the requested city name

        Keyword Arguments: 
        city_name -- The name of the city to get the weather for.
        state_name -- The name of the state 
        country_code -- The ISO 3166 Alpha-2 country code.
        units -- Sets the return data type in metric, imperial, or kelvin. 

        returns -- The data
        """

        acceptable_units = ["imperial", "kelvin", "metric"]
        if units.lower() not in acceptable_units:

            raise AttributeError("The value provided for units was not valid")

        url = "https://" + self.host_name + "/data/2.5/weather?q="
        url += city_name + "," + state_name + "," + \
            country_code + "&appid=" + self.api_key
        url += "&units=" + units

        result = self.make_api_request(
            url,
            "GET",
            {}
        )

        weather_response = WeatherResponse(result, units)

        return weather_response