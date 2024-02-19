from collections import deque, OrderedDict

from Road import Road, RoadType
from RoadSign import RoadSign
from Route import Route

#TODO Finish implementation

class GPS:
    def __init__(self, current_location: OrderedDict[str, int], destination: OrderedDict[str, int], altitude: int, routes: list[Route], road: Road):
        """
        Constructor for the GPS Object
        Parameters:
            self (GPS): The GPS object
            current_location (OrderedDict[str,int]): Your current location
            destination (OrderedDict[str, int]): Your destination
            altitude (int): The current altitude
            routes (list[Route]): the routes to get to the destination
        Returns:
            None
        """
        # If current location isn't valid throw an error
        if -90 <= current_location['latitude'] <= 90 and -180 <= current_location['longitude'] <= 180 and len(current_location) == 2:
            self.__current_location = current_location
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        # If destination location isn't valid throw an error
        if -90 <= destination['latitude'] <= 90 and -180 <= destination['longitude'] <= 180 and len(destination) == 2:
            self.__destination = destination
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        self.__altitude = altitude
        # If there are no routes set the routes to an empty list
        if routes:
            self.__routes = routes
        else:
            self.__routes = []
        self.__road = road

    def __str__(self):
        """
        Returns the GPS object as a string
        Parameters:
            self (GPS): The GPS object
        Returns:
            Formatted string of a GPS object
        """
        return f"Current Location:" + f"".join(f"\n{key.capitalize()}: {value}" for key, value in self.__current_location.items()) + "\nDestination:" + f"".join(f"\n{key.capitalize()}: {value}" for key, value in self.__destination.items()) + "\nCurrent Altitude: " + str(self.__altitude) + " Meters\nRoutes:" + f"".join(f'\n{route}' for route in self.__routes) + f'\n{self.__road}'

    @property
    def current_location(self):
        """
        Returns your current location
        Parameters:
            self (GPS): The GPS object
        Returns:
            self.__current_location (OrderedDict[str,int]): Your current location
        """
        return self.__current_location

    @current_location.setter
    def current_location(self, current_location: OrderedDict[str, int]):
        """
        Set your current location
        Parameters:
            self (GPS): The GPS object
            current_location (OrderedDict[str,int]): Your current location
        Returns:
            None
        """
        # If current location isn't valid throw an error
        if -90 <= current_location['latitude'] <= 90 and -180 <= current_location['longitude'] <= 180 and len(current_location) == 2:
            self.__current_location = current_location
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def destination(self):
        """
        Returns your destination
        Parameters:
            self (GPS): The GPS object
        Returns:
            self.__destination (OrderedDict[str,int]): Your destination
        """
        return self.__destination

    @destination.setter
    def destination(self, destination: OrderedDict[str, int]):
        """
        Set your destination
        Parameters:
            self (GPS): The GPS object
            destination (OrderedDict[str,int]): Your destination
        Returns:
            None
        """
        # If destination location isn't valid throw an error
        if -90 <= destination['latitude'] <= 90 and -180 <= destination['longitude'] <= 180 and len(destination) == 2:
            self.__destination = destination
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def altitude(self):
        """
        Returns your current altitude
        Parameters:
            self (GPS): The GPS object
        Returns:
            self.__altitude (int): Your current altitude
        """
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: int):
        """
        Set your current altitude
        Parameters:
            self (GPS): The GPS object
            altitude (int): Your current altitude
        Returns:
            None
        """
        self.__altitude = altitude

    @property
    def routes(self):
        """
        Return the routes object
        Parameters:
            self (GPS): The GPS object
        Returns:
            self.__routes (list[Route]): The available routes to reach the destination
        """
        return self.__routes

    @routes.setter
    def routes(self, routes: list[Route]):
        """
        Set the routes to reach the destination
        Parameters:
            self (GPS): The GPS object
            routes (list[Route]): The available routes to reach the destination
        Returns:
            None
        """
        # If there are no routes set the routes to an empty list
        if routes:
            self.__routes = routes
        else:
            self.__routes = []

    @property
    def road(self):
        """
        Return the road your on
        Parameters:
            self (GPS): The GPS object
        :returns: The road your on
        """
        return self.__road

    @road.setter
    def road(self, road: Road):
        """
        Set the road your on
        Parameters:
            self (GPS): The GPS object
            Road road: The road your on
        :returns: None
        """
        self.__road = road

    def shortest_route(self):
        """
        Return the shortest route to the destination
        Parameters:
            self (GPS): The GPS object
        Returns:
            self.__routes[0] (Route): The shortest route
        """
        # Sort the routes by distance in ascending order
        self.__routes.sort(key=lambda x: x.distance)
        return self.__routes[0]

    def quickest_route(self):
        """
        Return the quickest route to the destination
        Parameters:
            self (GPS): The GPS object
        Returns:
            self.__routes[0] (Route): The quickest route
        """
        # Sort the routes by duration in ascending order
        self.__routes.sort(key=lambda x: x.duration)
        return self.__routes[0]


def main():
    current_location = OrderedDict()
    current_location["latitude"] = 10
    current_location["longitude"] = 50
    destination = OrderedDict()
    destination["latitude"] = 10
    destination["longitude"] = 60
    directions_to_destination = deque()
    directions_to_destination_using_shortest_route = deque()
    directions_to_destination_using_quickest_route = deque()
    directions_to_destination.append("In 500 yards turn left")
    directions_to_destination.append("In 300 yards turn right")
    directions_to_destination.append("In 2 miles you have reached your destination")
    directions_to_destination_using_shortest_route.append("In 1 mile turn left")
    directions_to_destination_using_shortest_route.append("In 500 yards you have reached your destination")
    directions_to_destination_using_quickest_route.append("In 1.2 miles turn left")
    directions_to_destination_using_quickest_route.append("in 200 yards you have reached your destination")
    route = Route(10, 10, directions_to_destination)
    shortest_route = Route(1, 10, directions_to_destination_using_shortest_route)
    quickest_route = Route(10, 1, directions_to_destination_using_quickest_route)
    routes = [route, shortest_route, quickest_route]
    sign = RoadSign(30)
    road = Road("M25", 3, RoadType.MOTORWAY, current_location, False, sign)
    gps = GPS(current_location, destination, 500, routes, road)
    print(gps)


if __name__ == "__main__":
    main()
