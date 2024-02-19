from Colour import Colour
from Utils import is_null_or_white_space
from collections import OrderedDict


class Part:

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str, dimensions: OrderedDict[str, float]):
        """
        Constructor for a Part Object
        Parameters:
            self (Part): The Part Object
            part_id (int): The Part ID number
            name (str): The name of the part
            colour (Colour): The colour of the part
            manufacturer (str): The parts manufacture
            dimensions (OrderedDict[str, float]): The parts dimensions
        :raises ValueError if the parameters aren't valid
        Returns:
            None
        """
        # If the part ID is not a positive number throw an error
        if part_id > 0:
            self.__part_id = part_id
        else:
            raise ValueError("Part ID must be a positive number")
        # If the part name is null or empty throw an exception as a part must have a name
        if is_null_or_white_space(name):
            raise ValueError("A vehicle part must have a name")
        else:
            self.__name = name
        self.__colour = colour
        # If the part manufacture is null or empty throw an exception as a part must have a manufacture
        if is_null_or_white_space(manufacturer):
            raise ValueError("A vehicle part must have a manufacture")
        else:
            self.__manufacturer = manufacturer
        # If the dimensions are valid throw an error
        if dimensions["Length"] > 0 and dimensions["Width"] > 0 and dimensions["Height"] > 0:
            self.__dimensions = dimensions
        else:
            raise ValueError("A parts length, width and height must be a positive number")

    def __str__(self):
        """
        Returns a Part object as a string
        Parameters:
            self (Part): The Part object
        Returns:
            Formatted string of a Part object
        """
        return f"Part Name: {self.__name}\nPart ID: {self.__part_id}\nColour: \n{self.__colour}\n" \
               f"Manufacture: {self.__manufacturer}\n" + f'\n'.join(f"{dimension_type}: {dimension_value} Meters"
                                                                    for dimension_type, dimension_value in
                                                                    self.__dimensions.items())

    @property
    def part_id(self):
        """
        Return the Part ID number
        Parameters:
            self (Part): The Part Object
        Returns:
            self.__part_id (int): The Part ID number
        """
        return self.__part_id

    @part_id.setter
    def part_id(self, part_id: int):
        """
        Set the Part ID number
        :param Part self: The Part
        :param int part_id: The Part ID number
        :return: None
        :raises ValueError: if the part ID isn't a positive number
        """
        # If the part ID is not a positive number throw an error
        if part_id > 0:
            self.__part_id = part_id
        else:
            raise ValueError("Part ID must be a positive number")

    @property
    def name(self):
        """
        Return the name of the part
        Parameters:
            self (Part): The Part Object
        Returns:
            self.__name (str): The name of the part
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Set the name of the part
        Parameters:
            self (Part): The Part Object
            name (str): The name of the part
        Returns:
            None
        """
        # If the part name is null or empty throw an exception as a part must have a name
        if is_null_or_white_space(name):
            raise ValueError("A vehicle part must have a name")
        else:
            self.__name = name

    @property
    def colour(self):
        """
        Return the colour of the part
        Parameters:
            self (Part): The Part Object
        Returns:
            self.__colour (Colour): The colour of the part
        """
        return self.__colour

    @colour.setter
    def colour(self, colour: Colour):
        """
        Set the colour of the part
        Parameters:
            self (Part): The Part Object
            colour (Colour): The colour of the part
        Returns:
            None
        """
        self.__colour = colour

    @property
    def manufacturer(self):
        """
        Return the parts manufacture
        Parameters:
            self (Part): The Part Object
        Returns:
            self.__manufacturer (str): The parts manufacture
        """
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        """
        Set the parts manufacture
        Parameters:
            self (Part): The Part Object
            manufacturer (str): The parts manufacture
        Returns:
            None
        """
        # If the part manufacture is null or empty throw an exception as a part must have a manufacture
        if is_null_or_white_space(manufacturer):
            raise ValueError("A vehicle part must have a manufacture")
        else:
            self.__manufacturer = manufacturer

    @property
    def dimensions(self):
        """
        Return the parts dimensions
        Parameters:
            self (Part): The Part Object
        Returns:
            self.__dimensions (OrderedDict[str, float]): The parts dimensions
        """
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: dict[str, float]):
        """
        Set the parts dimensions
        Parameters:
            self (Part): The Part Object
            dimensions (OrderedDict[str, float]): The parts dimensions
        Returns:
            None
        """
        # If the dimensions are valid throw an error
        if dimensions["length"] > 0 and dimensions["width"] > 0 and dimensions["height"] > 0:
            self.__dimensions = dimensions
        else:
            raise ValueError("A parts length, width and height must be a positive number")


def main():
    colour = Colour(1, 0.2, 0.3, 0.4)
    dimensions = OrderedDict()
    dimensions["Length"] = 100
    dimensions["Width"] = 100
    dimensions["Height"] = 100
    part = Part(1, "wheel", colour, "Audi", dimensions)
    print(part)


if __name__ == "__main__":
    main()
