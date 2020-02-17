#!/usr/bin/python

class Util:
    """A collection of utility methods for the program"""

    @staticmethod
    def validate_weather_params(city: str, state: str, country: str):
        """Ensures the provided parameters are likely to be valid

        Keyword Arguments: 
        city -- The city that the weather is being queried for. 
        state -- The state that the city is in. 
        country -- The ISO 3166 Alpha-2 country code that the city is in.
        """
        if not all(x.isalpha() or x.isspace() for x in city):
            raise ValueError("The provided value does not match the pattern of a valid city")
        if not state.isalpha():
            raise ValueError("The provided value does not match the pattern of a valid state")
        if not country.isalpha():
            raise ValueError("The provided value does not match the pattern of a valid country code")
    @staticmethod
    def print_help(mode: str):

        city_help = "The name of the city to get the weather for."
        state_help = "The two-character abbreviation for the state to search for the city"
        country_help = "The ISO 3166 Alpha-2 country code that goes with the city and state."

        all_help_text = f"""
        Running in {mode} mode. Please provide the city, state, and country
        to get the current weather for the specified location. please refer to 
        the explanations for each required parameter: 

        city -- {city_help}
        state -- {state_help}
        country -- {country_help}
        """

        single_help_text = f"""

        The script will automatically exit after returning the requested data. 
        """

        console_help_text = f"""
        
        The script will continue to request locations until requested to exit. 
        type 'exit' or 'quit' in a prompt to leave the script.
        """

        if mode.lower() == "single":

            print(all_help_text + single_help_text)
        elif mode.lower() == "console":

            print(all_help_text + console_help_text)