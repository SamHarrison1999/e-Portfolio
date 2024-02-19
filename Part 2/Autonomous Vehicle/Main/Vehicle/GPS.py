from Main.Vehicle.Location import Location
from Main.Vehicle.Route import Route


class GPS:
    def __init__(self, current_location: Location, destination: Location, routes: list[Route]) -> None:
        """
        Constructor for a GPS Object
        :parameter GPS self: A GPS object
        :parameter Location current_location: Your current location
        :parameter Location destination: The destination
        :parameter list[Route] routes: The routes to get to the destination from your location
        :returns: None
        """
        self._current_location = current_location
        self._destination = destination
        # If there are no routes set the routes to an empty list
        if routes:
            self._routes = routes
        else:
            self._routes = []

    def __str__(self) -> str:
        """
        Returns the GPS object as a string
        :parameter GPS self: A GPS object
        :returns: The GPS object as a string
        """
        return (f"Current Location:\n{self._current_location}\nDestination:\n{self._destination}\nRoutes:" + ""
                + f"".join(f'\nRoute {route_number + 1}:\n{route}' for route_number, route in enumerate(self._routes)))

    @property
    def current_location(self) -> Location:
        """
        Returns your current location
        :parameter GPS self: A GPS object
        :returns: Your current location
        """
        return self._current_location

    @current_location.setter
    def current_location(self, current_location: Location) -> None:
        """
        Set your current location
        :parameter GPS self: A GPS object
        :parameter Location current_location: Your current location
        :returns: None
        """
        self._current_location = current_location

    @property
    def destination(self) -> Location:
        """
        Returns the destination
        :parameter GPS self: A GPS object
        :returns: The destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination: Location) -> None:
        """
        Set the destination
        :parameter GPS self: A GPS object
        :parameter Location destination: The destination
        :returns: None
        """
        self._destination = destination

    @property
    def routes(self) -> list[Route]:
        """
        Returns a list of the routes to get to the destination from your location
        :parameter GPS self: A GPS object
        :returns: The routes to get to the destination from your location
        """
        return self._routes

    @routes.setter
    def routes(self, routes: list[Route]) -> None:
        """
        Set the routes to reach the destination
        :parameter GPS self: A GPS object
        :parameter list[Route] routes: The available routes to reach the destination
        :returns: None
        """
        # If there are no routes set the routes to an empty list
        if routes:
            self._routes = routes
        else:
            self._routes = []

    def shortest_route(self) -> str:
        """
        Returns the shortest route to the destination
        :parameter GPS self: A GPS object
        :returns: The shortest route
        """
        # Sort the routes by distance in ascending order
        self._routes.sort(key=lambda x: x.distance)
        return str(self._routes[0])

    def quickest_route(self) -> str:
        """
        Returns the quickest route to the destination
        :parameter GPS self: A GPS object
        :returns: The quickest route
        """
        # Sort the routes by duration in ascending order
        self._routes.sort(key=lambda x: x.duration)
        return str(self._routes[0])
