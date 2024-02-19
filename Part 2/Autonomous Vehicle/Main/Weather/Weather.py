from Main.Utils.Utils import is_null_or_white_space


class Weather:

    def __init__(self, weather_condition: str, temperature: int) -> None:
        """
        Constructor for a weather object
        :parameter Weather self: The weather object
        :parameter str weather_condition: The weather condition
        :parameter int temperature: The temperature
        :returns: None
        :raises ValueError: If the weather condition is blank
        """
        # If the weather condition is not given throw an error
        if is_null_or_white_space(weather_condition):
            raise ValueError("The weather condition must be given")
        else:
            self._weather_condition = weather_condition
        self._temperature = temperature

    def __str__(self) -> str:
        """
        Return the weather object as a string
        :parameter Weather self: The weather object
        :returns: The weather object as a string
        """
        return (f'Weather Condition: {self._weather_condition}\nTemperature: {self._temperature} degrees\n'
                f'Recommended Following Distance: {self.recommended_following_distance()} Meters')

    @property
    def weather_condition(self):
        """
        Returns the weather condition
        :parameter Weather self: The weather object
        :returns: The weather condition
        """
        return self._weather_condition

    @weather_condition.setter
    def weather_condition(self, weather_condition: str):
        """
        Set the weather condition
        :parameter Weather self: The weather object
        :parameter str weather_condition: The weather condition
        :returns: None
        :raises ValueError: If the weather condition is blank
        """
        # If the weather condition is not given throw an error
        if is_null_or_white_space(weather_condition):
            raise ValueError("The weather condition must be given")
        else:
            self._weather_condition = weather_condition

    @property
    def temperature(self):
        """
        Return the temperature
        :parameter Weather self: The weather object
        :returns: The temperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: int):
        """
        Set the temperature
        :parameter Weather self: The weather object
        :parameter int temperature: The temperature
        :returns: None
        """
        self._temperature = temperature

    @property
    def weather(self):
        return self.__str__()

    @weather.setter
    def weather(self, weather):
        self._weather_condition = weather.weather_condition
        self._temperature = weather.temperature

    def recommended_following_distance(self) -> int:
        """
        Returns the recommended following distance
        :parameter Weather self: The weather object
        :returns: The recommended following distance
        """
        # Return 2 if its sunny, 4 if its raining, 10 if it is snowing otherwise throw an error
        match str(self._weather_condition).casefold():
            case "sunny":
                return 2
            case "raining":
                return 4
            case "snowing":
                return 10
            case _:
                raise ValueError(self._weather_condition + " not supported")
