import unittest
from Main.Vehicle.Radio import Radio


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._radio = Radio("Capital", 95.8, None)

    def tearDown(self):
        self._radio = None

    def testValueErrorRaiseIfTheRadioStationHasNoName(self):
        """Testing a value error is raised if the radio station has no name"""
        with self.assertRaises(ValueError):
            self._radio = Radio("", 95.8, None)

    def testValueErrorRaiseIfTheRadioStationFMNumberIsNotValid(self):
        """Testing a value error is raised if the radio stations fm number isn't valid (not between 87.5 and 108)"""
        with self.assertRaises(ValueError):
            self._radio = Radio("Capital", 200, None)

    def testValueErrorRaiseIfTheRadioStationAMNumberIsNotValid(self):
        """Testing a value error is raised if the radio stations am number isn't valid (not between 535 and 1705)"""
        with self.assertRaises(ValueError):
            self._radio = Radio("Blackburn Radio", None, 200)

    def testFMIsSetToZeroWhenNoFMNumberIsSupplied(self):
        """Testing the default value for a radio stations fm number is 0 if no fm number has been provided"""
        self._radio = Radio("Blackburn Radio", None, 630)
        self.assertEqual(self._radio.frequency_modulation, 0)

    def testAMIsSetToZeroWhenNoAMNumberIsSupplied(self):
        """Testing the default value for a radio stations am number is 0 if no am number has been provided"""
        self.assertEqual(self._radio.amplitude_modulation, 0)

    def testStationNameGetter(self):
        """Testing the radio station name is returned when you call the radio station getter"""
        self.assertEqual(self._radio.station_name, "Capital")

    def testStationNameSetter(self):
        """Testing if you can update the radio station name by calling the radio station setter"""
        self._radio = Radio("Kiss FM", 95.8, None)
        self._radio.station_name = "Capital"
        self.assertEqual(self._radio.station_name, "Capital")

    def testValueErrorRaiseWhenTheRadioStationNameSetUsingTheStationNameSetterIsEmpty(self):
        """Testing a value error is raised if the radio station name set using the station name setter has no name"""
        with self.assertRaises(ValueError):
            self._radio.station_name = ""

    def testFMGetter(self):
        """Testing the radio stations frequency modulation is returned when you call the fm getter"""
        self.assertEqual(self._radio.frequency_modulation, 95.8)

    def testFMSetter(self):
        """Testing if you can update the radio stations fm number by calling the fm setter"""
        self._radio = Radio("Capital", 100, None)
        self._radio.frequency_modulation = 95.8
        self.assertEqual(self._radio.frequency_modulation, 95.8)

    def testFMSetterWithNone(self):
        """Testing what happens when you set the fm number to none using the fm setter"""
        self._radio.frequency_modulation = None
        self.assertEqual(self._radio.frequency_modulation, 0)

    def testValueErrorRaiseIfTheRadioStationFMNumberSetUsingTheFMSetterIsNotValid(self):
        """Testing a value error is raised if the radio stations fm number isn't valid"""
        with self.assertRaises(ValueError):
            self._radio.frequency_modulation = 200

    def testAMGetter(self):
        """Testing the radio stations amplitude modulation is returned when you call the am getter"""
        self._radio = Radio("Blackburn Radio", None, 630)
        self.assertEqual(self._radio.amplitude_modulation, 630)

    def testAMSetter(self):
        """Testing if you can update the radio stations am number by calling the am setter"""
        self._radio = Radio("Blackburn Radio", None, 880)
        self._radio.amplitude_modulation = 630
        self.assertEqual(self._radio.amplitude_modulation, 630)

    def testValueErrorRaiseIfTheRadioStationAMNumberSetUsingTheAMSetterIsNotValid(self):
        """Testing a value error is raised if the radio stations am number set using the am setter isn't valid"""
        with self.assertRaises(ValueError):
            self._radio = Radio("Blackburn Radio", None, 880)
            self._radio.amplitude_modulation = 200

    def testTheRadioStationAMNumberSetUsingTheAMSetterWithNone(self):
        """Testing the radio stations am number with none"""
        self._radio = Radio("Blackburn Radio", None, 880)
        self._radio.amplitude_modulation = None
        self.assertEqual(self._radio.amplitude_modulation, 0)

    def testGetRadioObject(self):
        """Testing getting the radio object"""
        with self.subTest("Station Name"):
            self.assertEqual(self._radio.station_name, "Capital")
        with self.subTest("FM"):
            self.assertEqual(self._radio.frequency_modulation, 95.8)
        with self.subTest("AM"):
            self.assertEqual(self._radio.amplitude_modulation, 0)
        with self.subTest("Radio Object"):
            self.assertEqual(self._radio.__str__(), "Station Name: Capital\nFM: 95.8\nAM: 0Hz")


if __name__ == '__main__':
    unittest.main()
