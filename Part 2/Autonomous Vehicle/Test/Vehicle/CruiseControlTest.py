import unittest
from Main.Vehicle.CruiseControl import CruiseControl
from Main.Weather.Weather import Weather


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._weather = Weather("Sunny", 25)
        self._cruise_control = CruiseControl(True, 70, self._weather, 30)

    def tearDown(self):
        self._weather = None
        self._cruise_control = None

    def testValueErrorIsRaisedIfTheDistanceFromTheClosestVehicleIsNegative(self):
        """Testing a value error is raised if the distance from the closest vehicle is a negative number"""
        with self.assertRaises(ValueError):
            self._cruise_control = CruiseControl(True, 70, self._weather, -10)

    def testValueErrorIsRaisedIfTheTargetSpeedIsNegative(self):
        """Testing a value error is raised if the target speed is a negative number"""
        with self.assertRaises(ValueError):
            self._cruise_control = CruiseControl(True, -10, self._weather, 30)

    def testTargetSpeedWhenItIsNone(self):
        """Testing the target speed defaults to 0 if you create a cruise control object with a target speed"""
        cruise_control = CruiseControl(True, None, self._weather, 30)
        self.assertEqual(cruise_control.target_speed, 0)

    def testCruiseControlStatusGetter(self):
        """Testing the cruise control status is returned when you call the cruise control status getter"""
        self.assertEqual(self._cruise_control.activated, True)

    def testCruiseControlStatusSetter(self):
        """Testing if you can update the status by calling the status setter"""
        self._cruise_control.activated = False
        self.assertEqual(self._cruise_control.activated, False)

    def testTargetSpeedGetter(self):
        """Testing the target speed is returned when you call the target speed getter"""
        self.assertEqual(self._cruise_control.target_speed, 70)

    def testTargetSpeedSetter(self):
        """Testing if you can update the target speed by calling the target speed setter"""
        self._cruise_control.target_speed = 50
        self.assertEqual(self._cruise_control.target_speed, 50)

    def testTargetSpeedSetterWithNone(self):
        """Testing the target speed defaults to 0 if you create a cruise control object with a target speed"""
        self._cruise_control.target_speed = None
        self.assertEqual(self._cruise_control.target_speed, 0)

    def testValueErrorIsRaisedIfTheTargetSpeedSetIsNegative(self):
        """Testing a value error is raised when trying to update the target speed to a negative number"""
        with self.assertRaises(ValueError):
            self._cruise_control.target_speed = -10

    def testWeatherGetter(self):
        """Testing the weather is returned when you call the weather getter"""
        with self.subTest():
            self.assertEqual(self._cruise_control.weather.weather_condition, "Sunny")
        with self.subTest():
            self.assertEqual(self._cruise_control.weather.temperature, 25)

    def testWeatherSetter(self):
        """Testing if you can update the weather by calling the weather setter"""
        self._cruise_control.weather = Weather("Raining", 10)
        with self.subTest():
            self.assertEqual(self._cruise_control.weather.weather_condition, "Raining")
        with self.subTest():
            self.assertEqual(self._cruise_control.weather.temperature, 10)

    def testFollowingDistanceGetter(self):
        """Testing the following distance is returned when you call the following distance getter"""
        self.assertEqual(self._cruise_control.following_distance, 30)

    def testFollowingDistanceSetter(self):
        """Testing if you can update the following distance by calling the following distance setter"""
        self._cruise_control.following_distance = 10
        self.assertEqual(self._cruise_control.following_distance, 10)

    def testValueErrorIsRaisedIfTheFollowingDistanceSetIsNegative(self):
        """Testing a value error is raised when you attempt to set the following distance to a negative number"""
        with self.assertRaises(ValueError):
            self._cruise_control.following_distance = -10

    def testTurnOnCruiseControl(self):
        """Testing if cruise control is on once you turn it on"""
        self._cruise_control = CruiseControl(False, 70, self._weather, 30)
        self._cruise_control.enable_cruise_control()
        self.assertEqual(self._cruise_control.activated, True)

    def testTurnOffCruiseControl(self):
        """Testing if cruise control is off once you turn it off"""
        self._cruise_control.disable_cruise_control()
        self.assertEqual(self._cruise_control.activated, False)

    def testGetCruiseControlObject(self):
        """Testing if you can get the cruise control object"""
        self.assertEqual(self._cruise_control.cruise_control, "Cruise Control Activated\n"
                                                              "Target Speed: 70MPH\n"
                                                              "Recommended Following Distance: 2 Meters\n"
                                                              "Distance From The Closest Car: 30 Meters")

    def testCruiseControlSetter(self):
        """Testing if you can update the cruise control object by calling the cruise control setter"""
        self._cruise_control.cruise_control = CruiseControl(True, 50, Weather("Raining", 10), 15)
        with self.subTest("Activated Status"):
            self.assertEqual(self._cruise_control.activated, True)
        with self.subTest("Target Speed"):
            self.assertEqual(self._cruise_control.target_speed, 50)
        with self.subTest("Weather Condition"):
            self.assertEqual(self._cruise_control.weather.weather_condition, "Raining")
        with self.subTest("Temperature"):
            self.assertEqual(self._cruise_control.weather.temperature, 10)
        with self.subTest("Following Distance"):
            self.assertEqual(self._cruise_control.following_distance, 15)


if __name__ == '__main__':
    unittest.main()
