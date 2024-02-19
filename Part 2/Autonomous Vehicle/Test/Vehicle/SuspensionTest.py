import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Suspension import Suspension


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._suspension = Suspension(1, "Suspension", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})

    def tearDown(self):
        self._suspension = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._suspension = Suspension(1, "", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._suspension = Suspension(1, "Suspension", Colour(255, 255, 255), "", {"Length": 3, "Width": 5})

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._suspension = Suspension(1, "Suspension", Colour(255, 255, 255), "Audi", {"Length": -3, "Width": -5})

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._suspension = Suspension(-1, "Suspension", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._suspension.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._suspension.part_id = 1000
        self.assertEqual(self._suspension.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised if you try to set the part ID to a negative number using the part ID
        setter"""
        with self.assertRaises(ValueError):
            self._suspension.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._suspension.name, "Suspension")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._suspension = Suspension(1, "Engine", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})
        self._suspension.name = "Suspension"
        self.assertEqual(self._suspension.name, "Suspension")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if you try to set the part name to an empty string using the part name
        setter"""
        with self.assertRaises(ValueError):
            self._suspension.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._suspension.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._suspension.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._suspension.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._suspension.colour), "RGB(255, 255, 255)\n"
                                                           "CMYK(0, 0, 0, 0)\n"
                                                           "#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._suspension.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._suspension.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._suspension.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._suspension.colour.blue, 0)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._suspension.colour), "RGB(0, 0, 0)\n"
                                                           "CMYK(0, 0, 0, 100)\n"
                                                           "#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._suspension.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._suspension.manufacturer = "BMW"
        self.assertEqual(self._suspension.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if you try to set the parts manufacturer to an empty string using the
        manufacture setter"""
        with self.assertRaises(ValueError):
            self._suspension.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._suspension.dimensions, {"Length": 3, "Width": 5})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._suspension.dimensions = {"Length": 1, "Width": 2}
        self.assertEqual(self._suspension.dimensions, {"Length": 1, "Width": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the suspensions dimensions are below zero"""
        with self.assertRaises(ValueError):
            self._suspension = Suspension(1, "Suspension", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})
            self._suspension.dimensions = {"Length": -1, "Width": -2}

    def testSuspensionObject(self):
        """Testing the Suspension object"""
        self._suspension = Suspension(1, "Suspension", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})
        with self.subTest("Part ID"):
            self.assertEqual(self._suspension.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._suspension.name, "Suspension")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._suspension.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._suspension.dimensions, {"Length": 3, "Width": 5})
        with self.subTest("Suspension Object"):
            self.assertEqual(self._suspension.__str__(), "Part Name: Suspension\n"
                                                         "Part ID: 1\n"
                                                         "Colour: \n"
                                                         "RGB(255, 255, 255)\n"
                                                         "CMYK(0, 0, 0, 0)\n"
                                                         "#FFFFFF\n"
                                                         "Manufacture: Audi\n"
                                                         "Length: 3 Meters\n"
                                                         "Width: 5 Meters")


if __name__ == '__main__':
    unittest.main()
