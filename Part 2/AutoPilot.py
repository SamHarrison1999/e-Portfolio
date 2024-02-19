from Weather import Weather


class AutoPilot:

    def __init__(self, enabled: bool, objects_detected: list, recommended_following_distance: int, following_distance: float, weather: Weather) -> None:
        """
        Constructor for a auto pilot object
        :parameter AutoPilot self: The auto pilot object
        :parameter bool enabled: Whether auto pilot is turned on or turned off
        :parameter list objects_detected: A list of objects that have been detected
        :parameter int recommended_following_distance: The recommended following distance
        :parameter float following_distance: The distance from the car in front
        :parameter Weather weather: The current weather
        :returns: None
        :raises ValueError: if the recommended following distance isn't a positive number
        """
        self.__enabled = enabled
        # If there are no objects set the list of objects detected to an empty list
        if objects_detected:
            self.__objects_detected = objects_detected
        else:
            self.__objects_detected = []
        # If the recommended following distance isn't a positive number throw an error
        if recommended_following_distance > 0:
            self.__recommended_following_distance = recommended_following_distance
        else:
            raise ValueError("The recommended following distance must be a positive number")
        if following_distance == 0:
            print("Crash")
        self.__following_distance = following_distance
        self.__weather = weather

    def __str__(self) -> str:
        """
        Returns an auto pilot object as a string
        :parameter AutoPilot self: An auto pilot object
        :returns: The auto pilot object as a string
        """
        if len(self.__objects_detected) > 1:
            object_output_string = "Objects Detected: "
        elif len(self.__objects_detected) == 1:
            object_output_string = "Object Detected: "
        else:
            object_output_string = ""
        return object_output_string + f''.join(f"\n{object_detected}" for object_detected in self.__objects_detected) + f"\nAutoPilot: {'Enabled' if self.__enabled else 'Disabled'}\nRecommended Following Distance: {self.__recommended_following_distance} meters\nDistance From The Closest Car: {self.__following_distance} meters\n{self.__weather}"

    @property
    def enabled(self) -> bool:
        """
        Get the auto pilot status (Whether auto pilot is turned on or turned off)
        :parameter self: An auto pilot object
        :returns: A boolean value representing if auto pilot is turned on or off
        """
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Set the auto pilot status
        :parameter AutoPilot self: An auto pilot object
        :parameter bool enabled: Whether auto pilot is turned on or turned off
        :returns: None
        """
        self.__enabled = enabled

    @property
    def objects_detected(self) -> list:
        """
        Get a list of all the objects detected
        :parameter AutoPilot self: An auto pilot object
        :returns: A List of objects that have been detected
        """
        return self.__objects_detected

    @objects_detected.setter
    def objects_detected(self, objects_detected: list) -> None:
        """
        Set the objects that have been detected
        :parameter AutoPilot self: An auto pilot object
        :parameter list objects_detected: A List of objects that have been detected
        :returns: None
        """
        # If there are no objects set the list of objects detected to an empty list
        if objects_detected:
            self.__objects_detected = objects_detected
        else:
            self.__objects_detected = []

    @property
    def recommended_following_distance(self) -> int:
        """
        Get the recommended following distance
        :parameter AutoPilot self: An auto pilot object
        :returns: The recommended following distance
        """
        return self.__recommended_following_distance

    @recommended_following_distance.setter
    def recommended_following_distance(self, recommended_following_distance: int) -> None:
        """
        Set the recommended following distance
        :parameter AutoPilot self: An auto pilot object
        :parameter int recommended_following_distance: The recommended following distance
        :returns: None
        :raises ValueError: if the recommended following distance isn't a positive number
        """
        # If the recommended following distance isn't a positive number throw an error
        if recommended_following_distance > 0:
            self.__recommended_following_distance = recommended_following_distance
        else:
            raise ValueError("The recommended following distance must be a positive number")

    @property
    def following_distance(self) -> float:
        """
        Get the actual following distance
        :parameter AutoPilot self: An auto pilot object
        :returns: The actual following distance
        """
        return self.__following_distance

    @following_distance.setter
    def following_distance(self, following_distance: float) -> None:
        """
        Set the distance from the closest car
        :parameter AutoPilot self: An auto pilot object
        :parameter int following_distance: The distance from the closest car
        :returns: None
        """
        self.__following_distance = following_distance

    @property
    def weather(self) -> Weather:
        """
        Returns the current weather
        :parameter AutoPilot self: An auto pilot object
        :returns: The current weather
        """
        return self.__weather

    @weather.setter
    def weather(self, weather: Weather) -> None:
        """
        Set the current weather
        :parameter AutoPilot self: An auto pilot object
        :parameter Weather weather: The current weather
        :returns: None
        """
        self.__weather = weather

    def turn_on_auto_pilot(self) -> None:
        """
        Turns on Auto Pilot
        :parameter AutoPilot self: An auto pilot object
        :returns: None
        """
        self.__enabled = True

    def turn_off_auto_pilot(self) -> None:
        """
        Turns off Auto Pilot
        :parameter AutoPilot self: An auto pilot object
        :returns: None
        """
        self.__enabled = False


def main():
    weather = Weather("Sunny", 25)
    auto_pilot = AutoPilot(True, ["Rock", "Cone"], 30, 30, weather)
    print(auto_pilot)


if __name__ == "__main__":
    main()
