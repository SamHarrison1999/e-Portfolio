from Main.Vehicle.RoadType import RoadType
from Main.Utils.Utils import is_null_or_white_space


class Location:

    def __init__(self, longitude: float, latitude: float, altitude: float, road_name: str, number_of_lanes: int,
                 road_type: RoadType, in_traffic: bool, speed_limit: int) -> None:
        """
        Constructor for a location object
        :parameter Location self: A location object
        :parameter float longitude: The locations longitude
        :parameter float latitude: The locations latitude
        :parameter float altitude: The locations altitude
        :parameter str road_name: The name of the road
        :parameter int number_of_lanes: The number of lanes on the road
        :parameter RoadType road_type: The type of road
        :parameter bool in_traffic: Whether you're in traffic or not
        :parameter int speed_limit: The speed limit of the road
        :raises ValueError: If the locations longitude or latitude isn't valid or if the road has no name or lanes
        :returns: None
        """
        # If the longitude isn't valid throw an error
        if -180 <= longitude <= 180:
            self._longitude = longitude
        else:
            raise ValueError("The locations longitude has to be between -180 and 180")
        # If the latitude isn't valid throw an error
        if -90 <= latitude <= 90:
            self._latitude = latitude
        else:
            raise ValueError("The location latitude has to be between -90 and 90")
        self._altitude = altitude
        # If the road has no name throw an error
        if is_null_or_white_space(road_name):
            raise ValueError("A road must have a name")
        else:
            self._road_name = road_name
        # If the road has no lanes throw an error
        if number_of_lanes > 0:
            self._number_of_lanes = number_of_lanes
        else:
            raise ValueError("A road must have at least one lane")
        self._road_type = road_type
        self._in_traffic = in_traffic
        self._speed_limit = speed_limit

    def __str__(self) -> str:
        """
        Returns the location object as a string
        :parameter Location self: A location object
        :returns: The location object as a string
        """
        return (f'Longitude: {self._longitude}\n'
                f'Latitude: {self._latitude}\n'
                f'Altitude: {self._altitude} Meters\n'
                f'Road Name: {self._road_name}\n'
                f'Number Of Lanes: {self._number_of_lanes} lanes\n'
                f'Road Type: '
                f'{str(self._road_type.value)}') + (f'\nTraffic Status: '
                                                    f'{"Traffic ahead" if self._in_traffic else "No Traffic ahead"}\n'
                                                    f'Speed Limit: {self._speed_limit}MPH')

    @property
    def longitude(self) -> float:
        """
        Returns the locations longitude
        :parameter Location self: A location object
        :returns: The locations longitude
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        """
        Set the locations longitude
        :parameter Location self: A location object
        :parameter float longitude: The locations longitude
        :raises ValueError: If the locations longitude isn't valid
        :returns: None
        """
        # If the longitude isn't valid throw an error
        if -180 <= longitude <= 180:
            self._longitude = longitude
        else:
            raise ValueError("The locations longitude has to be between -180 and 180")

    @property
    def latitude(self) -> float:
        """
        Returns the locations latitude
        :parameter Location self: A location object
        :returns: The locations latitude
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        """
        Set the locations latitude
        :parameter Location self: A location object
        :parameter float latitude: The locations latitude
        :raises ValueError: If the locations latitude isn't valid
        :returns: None
        """
        # If the latitude isn't valid throw an error
        if -90 <= latitude <= 90:
            self._latitude = latitude
        else:
            raise ValueError("The location latitude has to be between -90 and 90")

    @property
    def altitude(self) -> float:
        """
        Returns the locations altitude
        :parameter Location self: A location object
        :returns: The locations altitude
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude: float) -> None:
        """
        Set the locations altitude
        :parameter Location self: A location object
        :parameter float altitude: The locations altitude
        :returns: None
        """
        self._altitude = altitude

    @property
    def road_name(self) -> str:
        """
        Returns the name of the road
        :parameter Location self: A location object
        :returns: The name of the road
        """
        return self._road_name

    @road_name.setter
    def road_name(self, road_name: str) -> None:
        """
        Set the name of the road
        :parameter Location self: A location object
        :parameter str road_name: The name of the road
        :raises ValueError: If the road has no name
        :returns: None
        """
        # If the road has no name throw an error
        if is_null_or_white_space(road_name):
            raise ValueError("A road must have a name")
        else:
            self._road_name = road_name

    @property
    def number_of_lanes(self) -> int:
        """
        Returns the number of lanes on the road
        :parameter Location self: A location object
        :returns: The number of lanes on the road
        """
        return self._number_of_lanes

    @number_of_lanes.setter
    def number_of_lanes(self, number_of_lanes: int) -> None:
        """
        Set the number of lanes on the road
        :parameter Location self: A location object
        :parameter int number_of_lanes: The number of lanes on the road
        :raises ValueError: If the road has no lanes
        :returns: None
        """
        # If the road has no lanes throw an error
        if number_of_lanes > 0:
            self._number_of_lanes = number_of_lanes
        else:
            raise ValueError("A road must have at least one lane")

    @property
    def road_type(self) -> RoadType:
        """
        Returns the type of road
        :parameter Location self: A location object
        :returns: The type of road
        """
        return self._road_type

    @road_type.setter
    def road_type(self, road_type: RoadType) -> None:
        """
        Set the type of road
        :parameter Location self: A location object
        :parameter RoadType road_type: The type of road
        :returns: None
        """
        self._road_type = road_type

    @property
    def in_traffic(self) -> bool:
        """
        Checks whether you're in traffic or not
        :parameter Location self: A location object
        :returns: Whether you're in traffic or not
        """
        return self._in_traffic

    @in_traffic.setter
    def in_traffic(self, in_traffic: bool) -> None:
        """
        Set whether you're in traffic or not
        :parameter Location self: A location object
        :parameter bool in_traffic: Whether you're in traffic or not
        :returns: None
        """
        self._in_traffic = in_traffic

    @property
    def speed_limit(self) -> int:
        """
        Returns the speed limit
        :parameter Location self: A location object
        :returns: The speed limit
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit: int) -> None:
        """
        Returns the speed limit
        :parameter Location self: A location object
        :parameter int speed_limit: The speed limit of the road
        :returns: None
        """
        self._speed_limit = speed_limit

    def traffic_jam(self) -> None:
        """
        Start of traffic
        :parameter Location self: A location object
        :returns: None
        """
        self._in_traffic = True

    def traffic_ended(self) -> None:
        """
        End of traffic
        :parameter Location self: A location object
        :returns: None
        """
        self._in_traffic = False
