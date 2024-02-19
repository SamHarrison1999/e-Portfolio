from Colour import Colour
from Part import Part
from enum import Enum
from collections import OrderedDict


class Mode(Enum):
    ECO = 1
    COMFORT = 2
    SPORT = 3


class Engine:
    def __init__(self, size: float, horse_power: int, cylinders: int, valves: int, rpm: int, torque: int, mode: Mode, parts: list[Part]):
        """
        Constructor for a Engine Object
        Parameters:
            self (Engine): The Engine object
            size (float): The size of the engine
            horse_power (int): The break horse power produced by the engine
            cylinders (int): The number of cylinders in the engine
            valves (int): The number of valves in the eng
            rpm (int): The current RMP (Revs Per Minuet)
            torque (int): The amount of torque produced by the engine
            mode (Mode): The mode the engine is in (E.G. Sports)
            parts (list[Part]): The parts that make up the engine
        Returns:
            None
        """
        # If the engine size isn't a positive number throw an error
        if size > 0:
            self.__size = size
        else:
            raise ValueError("Engine size must be a positive number")
        # If the horse power isn't a positive number throw an error
        if horse_power > 0:
            self.__horse_power = horse_power
        else:
            raise ValueError("The engines break horse power must be a positive number")
        # If the number of cylinders in a engine isn't a positive number throw an error
        if cylinders > 0:
            self.__cylinders = cylinders
        else:
            raise ValueError("A Engine must have at least one cylinder")
        # If the number of valves in a engine isn't a positive number throw an error
        if valves > 0:
            self.__valves = valves
        else:
            raise ValueError("The number of valves in an engine must be a positive number")
        # If the RPM is below 0 throw an error
        if rpm >= 0:
            self.__rpm = rpm
        else:
            raise ValueError("The RPM must be at least 0")
        # If the amount of torque produced by the engine is below 0 throw an error
        if torque >= 0:
            self.__torque = torque
        else:
            raise ValueError("The torque must be at least 0")
        self.__mode = mode
        # If the engine is made up of 0 parts throw an error
        if parts:
            self.__parts = parts
        else:
            raise ValueError("A Vehicles engine is made up of at least one part")

    def __str__(self):
        """
        Returns an Engine object as a string
        Parameters:
            self (Engine): The Engine object
        Returns:
                Formatted string of an Engine object
        """
        return f"Engine Size: {self.__size}L\nBreak Horse Power: {self.__horse_power}\nNumber of Cylinders: {self.__cylinders}\nNumber of Valves: {self.__valves}\nRPM: {self.__rpm}\nTorque: {self.__torque}\nMode: {str(self.__mode.name).capitalize()}" + f''.join(f"\n{part}" for part in self.__parts)

    @property
    def size(self):
        """
        Returns the size of the engine
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__size (float): The size of the engine
        """
        return self.__size

    @size.setter
    def size(self, size: float):
        """
        Set the size of the engine
        Parameters:
            self (Engine): The Engine object
            size (float): The size of the engine
        Returns:
            None
        """
        # If the engine size isn't a positive number throw an error
        if size > 0:
            self.__size = size
        else:
            raise ValueError("Engine size must be a positive number")

    @property
    def horse_power(self):
        """
        Returns the amount of break horse power produced by the engine
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__horse_power (int): The amount of break horse power produced by the engine
        """
        return self.__horse_power

    @horse_power.setter
    def horse_power(self, horse_power: int):
        """
        Set the amount of break horse power produced by the engine
        Parameters:
            self (Engine): The Engine object
            horse_power (int): The amount of break horse power produced by the engine
        Returns:
            None
        """
        # If the horse power isn't a positive number throw an error
        if horse_power > 0:
            self.__horse_power = horse_power
        else:
            raise ValueError("The engines break horse power must be a positive number")

    @property
    def cylinders(self):
        """
        Returns the number of cylinders in a engine
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__cylinders (int): The number of cylinders in a engine
        """
        return self.__cylinders

    @cylinders.setter
    def cylinders(self, cylinders: int):
        """
        Set the number of cylinders in a engine
        Parameters:
            self (Engine): The Engine object
            cylinders (int): The number of cylinders in a engine
        Returns:
            None
        """
        # If the number of cylinders in a engine isn't a positive number throw an error
        if cylinders > 0:
            self.__cylinders = cylinders
        else:
            raise ValueError("A Engine must have at least one cylinder")

    @property
    def valves(self):
        """
        Returns the number of valves in a engine
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__valves (int): The number of valves in a engine
        """
        return self.__valves

    @valves.setter
    def valves(self, valves: int):
        """
        Set the number of valves in a engine
        Parameters:
            self (Engine): The Engine object
            valves (int): The number of valves in a engine
        Returns:
            None
        """
        # If the number of valves in a engine isn't a positive number throw an error
        if valves > 0:
            self.__valves = valves
        else:
            raise ValueError("The number of valves in an engine must be a positive number")

    @property
    def rpm(self):
        """
        Returns the current RPM
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__rpm (int): The current RPM
        """
        return self.__rpm

    @rpm.setter
    def rpm(self, rpm: int):
        """
        Set the current RPM
        Parameters:
            self (Engine): The Engine object
            rpm (int): The current RPM
        Returns:
            None
        """
        # If the RPM is below 0 throw an error
        if rpm >= 0:
            self.__rpm = rpm
        else:
            raise ValueError("The RPM must be at least 0")

    @property
    def torque(self):
        """
        Returns the amount of torque produced by the engine
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__torque (int): The amount of torque produced by the engine
        """
        return self.__torque

    @torque.setter
    def torque(self, torque: int):
        """
        Sets the amount of torque produced by the engine
        Parameters:
            self (Engine): The Engine object
            torque (int): The amount of torque produced by the engine
        Returns:
            None
        """
        # If the amount of torque produced by the engine is below 0 throw an error
        if torque >= 0:
            self.__torque = torque
        else:
            raise ValueError("The torque must be at least 0")

    @property
    def mode(self):
        """
        Returns the mode the engine is in
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__mode (Mode): The mode the engine is in
        """
        return self.__mode

    @mode.setter
    def mode(self, mode: Mode):
        """
        Sets the mode the engine is in
        Parameters:
            self (Engine): The Engine object
            mode (Mode): The mode the engine is in
        Returns:
            None
        """
        self.__mode = mode

    @property
    def parts(self):
        """
        Returns the parts in the engine
        Parameters:
            self (Engine): The Engine object
        Returns:
            self.__parts (list[Part]): The parts in the engine
        """
        return self.__parts

    @parts.setter
    def parts(self, parts: list[Part]):
        """
        Set the parts in the engine
        Parameters:
            self (Engine): The Engine object
            parts (list[Part]): The parts in the engine
        Returns:
            None
        """
        # If the engine is made up of 0 parts throw an error
        if parts:
            self.__parts = parts
        else:
            raise ValueError("A Vehicles engine is made up of at least one part")


def main():
    gear_box_colour = Colour(1, 0.2, 0.3, 0.4)
    crankshaft_colour = Colour(0.2, 0.5, 0.7, 0.8)
    gearbox_dimensions = OrderedDict()
    gearbox_dimensions["Length"] = 100
    gearbox_dimensions["Width"] = 50
    gearbox_dimensions["Height"] = 200
    crankshaft_dimensions = OrderedDict()
    crankshaft_dimensions["Length"] = 50
    crankshaft_dimensions["Width"] = 50
    crankshaft_dimensions["Height"] = 250
    gearbox = Part(1, "Gear Box", gear_box_colour, "Audi", gearbox_dimensions)
    crankshaft = Part(2, "Crankshaft", crankshaft_colour, "Audi", crankshaft_dimensions)
    parts = [gearbox, crankshaft]
    engine = Engine(2, 250, 12, 8, 1000, 100, Mode.SPORT, parts)
    print(engine)


if __name__ == "__main__":
    main()
