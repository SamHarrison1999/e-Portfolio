from Main.Colour.Colour import Colour
from Main.Vehicle.Part import Part
from Main.Vehicle.EngineMode import EngineMode


class Engine(Part):

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str, dimensions: dict[str, float],
                 size: float, horse_power: int, cylinders: int, valves: int, mode: EngineMode) -> None:
        """
        Constructor for the engine object
        :parameter Engine self: The engine object
        :parameter int part_id: The part ID number
        :parameter str name: The name of the part
        :parameter Colour colour: The colour of the part
        :parameter str manufacturer: The parts manufacture
        :parameter dict[str, float] dimensions: The parts dimensions
        :parameter float size: The size of the engine
        :parameter int horse_power: The break horsepower produced by the engine
        :parameter int cylinders: The number of cylinders in the engine
        :parameter valves: The number of valves in the eng
        :parameter EngineMode mode: The mode the engine is in (E.G. Sports)
        :raises ValueError: if the part has a negative part id no name or manufacture or the dimensions aren't valid or the engine size or horsepower or number of cylinders or number of valves is below 0
        :returns: None
        """
        # The engine class inherits from the part class so uses the parent class constructor.
        # I did this, so I wouldn't have to rewrite the same code over and over again
        # (following the DRY principle).
        super().__init__(part_id, name, colour, manufacturer, dimensions)
        # If the engine size isn't a positive number throw an error
        if size > 0:
            self._size = size
        else:
            raise ValueError("Engine size must be a positive number")
        # If the horsepower isn't a positive number throw an error
        if horse_power > 0:
            self._horse_power = horse_power
        else:
            raise ValueError("The engines break horse power must be a positive number")
        # If the number of cylinders in the engine isn't a positive number throw an error
        if cylinders > 0:
            self._cylinders = cylinders
        else:
            raise ValueError("A Engine must have at least one cylinder")
        # If the number of valves in the engine isn't a positive number throw an error
        if valves > 0:
            self._valves = valves
        else:
            raise ValueError("The number of valves in an engine must be a positive number")
        self._mode = mode

    def __str__(self) -> str:
        """
        Returns an engine object as a string
        :parameter Engine self: The engine object
        Returns: The engine object as a string
        """
        return (f"{super().__str__()}\nEngine Size: {self._size}L\nBreak Horse Power: {self._horse_power}"
                f"\nNumber of Cylinders: {self._cylinders}\nNumber of Valves: {self._valves}\nMode: "
                f"{str(self._mode.name).capitalize()}")

    @property
    def size(self) -> float:
        """
        Returns the size of the engine in liters
        :parameter Engine self: The engine object
        :returns: The size of the engine
        """
        return self._size

    @size.setter
    def size(self, size: float) -> None:
        """
        Set the size of the engine in liters
        :parameter Engine self: The engine object
        :parameter float size: The size of the engine
        :raises ValueError: If the engine size is a negative number
        :returns: None
        """
        # If the engine size isn't a positive number throw an error
        if size > 0:
            self._size = size
        else:
            raise ValueError("Engine size must be a positive number")

    @property
    def horse_power(self) -> int:
        """
        Returns the amount of break horsepower produced by the vehicle
        :parameter Engine self: The engine object
        :returns: The amount of break horsepower produced by the engine
        """
        return self._horse_power

    @horse_power.setter
    def horse_power(self, horse_power: int) -> None:
        """
        Set the amount of break horsepower produced
        :parameter Engine self: The engine object
        :parameter int horse_power: The amount of break horsepower produced by the engine
        :raises ValueError: If the horsepower is a negative number
        :returns: None
        """
        # If the horsepower isn't a positive number throw an error
        if horse_power > 0:
            self._horse_power = horse_power
        else:
            raise ValueError("The engines break horse power must be a positive number")

    @property
    def cylinders(self) -> int:
        """
        Returns the number of cylinders
        :parameter Engine self: The engine object
        :returns: The number of cylinders in the engine
        """
        return self._cylinders

    @cylinders.setter
    def cylinders(self, cylinders: int) -> None:
        """
        Update the number of cylinders
        :parameter Engine self: The engine object
        :parameter int cylinders: The number of cylinders in the engine
        :returns: None
        """
        # If the number of cylinders in the engine isn't a positive number throw an error
        if cylinders > 0:
            self._cylinders = cylinders
        else:
            raise ValueError("A Engine must have at least one cylinder")

    @property
    def valves(self) -> int:
        """
        Returns the number of valves
        :parameter Engine self: The engine object
        :returns: The number of valves in the engine
        """
        return self._valves

    @valves.setter
    def valves(self, valves: int) -> None:
        """
        Update the number of engine valves
        :parameter Engine self: The engine object
        :parameter int valves: The number of valves in the engine
        :returns: None
        """
        # If the number of valves in the engine isn't a positive number throw an error
        if valves > 0:
            self._valves = valves
        else:
            raise ValueError("The number of valves in an engine must be a positive number")

    @property
    def mode(self) -> EngineMode:
        """
        Returns the mode the engine is in
        :parameter Engine self: The engine object
        Returns: The mode the engine is in
        """
        return self._mode

    @mode.setter
    def mode(self, mode: EngineMode) -> None:
        """
        Sets the mode the engine is in
        :parameter Engine self: The engine object
        :parameter EngineMode mode: The mode the engine is in
        :returns: None
        """
        self._mode = mode
