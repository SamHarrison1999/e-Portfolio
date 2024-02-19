from Main.Weather.Weather import Weather


class AutoPilot:

    def __init__(self, enabled: bool, weather: Weather, following_distance: float) -> None:
        """
        Constructor for an autopilot object
        :parameter AutoPilot self: The autopilot object
        :parameter bool enabled: Whether autopilot is turned on or turned off
        :parameter float following_distance: The distance from the car in front
        :parameter Weather weather: The current weather
        :returns: None
        :raises ValueError: if the recommended following distance isn't a positive number
        """
        self._enabled = enabled
        self._weather = weather
        # If the follow distance is below zero throw an error
        if following_distance >= 0:
            self._following_distance = following_distance
        else:
            raise ValueError("The following distance must be a positive number")

    def __str__(self) -> str:
        """
        Returns an autopilot object as a string
        :parameter AutoPilot self: An autopilot object
        :returns: The autopilot object as a string
        """
        return (f"AutoPilot: {'Enabled' if self._enabled else 'Disabled'}\nDistance From The Closest Car:"
                f" {self._following_distance} meters\n{self._weather}")

    @property
    def enabled(self) -> bool:
        """
        Get the autopilot status (Whether autopilot is turned on or turned off)
        :parameter self: An autopilot object
        :returns: A boolean value representing if autopilot is turned on or off
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Set the autopilot status
        :parameter AutoPilot self: An autopilot object
        :parameter bool enabled: Whether autopilot is turned on or turned off
        :returns: None
        """
        self._enabled = enabled

    @property
    def following_distance(self) -> float:
        """
        Get the actual following distance
        :parameter AutoPilot self: An autopilot object
        :returns: The actual following distance
        """
        return self._following_distance

    @following_distance.setter
    def following_distance(self, following_distance: float) -> None:
        """
        Set the distance from the closest car
        :parameter AutoPilot self: An autopilot object
        :parameter int following_distance: The distance from the closest car
        :returns: None
        """
        # If the follow distance is below zero throw an error
        if following_distance >= 0:
            self._following_distance = following_distance
        else:
            raise ValueError("The following distance must be a positive number")

    @property
    def weather(self) -> Weather:
        """
        Returns the current weather
        :parameter AutoPilot self: An autopilot object
        :returns: The current weather
        """
        return self._weather

    @weather.setter
    def weather(self, weather: Weather) -> None:
        """
        Set the current weather
        :parameter AutoPilot self: An autopilot object
        :parameter Weather weather: The current weather
        :returns: None
        """
        self._weather = weather

    def turn_on_auto_pilot(self) -> None:
        """
        Turns on Auto Pilot
        :parameter AutoPilot self: An auto pilot object
        :returns: None
        """
        self._enabled = True

    def turn_off_auto_pilot(self) -> None:
        """
        Turns off Auto Pilot
        :parameter AutoPilot self: An autopilot object
        :returns: None
        """
        self._enabled = False
