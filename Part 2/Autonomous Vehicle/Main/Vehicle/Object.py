from Main.Utils.Utils import is_null_or_white_space


class Object:
    def __init__(self, name: str, dimensions: dict[str, float], lane_object_is_in: int, distance_to_object: float,
                 time_until_impact_with_object: float) -> None:
        """
        Constructor for the object being detected
        :parameter ObjectDetection self: The object being detected
        :parameter str name: The type of object (E.G. Cone)
        :parameter dict[str, float] dimensions: The dimensions of the object
        :parameter int lane_object_is_in: The lane the object is in
        :parameter float distance_to_object: The distance to the object
        :parameter float time_until_impact_with_object: The time until collision with the object at current speed
        :raises ValueError: If the object has no name or the dimensions are negative or the object is a negative number of meters away or the object is a negative number of seconds away
        :returns: None
        """
        # If the object has no type associated with it throw an error
        if is_null_or_white_space(name):
            raise ValueError("A object must have a name")
        else:
            self._name = name
        # If the object has any negative dimensions throw an error
        if any(value < 0 for value in dimensions.values()):
            raise ValueError("An Objects Length, Width and Height must be a positive number")
        else:
            self._dimensions = dimensions
        # If the object is on the road set the lane the object is in
        if lane_object_is_in > 0:
            self._lane_object_is_in = lane_object_is_in
        else:
            self._lane_object_is_in = None
        # If the object is closer than 0 meters from the vehicle throw an error
        if distance_to_object >= 0:
            # If the object is in a lane set the distance until collision with the object otherwise it can be ignored
            if self._lane_object_is_in is None:
                self._distance_to_object = None
            elif self._lane_object_is_in > 0:
                self._distance_to_object = distance_to_object
        else:
            raise ValueError("Distance to the object must be at least 0 meters")
        # If the time until collision with the object at current speed is less than 0 seconds throw an error
        if time_until_impact_with_object >= 0:
            # If the object is in a lane set the time until collision with the object otherwise it can be ignored
            if self._lane_object_is_in is None:
                self._time_until_impact_with_object = None
            elif self._lane_object_is_in > 0:
                self._time_until_impact_with_object = time_until_impact_with_object
        else:
            raise ValueError("The time until impact with the object must be at least 0 seconds")

    def __str__(self) -> str:
        return f'Object Name: {self._name}\nObject Dimensions:' + f"".join(
            f"\n{key.capitalize()}: {value} Meters" for key, value in
            self.dimensions.items()) + (f"\nObject in Lane {self._lane_object_is_in}\nDistance to object: "
                                        f"{self._distance_to_object} Meters\n"
                                        f"Time until impact with object at current speed: "
                                        f"{self._time_until_impact_with_object} Seconds") \
            if self._lane_object_is_in else f'Object Name: {self._name}\nObject Dimensions:' + f"".join(
            f"\n{key.capitalize()}: {value} Meters" for key, value in
            self.dimensions.items()) + f'\nObject not on road'

    @property
    def name(self) -> str:
        """
        Returns the name of the object that was detected
        :parameter ObjectDetection self: The object being detected
        :returns: The type of object (E.G. Cone)
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Update the name of the object being detected
        :parameter ObjectDetection self: The object being detected
        :parameter str name: The type of object (E.G. Cone)
        :raises ValueError: If the object has no name
        :returns: None
        """
        # If the object has no type associated with it throw an error
        if is_null_or_white_space(name):
            raise ValueError("A object must have a name")
        else:
            self._name = name

    @property
    def dimensions(self) -> dict[str, float]:
        """
        Returns the dimensions of the object that was detected
        :parameter ObjectDetection self: The object being detected
        :returns: The objects dimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions: dict[str, float]) -> None:
        """
        Update the dimensions of the object that was detected
        :parameter ObjectDetection self: The object being detected
        :parameter dict[str,float] dimensions: The objects dimensions
        :raises ValueError: If any of the dimensions of the object are a negative number
        :returns: None
        """
        # If the object has any negative dimensions throw an error
        if any(value < 0 for value in dimensions.values()):
            raise ValueError("An Objects Length, Width and Height must be a positive number")
        else:
            self._dimensions = dimensions

    @property
    def lane_object_is_in(self) -> int:
        """
        Returns the lane the object is in
        :parameter ObjectDetection self: The object being detected
        :returns: The lane the object is in
        """
        return self._lane_object_is_in

    @lane_object_is_in.setter
    def lane_object_is_in(self, lane_object_is_in: int) -> None:
        """
        Set the lane the object is in
        :parameter ObjectDetection self: The object being detected
        :parameter int lane_object_is_in: The lane the object is in
        :returns: None
        """
        # If the object is on the road set the lane the object is in
        if lane_object_is_in > 0:
            self._lane_object_is_in = lane_object_is_in
        else:
            self._lane_object_is_in = None

    @property
    def distance_to_object(self) -> float:
        """
        Returns the distance to the object from your current position
        :parameter ObjectDetection self: The object being detected
        :returns: The distance to the object
        """
        return self._distance_to_object

    @distance_to_object.setter
    def distance_to_object(self, distance_to_object: float) -> None:
        """
        Update the distance to the object from your current position
        :parameter ObjectDetection self: The object being detected
        :parameter float distance_to_object: The distance to the object
        :raises ValueError: If the object is a negative number of meters away
        :returns: None
        """
        # If the object is closer than 0 meters from the vehicle throw an error
        if distance_to_object >= 0:
            # If the object is in a lane set the distance until collision with the object otherwise it can be ignored
            if self._lane_object_is_in is None:
                self._distance_to_object = None
            elif self._lane_object_is_in > 0:
                self._distance_to_object = distance_to_object
        else:
            raise ValueError("Distance to the object must be at least 0 meters")

    @property
    def time_until_impact_with_object(self) -> float:
        """
        Returns the time until collision with the object at current speed
        :parameter ObjectDetection self: The object being detected
        :returns: The time until collision with the object at current speed
        """
        return self._time_until_impact_with_object

    @time_until_impact_with_object.setter
    def time_until_impact_with_object(self, time_until_impact_with_object: float) -> None:
        """
        Set the time until collision with the object at current speed
        :parameter ObjectDetection self: The object being detected
        :parameter float time_until_impact_with_object:  The time until collision with the object at current speed
        :raises ValueError: If the object is a negative number of seconds away
        :returns: None
        """
        # If the time until collision with the object at current speed is less than 0 seconds throw an error
        if time_until_impact_with_object >= 0:
            # If the object is in a lane set the time until collision with the object otherwise it can be ignored
            if self._lane_object_is_in is None:
                self._time_until_impact_with_object = None
            elif self._lane_object_is_in > 0:
                self._time_until_impact_with_object = time_until_impact_with_object
        else:
            raise ValueError("The time until impact with the object must be at least 0 seconds")
