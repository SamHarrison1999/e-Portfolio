from collections import OrderedDict
from typing import Optional
from Phone import Phone
from Radio import Radio
from Utils import is_null_or_white_space


class InfotainmentSystem:
    def __init__(self, phone: Phone, radio: Radio, language: str):
        """
        Constructor for Infotainment System Object
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
            phone (Phone): The phone connected to the vehicle
            radio (Radio): The vehicle radio
            language (str): The language of the infotainment system
        Returns:
            None
        """
        self.__phone = phone
        self.__radio = radio
        # If the language isn't set throw an error
        if is_null_or_white_space(language):
            raise ValueError("Language can't be null or empty")
        else:
            self.__language = language

    def __str__(self):
        """
        Returns an Infotainment System object as a string
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
        Returns:
             Formatted string of an Infotainment System object as a string
        """
        return f"{self.__phone}\nRadio:\n{self.__radio}\nLanguage: {self.__language}"

    @property
    def phone(self):
        """
        Get information about the phone connected to the vehicle
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
        Returns:
            self.__phone (Phone): The phone connected to the vehicle
        """
        return self.__phone

    @phone.setter
    def phone(self, phone: Phone):
        """
        Set information about the phone connected to the vehicle
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
            phone (Phone): The phone connected to the vehicle
        Returns:
            None
        """
        self.__phone = phone

    @property
    def radio(self):
        """
        Get information about the vehicles radio
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
        Returns:
            self.__radio (Radio): The vehicle's radio
        """
        return self.__radio

    @radio.setter
    def radio(self, radio: Radio):
        """
        Set information about the vehicles radio
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
            radio (Radio): The vehicle's radio
        Returns:
            None
        """
        self.__radio = radio

    @property
    def language(self):
        """
        Returns the language of the infotainment system
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
        Returns:
            self.__language (str): The language of the infotainment system
        """
        return self.__language

    @language.setter
    def language(self, language):
        """
        Set the language of the infotainment system
        Parameters:
            self (InfotainmentSystem): InfotainmentSystem Object
            language (str): The language of the infotainment system
        Returns:
            None
        """
        # If the language isn't set throw an error
        if is_null_or_white_space(language):
            raise ValueError("Language can't be null or empty")
        else:
            self.__language = language

    @staticmethod
    def call_emergency_services():
        """
        Calls emergency services in the event of a crash or the drivers vitals flat-lining
        Returns:
            A String saying calling emergency services
        """
        return "Calling Emergency Services"

    def call_emergency_contact(self):
        """
        Calls Emergency Contact in the event of a crash or the drivers vitals flat-lining
        Returns:
            A String saying calling your emergency contact with the emergency contacts information
        """
        return "Calling Emergency Contact\n" + f"".join(f'{key}: {value}\n' for key, value in self.__phone.emergency_contact.items())

    def change_radio_station(self, station_name: str, frequency_modulation: Optional[float], amplitude_modulation: Optional[int]):
        """
        Allows you to change the radio station on the vehicle radio
        Parameters:
            station_name (str):
            frequency_modulation (Optional[float]):
            amplitude_modulation (Optional[int]):
        Returns:
            None
        """
        self.__radio.station_name = station_name
        self.__radio.frequency_modulation = frequency_modulation
        self.__radio.amplitude_modulation = amplitude_modulation


def main():
    emergency_contact = OrderedDict()
    emergency_contact["Name"] = "Emergency Contact"
    emergency_contact["number"] = "+447987654321"
    phone = Phone("+447123456789", emergency_contact, [], [])
    radio = Radio("Capital", 95.8, None)
    infotainment_system = InfotainmentSystem(phone, radio, "English")
    infotainment_system.change_radio_station("Kiss", 100.0, None)
    print(infotainment_system)
    print(InfotainmentSystem.call_emergency_services())
    print(infotainment_system.call_emergency_contact())


if __name__ == "__main__":
    main()
