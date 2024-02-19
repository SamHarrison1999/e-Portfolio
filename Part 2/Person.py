from abc import ABC, abstractmethod
from collections import OrderedDict
from Utils import is_null_or_white_space


# Abstract Person Class
class Person(ABC):

    @property
    @abstractmethod
    def vitals(self) -> dict[str, float]:
        pass

    @vitals.setter
    @abstractmethod
    def vitals(self, vitals: dict[str, float]):
        pass


# Driver class
class Driver(Person):
    # The users credentials
    users: set[OrderedDict[str, str]] = []

    def __init__(self, credentials: OrderedDict[str, str], vitals: dict[str, float]):
        """
        Constructor for a Driver Object
        Parameters:
            self (Driver): The Driver Object
            credentials (OrderedDict[str, str]): The drivers credentials
            vitals (dict[str, float]): The drivers vitals
        Returns:
            None
        """
        # If credentials aren't set use the admin user
        if is_null_or_white_space(credentials["username"]) or is_null_or_white_space(credentials["password"]):
            self.__credentials = OrderedDict()
            self.__credentials["username"] = "admin"
            self.__credentials["password"] = "admin"
        else:
            self.__credentials = credentials
        # If all the drivers vitals aren't a positive number throw an error
        if all(value > 0 for value in vitals.values()):
            self.__vitals = vitals
        else:
            raise ValueError("All vitals values must be a positive integer")

    def __str__(self):
        """
        Returns a Driver Object as a string
        Parameters:
            self (Driver): The Driver object
        Returns:
            Formatted string of a Driver object
        """
        return f"Driver:\nVitals:" + f"".join(f"\n{key.capitalize()}: {value}" for key, value in self.__vitals.items()) + f"\nCredentials:" + f"".join(f"\n{key.capitalize()}: {value}" for key, value in self.__credentials.items())

    @property
    def credentials(self):
        """
        Returns the drivers credentials
        Parameters:
            self (Driver): The Driver object
        Returns:
            self.__credentials (dict[str, str]): The drivers credentials
        """
        return self.__credentials

    @credentials.setter
    def credentials(self, credentials: OrderedDict[str, str]):
        """
        Set the drivers credentials
        Parameters:
            self (Driver): The Driver object
            credentials (OrderedDict[str, str]): The drivers credentials
        Returns:
            None
        """
        # If credentials aren't set use the admin user
        if is_null_or_white_space(credentials["username"]) or is_null_or_white_space(credentials["password"]):
            self.__credentials = OrderedDict()
            self.__credentials["username"] = "admin"
            self.__credentials["password"] = "admin"
        else:
            self.__credentials = credentials

    @property
    def vitals(self):
        """
        Get the drivers vitals
        Parameters:
            self (Driver): The Driver object
        Returns:
            self.__vitals (dict[str, float]): The Drivers Vitals
        """
        return self.__vitals

    @vitals.setter
    def vitals(self, vitals: dict[str, float]):
        """
        Set the drivers vitals
        Parameters:
            self (Driver): The Driver object
            vitals (dict[str, float]): The Drivers Vitals
        Returns:
            None
        """
        if all(value > 0 for value in vitals.values()):
            self.__vitals = vitals
        else:
            raise ValueError("All vitals values must be a positive integer")

    def create_user(self, credentials: OrderedDict[str, str]):
        """
        Create a new user
        Parameters:
            self (Driver): The Driver object
            credentials (OrderedDict[str, str]): The users credentials
        Returns:
            None
        """
        # Add credentials to users list
        self.users.add(credentials)

    def delete_user(self, credentials: OrderedDict[str, str]):
        """
        Deletes a user
        Parameters:
            self (Driver): The Driver object
            credentials (OrderedDict[str, str]): The users credentials
        Returns:
            None
        """
        # Remove credentials from users list
        self.users.remove(credentials)

    def authenticate(self, username, password):
        """
        Authenticates the user
        Parameters:
            username (str): Their username
            password (str): Their password
        Returns:
            Confirmation that the user exists or doesn't exist
        """
        # If the user name and password are in the users list verify the user
        for user in self.users:
            for uname, pwd in user.items():
                if uname == username and pwd == password:
                    return "User Authenticated"
        return "Unable to Authenticate User"


# Passenger class
class Passenger(Person):

    def __init__(self, vitals: dict[str, float]):
        """
        Constructor for the Passenger Object
        Parameters:
            self (Passenger): The Passenger Object
            vitals (dict[str, float]): The passengers vitals
        Returns:
            None
        """
        if all(value > 0 for value in vitals.values()):
            self.__vitals = vitals
        else:
            raise ValueError("All vitals values must be a positive integer")

    def __str__(self):
        """
        Returns a Driver Passenger as a string
        Parameters:
            self (Passenger): The Passenger Object
        Returns:
            Formatted string of a Passenger Object
        """
        return f"Passenger:\nVitals:" + f"".join(f"\n{key.capitalize()}: {value}" for key, value in self.__vitals.items())

    @property
    def vitals(self):
        """
        Get the drivers vitals
        Parameters:
            self (Passenger): The Driver object
        Returns:
            self.__vitals (dict[str, float]): The Passengers Vitals
        """
        return self.__vitals

    @vitals.setter
    def vitals(self, vitals: dict[str, float]):
        """
        Set the drivers vitals
        Parameters:
            self (Passenger): The Passenger object
            vitals (dict[str, float]): The Drivers Vitals
        Returns:
            None
        """
        if all(value > 0 for value in vitals.values()):
            self.__vitals = vitals
        else:
            raise ValueError("All vitals values must be a positive integer")


def main():
    driver_vitals = {
        "heart rate": 100,
        "blood pressure": 50,
        "pulse": 30
    }
    passenger_vitals = {
        "heart rate": 120,
        "blood pressure": 60,
        "pulse": 80
    }
    credentials = OrderedDict()
    credentials["username"] = "test"
    credentials["password"] = "qwerty"
    driver = Driver(credentials, driver_vitals)
    print(driver)
    passenger = Passenger(passenger_vitals)
    print(passenger)


if __name__ == "__main__":
    main()
