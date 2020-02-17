#!/usr/bin/python

class WeatherResponse:

    _requested_city = ""
    _visibility = ""
    _visibility_description = ""
    _actual_temp = ""
    _feels_like = ""
    _high_temp = 0
    _low_temp = 0
    _temp_system = ""
    _wind_speed = 0
    _wind_angle = 0
    _wind_direction = ""
    _wind_speed_system = ""

    def __init__(self, response: dict, measurement_system: str):
        
        self.parse_response(response)
        self.set_systems(measurement_system)
        return
    def get_requested_city(self):
        return self._requested_city
    def get_visibility(self):
        return self._visibility
    def get_visibility_description(self):
        return self._visibility_description
    def get_actual_temp(self):
        return self._actual_temp
    def get_feels_like(self):
        return self._feels_like
    def get_high_temp(self):
        return self._high_temp
    def get_low_temp(self):
        return self._low_temp
    def get_temp_system(self):
        return self._temp_system
    def get_wind_speed(self):
        return self._wind_speed
    def get_wind_direction(self):
        return self._wind_direction
    def get_wind_speed_system(self):
        return self._wind_speed_system
    def parse_response(self, response: dict):

        self._requested_city = response.get("name")
        self._visibility = response.get("weather")[0].get("main")
        self._visibility_description = response.get("weather")[0].get("description")
        #
        self._actual_temp = response.get("main").get("temp")
        self._feels_like = response.get("main").get("feels_like")
        self._high_temp = response.get("main").get("temp_max")
        self._low_temp = response.get("main").get("temp_min")
        #
        self._wind_speed = response.get("wind").get("speed")
        self._wind_angle = response.get("wind").get("deg")
        #
        if self._wind_angle != None:
            self.set_wind_direction(self._wind_angle)
        else:
            self._wind_direction = "UNK"

    def set_wind_direction(self, wind_angle: int):
        
        if (wind_angle >= 348.75 and wind_angle <= 359.99) or (wind_angle >= 0 and wind_angle <= 11.25):
            self._wind_direction = "N"
        elif (wind_angle >= 11.25 and wind_angle <= 33.75):
            self._wind_direction = "NNE"
        elif (wind_angle >= 33.75 and wind_angle <= 56.25):
            self._wind_direction = "NE"
        elif (wind_angle >= 56.25 and wind_angle <= 78.75):
            self._wind_direction = "ENE"
        elif (wind_angle >= 78.75 and wind_angle <= 101.25):
            self._wind_direction = "E"
        elif (wind_angle >= 101.25 and wind_angle <= 123.75):
            self._wind_direction = "ESE"
        elif (wind_angle >= 123.75 and wind_angle <= 146.25):
            self._wind_direction = "SE"
        elif (wind_angle >= 146.25 and wind_angle <= 168.75):
            self._wind_direction = "SSE"
        elif (wind_angle >= 168.75 and wind_angle <= 191.25):
            self._wind_direction = "S"
        elif (wind_angle >= 191.25 and wind_angle <= 213.75):
            self._wind_direction = "SSW"
        elif (wind_angle >= 213.75 and wind_angle <= 236.25):
            self._wind_direction = "SW"
        elif (wind_angle >= 236.25 and wind_angle <= 258.75):
            self._wind_direction = "WSW"
        elif (wind_angle >= 258.75 and wind_angle <= 281.25):
            self._wind_direction = "W"
        elif (wind_angle >= 281.25 and wind_angle <= 303.75):
            self._wind_direction = "WNW"
        elif (wind_angle >= 303.75 and wind_angle <= 326.25):
            self._wind_direction = "NW"
        elif (wind_angle >= 326.25 and wind_angle <= 348.75):
            self._wind_direction = "NNW"
        else:
            self._wind_direction = "UNK"

    def set_systems(self, system: str):

        if system.lower() == "imperial":
            self._temp_system = "F"
            self._wind_speed_system = "miles/hour"
        elif system.lower() == "metric":
            self._temp_system = "C"
            self._wind_speed_system = "meters/second"
        elif system.lower() == "kelvin":
            self._temp_system = "K"
            self._wind_speed_system = "meters/second"