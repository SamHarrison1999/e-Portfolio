import unittest
from collections import deque

from Main.Vehicle.Location import Location
from Main.Vehicle.RoadType import RoadType
from Main.Vehicle.Route import Route
from Main.Vehicle.GPS import GPS


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # The set-up method is run before each test case
        self._current_location = Location(10, 50, 0, "Maple Drive", 2, RoadType.CRoad, False, 30)
        self._destination = Location(10, 60, 0, "Pine Lane", 2, RoadType.CRoad, False, 30)
        directions_to_destination = deque()
        directions_to_destination_using_shortest_route = deque()
        directions_to_destination_using_quickest_route = deque()
        directions_to_destination.append("In 500 yards turn left")
        directions_to_destination.append("In 300 yards turn right")
        directions_to_destination.append("In 2 miles you have reached your destination")
        directions_to_destination_using_shortest_route.append("In 1 mile turn left")
        directions_to_destination_using_shortest_route.append("In 500 yards you have reached your destination")
        directions_to_destination_using_quickest_route.append("In 1.2 miles turn left")
        directions_to_destination_using_quickest_route.append("In 200 yards you have reached your destination")
        route = Route(10, 10, directions_to_destination)
        shortest_route = Route(1, 10, directions_to_destination_using_shortest_route)
        quickest_route = Route(10, 1, directions_to_destination_using_quickest_route)
        routes = [route, shortest_route, quickest_route]
        self._gps = GPS(self._current_location, self._destination, routes)

    def tearDown(self):
        self._current_location = None
        self._destination = None
        self._gps = None

    def testWhenRoutesIsNone(self):
        """Testing when the routes to the destination are None"""
        gps = GPS(self._current_location, self._destination, None)
        self.assertEqual(gps.routes, [])

    def testCurrentLocationGetter(self):
        """Testing the current location is returned when you call the current location getter"""
        with self.subTest("Longitude"):
            self.assertEqual(self._gps.current_location.longitude, 10)
        with self.subTest("Latitude"):
            self.assertEqual(self._gps.current_location.latitude, 50)
        with self.subTest("Altitude"):
            self.assertEqual(self._gps.current_location.altitude, 0)
        with self.subTest("Road Name"):
            self.assertEqual(self._gps.current_location.road_name, "Maple Drive")
        with self.subTest("Number of Lanes"):
            self.assertEqual(self._gps.current_location.number_of_lanes, 2)
        with self.subTest("Road Type"):
            self.assertEqual(self._gps.current_location.road_type.value, "C Road")
        with self.subTest("Traffic Status"):
            self.assertEqual(self._gps.current_location.in_traffic, False)
        with self.subTest("Speed Limit"):
            self.assertEqual(self._gps.current_location.speed_limit, 30)

    def testCurrentLocationSetter(self):
        """Testing if you can update the current location by calling the current location setter"""
        self._gps.current_location = Location(10, 55, 0, "Oak Street", 2, RoadType.BRoad, True, 30)
        with self.subTest("Longitude"):
            self.assertEqual(self._gps.current_location.longitude, 10)
        with self.subTest("Latitude"):
            self.assertEqual(self._gps.current_location.latitude, 55)
        with self.subTest("Altitude"):
            self.assertEqual(self._gps.current_location.altitude, 0)
        with self.subTest("Road Name"):
            self.assertEqual(self._gps.current_location.road_name, "Oak Street")
        with self.subTest("Number of Lanes"):
            self.assertEqual(self._gps.current_location.number_of_lanes, 2)
        with self.subTest("Type of Road"):
            self.assertEqual(self._gps.current_location.road_type.value, "B Road")
        with self.subTest("Traffic Status"):
            self.assertEqual(self._gps.current_location.in_traffic, True)
        with self.subTest("Speed Limit"):
            self.assertEqual(self._gps.current_location.speed_limit, 30)

    def testDestinationGetter(self):
        """Testing the destination is returned when you call the destination getter"""
        with self.subTest("Longitude"):
            self.assertEqual(self._gps.destination.longitude, 10)
        with self.subTest("Latitude"):
            self.assertEqual(self._gps.destination.latitude, 60)
        with self.subTest("Altitude"):
            self.assertEqual(self._gps.destination.altitude, 0)
        with self.subTest("Road Name"):
            self.assertEqual(self._gps.destination.road_name, "Pine Lane")
        with self.subTest("Number of Lanes"):
            self.assertEqual(self._gps.destination.number_of_lanes, 2)
        with self.subTest("Type of Road"):
            self.assertEqual(self._gps.destination.road_type.value, "C Road")
        with self.subTest("Traffic Status"):
            self.assertEqual(self._gps.destination.in_traffic, False)
        with self.subTest("Speed limit"):
            self.assertEqual(self._gps.destination.speed_limit, 30)

    def testDestinationSetter(self):
        """Testing if you can update the destination by calling the destination setter"""
        self._gps.destination = Location(10, 55, 0, "Oak Street", 2, RoadType.BRoad, True, 30)
        with self.subTest("Longitude"):
            self.assertEqual(self._gps.destination.longitude, 10)
        with self.subTest("Latitude"):
            self.assertEqual(self._gps.destination.latitude, 55)
        with self.subTest("Altitude"):
            self.assertEqual(self._gps.destination.altitude, 0)
        with self.subTest("Road Name"):
            self.assertEqual(self._gps.destination.road_name, "Oak Street")
        with self.subTest("Number of Lanes"):
            self.assertEqual(self._gps.destination.number_of_lanes, 2)
        with self.subTest("Type of Road"):
            self.assertEqual(self._gps.destination.road_type.value, "B Road")
        with self.subTest("Traffic Status"):
            self.assertEqual(self._gps.destination.in_traffic, True)
        with self.subTest("Speed Limit"):
            self.assertEqual(self._gps.destination.speed_limit, 30)

    def testRoutesGetter(self):
        """Testing the routes are returned when you call the routes getter"""
        with self.subTest("Routes"):
            self.assertEqual(self._gps.routes, [self._gps.routes[0], self._gps.routes[1], self._gps.routes[2]])
        with self.subTest("First Route"):
            self.assertEqual(str(self._gps.routes[0]), "Distance to destination: 10 Miles\n"
                                                       "Duration to destination: 10 Minuets\n"
                                                       "Directions:\n"
                                                       "In 500 yards turn left\n"
                                                       "In 300 yards turn right\n"
                                                       "In 2 miles you have reached your destination")
        with self.subTest("second Route"):
            self.assertEqual(str(self._gps.routes[1]), "Distance to destination: 1 Miles\n"
                                                       "Duration to destination: 10 Minuets\n"
                                                       "Directions:\n"
                                                       "In 1 mile turn left\n"
                                                       "In 500 yards you have reached your destination")
        with self.subTest("third Route"):
            self.assertEqual(str(self._gps.routes[2]), "Distance to destination: 10 Miles\n"
                                                       "Duration to destination: 1 Minuets\n"
                                                       "Directions:\n"
                                                       "In 1.2 miles turn left\n"
                                                       "In 200 yards you have reached your destination")

    def testRoutesSetter(self):
        """Testing if you can update the routes to the destination by calling the routes setter"""
        updated_directions_to_destination_using_shortest_route = deque()
        updated_directions_to_destination_using_quickest_route = deque()
        updated_directions_to_destination_using_shortest_route.append("In 15 miles turn left")
        updated_directions_to_destination_using_shortest_route.append("In 500 yards you have reached your destination")
        updated_directions_to_destination_using_quickest_route.append("In 17 miles you have reached your destination")
        updated_shortest_route = Route(15, 10, updated_directions_to_destination_using_shortest_route)
        updated_quickest_route = Route(17, 8, updated_directions_to_destination_using_quickest_route)
        routes = [updated_shortest_route, updated_quickest_route]
        self._gps.routes = routes
        with self.subTest("Routes"):
            self.assertEqual(self._gps.routes, [routes[0], routes[1]])
        with self.subTest("First Route"):
            self.assertEqual(str(self._gps.routes[0]), "Distance to destination: 15 Miles\n"
                                                       "Duration to destination: 10 Minuets\n"
                                                       "Directions:\n"
                                                       "In 15 miles turn left\n"
                                                       "In 500 yards you have reached your destination")
        with self.subTest("Second Route"):
            self.assertEqual(str(self._gps.routes[1]), "Distance to destination: 17 Miles\n"
                                                       "Duration to destination: 8 Minuets\n"
                                                       "Directions:\n"
                                                       "In 17 miles you have reached your destination")

    def testRoutesSetterWithNone(self):
        """Testing what happens if you update the routes to None"""
        self._gps.routes = None
        self.assertEqual(self._gps.routes, [])

    def testGetShortestRoute(self):
        """Testing the shortest route function"""
        self.assertEqual(self._gps.shortest_route(), "Distance to destination: 1 Miles\n"
                                                     "Duration to destination: 10 Minuets\n"
                                                     "Directions:\n"
                                                     "In 1 mile turn left\n"
                                                     "In 500 yards you have reached your destination")

    def testGetQuickestRoute(self):
        """Testing the quickest route function"""
        self.assertEqual(self._gps.quickest_route(), "Distance to destination: 10 Miles\n"
                                                     "Duration to destination: 1 Minuets\n"
                                                     "Directions:\n"
                                                     "In 1.2 miles turn left\n"
                                                     "In 200 yards you have reached your destination")

    def testGPSObject(self):
        """Testing the gps object"""
        self.assertEqual(self._gps.__str__(), "Current Location:\n"
                                              "Longitude: 10\n"
                                              "Latitude: 50\n"
                                              "Altitude: 0 Meters\n"
                                              "Road Name: Maple Drive\n"
                                              "Number Of Lanes: 2 lanes\n"
                                              "Road Type: C Road\n"
                                              "Traffic Status: No Traffic ahead\n"
                                              "Speed Limit: 30MPH\n"
                                              "Destination:\n"
                                              "Longitude: 10\n"
                                              "Latitude: 60\n"
                                              "Altitude: 0 Meters\n"
                                              "Road Name: Pine Lane\n"
                                              "Number Of Lanes: 2 lanes\n"
                                              "Road Type: C Road\n"
                                              "Traffic Status: No Traffic ahead\n"
                                              "Speed Limit: 30MPH\n"
                                              "Routes:\n"
                                              "Route 1:\n"
                                              "Distance to destination: 10 Miles\n"
                                              "Duration to destination: 10 Minuets\n"
                                              "Directions:\n"
                                              "In 500 yards turn left\n"
                                              "In 300 yards turn right\n"
                                              "In 2 miles you have reached your destination\n"
                                              "Route 2:\n"
                                              "Distance to destination: 1 Miles\n"
                                              "Duration to destination: 10 Minuets\n"
                                              "Directions:\n"
                                              "In 1 mile turn left\n"
                                              "In 500 yards you have reached your destination\n"
                                              "Route 3:\n"
                                              "Distance to destination: 10 Miles\n"
                                              "Duration to destination: 1 Minuets\n"
                                              "Directions:\n"
                                              "In 1.2 miles turn left\n"
                                              "In 200 yards you have reached your destination")


if __name__ == '__main__':
    unittest.main()
