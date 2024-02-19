import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Axel import Axel


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._axel = Axel(1, "Axel", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})

    def tearDown(self) -> None:
        self._axel = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._axel = Axel(1, "", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._axel = Axel(1, "Axel", Colour(255, 255, 255), "", {"Length": 3, "Width": 5})

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._axel = Axel(1, "Axel", Colour(255, 255, 255), "Audi", {"Length": -3, "Width": -5})

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._axel = Axel(-1, "Axel", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._axel.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._axel.part_id = 1000
        self.assertEqual(self._axel.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised if you try to set the part ID to a negative number using the part ID
        setter"""
        with self.assertRaises(ValueError):
            self._axel.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._axel.name, "Axel")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._axel = Axel(1, "Engine", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5})
        self._axel.name = "Axel"
        self.assertEqual(self._axel.name, "Axel")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if axel has no part name"""
        with self.assertRaises(ValueError):
            self._axel.name = ""

    def testColourGetter(self):
        """Testing the colour for the axel is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._axel.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._axel.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._axel.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._axel.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._axel.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._axel.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._axel.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._axel.colour.blue, 0)
        with self.subTest("Axel Colour"):
            self.assertEqual(str(self._axel.colour), "RGB(0, 0, 0)\nCMYK(0, 0, 0, 100)\n#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._axel.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._axel.manufacturer = "BMW"
        self.assertEqual(self._axel.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if the part has no manufacturer"""
        with self.assertRaises(ValueError):
            self._axel.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._axel.dimensions, {"Length": 3, "Width": 5})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._axel.dimensions = {"Length": 1, "Width": 2}
        self.assertEqual(self._axel.dimensions, {"Length": 1, "Width": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the parts dimensions are below zero"""
        with self.assertRaises(ValueError):
            self._axel.dimensions = {"Diameter": -1, "Radius": -2}

    def testAxelObject(self):
        """Testing the Axel object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._axel.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._axel.name, "Axel")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._axel.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._axel.dimensions, {"Length": 3, "Width": 5})
        with self.subTest("Axel Object"):
            self.assertEqual(self._axel.__str__(), "Part Name: Axel\n"
                                                   "Part ID: 1\n"
                                                   "Colour: \n"
                                                   "RGB(255, 255, 255)\n"
                                                   "CMYK(""0, 0, 0, 0)\n"
                                                   "#FFFFFF\n"
                                                   "Manufacture: Audi\n"
                                                   "Length: 3 Meters\n"
                                                   "Width: 5 Meters")


if __name__ == '__main__':
    unittest.main()
