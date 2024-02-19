import unittest
from collections import deque
from Main.Vehicle.Route import Route


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # The set-up method is run before each test case
        self._directions_to_destination = deque()
        self._directions_to_destination.append("In 500 yards turn left")
        self._directions_to_destination.append("In 300 yards turn right")
        self._directions_to_destination.append("In 2 miles you have reached your destination")
        self._route = Route(10, 10, self._directions_to_destination)

    def tearDown(self):
        self._directions_to_destination = None
        self._route = None

    def testValueErrorIsRaiseIfTheDurationIsNegative(self):
        """Testing a value error is raised if the time until you reach the destination is a negative number"""
        with self.assertRaises(ValueError):
            self._route = Route(10, -10, self._directions_to_destination)

    def testValueErrorIsRaiseIfTheDistanceIsNegative(self):
        """Testing a value error is raised if the distance until you reach the destination is a negative number"""
        with self.assertRaises(ValueError):
            self._route = Route(-10, 10, self._directions_to_destination)

    def testDistanceGetter(self):
        """Testing the distance until you reach the destination is returned when you call the distance getter"""
        self.assertEqual(self._route.distance, 10)

    def testingNoDirections(self):
        """Testing a route object with no directions"""
        self._route = Route(10, 10, None)
        self.assertEqual(self._route.directions, deque())

    def testDistanceSetter(self):
        """Testing if you can set the distance until you reach the destination by calling the distance setter"""
        self._route.distance = 5
        self.assertEqual(self._route.distance, 5)

    def testValueErrorIsRaiseIfTheDistanceSetIsNegative(self):
        """Testing a value error is raised if the distance until you reach the destination you have set is a negative
        number"""
        with self.assertRaises(ValueError):
            self._route.distance = -10

    def testDurationGetter(self):
        """Testing the time until you reach the destination is returned when you call the duration getter"""
        self.assertEqual(self._route.duration, 10)

    def testDurationSetter(self):
        """Testing if you can set the time until you reach the destination by calling the duration setter"""
        self._route.duration = 5
        self.assertEqual(self._route.duration, 5)

    def testValueErrorIsRaiseIfTheDurationSetIsNegative(self):
        """Testing a value error is raised if the time until you reach the destination you have set is a negative
        number"""
        with self.assertRaises(ValueError):
            self._route.duration = -10

    def testDirectionsGetter(self):
        """Testing the directions for you to reach the destination is returned when you call the directions getter"""
        self.assertEqual(self._route.directions, deque(["In 500 yards turn left",
                                                        "In 300 yards turn right",
                                                        "In 2 miles you have reached your destination"]))

    def testDirectionsSetter(self):
        """Testing if you can set the directions to reach the destination by calling the directions setter"""
        self._route.directions = deque(["In 5 miles you have reached your destination"])
        self.assertEqual(self._route.directions, deque(["In 5 miles you have reached your destination"]))

    def testDirectionsSetterWithNone(self):
        """Testing the directions setter with none"""
        self._route.directions = None
        self.assertEqual(self._route.directions, deque())

    def testGetRouteObject(self):
        """Testing the route object is returned when you call the route getter"""
        with self.subTest("Route Object"):
            self.assertEqual(self._route.__str__(), "Distance to destination: 10 Miles\n"
                                                    "Duration to destination: 10 Minuets\n"
                                                    "Directions:\n"
                                                    "In 500 yards turn left\n"
                                                    "In 300 yards turn right\n"
                                                    "In 2 miles you have reached your destination")
        with self.subTest("Distance"):
            self.assertEqual(self._route.distance, 10)
        with self.subTest("Duration"):
            self.assertEqual(self._route.duration, 10)
        with self.subTest("Directions"):
            self.assertEqual(self._route.directions, deque(["In 500 yards turn left",
                                                            "In 300 yards turn right",
                                                            "In 2 miles you have reached your destination"]))

    def testGetNextDirection(self):
        """Testing the next direction is returned when you call the next direction method"""
        self._route = Route(10, 10, self._directions_to_destination)
        self.assertEqual(self._route.next_direction(), "The next direction is: In 300 yards turn right")


if __name__ == '__main__':
    unittest.main()
