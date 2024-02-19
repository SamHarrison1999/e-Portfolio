class Speed:
    def __init__(self, top_speed: int, acceleration: float, current_speed: float):
        """
        Constructor for the speed object
        Parameters:
            self (Speed): The speed object
            top_speed (int): The vehicles top speed
            acceleration (float): The vehicles acceleration
            current_speed (float): The vehicles current speed
        Returns:
            None
        """
        # If the vehicles top speed is a negative number throw an error
        if top_speed > 0:
            self.__top_speed = top_speed
        else:
            raise ValueError("Top speed must be a positive number")
        if acceleration > 0:
            self.__acceleration = acceleration
        else:
            raise ValueError("The 0 - 60 time must be greater than 0 seconds")
        # If current speed is less than 0 throw an error
        if current_speed >= 0:
            # If current speed is greater than the top speed set current speed to the top speed
            if current_speed >= self.__top_speed:
                self.__current_speed = self.__top_speed
            else:
                self.__current_speed = current_speed
        else:
            raise ValueError("Current speed must be at least 0 MPH")

    def __str__(self):
        """
        Returns the speed object as a string
        Parameters:
            self (Speed): The speed object
        Returns:
            The speed object as a string
        """
        return f'Current Speed: {self.__current_speed}MPH\n' \
               f'Top Speed: {self.__top_speed}\n' \
               f'0-60 MPH Speed: {self.__acceleration} seconds '

    @property
    def current_speed(self):
        """
        Returns the vehicles current speed
        Parameters:
            self (Speed): The speed object
        Returns:
            self.__current_speed (float): The vehicles current speed
        """
        return self.__current_speed

    @current_speed.setter
    def current_speed(self, current_speed: float):
        """
        Set the vehicles current speed
        Parameters:
            self (Speed): The speed object
            current_speed (float): The vehicles current speed
        Returns:
            None
        """
        # If current speed is less than 0 throw an error
        if current_speed >= 0:
            # If current speed is greater than the top speed set current speed to the top speed
            if current_speed >= self.__top_speed:
                self.__current_speed = self.__top_speed
            else:
                self.__current_speed = current_speed
        else:
            raise ValueError("Current speed must be at least 0 MPH")

    @property
    def top_speed(self):
        """
        Returns the vehicles top speed
        Parameters:
            self (Speed): The speed object
        Returns:
            self.__top_speed (int): The vehicles top speed
        """
        return self.__top_speed

    @top_speed.setter
    def top_speed(self, top_speed: int):
        """
        Set the vehicles top speed
        Parameters:
            self (Speed): The speed object
            top_speed (int): The vehicles top speed
        Returns:
            None
        """
        # If the vehicles top speed is a negative number throw an error
        if top_speed > 0:
            self.__top_speed = top_speed
        else:
            raise ValueError("Top speed must be a positive number")

    @property
    def acceleration(self):
        """
        Returns the vehicles acceleration
        Parameters:
            self (Speed): The speed object
        Returns:
            self.__acceleration (float): The vehicles acceleration
        """
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, acceleration: float):
        """
        Set the vehicles acceleration (0-60 Speed)
        Parameters:
            self (Speed): The speed object
            acceleration (float): The vehicles acceleration
        Returns:
            None
        """
        if acceleration > 0:
            self.__acceleration = acceleration
        else:
            raise ValueError("The 0 - 60 MPH time must be greater than 0 seconds")

    def accelerate(self):
        """
        Increase the current speed if its less than the top speed
        Parameters:
            self (Speed): The speed object
        Returns:
            None
        """
        if self.__current_speed < self.__top_speed:
            self.__current_speed += 1

    def decelerate(self):
        """
        Decrease the current speed if there current speed is greater than 0 MPH
        Parameters:
            self (Speed): The speed object
        Returns:
            None
        """
        if self.__current_speed > 0:
            self.__current_speed -= 1


def main():
    speed = Speed(150, 5, 70)
    print(speed)
    speed.accelerate()
    print(speed)
    speed.decelerate()
    print(speed)


if __name__ == "__main__":
    main()
