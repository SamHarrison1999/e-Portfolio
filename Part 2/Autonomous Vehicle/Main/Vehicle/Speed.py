class Speed:
    def __init__(self, top_speed: int, acceleration: float, current_speed: float) -> None:
        """
        Constructor for the speed object
        :parameter Speed self: The speed object
        :parameter int top_speed: The vehicles top speed
        :parameter float acceleration: The vehicles acceleration
        :parameter float current_speed: The vehicles current speed
        :raises ValueError: If the current speed, top speed or acceleration is a negative number
        :returns: None
        """
        # If the vehicles top speed is a negative number throw an error
        if top_speed > 0:
            self._top_speed = top_speed
        else:
            raise ValueError("Top speed must be a positive number")
        # If the vehicles 0-60 speed is a negative number throw an error
        if acceleration > 0:
            self._acceleration = acceleration
        else:
            raise ValueError("The 0 - 60 time must be greater than 0 seconds")
        # If the current speed is between 0 and the top speed set the current speed
        # Else if the current speed is greater than the top speed set current speed to the top speed
        # Else throw an error
        if 0 <= current_speed <= self._top_speed:
            self._current_speed = current_speed
        elif current_speed >= self._top_speed:
            self._current_speed = self._top_speed
        else:
            raise ValueError("Current speed must be at least 0 MPH")

    def __str__(self) -> str:
        """
        Returns the speed object as a string
        :parameter Speed self: The speed object
        :returns: The speed object as a string
        """
        return f'Current Speed: {self._current_speed}MPH\n' \
               f'Top Speed: {self._top_speed}MPH\n' \
               f'0-60 MPH Speed: {self._acceleration} seconds '

    @property
    def current_speed(self) -> float:
        """
        Returns the vehicles current speed
        :parameter Speed self: The speed object
        :returns: The vehicles current speed
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed: float) -> None:
        """
        Set the vehicles current speed
        :parameter Speed self: The speed object
        :parameter float current_speed: The vehicles current speed
        :raises ValueError: If the current speed is a negative number
        :returns: None
        """
        # If the current speed is between 0 and the top speed set the current speed
        # Else if the current speed is greater than the top speed set current speed to the top speed
        # Else throw an error
        if 0 <= current_speed <= self._top_speed:
            self._current_speed = current_speed
        elif current_speed >= self._top_speed:
            self._current_speed = self._top_speed
        else:
            raise ValueError("Current speed must be at least 0 MPH")

    @property
    def top_speed(self) -> int:
        """
        Returns the vehicles top speed
        :parameter Speed self: The speed object
        :returns: The vehicles top speed
        """
        return self._top_speed

    @top_speed.setter
    def top_speed(self, top_speed: int) -> None:
        """
        Set the vehicles top speed
        :parameter Speed self: The speed object
        :parameter int top_speed: The vehicles top speed
        :returns: None
        :raises ValueError: If the top speed is a negative number
        """
        # If the vehicles top speed is a negative number throw an error
        if top_speed > 0:
            self._top_speed = top_speed
        else:
            raise ValueError("Top speed must be a positive number")

    @property
    def acceleration(self) -> float:
        """
        Returns the vehicles acceleration
        :parameter Speed self: The speed object
        :returns: The vehicles acceleration
        """
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration: float) -> None:
        """
        Set the vehicles acceleration (0-60 Speed)
        :parameter Speed self: The speed object
        :parameter float acceleration: The vehicles acceleration
        :returns: None
        :raises ValueError: If the acceleration is a negative number
        """
        # If the vehicles 0-60 speed is a negative number throw an error
        if acceleration > 0:
            self._acceleration = acceleration
        else:
            raise ValueError("The 0 - 60 MPH time must be greater than 0 seconds")

    def accelerate(self) -> None:
        """
        Increase the current speed if it is less than the top speed
        :parameter Speed self: The speed object
        :returns: None
        """
        # if the current speed is less than the top speed increase the current speed
        if self._current_speed < self._top_speed:
            self._current_speed += 1

    def decelerate(self) -> None:
        """
        Decrease the current speed if their current speed is greater than 0 MPH
        :parameter Speed self: The speed object
        :returns: None
        """
        # if the current speed is greater than 0 MPH slow down
        if self._current_speed > 0:
            self._current_speed -= 1
