class CollisionDetectionSystem:

    def __init__(self, collision_occurred: bool, handbrake_engaged: bool, hazard_lights_turned_on: bool):
        """
        Constructor for Collision Detection Object
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :parameter bool collision_occurred: Whether a collision occurred
        :parameter bool handbrake_engaged: Whether the handbrake is engaged
        :parameter bool hazard_lights_turned_on: Whether the hazard lights are turned on or off
        :returns: None
        """
        self.__collision_occurred = collision_occurred
        self.__handbrake_engaged = handbrake_engaged
        self.__hazard_lights_turned_on = hazard_lights_turned_on

    def __str__(self):
        """
        Returns the Collision Detection Object as a string
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :returns: The Collision Detection Object as a string
        """
        return (f''.join({"Collision Detected" if self.__collision_occurred else "No Collision Detected"}) + f'\n'
                + f''.join({"Handbrake Engaged" if self.__handbrake_engaged else "Handbrake not engaged"}) + f'\n'
                + f'\n'.join({"Hazard Lights On" if self.__hazard_lights_turned_on else "Hazard Lights Off"}))

    @property
    def collision_occurred(self):
        """
        Checks whether a collision occurred
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :returns: Whether a collision occurred
        """
        return self.__collision_occurred

    @collision_occurred.setter
    def collision_occurred(self, collision_occurred: bool):
        """
        Set whether a collision occurred
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :parameter bool collision_occurred: Whether a collision occurred
        :returns: None
        """
        self.__collision_occurred = collision_occurred

    @property
    def handbrake_engaged(self):
        """
        Checks whether the handbrake is engaged
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :returns: Whether the handbrake is engaged
        """
        return self.__handbrake_engaged

    @handbrake_engaged.setter
    def handbrake_engaged(self, handbrake_engaged: bool):
        """
        Sets whether the handbrake is engaged
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :parameter bool handbrake_engaged: Whether the handbrake is engaged
        :returns: None
        """
        self.__handbrake_engaged = handbrake_engaged

    @property
    def hazard_lights_turned_on(self):
        """
        Checks whether the hazard lights are turned on or off
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :returns: Whether the hazard lights are turned on or off
        """
        return self.__hazard_lights_turned_on

    @hazard_lights_turned_on.setter
    def hazard_lights_turned_on(self, hazard_lights_turned_on: bool):
        """
        Set whether the hazard lights are turned on or off
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :parameter bool hazard_lights_turned_on: Whether the hazard lights are turned on or off
        :returns: None
        """
        self.__hazard_lights_turned_on = hazard_lights_turned_on

    def emergency_stop(self):
        """
        Performs an emergency stop
        :parameter CollisionDetectionSystem self: Collision Detection System Object
        :returns: None
        """
        # When you perform an emergency stop you engage the handbrake and turn your hazard lights on
        self.__handbrake_engaged = True
        self.__hazard_lights_turned_on = True
