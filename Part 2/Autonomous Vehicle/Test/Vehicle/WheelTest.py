import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Wheel import Wheel


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._wheel = Wheel(1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10})

    def tearDown(self):
        self._wheel = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._wheel = Wheel(1, "", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10})

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._wheel = Wheel(1, "Wheel", Colour(255, 255, 255), "", {"Diameter": 3, "Radius": 10})

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._wheel = Wheel(1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": -3, "Radius": -10})

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._wheel = Wheel(-1, "Wheel", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10})

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._wheel.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._wheel.part_id = 1000
        self.assertEqual(self._wheel.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised the wheels part ID is a negative number"""
        with self.assertRaises(ValueError):
            self._wheel.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._wheel.name, "Wheel")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._wheel = Wheel(1, "Engine", Colour(255, 255, 255), "Audi", {"Diameter": 3, "Radius": 10})
        self._wheel.name = "Wheel"
        self.assertEqual(self._wheel.name, "Wheel")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if the wheel has no part name"""
        with self.assertRaises(ValueError):
            self._wheel.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._wheel.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._wheel.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._wheel.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._wheel.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._wheel.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._wheel.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._wheel.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._wheel.colour.blue, 0)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._wheel.colour), "RGB(0, 0, 0)\nCMYK(0, 0, 0, 100)\n#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._wheel.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._wheel.manufacturer = "BMW"
        self.assertEqual(self._wheel.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if the wheel has no manufacturer """
        with self.assertRaises(ValueError):
            self._wheel.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._wheel.dimensions, {"Diameter": 3, "Radius": 10})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._wheel.dimensions = {"Diameter": 1, "Radius": 2}
        self.assertEqual(self._wheel.dimensions, {"Diameter": 1, "Radius": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the wheels dimensions are below zero"""
        with self.assertRaises(ValueError):
            self._wheel.dimensions = {"Diameter": -1, "Radius": -2}

    def testWheelObject(self):
        """Testing the wheel object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._wheel.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._wheel.name, "Wheel")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._wheel.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._wheel.dimensions, {"Diameter": 3, "Radius": 10})
        with self.subTest("Part Object"):
            self.assertEqual(self._wheel.__str__(), "Part Name: Wheel\n"
                                                    "Part ID: 1\n"
                                                    "Colour: \n"
                                                    "RGB(255, 255, 255)\n"
                                                    "CMYK(0, 0, 0, 0)\n"
                                                    "#FFFFFF\n"
                                                    "Manufacture: Audi\n"
                                                    "Diameter: 3 Meters\n"
                                                    "Radius: 10 Meters")


if __name__ == '__main__':
    unittest.main()
