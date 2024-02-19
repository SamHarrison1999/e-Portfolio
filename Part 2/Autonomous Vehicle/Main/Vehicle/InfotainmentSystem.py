from Main.Utils.Utils import is_null_or_white_space
from Main.Vehicle.Phone import Phone
from Main.Vehicle.Radio import Radio


class InfotainmentSystem:
    def __init__(self, phone: Phone, radio: Radio, language: str) -> None:
        """
        Constructor for the infotainment system object
        :parameter InfotainmentSystem self: The infotainment system object
        :parameter Phone phone: The phone connected to the vehicle via bluetooth or AUX
        :parameter Radio radio: The vehicle's radio
        :parameter str language: The language of the infotainment system
        :raises ValueError: If no language is given
        :returns: None
        """
        self.__phone = phone
        self.__radio = radio
        # If the language isn't set throw an error
        if is_null_or_white_space(language):
            raise ValueError("Language can't be null or empty")
        else:
            self.__language = language

    def __str__(self) -> str:
        """
        Returns an Infotainment System object as a string
        :parameter InfotainmentSystem self: The infotainment system object
        :returns: The infotainment system object as a string
        """
        return f"{self.__phone}\nRadio:\n{self.__radio}\nLanguage: {self.__language}"

    @property
    def phone(self) -> Phone:
        """
        Returns information about the phone connected to the vehicle
        :parameter InfotainmentSystem self: The infotainment system object
        :returns: The phone connected to the vehicle
        """
        return self.__phone

    @phone.setter
    def phone(self, phone: Phone) -> None:
        """
        Set information about the phone connected to the vehicle
        :parameter InfotainmentSystem self: The infotainment system object
        :parameter Phone phone: The phone connected to the vehicle
        :returns: None
        """
        self.__phone = phone

    @property
    def radio(self) -> Radio:
        """
        Returns information about the vehicles radio
        :parameter InfotainmentSystem self: The infotainment system object
        :returns: The vehicle's radio
        """
        return self.__radio

    @radio.setter
    def radio(self, radio: Radio) -> None:
        """
        Set information about the vehicles radio
        :parameter InfotainmentSystem self: The infotainment system object
        :parameter Radio radio: The vehicle's radio
        :returns: None
        """
        self.__radio = radio

    @property
    def language(self) -> str:
        """
        Returns the language of the infotainment system
        :parameter InfotainmentSystem self: The infotainment system object
        :returns: The language of the infotainment system
        """
        return self.__language

    @language.setter
    def language(self, language):
        """
        Set the language of the infotainment system
        :parameter InfotainmentSystem self: The infotainment system object
        :parameter str language: The language of the infotainment system
        :raises ValueError: If no language is given
        :returns: None
        """
        # If the language isn't set throw an error
        if is_null_or_white_space(language):
            raise ValueError("Language can't be null or empty")
        else:
            self.__language = language
