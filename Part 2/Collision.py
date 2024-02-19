class Collision:

    def __init__(self, collision_occurred: bool, handbrake_engaged: bool, hazard_lights_turned_on: bool):
        """
        Constructor for Collision Detection Object
        Parameters:
            self (Collision): Collision Detection Object
            collision_occurred (bool): Whether a collision occurred
            handbrake_engaged (bool): Whether the handbrake is engaged
            hazard_lights_turned_on (bool): Whether the hazard lights are turned on or off
        Returns:
            None
        """
        self.__collision_occurred = collision_occurred
        self.__handbrake_engaged = handbrake_engaged
        self.__hazard_lights_turned_on = hazard_lights_turned_on

    def __str__(self):
        """
        Returns the Collision Detection Object as a string
        Parameters:
            self (Collision): Collision Detection Object
        Returns:
            The Collision Detection Object as a string
        """
        return f''.join({"Collision Detected" if self.__collision_occurred else "No Collision Detect"}) + f'\n' + f''.join({"Handbrake Engaged" if self.__handbrake_engaged else "Handbrake not engaged"}) + f'\n' + f'\n'.join({"Hazard Lights On" if self.__hazard_lights_turned_on else "Hazard Lights Off"})

    @property
    def collision_occurred(self):
        """
        Checks whether a collision occurred
        Parameters:
            self (Collision): Collision Detection Object
        Returns:
            self.__collision_occurred (bool): Whether a collision occurred
        """
        return self.__collision_occurred

    @collision_occurred.setter
    def collision_occurred(self, collision_occurred: bool):
        """
        Set whether a collision occurred
        Parameters:
            self (Collision): Collision Detection Object
            collision_occurred (bool): Whether a collision occurred
        Returns:
            None
        """
        self.__collision_occurred = collision_occurred

    @property
    def handbrake_engaged(self):
        """
        Checks whether the handbrake is engaged
        Parameters:
            self (Collision): Collision Detection Object
        Returns:
            self.__handbrake_engaged (bool): Whether the handbrake is engaged
        """
        return self.__handbrake_engaged

    @handbrake_engaged.setter
    def handbrake_engaged(self, handbrake_engaged: bool):
        """
        Sets whether the handbrake is engaged
        Parameters:
            self (Collision): Collision Detection Object
            handbrake_engaged (bool): Whether the handbrake is engaged
        Returns:
            None
        """
        self.__handbrake_engaged = handbrake_engaged

    @property
    def hazard_lights_turned_on(self):
        """
        Checks whether the hazard lights are turned on or off
        Parameters:
            self (Collision): Collision Detection Object
        Returns:
            self.__hazard_lights_turned_on (bool): Whether the hazard lights are turned on or off

        """
        return self.__hazard_lights_turned_on

    @hazard_lights_turned_on.setter
    def hazard_lights_turned_on(self, hazard_lights_turned_on: bool):
        """
        Set whether the hazard lights are turned on or off
        Parameters:
            self (Collision): Collision Detection Object
            hazard_lights_turned_on (bool): Whether the hazard lights are turned on or off
        Returns:
            None
        """
        self.__hazard_lights_turned_on = hazard_lights_turned_on

    def emergency_stop(self):
        """
        Performs an emergency stop
        Parameters:
            self (Collision): Collision Detection Object
        Returns:
            None
        """
        self.__collision_occurred = True
        self.__handbrake_engaged = True
        self.__hazard_lights_turned_on = True


def main():
    collision_detection = Collision(True, True, True)
    print(collision_detection)


if __name__ == "__main__":
    main()
