from Main.Colour.Colour import Colour
from Main.Vehicle.Part import Part


class Tyre(Part):

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str, dimensions: dict[str, float],
                 tread: float, tyre_pressure: float) -> None:
        """
        Constructor for a tyre
        :parameter Tyre self: The tyre object
        :parameter int part_id: The part ID number
        :parameter str name: The name of the part
        :parameter Colour colour: The colour of the part
        :parameter str manufacturer: The parts manufacture
        :parameter dict[str, float] dimensions: The parts dimensions
        :parameter float tread: The amount of tread left
        :parameter float tyre_pressure: The tyre pressure
        :raises ValueError: if the part has a negative part id no name or manufacture or the dimensions aren't valid or the tyre tread remaining or air pressure is a negative number
        :returns: None
        """
        # The Tyre class inherits from the part class so uses the parent class constructor.
        # I did this, so I wouldn't have to rewrite the same code over and over again
        # (following the DRY principle).
        super().__init__(part_id, name, colour, manufacturer, dimensions)
        # If the amount of tread remaining is negative throw an error
        if tread >= 0:
            self._tread = tread
        else:
            raise ValueError("The tread remaining on the tire must be at least 0mm")
        # If the tyre pressure is negative throw an error
        if tyre_pressure >= 0:
            self._tyre_pressure = tyre_pressure
        else:
            raise ValueError("The tyre pressure must be at least 0 psi")

    def __str__(self) -> str:
        """
        Returns a tyre object as a string
        :parameter Tyre self: The tyre object
        :returns: A tyre object as a string
        """
        return f"{super().__str__()}\n" + (f"Current Air Pressure: {self._tyre_pressure} psi\n"
                                           f"Tyre Thread Remaining: {self._tread} mm")

    @property
    def tread(self):
        """
        Returns the amount of tyre tread left
        :parameter Tyre self: The tyre object
        :returns: The tread remaining on the tyre
        """
        return self._tread

    @tread.setter
    def tread(self, tread: float):
        """
        Update the amount of tread remaining
        :parameter Tyre self: The tyre object
        :parameter float tread: The tread remaining on the tyre
        :raises ValueError: If the tyre tread remaining is a negative number
        :returns: None
        """
        # If the amount of tread remaining is negative throw an error
        if tread >= 0:
            self._tread = tread
        else:
            raise ValueError("The tread remaining on the tire must be at least 0mm")

    @property
    def tyre_pressure(self):
        """
        Returns the tyre pressure
        :parameter Tyre self: The tyre object
        :returns: The tyre pressure
        """
        return self._tyre_pressure

    @tyre_pressure.setter
    def tyre_pressure(self, tyre_pressure: float):
        """
        Set the tyre pressure
        :parameter Tyre self: The tyre object
        :parameter float tyre_pressure: The tyre pressure
        :returns: None
        :raises ValueError: If the air pressure is a negative number
        """
        # If the tyre pressure is negative throw an error
        if tyre_pressure >= 0:
            self._tyre_pressure = tyre_pressure
        else:
            raise ValueError("The tyre pressure must be at least 0 psi")
