speed_limit_signs = [20, 30, 40, 50, 70]


class RoadSign:
    def __init__(self, speed_limit: int):
        """
        Constructor for a Road Sign
        Parameters:
            self (RoadSign): The Road Sign Object
            speed_limit (int): The speed limit
        Returns:
            None
        """
        # If the road sign speed isn't support throw an error
        if speed_limit in speed_limit_signs:
            self.__speed_limit = speed_limit
        else:
            raise ValueError("Road sign not supported")

    def __str__(self):
        """
        Returns the Road Sign object as a string
        Parameters:
            self (RoadSign): The Road Sign object
        Returns:
            Formatted string of the Road Sign Object
        """
        return f'Road Sign: {self.__speed_limit} MPH'

    @property
    def speed_limit(self):
        """
        Get the speed limit
        Parameters:
            self (RoadSign): The Road Sign Object
        Returns:
            self.__speed_limit (int): The speed limit
        """
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit: str):
        """
        Set the speed limit
        Parameters:
            self (RoadSign): The Road Sign Object
            speed_limit (int): The speed limit
        Returns:
            None
        """
        if speed_limit in speed_limit_signs:
            self.__speed_limit = speed_limit
        else:
            raise ValueError("Road sign not supported")


def main():
    sign = RoadSign(30)
    print(sign)


if __name__ == "__main__":
    main()
