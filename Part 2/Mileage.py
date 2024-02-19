class Mileage:
    def __init__(self, miles_per_gallon: int, current_mileage: int):
        """
        Constructor for a Mileage Object
        Parameters:
            self (Mileage): Mileage Object
            miles_per_gallon (int): The MPG (Miles per gallon) the vehicle gets
            current_mileage (int): The vehicles current mileage
        Returns:
            None
        """
        # If the MPG is not a positive number throw an error
        if miles_per_gallon > 0:
            self.__miles_per_gallon = miles_per_gallon
        else:
            raise ValueError("The MPG must be a positive number")
        # If the vehicles current mileage is not at least 0 throw an error
        if current_mileage >= 0:
            self.__current_mileage = current_mileage
        else:
            raise ValueError("The vehicles current mileage must be at least 0")

    def __str__(self):
        """
        Returns the Mileage Object as a string
        Parameters:
            self (Mileage): Mileage Object
        Returns:
             The Mileage Object as a string
        """
        return f'MPG: {self.__miles_per_gallon}\nCurrent Mileage: {self.__current_mileage}'

    @property
    def miles_per_gallon(self):
        """
        Gets the MPG for the vehicle
        Parameters:
            self (Mileage): Mileage Object
        Returns:
            self.__miles_per_gallon (int): The MPG (Miles per gallon) the vehicle gets
        """
        return self.__miles_per_gallon

    @miles_per_gallon.setter
    def miles_per_gallon(self, miles_per_gallon):
        """
        Sets the MPG for the vehicle
        Parameters:
            self (Mileage): Mileage Object
            miles_per_gallon (int): The MPG (Miles per gallon) the vehicle gets
        Returns:
            None
        """
        # If the MPG is not a positive number throw an error
        if miles_per_gallon > 0:
            self.__miles_per_gallon = miles_per_gallon
        else:
            raise ValueError("The MPG must be a positive number")

    @property
    def current_mileage(self):
        """
        Gets the current mileage of the vehicle
        Parameters:
            self (Mileage): Mileage Object
        Returns:
            self.__current_mileage (int): The vehicles current mileage
        """
        return self.__current_mileage

    @current_mileage.setter
    def current_mileage(self, current_mileage):
        """
        Sets the current mileage of the vehicle
        Parameters:
            self (Mileage): Mileage Object
            current_mileage (int): The vehicles current mileage
        Returns:
            None
        """
        # If the vehicles current mileage is not at least 0 throw an error
        if current_mileage >= 0:
            self.__current_mileage = current_mileage
        else:
            raise ValueError("The vehicles current mileage must be at least 0")


def main():
    mileage = Mileage(40, 100000)
    print(mileage)


if __name__ == "__main__":
    main()
