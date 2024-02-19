from typing import Optional

from Main.Utils.Utils import is_null_or_white_space


class Radio:
    def __init__(self, station_name: str, frequency_modulation: Optional[float], amplitude_modulation: Optional[int])\
            -> None:
        """
        Constructor for a radio object
        :parameter Radio self: The radio object
        :parameter str station_name: The name of the radio station
        :parameter Optional[float] frequency_modulation: The radio stations FM number
        :parameter Optional[int] amplitude_modulation: The radio stations AM number
        :raises ValueError: If the radio station has no name or the fm or am numbers are not valid
        :returns: None
        """
        # If radio station has no name throw an error
        if is_null_or_white_space(station_name):
            raise ValueError("A radio station must have a name")
        else:
            self._station_name = station_name
        # If FM is set and not in the FM range throw an error
        if frequency_modulation is None:
            self._frequency_modulation = 0
        elif 87.5 <= frequency_modulation <= 108.0:
            self._frequency_modulation = frequency_modulation
        else:
            raise ValueError("The FM range for radio is 87.5-108.0")
        # If AM is set and not in the AM range throw an error
        if amplitude_modulation is None:
            self._amplitude_modulation = 0
        elif 535 <= amplitude_modulation <= 1705:
            self._amplitude_modulation = amplitude_modulation
        else:
            raise ValueError("The AM range for radio is 535-1705")

    def __str__(self) -> str:
        """
        Returns the radio object as a string
        :parameter Radio self: The radio object
        :returns: The radio object as a string
        """
        return (f"Station Name: {self._station_name}\nFM: {self._frequency_modulation}\nAM: "
                f"{self._amplitude_modulation}Hz")

    @property
    def station_name(self) -> str:
        """
        Returns the name of the radio station
        :parameter Radio self: The radio object
        :returns: The name of the radio station
        """
        return self._station_name

    @station_name.setter
    def station_name(self, station_name: str) -> None:
        """
        Sets the name of the radio station
        :parameter Radio self: The radio object
        :parameter str station_name: The name of the radio station
        :raises ValueError: If the radio station has no name
        :returns: None
        """
        # If radio station has no name throw an error
        if is_null_or_white_space(station_name):
            raise ValueError("A radio station must have a name")
        else:
            self._station_name = station_name

    @property
    def frequency_modulation(self) -> float:
        """
        Returns the FM number of the radio station
        :parameter Radio self: The radio object
        :returns: The radio stations FM number
        """
        return self._frequency_modulation

    @frequency_modulation.setter
    def frequency_modulation(self, frequency_modulation: Optional[float]) -> None:
        """
        Sets the FM number of the radio station
        :parameter Radio self: The radio object
        :parameter Optional[float] frequency_modulation: The radio stations FM number
        :raises ValueError: If the radio station fm number is not valid
        :returns: None
        """
        # If FM is set and not in the FM range throw an error
        if frequency_modulation is None:
            self._frequency_modulation = 0
        elif 87.5 <= frequency_modulation <= 108.0:
            self._frequency_modulation = frequency_modulation
        else:
            raise ValueError("The FM range for radio is 87.5-108.0")

    @property
    def amplitude_modulation(self) -> int:
        """
        Returns the AM number of the radio station
        :parameter Radio self: The radio object
        :returns: The radio stations AM number
        """
        return self._amplitude_modulation

    @amplitude_modulation.setter
    def amplitude_modulation(self, amplitude_modulation: Optional[int]) -> None:
        """
        Sets the AM number of the radio station
        :parameter Radio self: The radio object
        :parameter Optional[int] amplitude_modulation: The radio stations AM number
        :raises ValueError: If the radio station am number is not valid
        :returns: None
        """
        # If AM is set and not in the AM range throw an error
        if amplitude_modulation is None:
            self._amplitude_modulation = 0
        elif 535 <= amplitude_modulation <= 1705:
            self._amplitude_modulation = amplitude_modulation
        else:
            raise ValueError("The AM range for radio is 535-1705")
