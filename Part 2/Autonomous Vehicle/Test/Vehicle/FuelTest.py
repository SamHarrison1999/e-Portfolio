import unittest
from Main.Vehicle.FuelType import FuelType
from Main.Vehicle.Fuel import Fuel


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._fuel = Fuel(FuelType.Diesel, 100, 50)

    def tearDown(self):
        self._fuel = None

    def testValueErrorIsRaisedIfTheFuelTankSizeIsANegativeNumber(self):
        """Testing a value error is raised if the fuel tank size is a negative number"""
        with self.assertRaises(ValueError):
            self._fuel = Fuel(FuelType.Diesel, -10, 50)

    def testValueErrorIsRaisedIfTheAmountOfFuelRemainingIsANegativeNumber(self):
        """Testing a value error is raised if the amount of fuel remaining is a negative number"""
        with self.assertRaises(ValueError):
            self._fuel = Fuel(FuelType.Diesel, 100, -10)

    def testWhenTheAmountOfFuelRemainingIsGreaterThanTheFuelTankSize(self):
        """Testing when the amount of fuel remaining is greater than the fuel tank size"""
        self._fuel = Fuel(FuelType.Diesel, 30, 50)
        self.assertEqual(self._fuel.fuel_remaining, 30)

    def testFuelTypeGetter(self):
        """Testing the fuel type is returned when you call the fuel type getter"""
        self._fuel = Fuel(FuelType.Diesel, 100, 50)
        self.assertEqual(self._fuel.fuel_type.name, "Diesel")

    def testFuelTypeSetter(self):
        """Testing if you can update the fuel type by calling the setter fuel type function"""
        self._fuel.fuel_type = FuelType.Electric
        self.assertEqual(self._fuel.fuel_type.name, "Electric")

    def testCapacityGetter(self):
        """Testing the fuel tank size is returned when you call the fuel tank size getter"""
        self.assertEqual(self._fuel.capacity, 100)

    def testCapacitySetter(self):
        """Testing if you can update the fuel tank size by calling the fuel tank size setter"""
        self._fuel.capacity = 200
        self.assertEqual(self._fuel.capacity, 200)

    def testValueErrorIsRaisedIfTheFuelTankSizeSetIsANegativeNumber(self):
        """Testing a value error is raised if the fuel tank size set is a negative number"""
        with self.assertRaises(ValueError):
            self._fuel.capacity = -10

    def testFuelRemainingGetter(self):
        """Testing the amount of fuel remaining is returned when you call the amount of fuel remaining getter"""
        self.assertEqual(self._fuel.fuel_remaining, 50)

    def testFuelRemainingSetter(self):
        """Testing if you can update the amount of fuel remaining by calling the amount of fuel remaining setter"""
        self._fuel.fuel_remaining = 20
        self.assertEqual(self._fuel.fuel_remaining, 20)

    def testWhenTheAmountOfFuelRemainingSetUsingTheSetterIsGreaterThanTheFuelTankSize(self):
        """Testing when the amount of fuel remaining is greater than the fuel tank size"""
        self._fuel.fuel_remaining = 200
        self.assertEqual(self._fuel.fuel_remaining, 100)

    def testValueErrorIsRaisedIfTheAmountOfFuelRemainingSetIsANegativeNumber(self):
        """Testing a value error is raised if the amount of fuel remaining is a negative number"""
        with self.assertRaises(ValueError):
            self._fuel.fuel_remaining = -10

    def testFuelObject(self):
        """Testing if you can get the fuel object"""
        self.assertEqual(self._fuel.__str__(), "Fuel Type: Diesel\n"
                                               "Fuel Tank Capacity: 100L\n"
                                               "Amount of fuel remaining: 50L")

    def testLowOnFuel(self):
        """Testing the low on fuel function"""
        self._fuel = Fuel(FuelType.Diesel, 100, 5)
        self.assertEqual(self._fuel.low_on_fuel(), True)

    def testNoFuel(self):
        """Testing the out of fuel function"""
        self._fuel = Fuel(FuelType.Diesel, 100, 0)
        self.assertEqual(self._fuel.out_of_fuel(), True)


if __name__ == '__main__':
    unittest.main()
