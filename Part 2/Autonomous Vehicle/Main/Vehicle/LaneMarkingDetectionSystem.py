class LaneMarkingDetectionSystem:
    def __init__(self, left_distance: float, right_distance: float) -> None:
        """
        Constructor for the lane marking detection system object
        :parameter LaneMarkingDetectionSystem self: The lane marking detection system object
        :parameter float left_distance: Distance from left lane marking
        :parameter float right_distance: Distance from right lane marking
        :returns: None
        """
        # The distance from the lane markings
        self._left_distance = left_distance
        self._right_distance = right_distance

    def __str__(self):
        return (f"Distance from left lane marking: {self._left_distance} Meters\n"
                f"Distance from right lane marking: {self._right_distance} Meters\n"
                f"In Lane") if self.in_lane() \
            else (f'Distance from left lane marking: {self._left_distance} Meters\n'
                  f'Distance from right lane marking: {self._right_distance} Meters\n'
                  f'Not In Lane')

    @property
    def left_distance(self) -> float:
        """
        Returns the distance from left lane marking
        :parameter LaneMarkingDetectionSystem self: The lane marking detection system object
        :returns: The distance from left lane marking
        """
        return self._left_distance

    @left_distance.setter
    def left_distance(self, left_distance: float) -> None:
        """
        Set the distance from left lane marking
        :parameter LaneMarkingDetectionSystem self: The lane marking detection system object
        :parameter float left_distance: Distance from left lane marking
        :returns: None
        """
        self._left_distance = left_distance

    @property
    def right_distance(self) -> float:
        """
        Returns the distance from right lane marking
        :parameter LaneMarkingDetectionSystem self: The lane marking detection system object
        :returns: The distance from right lane marking
        """
        return self._right_distance

    @right_distance.setter
    def right_distance(self, right_distance: float) -> None:
        """
        Set the lane markings position on the right hand side of the vehicle
        :parameter LaneMarkingDetectionSystem self: The lane marking detection system object
        :parameter float right_distance: Distance from right lane marking
        :returns: None
        """
        self._right_distance = right_distance

    def in_lane(self) -> bool:
        """
        Checks your in the lane based on your distance from the lane markings
        :parameter LaneMarkingDetectionSystem self: The lane marking detection system object
        :returns: Boolean value representing if your in the lane based off the distance to the lane markings
        """
        # If the distance to the right and left lane are positive you are in the lane
        return self._right_distance >= 0 and self._left_distance >= 0
