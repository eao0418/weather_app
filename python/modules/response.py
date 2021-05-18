#!/usr/bin/python


class WeatherResponse:

    __requested_city = ""
    __visibility = ""
    __visibility_description = ""
    __actual_temp = ""
    __feels_like = ""
    __high_temp = 0
    __low_temp = 0
    __temp_system = ""
    __wind_speed = 0
    __wind_angle = 0
    ___wind_direction = ""
    __wind_speed_system = ""

    def __init__(self, response: dict, measurement_system: str):
        """Creates a new instance of WeatherResponse

        Keyword Arguments: 
        response -- The parsed JSON from the weather API. 
        measurement_system -- The measurement system being used.
        """
        self.__parse_response(response)
        self.__set_systems(measurement_system)

    def get_requested_city(self):
        """Returns the name of the city the weather was requested for"""
        return self.__requested_city

    def get_visibility(self):
        """Gets the visibility information from the response"""
        return self.__visibility

    def get_visibility_description(self):
        """Gets the description of the visibility"""
        return self.__visibility_description

    def get_actual_temp(self):
        """Gets the actual temp in the city"""
        return self.__actual_temp

    def get_feels_like(self):
        """Gets the 'feels like' temperature"""
        return self.__feels_like

    def get_high_temp(self):
        """Gets the high temperature for the city"""
        return self.__high_temp

    def get_low_temp(self):
        """Gets the low temperature for the city"""
        return self.__low_temp

    def get_temp_system(self):
        """Gets the temperature system being used"""
        return self.__temp_system

    def get_wind_speed(self):
        """Gets the wind speed"""
        return self.__wind_speed

    def get_wind_direction(self):
        """Gets the direction the wind is blowing from"""
        return self.__wind_direction

    def get_wind_speed_system(self):
        """Gets the system being used for the wind speed"""
        return self.__wind_speed_system

    def __parse_response(self, response: dict):
        """Parses the response into the WeatherResponse object

        Keyword Arguments: 
        response -- The parsed json from the openweather API
        """
        self.__requested_city = response.get("name")
        self.__visibility = response.get("weather")[0].get("main")
        self.__visibility_description = response.get(
            "weather")[0].get("description")
        #
        self.__actual_temp = response.get("main").get("temp")
        self.__feels_like = response.get("main").get("feels_like")
        self.__high_temp = response.get("main").get("temp_max")
        self.__low_temp = response.get("main").get("temp_min")
        #
        self.__wind_speed = response.get("wind").get("speed")
        self.__wind_angle = response.get("wind").get("deg")
        #
        if self.__wind_angle != None:
            self.__set_wind_direction(self.__wind_angle)
        else:
            self.__wind_direction = "UNK"

    def __set_wind_direction(self, wind_angle: int):
        """Sets the wind direction string

        Keyword Arguments: 
        wind_angle -- The wind angle in degrees.
        """
        if (wind_angle >= 348.75 and wind_angle <= 359.99) or (wind_angle >= 0 and wind_angle <= 11.25):
            self.__wind_direction = "N"
        elif (wind_angle >= 11.25 and wind_angle <= 33.75):
            self.__wind_direction = "NNE"
        elif (wind_angle >= 33.75 and wind_angle <= 56.25):
            self.__wind_direction = "NE"
        elif (wind_angle >= 56.25 and wind_angle <= 78.75):
            self.__wind_direction = "ENE"
        elif (wind_angle >= 78.75 and wind_angle <= 101.25):
            self.__wind_direction = "E"
        elif (wind_angle >= 101.25 and wind_angle <= 123.75):
            self.__wind_direction = "ESE"
        elif (wind_angle >= 123.75 and wind_angle <= 146.25):
            self.__wind_direction = "SE"
        elif (wind_angle >= 146.25 and wind_angle <= 168.75):
            self.__wind_direction = "SSE"
        elif (wind_angle >= 168.75 and wind_angle <= 191.25):
            self.__wind_direction = "S"
        elif (wind_angle >= 191.25 and wind_angle <= 213.75):
            self.__wind_direction = "SSW"
        elif (wind_angle >= 213.75 and wind_angle <= 236.25):
            self.__wind_direction = "SW"
        elif (wind_angle >= 236.25 and wind_angle <= 258.75):
            self.__wind_direction = "WSW"
        elif (wind_angle >= 258.75 and wind_angle <= 281.25):
            self.__wind_direction = "W"
        elif (wind_angle >= 281.25 and wind_angle <= 303.75):
            self.__wind_direction = "WNW"
        elif (wind_angle >= 303.75 and wind_angle <= 326.25):
            self.__wind_direction = "NW"
        elif (wind_angle >= 326.25 and wind_angle <= 348.75):
            self.__wind_direction = "NNW"
        else:
            self.__wind_direction = "UNK"

    def __set_systems(self, system: str):
        """Sets the measurement systems being used

        Keyword Arguments: 
        system -- The system being used.
        """
        if system.lower() == "imperial":
            self.__temp_system = "F"
            self.__wind_speed_system = "miles/hour"
        elif system.lower() == "metric":
            self.__temp_system = "C"
            self._wind_speed_system = "meters/second"
        elif system.lower() == "kelvin":
            self.__temp_system = "K"
            self.__wind_speed_system = "meters/second"
