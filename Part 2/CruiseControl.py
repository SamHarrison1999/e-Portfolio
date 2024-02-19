from Speed import Speed


class CruiseControl:
    def __init__(self, activated: bool, target_speed: int, recommended_following_distance: int, following_distance: int, speed: Speed):
        """
        Constructor for Cruise Control Object
        Parameters:
            self (CruiseControl): Cruise Control Object
            activated (bool): Whether Cruise Control is turned on or off
            target_speed (int): Target speed
            recommended_following_distance: The recommended following distance
            following_distance: The distance from the car in front
            speed (Speed): The speed object for the vehicle (Contains current speed, top speed and 0-60 speed)
        Returns:
            None
        """
        self.__activated = activated
        # If the target speed isn't a positive number throw an error
        if target_speed > 0:
            self.__target_speed = target_speed
        else:
            raise ValueError("Target speed must be a positive number")
        # If the recommended following distance isn't a positive number throw an error
        if recommended_following_distance > 0:
            self.__recommended_following_distance = recommended_following_distance
        else:
            raise ValueError("The recommended following distance must be a positive number")
        if following_distance == 0:
            print("Crash")
        self.__following_distance = following_distance
        if speed.current_speed > target_speed and activated:
            speed.current_speed = target_speed
        self.__speed = speed

    def __str__(self):
        """
        Returns the Cruise Control object as a string
        Parameters:
            self (CruiseControl): Cruise Control Object
        Returns:
            Formatted string of a Cruise Control Object
        """
        return "Cruise Control " + f''.join("Activated" if self.__activated else "Deactivated") + "\nTarget Speed: " + str(self.__target_speed) + "MPH" + f'\nCurrent Speed: {self.__speed.current_speed}MPH\nRecommended Following Distance: {self.__recommended_following_distance} meters\nDistance From The Closest Car: {self.__following_distance} meters'

    @property
    def activated(self):
        """
        Checks Whether Cruise Control is turned on or off
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            self.__activated (bool): Whether Cruise Control is turned on or off
        """
        return self.__activated

    @activated.setter
    def activated(self, activated):
        """
        Update Cruise Control status
        Parameters:
            self (CruiseControl): Cruise Control object
            activated (bool): Whether Cruise Control is turned on or off
        Returns:
            None
        """
        self.__activated = activated

    @property
    def target_speed(self):
        """
        Returns the set target speed
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            self.__speed (int): The target speed
        """
        return self.__speed

    @target_speed.setter
    def target_speed(self, target_speed):
        """
        Set the target speed
        Parameters:
            self (CruiseControl): Cruise Control object
            target_speed (int): The target speed
        Returns:
            None
        """
        # If the target speed isn't a positive number throw an error
        if target_speed > 0:
            self.__target_speed = target_speed
        else:
            raise ValueError("Target speed must be a positive number")

    @property
    def recommended_following_distance(self):
        """
        Gets the recommended following distance
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            self.__recommended_following_distance (int): The recommended following distance
        """
        return self.__recommended_following_distance

    @recommended_following_distance.setter
    def recommended_following_distance(self, recommended_following_distance):
        """
        Set the recommended following distance
        Parameters:
            self (CruiseControl): Cruise Control object
            recommended_following_distance (int): The recommended following distance
        Returns:
            None
        """
        # If the recommended following distance isn't a positive number throw an error
        if recommended_following_distance > 0:
            self.__recommended_following_distance = recommended_following_distance
        else:
            raise ValueError("The recommended following distance must be a positive number")

    @property
    def following_distance(self):
        """
        Gets the actual following distance
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            self.__following_distance (int): The actual following distance
        """
        return self.__following_distance

    @following_distance.setter
    def following_distance(self, following_distance):
        """
        Set the distance from the closest car
        Parameters:
            self (CruiseControl): Cruise Control object
            following_distance (int): The distance from the closest car
        Returns:
            None
        """
        self.__following_distance = following_distance

    @property
    def speed(self):
        """
        Returns the current speed
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            self.__speed (int): The current speed
        """
        return self.__speed

    @speed.setter
    def speed(self, speed):
        """
        Set the current speed
        Parameters:
            self (CruiseControl): Cruise Control object
            speed (int): The current speed
        Returns:
            None
        """
        if speed.current_speed > self.__target_speed:
            speed.current_speed = self.__target_speed
        self.__speed = speed

    def enable_cruise_control(self):
        """
        Turn on Cruise Control
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            None
        """
        self.__activated = True

    def disable_cruise_control(self):
        """
        Turn off Cruise Control
        Parameters:
            self (CruiseControl): Cruise Control object
        Returns:
            None
        """
        self.__activated = False


def main():
    speed = Speed(100, 5, 30)
    cc = CruiseControl(True, 70, 30, 30, speed)
    print(cc)


if __name__ == "__main__":
    main()
