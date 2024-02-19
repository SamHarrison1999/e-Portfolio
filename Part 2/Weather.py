from Utils import is_null_or_white_space


class Weather:

    def __init__(self, weather_condition: str, temperature: int):
        """
        Constructor for a weather object
        Parameters:
            self (Weather): The weather object
            weather_condition (str): The weather condition
            temperature (int): The temperature
        Returns:
            None
        """
        # If the weather condition is not given throw an error
        if is_null_or_white_space(weather_condition):
            raise ValueError("The weather condition must be given")
        else:
            self.__weather_condition = weather_condition
        self.__temperature = temperature

    def __str__(self):
        """
        Return the weather object as a string
        Parameters:
            self (Weather): The weather object
        Returns:
            The weather object as a string
        """
        return f'Weather Condition: {self.__weather_condition}\nTemperature: {self.__temperature} degrees'

    @property
    def weather_condition(self):
        """
        Returns the weather condition
        Parameters:
            self (Weather): The weather object
        Returns:
            self.__weather_condition (str): The weather condition
        """
        return self.__weather_condition

    @weather_condition.setter
    def weather_condition(self, weather_condition: str):
        """
        Set the weather condition
        Parameters:
            self (Weather): The weather object
            weather_condition (str): The weather condition
        Returns:
            None
        """
        # If the weather condition is not given throw an error
        if is_null_or_white_space(weather_condition):
            raise ValueError("The weather condition must be given")
        else:
            self.__weather_condition = weather_condition

    @property
    def temperature(self):
        """
        Return the temperature
        Parameters:
            self (Weather): The weather object
        Returns:
            self.__temperature (int): The temperature
        """
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature: int):
        """
        Set the temperature
        Parameters:
            self (Weather): The weather object
            temperature (int): The temperature
        Returns:
            None
        """
        self.__temperature = temperature


def main():
    weather = Weather("Sunny", 25)
    print(weather)


if __name__ == "__main__":
    main()
