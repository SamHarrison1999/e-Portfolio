import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Tyre import Tyre


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._tyre = Tyre(1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10}, 10, 50)

    def tearDown(self):
        self._tyre = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._tyre = Tyre(1, "", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10}, 10, 50)

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._tyre = Tyre(1, "Wheel", Colour(255, 255, 255), "", {"Diameter": 3, "Radius": 10}, 10, 50)

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._tyre = Tyre(1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": -3, "Radius": -10}, 10, 50)

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._tyre = Tyre(-1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10}, 10, 50)

    def testValueErrorIsRaisedIfTheTreadRemainingIsANegativeNumber(self):
        """Testing a value error is raised if the tread remaining is a negative number"""
        with self.assertRaises(ValueError):
            self._tyre = Tyre(1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10}, -10, 50)

    def testValueErrorIsRaisedIfTheTyrePressureIsANegativeNumber(self):
        """Testing a value error is raised if the tyre pressure is a negative number"""
        with self.assertRaises(ValueError):
            self._tyre = Tyre(1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10}, 10, -50)

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._tyre.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._tyre.part_id = 1000
        self.assertEqual(self._tyre.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised the part ID is a negative number """
        with self.assertRaises(ValueError):
            self._tyre.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._tyre.name, "Wheel")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._tyre = Tyre(1, "Engine", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10}, 10, 50)
        self._tyre.name = "Wheel"
        self.assertEqual(self._tyre.name, "Wheel")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if you try to set the part name to an empty string using the part name
        setter"""
        with self.assertRaises(ValueError):
            self._tyre.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._tyre.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._tyre.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._tyre.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._tyre.colour), "RGB(255, 255, 255)\n"
                                                     "CMYK(0, 0, 0, 0)\n"
                                                     "#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._tyre.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._tyre.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._tyre.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._tyre.colour.blue, 0)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._tyre.colour), "RGB(0, 0, 0)\n"
                                                     "CMYK(0, 0, 0, 100)\n"
                                                     "#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._tyre.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._tyre.manufacturer = "BMW"
        self.assertEqual(self._tyre.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if you try to set the parts manufacturer to an empty string using the
        manufacture setter"""
        with self.assertRaises(ValueError):
            self._tyre.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._tyre.dimensions, {"Diameter": 3, "Radius": 10})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._tyre.dimensions = {"Diameter": 1, "Radius": 2}
        self.assertEqual(self._tyre.dimensions, {"Diameter": 1, "Radius": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the parts dimensions you've set using the dimensions setter are
        a negative number"""
        with self.assertRaises(ValueError):
            self._tyre.dimensions = {"Diameter": -1, "Radius": -2}

    def testTreadRemainingGetter(self):
        """Testing the tread remaining on the tyre is returned when you call the tread getter"""
        self.assertEqual(self._tyre.tread, 10)

    def testTreadRemainingSetter(self):
        """Testing the amount of tread remaining on the tyre can be updated by calling the tread setter"""
        self._tyre.tread = 5
        self.assertEqual(self._tyre.tread, 5)

    def testValueErrorIsRaisedIfYouSetTheTreadRemainingToANegativeNumberUsingTheTreadSetter(self):
        """Testing a value error is raised if you try to set the tread remaining to a negative number using the tread
        setter"""
        with self.assertRaises(ValueError):
            self._tyre.tread = -10

    def testTyrePressureGetter(self):
        """Testing the tyre pressure is returned when you call the tyre pressure getter"""
        self.assertEqual(self._tyre.tyre_pressure, 50)

    def testTyrePressureSetter(self):
        """Testing the tyre pressure can be updated by calling the tyre pressure setter"""
        self._tyre.tyre_pressure = 20
        self.assertEqual(self._tyre.tyre_pressure, 20)

    def testValueErrorIsRaisedIfYouSetTheTyrePressureToANegativeNumberUsingTheTyrePressureSetter(self):
        """Testing a value error is raised if you try to set the tyre pressure to a negative number using the tyre
        pressure setter"""
        with self.assertRaises(ValueError):
            self._tyre.tyre_pressure = -50

    def testTyreObject(self):
        """Testing the tyre object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._tyre.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._tyre.name, "Wheel")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._tyre.colour), "RGB(255, 255, 255)\n"
                                                     "CMYK(0, 0, 0, 0)\n"
                                                     "#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._tyre.dimensions, {"Diameter": 3, "Radius": 10})
        with self.subTest("Part Object"):
            self.assertEqual(self._tyre.__str__(), "Part Name: Wheel\n"
                                                   "Part ID: 1\n"
                                                   "Colour: \n"
                                                   "RGB(255, 255, 255)\n"
                                                   "CMYK(0, 0, 0, 0)\n"
                                                   "#FFFFFF\n"
                                                   "Manufacture: Audi\n"
                                                   "Diameter: 3 Meters\n"
                                                   "Radius: 10 Meters\n"
                                                   "Current Air Pressure: 50 psi\n"
                                                   "Tyre Thread Remaining: 10 mm")


if __name__ == '__main__':
    unittest.main()
