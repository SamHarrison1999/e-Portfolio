import unittest
from Main.Vehicle.Mileage import Mileage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._mileage = Mileage(40, 100000)

    def tearDown(self):
        self._mileage = None

    def testValueErrorIsRaisedIfTheMilesPerGallonIsLessThanZero(self):
        """Testing a value error is raised if ths MPG is less than 0"""
        with self.assertRaises(ValueError):
            self._mileage = Mileage(-40, 100000)

    def testValueErrorIsRaisedIfTheCurrentMileageIsLessThanZero(self):
        """Testing a value error is raised if ths current mileage is less than 0"""
        with self.assertRaises(ValueError):
            self._mileage = Mileage(40, -100000)

    def testMilesPerGallonGetter(self):
        """Testing the MPG is returned when you call the MPG getter"""
        self.assertEqual(self._mileage.miles_per_gallon, 40)

    def testMilesPerGallonSetter(self):
        """Testing the MPG can be updated by calling the MPG setter"""
        self._mileage.miles_per_gallon = 50
        self.assertEqual(self._mileage.miles_per_gallon, 50)

    def testValueErrorIsRaisedIfYouSetTheMilesPerGallonToLessThanZeroUsingTheMilesPerGallonSetter(self):
        """Testing a value error is raised if ths MPG set using the MPG setter is less than 0"""
        with self.assertRaises(ValueError):
            self._mileage.miles_per_gallon = -40

    def testCurrentMileageGetter(self):
        """Testing the current mileage is returned when you call the current mileage getter"""
        self.assertEqual(self._mileage.current_mileage, 100000)

    def testCurrentMileageSetter(self):
        """Testing the current mileage can be updated by calling the current mileage setter"""
        self._mileage.current_mileage = 200000
        self.assertEqual(self._mileage.current_mileage, 200000)

    def testValueErrorIsRaisedIfYouSetTheCurrentMileageToLessThanZeroUsingTheCurrentMileageSetter(self):
        """Testing a value error is raised if ths current mileage set using the current mileage setter is less than 0"""
        with self.assertRaises(ValueError):
            self._mileage.current_mileage = -100000

    def testMileageObject(self):
        """Testing the mileage object"""
        with self.subTest("MPG"):
            self.assertEqual(self._mileage.miles_per_gallon, 40)
        with self.subTest("Current Mileage"):
            self.assertEqual(self._mileage.current_mileage, 100000)
        with self.subTest("Mileage Object"):
            self.assertEqual(self._mileage.__str__(), "MPG: 40\nCurrent Mileage: 100000 Miles")


if __name__ == '__main__':
    unittest.main()
