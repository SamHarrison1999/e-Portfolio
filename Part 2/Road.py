from enum import Enum
from collections import OrderedDict

from RoadSign import RoadSign
from Utils import is_null_or_white_space


class RoadType(Enum):
    A_ROAD = 1
    B_ROAD = 2
    C_ROAD = 3
    MOTORWAY = 4


class Road:
    def __init__(self, name: str, number_of_lanes: int, road_type: RoadType, location: OrderedDict[str, int],
                 in_traffic: bool, speed_limit: RoadSign):
        """
        Constructor for a road object
        Parameters:
            self (Road): A road object
            name (str): The name of the road
            number_of_lanes (int): The number of lanes on the road
            road_type (RoadType): The type of road
            location (OrderedDict[str, int]): The location of the road
            in_traffic (bool): Whether you're in traffic or not
            speed_limit (RoadSign): The speed limit of the road
        Returns:
            None
        """
        # If the road has no name throw an error
        if is_null_or_white_space(name):
            raise ValueError("A road must have a name")
        else:
            self.__name = name
        # If the road has no lanes throw an error
        if number_of_lanes > 0:
            self.__number_of_lanes = number_of_lanes
        else:
            raise ValueError("A road must have at least one lane")
        self.__road_type = road_type
        # If the location of the road isn't valid throw an error
        if -90 <= location['latitude'] <= 90 and -180 <= location['longitude'] <= 180 and len(location) == 2:
            self.__location = location
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        self.__in_traffic = in_traffic
        self.__speed_limit = speed_limit

    def __str__(self):
        return f'Road Name: {self.__name}\nNumber of Lanes: {self.__number_of_lanes} Lanes\nRoad Type: {str(self.__road_type.name).capitalize()}\n' f"Current Location:" + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.__location.items()) + f'\nTraffic Status: {"Traffic ahead" if self.__in_traffic else "No Traffic ahead"}\n{self.__speed_limit}'

    @property
    def name(self):
        """
        Returns the name of the road
        Parameters:
            self (Road): A road object
        Returns:
            self.__name (str): The name of the road
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the name of the road
        Parameters:
            self (Road): A road object
            name (str): The name of the road
        Returns:
            None
        """
        if is_null_or_white_space(name):
            self.__name = name
        else:
            raise ValueError("A road must have a name")

    @property
    def number_of_lanes(self):
        """
        Returns the number of lanes on the road
        Parameters:
            self (Road): A road object
        Returns:
            self.__number_of_lanes (int): The number of lanes on the road
        """
        return self.__number_of_lanes

    @number_of_lanes.setter
    def number_of_lanes(self, number_of_lanes):
        """
        Set the number of lanes on the road
        Parameters:
            self (Road): A road object
            number_of_lanes (int): The number of lanes on the road
        Returns:
            None
        """
        if number_of_lanes > 0:
            self.__number_of_lanes = number_of_lanes
        else:
            raise ValueError("A road must have at least one lane")

    @property
    def road_type(self):
        """
        Returns the type of road
        Parameters:
            self (Road): A road object
        Returns:
            self.__road_type (RoadType): The type of road
        """
        return self.__road_type

    @road_type.setter
    def road_type(self, road_type):
        """
        Set the type of road
        Parameters:
            self (Road): A road object
            road_type (RoadType): The type of road
        Returns:
            None
        """
        self.__road_type = road_type

    @property
    def location(self):
        """
        Returns The location of the road
        Parameters:
            self (Road): A road object
        Returns:
            self.__location (OrderedDict[str, int]): The location of the road
        """
        return self.__location

    @location.setter
    def location(self, location):
        """
        Set The location of the road
        Parameters:
            self (Road): A road object
            location (OrderedDict[str, int]): The location of the road
        Returns:
            None
        """
        if -90 <= location['latitude'] <= 90 and -180 <= location['longitude'] <= 180 and len(location) == 2:
            self.__location = location
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def in_traffic(self):
        """
        Checks whether you're in traffic or not
        Parameters:
            self (Road): A road object
        Returns:
            self.__in_traffic (bool): Whether you're in traffic or not
        """
        return self.__in_traffic

    @in_traffic.setter
    def in_traffic(self, in_traffic: bool):
        """
        Set whether you're in traffic or not
        Parameters:
            self (Road): A road object
            in_traffic (bool): Whether you're in traffic or not
        Returns:
            None
        """
        self.__in_traffic = in_traffic

    @property
    def speed_limit(self):
        """
        Returns the speed limit
        Parameters:
            self (Road): A road object
        :return: The speed limit
        """
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit: RoadSign):
        """
        Returns the speed limit
        Parameters:
            self (Road): A road object
            speed_limit (int): The speed limit
        :return: None
        """
        self.__speed_limit = speed_limit

    def traffic_jam(self):
        """
        Start of traffic
        Parameters:
            self (Road): A road object
        Returns:
            None
        """
        self.__in_traffic = True

    def traffic_ended(self):
        """
        End of traffic
        Parameters:
            self (Road): A road object
        Returns:
            None
        """
        self.__in_traffic = False


def main():
    current_location = OrderedDict()
    current_location["latitude"] = 10
    current_location["longitude"] = 50
    sign = RoadSign(30)
    road = Road("M25", 3, RoadType.MOTORWAY, current_location, False, sign)
    road.traffic_jam()
    print(road)


if __name__ == "__main__":
    main()
