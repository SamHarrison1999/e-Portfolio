from Main.Colour.Colour import Colour
from Main.Vehicle.Part import Part


class Wheel(Part):

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str, dimensions: dict[str, float])\
            -> None:
        """
        Constructor for the wheel object
        :parameter Wheel self: The wheel object
        :parameter int part_id: The part ID number
        :parameter str name: The name of the part
        :parameter Colour colour: The colour of the part
        :parameter str manufacturer: The parts manufacture
        :parameter dict[str, float] dimensions: The parts dimensions
        :raises ValueError: if the part has a negative part id no name or manufacture or the dimensions aren't valid
        :returns: None
        """
        # The Wheel class inherits from the part class so uses the parent class constructor.
        # I did this, so I wouldn't have to rewrite the same code over and over again
        # (following the DRY principle).
        super().__init__(part_id, name, colour, manufacturer, dimensions)
