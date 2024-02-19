from collections import OrderedDict
from enum import Enum


class FuelType(Enum):
    DIESEL = 1
    UNLEADED = 2
    ELECTRIC = 3


class Fuel:
    def __init__(self, fuel_type: FuelType, capacity: int, fuel_remaining: float, closest_petrol_station: OrderedDict[str, int]):
        """
        Constructor for a Fuel Object
        Parameters:
            fuel_type (FuelType): The type of fuel (E.G. Diesel)
            capacity (int): The size of the fuel tank in liters
            fuel_remaining (float): The amount of fuel remaining in liters
            closest_petrol_station (OrderedDict[str, int]): The location of the closest petrol station
        Returns:
            None
        """
        self.__fuel_type = fuel_type
        # If the fuel tank can hold less than 0 Liters of fuel throw an error
        if capacity > 0:
            self.__capacity = capacity
        else:
            raise ValueError("Fuel tank size must be a positive number")
        # If there is less than 0 liters of fuel remaining throw an error
        if fuel_remaining >= 0:
            self.__fuel_remaining = fuel_remaining
        else:
            raise ValueError("The amount of fuel remaining must be at least 0 Liters")
        # If the location of the closest petrol station is not valid throw an error
        if -90 <= closest_petrol_station['latitude'] <= 90 and -180 <= closest_petrol_station['longitude'] <= 180 and len(closest_petrol_station) == 2:
            self.__closest_petrol_station = closest_petrol_station
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    def __str__(self):
        """
        Returns a Fuel object as a string
        Parameters:
            self (Fuel): The Fuel object
        Returns:
            Formatted string of a Fuel object
        """
        return f"Fuel Type: {str(self.__fuel_type.name).capitalize()}\nFuel Tank Capacity: {self.__capacity}L\nAmount of fuel remaining: {self.__fuel_remaining}L\nLocation of Closest Petrol Station: " + f"".join(f"\n{key.capitalize()}: {value}"for key, value in self.__closest_petrol_station.items())

    @property
    def fuel_type(self):
        """
        Returns the type of fuel (E.G. Diesel)
        Parameters:
            self (Fuel): The Fuel object
        Returns:
            self.__fuel_type (FuelType): The type of fuel
        """
        return self.__fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type: FuelType):
        """
        Sets the type of fuel (E.G. Diesel)
        Parameters:
            self (Fuel): The Fuel object
            fuel_type (FuelType): The type of fuel
        Returns:
            None
        """
        self.__fuel_type = fuel_type

    @property
    def capacity(self):
        """
        Returns the size of the fuel tank in liters
        Parameters:
            self (Fuel): The Fuel object
        Returns:
            self.__capacity (int): The size of the fuel tank in liters
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        """
        Sets the size of the fuel tank in liters
        Parameters:
            self (Fuel): The Fuel object
            capacity (int): The size of the fuel tank in liters
        Returns:
            None
        """
        # If the fuel tank can hold less than 0 Liters of fuel throw an error
        if capacity > 0:
            self.__capacity = capacity
        else:
            raise ValueError("Fuel tank size must be a positive number")

    @property
    def fuel_remaining(self):
        """
        Returns the amount of fuel remaining in liters
        Parameters:
            self (Fuel): The Fuel object
        Returns:
            self.__fuel_remaining (int): The amount of fuel remaining in liters
        """
        return self.__fuel_remaining

    @fuel_remaining.setter
    def fuel_remaining(self, fuel_remaining: float):
        """
        Set the amount of fuel remaining in liters
        Parameters:
            self (Fuel): The Fuel object
            fuel_remaining (float): The amount of fuel remaining in liters
        Returns:
            None
        """
        # If there is less than 0 liters of fuel remaining throw an error
        if fuel_remaining >= 0:
            self.__fuel_remaining = fuel_remaining
        else:
            raise ValueError("The amount of fuel remaining must be at least 0 Liters")

    @property
    def closest_petrol_station(self):
        """
        Returns the location of the closest petrol station
        Parameters:
            self (Fuel): The Fuel object
        Returns:
            self.__closest_petrol_station (OrderedDict[str, int]): The location of the closest petrol station
        """
        return self.__closest_petrol_station

    @closest_petrol_station.setter
    def closest_petrol_station(self, closest_petrol_station):
        """
        Set the location of the closest petrol station
        Parameters:
            self (Fuel): The Fuel object
            closest_petrol_station (OrderedDict[str, int]): The location of the closest petrol station
        Returns:
             None
        """
        # If the location of the closest petrol station is not valid throw an error
        if -90 <= closest_petrol_station['latitude'] <= 90 and -180 <= closest_petrol_station['longitude'] <= 180 and len(closest_petrol_station) == 2:
            self.__closest_petrol_station = closest_petrol_station
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")


def main():
    closest_petrol_station = OrderedDict()
    closest_petrol_station["latitude"] = 10
    closest_petrol_station["longitude"] = 50
    fuel = Fuel(FuelType.DIESEL, 100, 50, closest_petrol_station)
    print(fuel)


if __name__ == "__main__":
    main()
