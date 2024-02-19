from Main.Weather.Weather import Weather


class CruiseControl:
    def __init__(self, activated: bool, target_speed: int, weather: Weather, following_distance: float) -> None:
        """
        Constructor for a cruise control object
        :parameter CruiseControl self: A cruise control object
        :parameter bool activated: Whether cruise control is turned on or off
        :parameter int target_speed: The target speed
        :parameter Weather weather: The current weather
        :parameter float following_distance: The distance from the car in front
        :raises ValueError: If the target speed or following distance is a negative number
        :returns: None
        """
        self._activated = activated
        # If the target speed isn't set default the target speed to 0
        # else if the target speed isn't a positive number throw an error
        if target_speed is None:
            self._target_speed = 0
        elif target_speed > 0:
            self._target_speed = target_speed
        else:
            raise ValueError("Target speed must be a positive number")
        self._weather = weather
        # If the following distance is a negative number throw an error
        if following_distance >= 0.0:
            self._following_distance = following_distance
        else:
            raise ValueError("The following distance must be a positive number")

    def __str__(self) -> str:
        """
        Returns the cruise control object as a string
        :parameter CruiseControl self: A cruise control object
        :returns: A cruise control object as a string
        """
        return "Cruise Control " + f''.join(
            "Activated" if self._activated else "Deactivated") + "\nTarget Speed: " + str(
            self._target_speed) + "MPH" + (f'\nRecommended Following Distance:'
                                           f' {self._weather.recommended_following_distance()} Meters\n'
                                           f'Distance From The Closest Car: {self._following_distance} Meters')

    @property
    def activated(self) -> bool:
        """
        Checks whether cruise control is turned on or off
        :parameter CruiseControl self: A cruise control object
        :returns: Whether cruise control is turned on or off
        """
        return self._activated

    @activated.setter
    def activated(self, activated: bool) -> None:
        """
        Update cruise control status
        :parameter CruiseControl self: A cruise control object
        :parameter bool activated: Whether cruise control is turned on or off
        :returns: None
        """
        self._activated = activated

    @property
    def target_speed(self) -> int:
        """
        Returns the set target speed
        :parameter CruiseControl self: A cruise control object
        :returns: The target speed
        """
        return self._target_speed

    @target_speed.setter
    def target_speed(self, target_speed: int) -> None:
        """
        Set the target speed
        :parameter CruiseControl self: A cruise control object
        :parameter int target_speed: The target speed
        :raises ValueError: If the target speed is a negative number
        :returns: None
        """
        # If the target speed isn't set default the target speed to 0
        # else if the target speed isn't a positive number throw an error
        if target_speed is None:
            self._target_speed = 0
        elif target_speed > 0:
            self._target_speed = target_speed
        else:
            raise ValueError("Target speed must be a positive number")

    @property
    def weather(self) -> Weather:
        """
        Returns the current weather
        :parameter CruiseControl self: An cruise control object
        :returns: The current weather
        """
        return self._weather

    @weather.setter
    def weather(self, weather: Weather) -> None:
        """
        Set the current weather
        :parameter CruiseControl self: An cruise control object
        :parameter Weather weather: The current weather
        :returns: None
        """
        self._weather = weather

    @property
    def following_distance(self) -> float:
        """
        Gets the distance from the car in front
        :parameter CruiseControl self: A cruise control object
        :returns:  The distance from the car in front
        """
        return self._following_distance

    @following_distance.setter
    def following_distance(self, following_distance) -> None:
        """
        Set the distance from the closest car
        :parameter CruiseControl self: A cruise control object
        :parameter int following_distance: The distance from the car in front
        :raises ValueError: If the following distance is a negative number
        :returns: None
        """
        # If the following distance is a negative number throw an error
        if following_distance >= 0.0:
            self._following_distance = following_distance
        else:
            raise ValueError("The following distance must be a positive number")

    @property
    def cruise_control(self) -> str:
        """
        Get the cruise control object as a string
        :parameter CruiseControl self: A cruise control object
        :returns: A cruise control object as a string
        """
        return self.__str__()

    @cruise_control.setter
    def cruise_control(self, cruise_control) -> None:
        """
        Update the cruise control object
        :parameter CruiseControl self: The original cruise control object
        :parameter CruiseControl cruise_control: The updated cruise control object
        :returns: None
        """
        self._activated = cruise_control.activated
        self._target_speed = cruise_control.target_speed
        self._weather.weather_condition = cruise_control.weather.weather_condition
        self._weather.temperature = cruise_control.weather.temperature
        self._following_distance = cruise_control.following_distance

    def enable_cruise_control(self) -> None:
        """
        Turn on cruise control
        :parameter CruiseControl self: A cruise control object
        :returns: None
        """
        # Turn on cruise control if it is not already on
        if not self._activated:
            self._activated = True

    def disable_cruise_control(self) -> None:
        """
        Turn off cruise control
        :parameter CruiseControl self: A cruise control object
        :returns: None
        """
        # Turn off cruise control if it is not already off
        if self._activated:
            self._activated = False
