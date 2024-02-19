from enum import Enum


class TransmissionType(Enum):
    AUTOMATIC = 1
    SEMI_AUTOMATIC = 2
    MANUAL = 3


class Transmission:
    def __init__(self, transmission_type: TransmissionType, number_of_gears: int, current_gear: int):
        """
        Constructor for the transmission object
        Parameters:
            self (Transmission): The transmission object
            transmission_type (TransmissionType): The type of transmission (E.G. Manual)
            number_of_gears (int): The number of gears
            current_gear (int): The current gear
        Returns:
            None
        """
        self.__transmission_type = transmission_type
        # If the number of gears is not a positive number throw an error
        if number_of_gears > 0:
            self.__number_of_gears = number_of_gears
        else:
            raise ValueError("The vehicle must have at least 1 gear")
        # If the current gear isn't a valid gear throw an error
        if 0 <= current_gear <= self.__number_of_gears:
            self.__current_gear = current_gear
        else:
            raise ValueError("The current gear must be at least 0")

    def __str__(self):
        return f'Transmission: {str(self.__transmission_type.name).capitalize()}\n' \
               f'Number of Gears: {self.__number_of_gears}\n' \
               f'Current Gear: {self.__current_gear}'

    @property
    def transmission_type(self):
        """
        Returns the type of transmission
        Parameters:
            self (Transmission): The transmission object
        Returns:
            self.__transmission_type (TransmissionType): The type of transmission (E.G. Manual)
        """
        return self.__transmission_type

    @transmission_type.setter
    def transmission_type(self, transmission_type):
        """
        Set the type of transmission
        Parameters:
            self (Transmission): The transmission object
            transmission_type (TransmissionType): The type of transmission (E.G. Manual)
        Returns:
            None
        """
        self.__transmission_type = transmission_type

    @property
    def number_of_gears(self):
        """
        Returns the number of gears
        Parameters:
            self (Transmission): The transmission object
        Returns:
            self.__number_of_gears (int): The number of gears
        """
        return self.__number_of_gears

    @number_of_gears.setter
    def number_of_gears(self, number_of_gears: int):
        """
        Set the number of gears
        Parameters:
            self (Transmission): The transmission object
            number_of_gears (int): The number of gears
        Returns:
            None
        """
        # If the number of gears is not a positive number throw an error
        if number_of_gears > 0:
            self.__number_of_gears = number_of_gears
        else:
            raise ValueError("The vehicle must have at least 1 gear")

    @property
    def current_gear(self):
        """
        Returns the current gear
        Parameters:
            self (Transmission): The transmission object
        Returns:
            self.__current_gear (int): The current gear
        """
        return self.__current_gear

    @current_gear.setter
    def current_gear(self, current_gear: int):
        """
        Set the current gear
        Parameters:
            self (Transmission): The transmission object
            current_gear (int): The current gear
        Returns:
            None
        """
        # If the current gear isn't a valid gear throw an error
        if 0 <= current_gear <= self.__number_of_gears:
            self.__current_gear = current_gear
        else:
            raise ValueError("The current gear must be at least 0")

    def gear_up(self):
        """
        Switch to the next gear if its possible
        Parameters:
            self (Transmission): The transmission object
        Returns:
            None
        """
        if self.__current_gear + 1 <= self.__number_of_gears:
            self.__current_gear += 1

    def gear_down(self):
        """
        Switch to the previous gear if its possible
        Parameters:
            self (Transmission): The transmission object
        Returns:
            None
        """
        if self.__current_gear - 1 >= 0:
            self.__current_gear -= 1


def main():
    transmission = Transmission(TransmissionType.MANUAL, 6, 3)
    print(transmission)


if __name__ == "__main__":
    main()
