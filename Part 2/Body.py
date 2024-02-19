from Colour import Colour
from Part import Part
from Utils import is_null_or_white_space
from collections import OrderedDict


class Body:
    def __init__(self, body_type: str, parts: list[Part]):
        """
        Constructor for Body Object
        Parameters:
            self (Body): Body object
            body_type (str): The Body Type of the car (E.G. Coupe)
            parts (list[Part]): A list of parts on the body of a vehicle (E.G. Trunk)
        Returns:
            None
        """
        # If the body type is null or empty throw an exception as a vehicle must have a body type
        if is_null_or_white_space(body_type):
            raise ValueError("A vehicle must have a body type")
        else:
            self.__body_type = body_type
        if parts:
            self.__parts = parts
        else:
            # If the lists of parts is empty throw an exception as a vehicles body must have at least one part
            raise ValueError("A vehicle's body must contain at least one part")

    def __str__(self):
        """
        Returns the body object as a string
        Parameters:
            self (Body): Body object
        Returns:
            Formatted string of a body object
        """
        return "Body Type: " + self.__body_type + f''.join(f"\n{part}" for part in self.__parts)

    @property
    def body_type(self):
        """
        Returns the vehicles body type
        Parameters:
            self (Body): Body object
        Returns:
            self.__body_type (str): The body type of the vehicle
        """
        return self.__body_type

    @body_type.setter
    def body_type(self, body_type: str):
        """
        Sets the vehicles body type
        Parameters:
            self (Body): Body object
            body_type (str): The body type of the vehicle
        Raises:
            ValueError (str): A vehicle's body type can't be null or an empty string
        """
        # If the body type is null or empty throw an exception as a vehicle must have a body type
        if is_null_or_white_space(body_type):
            raise ValueError("A vehicle must have a body type")
        else:
            self.__body_type = body_type

    @property
    def parts(self):
        """
        Gets a list of all the parts for the vehicles body
        Parameters:
            self (Body): Body object
        Returns:
            self.__parts(list[Part]): A list of parts for the vehicles body
        """
        return self.__parts

    @parts.setter
    def parts(self, parts: list[Part]):
        """
        A list of parts for the vehicles body
        Parameters:
            self (Body): Body object
            parts (list[Part]): A list of parts for the vehicles body
        Raises:
            ValueError (str): A vehicle's body must contain at least one part
        """
        if parts:
            self.__parts = parts
        else:
            # If the lists of parts is empty throw an exception as a vehicles body must have at least one part
            raise ValueError("A vehicle's body must contain at least one part")


def main():
    colour = Colour(1, 0.2, 0.3, 0.4)
    dimensions = OrderedDict()
    dimensions["Length"] = 200
    dimensions["Width"] = 100
    dimensions["Height"] = 2000
    trunk = Part(1, "Trunk", colour, "Audi", dimensions)
    parts = [trunk]
    body = Body("Coupe", parts)
    print(body)


if __name__ == "__main__":
    main()
