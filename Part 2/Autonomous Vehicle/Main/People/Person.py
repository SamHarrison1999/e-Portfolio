import getpass
import re

from Main.Utils.Utils import is_null_or_white_space

# Constant for the password regex
PAASWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"


# Parent Class
class Person:
    vitals: dict


# The passenger class is a child class of the person class meaning it inherits all its methods and attributes
class Passenger(Person):

    def __init__(self, vitals: dict[str, float]) -> None:
        """
        Constructor for a passenger object
        :parameter Passenger self: A passenger
        :parameter dict[str, float] vitals: The passengers vitals
        :raises ValueError: If any of the passengers vitals are below 0
        :returns: None
        """
        # If any of the passengers vitals are below one throw an error
        if any(value < 0 for value in vitals.values()):
            raise ValueError("A persons vitals must be a positive number")
        else:
            self._vitals = vitals

    def __str__(self):
        """
        Return the passenger object as a string
        :parameter Passenger self: A passenger
        :returns: The passenger object as a string
        """
        return f'Passenger:' + f"".join(
            f"\n{vital_type}: {vital_value}" for vital_type, vital_value in self._vitals.items())

    @property
    def vitals(self) -> dict[str, float]:
        """
        Get the passengers vitals
        :parameter Passenger self: A passenger
        :returns: The passengers vitals
        """
        return self._vitals

    @vitals.setter
    def vitals(self, vitals: dict[str, float]) -> None:
        """
        Update the passengers vitals
        :parameter Passenger self: A passenger
        :parameter dict[str, float] vitals: The passengers vitals
        :raises ValueError: If any of the passengers vitals are below 0
        :returns: None
        """
        # If any of the passengers vitals are below one throw an error
        if any(value < 0 for value in vitals.values()):
            raise ValueError("A passengers vitals can't be a negative number")
        else:
            self._vitals = vitals


# The driver class is a child class of the person class meaning it inherits all its methods and attributes
class Driver(Person):

    def __init__(self, username: str, password: str, vitals: dict[str, float]) -> None:
        """
        Constructor for a driver object
        :parameter Driver self: The driver
        :parameter str username: The drivers username
        :parameter str password: The driver password
        :parameter dict[str, float] vitals: The drivers vitals
        :raises ValueError: If the username is empty or the password doesn't meet the password requirements or any of the drivers vitals are below 0
        :returns: None
        """
        # If the drivers username is empty throw an error
        if is_null_or_white_space(username):
            raise ValueError("Your username can't be empty")
        else:
            self._username = username
        # Password Requirements:
        # 1. At least one number.
        # 2. At least one uppercase and one lowercase character.
        # 3. At least one special symbol.
        # 4. Between 6 and 20 characters long.
        # compiling regex
        pattern = re.compile(PAASWORD_REGEX)
        # searching regex
        matcher = re.search(pattern, password)
        # validating conditions
        if matcher:
            self._password = password
        else:
            print(password)
            raise ValueError("Password is not valid")
        # If any of the drivers vitals are below one throw an error
        if any(value < 0 for value in vitals.values()):
            raise ValueError("The drivers vitals can't be below zero")
        else:
            self._vitals = vitals

    def __str__(self):
        """
        Return the driver object as a string
        :parameter Driver self: The Driver Object
        :returns: The driver object as a string
        """
        return f"Driver:\nUsername: {self._username}\nPassword: {self._password}" + f"".join(
            f"\n{vital_type}: {vital_value}" for vital_type, vital_value in self._vitals.items())

    @property
    def username(self) -> str:
        """
        Returns the drivers username
        :parameter Driver self: The driver
        :returns: The drivers username
        """
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        """
        Update the drivers username
        :parameter Driver self: The driver
        :parameter str username: The drivers username
        :raises ValueError: If the username is empty
        :returns: None
        """
        # If the drivers username is empty throw an error
        if is_null_or_white_space(username):
            raise ValueError("Your username can't be empty")
        else:
            self._username = username

    @property
    def password(self) -> str:
        """
        Returns the drivers password
        :parameter Driver self: The driver
        :returns: The drivers password
        """
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        """
        Update the users password
        :parameter Driver self: The driver
        :parameter str password: The drivers password new password
        :raises ValueError: If the password doesn't meet the password requirements
        """
        # Password Requirements:
        # 1. At least one number.
        # 2. At least one uppercase and one lowercase character.
        # 3. At least one special symbol.
        # 4. Between 6 and 20 characters long.
        # compiling regex
        pattern = re.compile(PAASWORD_REGEX)
        # searching PHONE_NUMBER_REGEX
        matcher = re.search(pattern, password)
        # validating conditions
        if matcher:
            self._password = password
        else:
            raise ValueError("Password is not valid")

    @property
    def vitals(self) -> dict[str, float]:
        """
        Get the drivers vitals
        :parameter Driver self: The driver
        :returns: The drivers vitals
        """
        return self._vitals

    @vitals.setter
    def vitals(self, vitals: dict[str, float]) -> None:
        """
        Update the drivers vitals
        :parameter Driver self: The driver
        :parameter dict[str, float] vitals: The drivers vitals
        :raises ValueError: If any of the drivers vitals are below 0
        :returns: None
        """
        # If any of the drivers vitals are below one throw an error
        if any(value < 0 for value in vitals.values()):
            raise ValueError("A persons vitals must be a positive number")
        else:
            self._vitals = vitals

    def login(self) -> bool:
        """
        Verify user credentials
        :parameter Driver self: The driver
        :returns: Weather user has been verified or not
        """
        # Authenticates the users based on their credentials
        usr = getpass.getuser()
        pwd = getpass.getpass(prompt="Enter your password")
        return usr == self._username and pwd == self._password
