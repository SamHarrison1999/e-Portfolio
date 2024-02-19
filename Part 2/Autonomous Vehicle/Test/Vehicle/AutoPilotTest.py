import unittest
from Main.Vehicle.AutoPilot import AutoPilot
from Main.Weather.Weather import Weather


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._weather = Weather("Sunny", 25)
        self._auto_pilot = AutoPilot(False, self._weather, 10)

    def tearDown(self):
        self._weather = None
        self._auto_pilot = None

    def testValueErrorIsRaisedIfTheDistanceFromTheClosestVehicleIsNegative(self):
        """Testing a value error is raised if the distance from the closest vehicle is a negative number"""
        with self.assertRaises(ValueError):
            self._auto_pilot = AutoPilot(True, self._weather, -10)

    def testAutoPilotStatusGetter(self):
        """Testing the autopilot status is returned when you call the autopilot status getter"""
        self.assertEqual(self._auto_pilot.enabled, False)

    def testAutoPilotStatusSetter(self):
        """Testing if you can update the status by calling the status setter"""
        self._auto_pilot.enabled = True
        self.assertEqual(self._auto_pilot.enabled, True)

    def testWeatherGetter(self):
        """Testing the weather is returned when you call the weather getter"""
        self.assertEqual(self._auto_pilot.weather.__str__(), "Weather Condition: Sunny\nTemperature: 25 degrees\n"
                                                             "Recommended Following Distance: 2 Meters")

    def testWeatherSetter(self):
        """Testing if you can update the weather by calling the weather setter"""
        self._auto_pilot.weather = Weather("Raining", 10)
        self.assertEqual(self._auto_pilot.weather.__str__(), "Weather Condition: Raining\nTemperature: 10 degrees"
                                                             "\nRecommended Following Distance: 4 Meters")

    def testFollowingDistanceGetter(self):
        """Testing the following distance is returned when you call the following distance getter"""
        self.assertEqual(self._auto_pilot.following_distance, 10)

    def testFollowingDistanceSetter(self):
        """Testing if you can update the following distance by calling the following distance setter"""
        self._auto_pilot.following_distance = 20
        self.assertEqual(self._auto_pilot.following_distance, 20)

    def testTurnOnAutoPilot(self):
        """Testing if autopilot is on once you turn it on"""
        self._auto_pilot.turn_on_auto_pilot()
        self.assertEqual(self._auto_pilot.enabled, True)

    def testTurnOffAutoPilot(self):
        """Testing if autopilot is off once you turn it off"""
        self._auto_pilot = AutoPilot(True, self._weather, 10)
        self._auto_pilot.turn_off_auto_pilot()
        self.assertEqual(self._auto_pilot.enabled, False)

    def testGetAutoPilotObject(self):
        """Testing if you can get the autopilot object"""
        self.assertEqual(self._auto_pilot.__str__(), "AutoPilot: Disabled\n"
                                                     "Distance From The Closest Car: 10 meters\n"
                                                     "Weather Condition: Sunny\n"
                                                     "Temperature: 25 degrees\n"
                                                     "Recommended Following Distance: 2 Meters")


if __name__ == '__main__':
    unittest.main()
