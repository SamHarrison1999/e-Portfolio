from Main.Colour.Colour import Colour
from Main.Vehicle.Part import Part
from Main.Vehicle.TransmissionType import TransmissionType


class Transmission(Part):

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str, dimensions: dict[str, float],
                 transmission_type: TransmissionType, number_of_gears: int, current_gear: int) -> None:
        """
        Constructor for the transmission object
        :parameter Transmission self: The transmission object
        :parameter int part_id: The part ID number
        :parameter str name: The name of the part
        :parameter Colour colour: The colour of the part
        :parameter str manufacturer: The parts manufacture
        :parameter dict[str, float] dimensions: The parts dimensions
        :parameter TransmissionType transmission_type: The type of transmission (E.G. Manual)
        :parameter int number_of_gears: The number of gears
        :parameter int current_gear: The current gear
        :raises ValueError: if the part has a negative part id no name or manufacture or the dimensions aren't valid or the number of gears isn't a positive number or the current gear isn't available
        :returns: None
        """
        # The transmission class inherits from the part class so uses the parent class constructor.
        # I did this, so I wouldn't have to rewrite the same code over and over again
        # (following the DRY principle).
        super().__init__(part_id, name, colour, manufacturer, dimensions)
        self._transmission_type = transmission_type
        # If the number of gears is not a positive number throw an error
        if number_of_gears > 0:
            self._number_of_gears = number_of_gears
        else:
            raise ValueError("The vehicle must have at least 1 gear")
        # If the current gear isn't a valid gear throw an error
        # -1 is reverse
        # 0 is neutral
        if -1 <= current_gear <= self._number_of_gears:
            self._current_gear = current_gear
        else:
            raise ValueError("The gear is not available")

    def __str__(self) -> str:
        """
        Returns the transmission object as a string
        :parameter Transmission self: The transmission object
        :returns: A transmission object as a string
        """
        return f"{super().__str__()}\n" + f'Transmission: {str(self._transmission_type.value)}\n' \
                                          f'Number of Gears: {self._number_of_gears}\n' \
                                          f'Current Gear: {self._current_gear}'

    @property
    def transmission_type(self) -> TransmissionType:
        """
        Returns the type of transmission
        :parameter Transmission self: The transmission object
        :returns: The type of transmission (E.G. Manual)
        """
        return self._transmission_type

    @transmission_type.setter
    def transmission_type(self, transmission_type) -> None:
        """
        Set the type of transmission
        :parameter Transmission self: The transmission object
        :parameter TransmissionType transmission_type: The type of transmission (E.G. Manual)
        :returns: None
        """
        self._transmission_type = transmission_type

    @property
    def number_of_gears(self) -> int:
        """
        Returns the number of gears
        :parameter Transmission self: The transmission object
        :returns: The number of gears
        """
        return self._number_of_gears

    @number_of_gears.setter
    def number_of_gears(self, number_of_gears: int) -> None:
        """
        Set the number of gears
        :parameter Transmission self: The transmission object
        :parameter int number_of_gears: The number of gears
        :raises ValueError: if the number of gears isn't a positive number
        :returns: None
        """
        # If the number of gears is not a positive number throw an error
        if number_of_gears > 0:
            self._number_of_gears = number_of_gears
        else:
            raise ValueError("The vehicle must have at least 1 gear")

    @property
    def current_gear(self) -> int:
        """
        Returns the current gear
        :parameter Transmission self: The transmission object
        :returns: The current gear
        """
        return self._current_gear

    @current_gear.setter
    def current_gear(self, current_gear: int) -> None:
        """
        Set the current gear
        :parameter Transmission self: The transmission object
        :parameter int current_gear: The current gear
        :raises ValueError: if the current gear isn't a valid gear
        :returns: None
        """
        # If the current gear isn't a valid gear throw an error
        if 0 <= current_gear <= self._number_of_gears:
            self._current_gear = current_gear
        else:
            raise ValueError("The gear is not available")

    def gear_up(self) -> None:
        """
        Switch to the next gear if its possible
        :parameter Transmission self: The transmission object
        :returns: None
        """
        # Go up to the next gear if it is available
        if self._current_gear + 1 <= self._number_of_gears:
            self._current_gear += 1

    def gear_down(self) -> None:
        """
        Switch to the previous gear if its possible
        :parameter Transmission self: The transmission object
        :returns: None
        """
        # Go down to the previous gear if it is available
        if self._current_gear - 1 >= -1:
            self._current_gear -= 1

    def reverse(self):
        """
        Switch to Reverse
        :parameter Transmission self: The transmission object
        :returns: None
        """
        # Switch to reverse gear if not already in reverse
        if self._current_gear != -1:
            self._current_gear = -1

    def neutral(self):
        """
        Switch to neutral
        :parameter Transmission self: The transmission object
        :returns: None
        """
        # Switch to neutral if not already in neutral
        if self._current_gear != 0:
            self._current_gear = 0
