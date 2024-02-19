import unittest
from Main.Vehicle.RoadType import RoadType
from Main.Vehicle.Location import Location


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._location = Location(10, 50, 10, "M25", 3, RoadType.Motorway, False, 70)

    def tearDown(self):
        self._location = None

    def testValueErrorIsRaisedIfTheLocationsLongitudeIsNotValid(self):
        """Testing a value error is raised if the locations longitude is not valid"""
        with self.assertRaises(ValueError):
            self._location = Location(-200, 50, 10, "M25", 3, RoadType.Motorway, False, 70)

    def testValueErrorIsRaisedIfTheLocationsLatitudeIsNotValid(self):
        """Testing a value error is raised if the locations latitude is not valid"""
        with self.assertRaises(ValueError):
            self._location = Location(10, -100, 10, "M25", 3, RoadType.Motorway, False, 70)

    def testValueErrorIsRaisedIfTheRoadHasNoName(self):
        """Testing a value error is raised if road has no name"""
        with self.assertRaises(ValueError):
            self._location = Location(10, 50, 10, "", 3, RoadType.Motorway, False, 70)

    def testValueErrorIsRaisedIfTheRoadHasNoLanes(self):
        """Testing a value error is raised if the road has no lanes"""
        with self.assertRaises(ValueError):
            self._location = Location(10, 50, 10, "M25", 0, RoadType.Motorway, False, 70)

    def testValueErrorIsRaisedIfTheRoadHasANegativeNumberOfLanes(self):
        """Testing a value error is raised if the road has no lanes"""
        with self.assertRaises(ValueError):
            self._location = Location(10, 50, 10, "M25", -1, RoadType.Motorway, False, 70)

    def testLongitudeGetter(self):
        """Testing the longitude is returned when you call the longitude getter"""
        self.assertEqual(10, self._location.longitude)

    def testLongitudeSetter(self):
        """Testing if you can update the longitude by calling the longitude setter"""
        self._location.longitude = 50
        self.assertEqual(50, self._location.longitude)

    def testValueErrorIsRaisedIfTheLocationsLongitudeSetIsNotValid(self):
        """Testing a value error is raised if the locations longitude set using the longitude setter is not valid"""
        with self.assertRaises(ValueError):
            self._location.longitude = -200

    def testLatitudeGetter(self):
        """Testing the latitude is returned when you call the latitude getter"""
        self.assertEqual(50, self._location.latitude)

    def testLatitudeSetter(self):
        """Testing if you can update the latitude by calling the latitude setter"""
        self._location.latitude = 20
        self.assertEqual(20, self._location.latitude)

    def testValueErrorIsRaisedIfTheLocationsLatitudeSetIsNotValid(self):
        """Testing a value error is raised if the locations latitude set using the latitude setter is not valid"""
        with self.assertRaises(ValueError):
            self._location.latitude = -100

    def testAltitudeGetter(self):
        """Testing the altitude is returned when you call the latitude getter"""
        self.assertEqual(10.0, self._location.altitude)

    def testAltitudeSetter(self):
        """Testing if you can update the altitude by calling the altitude setter"""
        self._location.altitude = 20
        self.assertEqual(20, self._location.altitude)

    def testRoadNameGetter(self):
        """Testing the name of the road is returned when you call the road name getter"""
        self.assertEqual("M25", self._location.road_name)

    def testRoadNameSetter(self):
        """Testing if you can update the road name by calling the road name setter"""
        self._location.road_name = "M1"
        self.assertEqual("M1", self._location.road_name)

    def testValueErrorIsRaisedIfTheRoadNameSetIsEmpty(self):
        """Testing a value error is raised if road name set using the road name setter has no name"""
        with self.assertRaises(ValueError):
            self._location.road_name = ""

    def testNumberOfLanesGetter(self):
        """Testing the number of lanes is returned when you call the number of lanes getter"""
        self.assertEqual(3, self._location.number_of_lanes)

    def testNumberOfLanesSetter(self):
        """Testing if you can update the number of lanes by calling the number of lanes setter"""
        self._location.number_of_lanes = 5
        self.assertEqual(5, self._location.number_of_lanes)

    def testValueErrorIsRaisedIfTheNumberOfLaneSetIsANegativeNumber(self):
        """Testing a value error is raised if the number of lanes set using the lanes setter is a negative number"""
        with self.assertRaises(ValueError):
            self._location.number_of_lanes = -1

    def testValueErrorIsRaisedIfTheNumberOfLaneSetIsZero(self):
        """Testing a value error is raised if the number of lanes set using the lanes setter is zero"""
        with self.assertRaises(ValueError):
            self._location.number_of_lanes = 0

    def testRoadTypeGetter(self):
        """Testing the type of road is returned when you call the road type getter"""
        self.assertEqual("Motorway", self._location.road_type.value)

    def testRoadTypeSetter(self):
        """Testing if you can update the road type by calling the set road type function"""
        self._location.road_type = RoadType.ARoad
        self.assertEqual("A Road", self._location.road_type.value)

    def testTrafficStatusGetter(self):
        """Testing the traffic status is returned when you call the traffic status getter"""
        self.assertEqual(False, self._location.in_traffic)

    def testTrafficStatusSetter(self):
        """Testing if you can update the traffic status by calling the traffic status setter"""
        self._location.in_traffic = True
        self.assertEqual(True, self._location.in_traffic)

    def testSpeedLimitGetter(self):
        """Testing the speed limit is returned when you call the speed limit getter"""
        self.assertEqual(70, self._location.speed_limit)

    def testSpeedLimitSetter(self):
        """Testing if you can update the speed limit by calling the speed limit setter"""
        self._location.speed_limit = 50
        self.assertEqual(50, self._location.speed_limit)

    def testGetLocation(self):
        """Testing you can get the location object as a string"""
        with self.subTest("Location"):
            self.assertEqual("Longitude: 10\n"
                             "Latitude: 50\n"
                             "Altitude: 10 Meters\n"
                             "Road Name: M25\n"
                             "Number Of Lanes: 3 lanes\n"
                             "Road Type: Motorway\n"
                             "Traffic Status: No Traffic ahead\n"
                             "Speed Limit: 70MPH",
                             self._location.__str__())
        with self.subTest("Longitude"):
            self.assertEqual(10, self._location.longitude)
        with self.subTest("Latitude"):
            self.assertEqual(50, self._location.latitude)
        with self.subTest("Altitude"):
            self.assertEqual(10, self._location.altitude)
        with self.subTest("Road Name"):
            self.assertEqual("M25", self._location.road_name)
        with self.subTest("Number of Lanes"):
            self.assertEqual(3, self._location.number_of_lanes)
        with self.subTest("Road Type"):
            self.assertEqual("Motorway", self._location.road_type.value)
        with self.subTest("Traffic Status"):
            self.assertEqual(False, self._location.in_traffic)
        with self.subTest("Speed Limit"):
            self.assertEqual(70, self._location.speed_limit)

    def testTrafficJam(self):
        """Testing if the traffic status is in traffic after traffic has started"""
        self._location.traffic_jam()
        self.assertEqual(True, self._location.in_traffic)

    def testTrafficEnded(self):
        """Testing if the traffic status is that traffic has ended after traffic has ended"""
        self._location = Location(10, 50, 10, "M25", 3, RoadType.Motorway, True, 70)
        self._location.traffic_ended()
        self.assertEqual(False, self._location.in_traffic)


if __name__ == '__main__':
    unittest.main()
