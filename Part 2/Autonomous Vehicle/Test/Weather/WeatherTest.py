import unittest
from Main.Weather.Weather import Weather


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._weather = Weather("Sunny", 25)

    def tearDown(self):
        self._weather = None

    def testRecommendedFollowingDistanceForSunnyWeather(self):
        """Testing the recommended following distance returns 2 when it's sunny"""
        self.assertEqual(self._weather.recommended_following_distance(), 2)

    def testRecommendedFollowingDistanceForRainyWeather(self):
        """Testing the recommended following distance returns 4 when it's raining"""
        self._weather = Weather("Raining", 10)
        self.assertEqual(self._weather.recommended_following_distance(), 4)

    def testRecommendedFollowingDistanceForSnowyWeather(self):
        """Testing the recommended follow distance returns 10 when it's snowing"""
        self._weather = Weather("Snowing", -10)
        self.assertEqual(self._weather.recommended_following_distance(), 10)

    def testValueErrorForRecommendedFollowingDistance(self):
        """Testing a Value error is raised if the weather condition is not supported"""
        with self.assertRaises(ValueError):
            self._weather = Weather("Cloudy", 5)
            self._weather.recommended_following_distance()

    def testValueErrorIsRaisedIfNoWeatherConditionIsSet(self):
        """Testing a value error is raised if no weather condition is set when creating a weather object"""
        with self.assertRaises(ValueError):
            self._weather = Weather("", 5)

    def testWeatherConditionGetter(self):
        """Testing the weather condition is returned when you call the weather condition getter"""
        self.assertEqual(self._weather.weather_condition, "Sunny")

    def testWeatherConditionSetter(self):
        """Testing if you can update the weather condition by calling the weather condition setter"""
        self._weather.weather_condition = "Raining"
        self.assertEqual(self._weather.weather_condition, "Raining")

    def testValueErrorIsRaisedWhenTryingToSetNoWeatherCondition(self):
        """Testing a value error is raised if you try to update the weather condition to an empty string"""
        with self.assertRaises(ValueError):
            self._weather.weather_condition = ""

    def testTemperatureGetter(self):
        """Testing the temperature is returned when you call the temperature getter"""
        self.assertEqual(self._weather.temperature, 25)

    def testTemperatureSetter(self):
        """Testing if you can update the temperature by calling the temperature setter and supplying the updated
        temperature"""
        self._weather.temperature = 35
        self.assertEqual(self._weather.temperature, 35)

    def testWeatherGetter(self):
        """Testing the weather object is return when you call the weather getter"""
        self.assertEqual(self._weather.weather, "Weather Condition: Sunny\n"
                                                "Temperature: 25 degrees\n"
                                                "Recommended Following Distance: 2 Meters")

    def testWeatherSetter(self):
        """Testing if you can update the weather by calling the weather setter"""
        self._weather.weather = Weather("Raining", 10)
        with self.subTest("Weather Condition"):
            self.assertEqual(self._weather.weather_condition, "Raining")
        with self.subTest("Temperature"):
            self.assertEqual(self._weather.temperature, 10)


if __name__ == '__main__':
    unittest.main()
