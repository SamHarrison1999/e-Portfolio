from typing import Optional

from Utils import is_null_or_white_space


class Radio:
    def __init__(self, station_name: str, frequency_modulation: Optional[float], amplitude_modulation: Optional[int]):
        """
        Constructor for a Radio Object
        Parameters:
            self (Radio): The Radio Object
            station_name (str): The name of the radio station
            frequency_modulation (Optional[float]): The radio stations FM number
            amplitude_modulation (Optional[int]): The radio stations AM number
        Returns:
            None
        """
        # If radio station has no name throw an error
        if is_null_or_white_space(station_name):
            raise ValueError("A radio station must have a name")
        else:
            self.__station_name = station_name
        # If FM is set and not in the FM range throw an error
        if frequency_modulation is None:
            self.__frequency_modulation = 0
        elif 87.5 <= frequency_modulation <= 108.0:
            self.__frequency_modulation = frequency_modulation
        else:
            raise ValueError("The FM range for radio is 87.5-108.0")
        # If AM is set and not in the AM range throw an error
        if amplitude_modulation is None:
            self.__amplitude_modulation = 0
        elif 535 <= amplitude_modulation <= 1705:
            self.__amplitude_modulation = amplitude_modulation
        else:
            raise ValueError("The AM range for radio is 535-1705")

    def __str__(self):
        """
        Returns the Radio Object as a string
        Parameters:
            self (Radio): The Radio Object
        Returns:
            Formatted string of the radio object
        """
        return f"Station Name: {self.__station_name}\nFM: {self.__frequency_modulation}\nAM: {self.__amplitude_modulation}Hz"

    @property
    def station_name(self):
        """
        Returns the name of the radio station
        Parameters:
            self (Radio): A Radio Object
        Returns:
            self.__station_name (str): The name of the radio station
        """
        return self.__station_name

    @station_name.setter
    def station_name(self, station_name: str):
        """
        Sets the name of the radio station
        Parameters:
            self (Radio): A Radio Object
            station_name (str): The name of the radio station
        Returns:
            None
        """
        # If radio station has no name throw an error
        if is_null_or_white_space(station_name):
            raise ValueError("A radio station must have a name")
        else:
            self.__station_name = station_name

    @property
    def frequency_modulation(self):
        """
        Returns the FM number of the radio station
        Parameters:
            self (Radio): A Radio Object
        Returns:
            self.__frequency_modulation (Optional[float]): The radio stations FM number
        """
        return self.__frequency_modulation

    @frequency_modulation.setter
    def frequency_modulation(self, frequency_modulation: Optional[float]):
        """
        Sets the FM number of the radio station
        Parameters:
            self (Radio): A Radio Object
            frequency_modulation (Optional[float]): The radio stations FM number
        Returns:
            None
        """
        # If FM is set and not in the FM range throw an error
        if frequency_modulation is None:
            self.__frequency_modulation = 0
        elif 87.5 <= frequency_modulation <= 108.0:
            self.__frequency_modulation = frequency_modulation
        else:
            raise ValueError("The FM range for radio is 87.5-108.0")

    @property
    def amplitude_modulation(self):
        """
        Returns the AM number of the radio station
        Parameters:
            self (Radio): A Radio Object
        Returns:
            self.__amplitude_modulation (Optional[int]): The radio stations AM number
        """
        return self.__amplitude_modulation

    @amplitude_modulation.setter
    def amplitude_modulation(self, amplitude_modulation: Optional[int]):
        """
        Sets the AM number of the radio station
        Parameters:
            self (Radio): A Radio Object
            amplitude_modulation (Optional[int]): The radio stations AM number
        Returns:
            None
        """
        # If AM is set and not in the AM range throw an error
        if amplitude_modulation is None:
            self.__amplitude_modulation = 0
        elif 535 <= amplitude_modulation <= 1705:
            self.__amplitude_modulation = amplitude_modulation
        else:
            raise ValueError("The AM range for radio is 535-1705")


def main():
    radio = Radio("Capital", 95.8, None)
    print(radio)


if __name__ == "__main__":
    main()
