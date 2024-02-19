from collections import OrderedDict


class LaneMarkingDetection:

    def __init__(self, vehicle_size: OrderedDict[str, float], left_lane_marking_position: OrderedDict[str, float], right_lane_marking_position: OrderedDict[str, float], vehicle_position: OrderedDict[str, float], lane_width: float, lane_unoccupied: bool):
        """
        Constructor for Lane Marking Detection Object
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            vehicle_size (OrderedDict[str, float]): The size of the vehicle
            left_lane_marking_position (OrderedDict[str, float]): The lane markings position on the left hand side of the vehicle
            right_lane_marking_position (OrderedDict[str, float]): The lane markings position on the right hand side of the vehicle
            vehicle_position (OrderedDict[str, float]): The vehicles current position
            lane_width (float): The width of the lane
            lane_unoccupied (bool): If the lane is unoccupied
        Returns:
            None
        """
        # If the vehicle dimensions aren't positive numbers throw an error
        if vehicle_size["length"] > 0 and vehicle_size["width"] > 0:
            self.__vehicle_size = vehicle_size
        else:
            raise ValueError("The vehicles size must be a positive number")
        # If the lane markings location aren't valid throw an error
        if -90 <= left_lane_marking_position['latitude'] <= 90 and -180 <= left_lane_marking_position['longitude'] <= 180 and len(left_lane_marking_position) == 2:
            self.__left_lane_marking_position = left_lane_marking_position
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        if -90 <= right_lane_marking_position['latitude'] <= 90 and -180 <= right_lane_marking_position['longitude'] <= 180 and len(right_lane_marking_position) == 2:
            self.__right_lane_marking_position = right_lane_marking_position
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        # If the vehicle location isn't valid throw an error
        if -90 <= vehicle_position['latitude'] <= 90 and -180 <= vehicle_position['longitude'] <= 180 and len(
                vehicle_position) == 2:
            self.__vehicle_position = vehicle_position
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        # If the lane width isn't a positive number throw an error
        if lane_width > 0:
            self.__lane_width = lane_width
        else:
            raise ValueError("The lane width must be a positive number")
        self.__lane_unoccupied = lane_unoccupied

    def __str__(self):
        """
        Returns the Lane Marking Detection object as a string
        Parameters:
            self (LaneMarkingDetection): The Lane Marking Detection object
        Returns:
            Formatted string of a the Lane Marking Detection object
        """
        return f"Vehicle Size:" + f"".join(f"\n{key.capitalize()}: {value}" for key, value in
                                           self.__vehicle_size.items()) + "\nLeft Lane Marking Position:" + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.__left_lane_marking_position.items()) + "\nRight Lane Marking Position:" + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.__right_lane_marking_position.items()) + "\nVehicle Position:" + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.__vehicle_position.items()) + f"\nLane Width: {self.lane_width}\n" + "" + f''.join(
            f"{'Lane Unoccupied' if self.__lane_unoccupied else 'Lane Occupied'}")

    @property
    def vehicle_size(self):
        """
        Get the vehicle size
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
        Returns:
            self.__vehicle_size (OrderedDict[str, float]): The size of the vehicle
        """
        return self.__vehicle_size

    @vehicle_size.setter
    def vehicle_size(self, vehicle_size: OrderedDict[str, float]):
        """
        Set the vehicle size
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            vehicle_size (OrderedDict[str, float]): The size of the vehicle
        Returns:
            None
        """
        # If the vehicle dimensions aren't positive numbers throw an error
        if vehicle_size["length"] > 0 and vehicle_size["width"] > 0:
            self.__vehicle_size = vehicle_size
        else:
            raise ValueError("The vehicles size must be a positive number")

    @property
    def left_lane_marking_position(self):
        """
        Get the lane markings position on the left hand side of the vehicle
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
        Returns:
            self.__left_lane_marking_position (OrderedDict[str, float]): The lane markings position on the left hand side of the vehicle
        """
        return self.__left_lane_marking_position

    @left_lane_marking_position.setter
    def left_lane_marking_position(self, left_lane_marking_position: OrderedDict[str, float]):
        """
        Set the lane markings position on the left hand side of the vehicle
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            left_lane_marking_position (OrderedDict[str, float]): The lane markings position on the left hand side of the vehicle
        Returns:
            None
        """
        # If the lane markings location aren't valid throw an error
        if -90 <= left_lane_marking_position['latitude'] <= 90 and -180 <= left_lane_marking_position['longitude'] <= 180 and len(left_lane_marking_position) == 2:
            self.__left_lane_marking_position = left_lane_marking_position
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def right_lane_marking_position(self):
        """
        Get the lane markings position on the right hand side of the vehicle
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
        Returns:
            self.__right_lane_marking_position (OrderedDict[str, float]): The lane markings position on the right hand side of the vehicle
        """
        return self.__right_lane_marking_position

    @right_lane_marking_position.setter
    def right_lane_marking_position(self, right_lane_marking_position: OrderedDict[str, float]):
        """
        Set the lane markings position on the right hand side of the vehicle
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            right_lane_marking_position (OrderedDict[str, float]): The lane markings position on the right hand side of the vehicle
        Returns:
            None
        """
        # If the lane markings location aren't valid throw an error
        if -90 <= right_lane_marking_position['latitude'] <= 90 and -180 <= right_lane_marking_position['longitude'] <= 180 and len(right_lane_marking_position) == 2:
            self.__right_lane_marking_position = right_lane_marking_position
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def vehicle_position(self):
        """
        Get the vehicles current position
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
        Returns:
            self.__vehicle_position (OrderedDict[str, float]): The vehicles current position
        """
        return self.__vehicle_position

    @vehicle_position.setter
    def vehicle_position(self, vehicle_position: OrderedDict[str, float]):
        """
        Set the vehicles current position
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            vehicle_position (OrderedDict[str, float]): The vehicles current position
        Returns:
            None
        """
        # If the vehicle location isn't valid throw an error
        if -90 <= vehicle_position['latitude'] <= 90 and -180 <= vehicle_position['longitude'] <= 180 and len(
                vehicle_position) == 2:
            self.__vehicle_position = vehicle_position
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def lane_width(self):
        """
        Get the width of the lane
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
        Returns:
            self.__lane_width (float): The width of the lane
        """
        return self.__lane_width

    @lane_width.setter
    def lane_width(self, lane_width: int):
        """
        Set the width of the lane
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            lane_width (float): The width of the lane
        Returns:
            None
        """
        if lane_width > 0:
            self.__lane_width = lane_width
        else:
            raise ValueError("The lane width must be a positive number")

    @property
    def lane_unoccupied(self):
        """
        Check if the lane is unoccupied
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
        Returns:
            self.__lane_unoccupied (bool): If the lane is unoccupied
        """
        return self.__lane_unoccupied

    @lane_unoccupied.setter
    def lane_unoccupied(self, lane_unoccupied: bool):
        """
        Set If the lane is unoccupied
        Parameters:
            self (LaneMarkingDetection): Lane Marking Detection Object
            lane_unoccupied (bool): If the lane is unoccupied
        Returns:
            None
        """
        self.__lane_unoccupied = lane_unoccupied

    def in_lane(self):
        """
        Checks weather the vehicle is in the lane
        Parameters:
            self (LaneMarkingDetection): Lank Marking Detection Object
        Returns:
            Boolean values indicating if the vehicle is in the lane
        """
        if self.vehicle_position["latitude"] >= self.left_lane_marking_position["latitude"] >= self.vehicle_position["latitude"] and self.vehicle_position["longitude"] >= self.left_lane_marking_position["longitude"] >= self.vehicle_position["longitude"]:
            return True
        else:
            return False


def main():
    vehicle_size = OrderedDict()
    vehicle_size["length"] = 100
    vehicle_size["width"] = 50
    left_lane_marking_position = OrderedDict()
    left_lane_marking_position["latitude"] = 10
    left_lane_marking_position["longitude"] = 50
    right_lane_marking_position = OrderedDict()
    right_lane_marking_position["latitude"] = 10
    right_lane_marking_position["longitude"] = 50
    vehicle_position = OrderedDict()
    vehicle_position["latitude"] = 10
    vehicle_position["longitude"] = 50
    lmd = LaneMarkingDetection(vehicle_size, left_lane_marking_position, right_lane_marking_position, vehicle_position, 100, True)
    print(lmd)


if __name__ == "__main__":
    main()
