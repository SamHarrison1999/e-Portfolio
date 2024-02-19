from Main.Vehicle.FuelType import FuelType


class Fuel:
    def __init__(self, fuel_type: FuelType, capacity: int, fuel_remaining: float) -> None:
        """
        Constructor for a Fuel Object
        :parameter Fuel self: The fuel object
        :parameter FuelType fuel_type: The type of fuel (E.G. Diesel)
        :parameter int capacity: The size of the fuel tank in liters
        :parameter float fuel_remaining: The amount of fuel remaining in liters
        :raises ValueError: If the fuel tank size or amount of fuel remaining is a negative number
        :returns:None
        """
        self._fuel_type = fuel_type
        # If the fuel tank can hold less than 0 Liters of fuel throw an error
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Fuel tank size must be a positive number")
        # If the amount of fuel remain is greater than 0 and less than the fuel tank size set the fuel
        # Else if the amount of fuel remaining is greater than the fuel tank size set the amount of fuel remaining
        # to the fuel tank size else throw an error
        if 0 <= fuel_remaining <= self._capacity:
            self._fuel_remaining = fuel_remaining
        elif fuel_remaining > self._capacity:
            self._fuel_remaining = self._capacity
        else:
            raise ValueError("The amount of fuel remaining must be at least 0 Liters")

    def __str__(self) -> str:
        """
        Returns a Fuel object as a string
        :parameter Fuel self: The fuel object
        :returns: The fuel object as a string
        """
        return (f"Fuel Type: {str(self._fuel_type.value).capitalize()}\nFuel Tank Capacity: "
                f"{self._capacity}L\nAmount of fuel remaining: {self._fuel_remaining}L")

    @property
    def fuel_type(self) -> FuelType:
        """
        Returns the type of fuel (E.G. Diesel)
        :parameter Fuel self: The fuel object
        :returns: The type of fuel
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type: FuelType) -> None:
        """
        Set the type of fuel (E.G. Diesel)
        :parameter Fuel self: The fuel object
        :parameter FuelType fuel_type: The type of fuel (E.G. Diesel)
        :returns: None
        """
        self._fuel_type = fuel_type

    @property
    def capacity(self) -> int:
        """
        Returns the size of the fuel tank in liters
        :parameter Fuel self: The fuel object
        :returns: The size of the fuel tank in liters
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        """
        Set the size of the fuel tank in liters
        :parameter Fuel self: The fuel object
        :parameter int capacity: The size of the fuel tank in liters
        :raises ValueError: If the fuel tank size is a negative number
        :returns: None
        """
        # If the fuel tank can hold less than 0 Liters of fuel throw an error
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Fuel tank size must be a positive number")

    @property
    def fuel_remaining(self) -> float:
        """
        Returns the amount of fuel remaining in liters
        :parameter Fuel self: The fuel object
        :returns: The amount of fuel remaining in liters
        """
        return self._fuel_remaining

    @fuel_remaining.setter
    def fuel_remaining(self, fuel_remaining: float) -> None:
        """
        Set the amount of fuel remaining in liters
        :parameter Fuel self: The fuel object
        :parameter float fuel_remaining: The amount of fuel remaining in liters
        :raises ValueError: If the amount of fuel remaining is a negative number
        :returns: None
        """
        # If the amount of fuel remain is greater than 0 and less than the fuel tank size set the fuel
        # Else if the amount of fuel remaining is greater than the fuel tank size set the amount of fuel remaining
        # to the fuel tank size else throw an error
        if 0 <= fuel_remaining <= self._capacity:
            self._fuel_remaining = fuel_remaining
        elif fuel_remaining > self._capacity:
            self._fuel_remaining = self._capacity
        else:
            raise ValueError("The amount of fuel remaining must be at least 0 Liters")

    def out_of_fuel(self) -> bool:
        """
        Check if there is no fuel remaining
        :parameter Fuel self: A fuel object
        :returns: If the vehicle is out of fuel
        """
        return self._fuel_remaining == 0.0

    def low_on_fuel(self) -> bool:
        """
        Check if the fuel level is low
        :parameter Fuel self: A fuel object
        :returns: If the vehicle is low on fuel
        """
        return self._fuel_remaining < 10
