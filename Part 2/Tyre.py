from Colour import Colour
from Part import Part
from collections import OrderedDict


class Tyre:
    def __init__(self, parts: list[Part], tread: float, tire_pressure: float):
        """
        Constructor for a tier object
        Parameters:
            self (Tyre): A tier object
            parts (list[Part): The parts that make up the tier (E.G. Rims)
            tread (float): The tread remaining on the tier
            tire_pressure (float): The tier pressure
        Returns:
            None
        """
        # If there are no parts throw an error
        if parts:
            self.__parts = parts
        else:
            raise ValueError("A tier is made up of at least one part")
        # If the amount of tread remaining is negative throw an error
        if tread >= 0:
            self.__tread = tread
        else:
            raise ValueError("The tread remaining on the tire must be at least 0mm")
        # If the tier pressure is negative throw an error
        if tire_pressure >= 0:
            self.__tire_pressure = tire_pressure
        else:
            raise ValueError("The tier pressure must be at least 0 psi")

    def __str__(self):
        """
        Returns the tier object as a string
        Parameters:
            self (Tyre): A tier object
        Returns:
            The tier object as a string
        """
        return f'\n'.join(f"{part}" for part in self.__parts) + f"\nCurrent Air Pressure: {self.__tire_pressure} psi\n" \
                                                                f"Tire Thread Remaining: {self.tread} mm"

    @property
    def parts(self):
        """
        Returns a list of the parts that make up the tier
        Parameters:
            self (Tyre): A tier object
        Returns:
            self.__parts (list[Part): The parts that make up the tier (E.G. Rims)
        """
        return self.__parts

    @parts.setter
    def parts(self, parts: list[Part]):
        """
        Set the parts that make up the tier
        Parameters:
            self (Tyre): A tier object
            parts (list[Part): The parts that make up the tier (E.G. Rims)
        Returns:
            None
        """
        # If there are no parts throw an error
        if parts:
            self.__parts = parts
        else:
            raise ValueError("A tier is made up of at least one part")

    @property
    def tread(self):
        """
        Returns the tread remaining on the tier
        Parameters:
            self (Tyre): A tier object
        Returns:
            self.__tread (float): The tread remaining on the tier
        """
        return self.__tread

    @tread.setter
    def tread(self, tread: float):
        """
        Set the tread remaining on the tier
        Parameters:
            self (Tyre): A tier object
            tread (float): The tread remaining on the tier
        Returns:
            None
        """
        # If the amount of tread remaining is negative throw an error
        if tread >= 0:
            self.__tread = tread
        else:
            raise ValueError("The tread remaining on the tire must be at least 0mm")

    @property
    def tire_pressure(self):
        """
        Returns the tier pressure
        Parameters:
            self (Tyre): A tier object
        Returns:
            self.__tire_pressure (float): The tier pressure
        """
        return self.__tire_pressure

    @tire_pressure.setter
    def tire_pressure(self, tire_pressure: float):
        """
        Set the tier pressure
        Parameters:
            self (Tyre): A tier object
            tire_pressure (float): The tier pressure
        Returns:
            None
        """
        # If the tier pressure is negative throw an error
        if tire_pressure >= 0:
            self.__tire_pressure = tire_pressure
        else:
            raise ValueError("The tier pressure must be at least 0 psi")


def main():
    wheel_colour = Colour(0, 0, 0, 1)
    rim_colour = Colour(0, 0, 0, 0)
    wheel_dimensions = OrderedDict()
    wheel_dimensions["Width"] = 200
    wheel_dimensions["Length"] = 200
    wheel_dimensions["Height"] = 20
    rim_dimensions = OrderedDict()
    rim_dimensions["Width"] = 100
    rim_dimensions["Length"] = 10
    rim_dimensions["Height"] = 10
    wheel = Part(1, "wheel", wheel_colour, "Audi", wheel_dimensions)
    rim = Part(2, "rim", rim_colour, "Audi", rim_dimensions)
    parts = [wheel, rim]
    tier = Tyre(parts, 10, 50)
    print(tier)


if __name__ == "__main__":
    main()
