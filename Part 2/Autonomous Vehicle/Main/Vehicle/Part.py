from Main.Colour.Colour import Colour
from Main.Utils.Utils import is_null_or_white_space


class Part:

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str,
                 dimensions: dict[str, float]) -> None:
        """
        Constructor for a part object
        :parameter Part self: The part object
        :parameter int part_id: The part ID number
        :parameter str name: The name of the part
        :parameter Colour colour: The colour of the part
        :parameter str manufacturer: The parts manufacture
        :parameter dict[str, float] dimensions: The parts dimensions
        :raises ValueError: if the part has a negative part id no name or manufacture or the dimensions aren't valid
        :returns: None
        """
        # If the part ID is not a positive number throw an error
        if part_id > 0:
            self._part_id = part_id
        else:
            raise ValueError("Part ID must be a positive number")
        # If the part name is null or empty throw an exception as a part must have a name
        if is_null_or_white_space(name):
            raise ValueError("A vehicle part must have a name")
        else:
            self._name = name
        self._colour = colour
        # If the part manufacture is null or empty throw an exception as a part must have a manufacture
        if is_null_or_white_space(manufacturer):
            raise ValueError("A vehicle part must have a manufacture")
        else:
            self._manufacturer = manufacturer
        # If the part has a negative dimensions throw an error
        if any(value < 0 for value in dimensions.values()):
            raise ValueError("An Objects Length, Width and Height must be a positive number")
        else:
            self._dimensions = dimensions

    def __str__(self) -> str:
        """
        Returns a part object as a string
        :parameter Part self: The part object
        :returns: A part object as a string
        """
        return f"Part Name: {self._name}\nPart ID: {self._part_id}\nColour: \n{self._colour}\n" \
               f"Manufacture: {self._manufacturer}\n" + f'\n'.join(f"{dimension_type}: {dimension_value} Meters"
                                                                   for dimension_type, dimension_value in
                                                                   self._dimensions.items())

    @property
    def part_id(self) -> int:
        """
        Return the Part ID number
        :parameter Part self: The part object
        :returns: The Part ID number
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id: int) -> None:
        """
        Set the Part ID number
        :parameter Part self: The part object
        :parameter int part_id: The Part ID number
        :returns: None
        :raises ValueError: if the part ID isn't a positive number
        """
        # If the part ID is not a positive number throw an error
        if part_id > 0:
            self._part_id = part_id
        else:
            raise ValueError("Part ID must be a positive number")

    @property
    def name(self) -> str:
        """
        Returns the parts name
        :parameter Part self: The part object
        :returns: The name of the part
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Update the parts name
        :parameter Part self: The part object
        :parameter str name: The name of the part
        :raises ValueError: If the part has no name
        :returns: None
        """
        # If the part name is null or empty throw an exception as a part must have a name
        if is_null_or_white_space(name):
            raise ValueError("A vehicle part must have a name")
        else:
            self._name = name

    @property
    def colour(self) -> Colour:
        """
        Returns the parts colour
        :parameter Part self: The part object
        :returns: The colour of the part
        """
        return self._colour

    @colour.setter
    def colour(self, colour: Colour) -> None:
        """
        Update the parts colour
        :parameter Part self: The part object
        :parameter Colour colour: The colour of the part
        :returns: None
        """
        self._colour = colour

    @property
    def manufacturer(self) -> str:
        """
        Returns the parts manufacture
        :parameter Part self: The part object
        :returns: The parts manufacture
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str) -> None:
        """
        Set the parts manufacture
        :parameter Part self: The part object
        :parameter str manufacturer: The parts manufacture
        :raises ValueError: if the part has no manufacture
        :returns: None
        """
        # If the part manufacture is null or empty throw an exception as a part must have a manufacture
        if is_null_or_white_space(manufacturer):
            raise ValueError("A vehicle part must have a manufacture")
        else:
            self._manufacturer = manufacturer

    @property
    def dimensions(self) -> dict[str, float]:
        """
        Return the parts dimensions
        :parameter Part self: The part object
        :returns: The parts dimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions: dict[str, float]) -> None:
        """
        Set the parts dimensions
        :parameter Part self: The part object
        :parameter dict[str, float] dimensions: The parts dimensions
        :raises ValueError: if the dimensions aren't valid
        :returns: None
        """
        # If the part has negative dimensions throw an error
        if any(value < 0 for value in dimensions.values()):
            raise ValueError("An Objects Length, Width and Height must be a positive number")
        else:
            self._dimensions = dimensions
