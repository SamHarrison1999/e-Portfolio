class Mileage:
    def __init__(self, miles_per_gallon: float, current_mileage: float) -> None:
        """
        Constructor for the mileage object
        :parameter Mileage self: The mileage object
        :parameter float miles_per_gallon: The MPG (miles per gallon) the vehicle gets
        :parameter float current_mileage: The vehicles current mileage
        :raises ValueError: If the MPG or current mileage is below 0
        :returns: None
        """
        # If the MPG is not a positive number throw an error
        if miles_per_gallon > 0:
            self._miles_per_gallon = miles_per_gallon
        else:
            raise ValueError("The MPG must be a positive number")
        # If the vehicles current mileage is not at least 0 throw an error
        if current_mileage >= 0:
            self._current_mileage = current_mileage
        else:
            raise ValueError("The vehicles current mileage must be at least 0")

    def __str__(self) -> str:
        """
        Returns the mileage object as a string
        :parameter Mileage self: The mileage object
        :returns: The mileage object as a string
        """
        return f'MPG: {self._miles_per_gallon}\nCurrent Mileage: {self._current_mileage} Miles'

    @property
    def miles_per_gallon(self) -> float:
        """
        Gets the MPG for the vehicle
        :parameter Mileage self: The mileage object
        :returns: The MPG (Miles per gallon) the vehicle gets
        """
        return self._miles_per_gallon

    @miles_per_gallon.setter
    def miles_per_gallon(self, miles_per_gallon: float) -> None:
        """
        Sets the MPG for the vehicle
        :parameter Mileage self: The mileage object
        :parameter float miles_per_gallon: The MPG (Miles per gallon) the vehicle gets
        :raises ValueError: If the MPG is below 0
        :returns: None
        """
        # If the MPG is not a positive number throw an error
        if miles_per_gallon > 0:
            self._miles_per_gallon = miles_per_gallon
        else:
            raise ValueError("The MPG must be a positive number")

    @property
    def current_mileage(self) -> float:
        """
        Gets the current mileage of the vehicle
        :parameter Mileage self: The mileage object
        :returns: The vehicles current mileage
        """
        return self._current_mileage

    @current_mileage.setter
    def current_mileage(self, current_mileage: float) -> None:
        """
        Sets the current mileage of the vehicle
        :parameter Mileage self: The mileage object
        :parameter float current_mileage: The vehicles current mileage
        :raises ValueError: If the current mileage is below 0
        :returns: None
        """
        # If the vehicles current mileage is not at least 0 throw an error
        if current_mileage >= 0:
            self._current_mileage = current_mileage
        else:
            raise ValueError("The vehicles current mileage must be at least 0")
