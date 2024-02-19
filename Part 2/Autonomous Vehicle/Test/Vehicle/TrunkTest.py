import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Trunk import Trunk


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._trunk = Trunk(1, "Trunk", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)

    def tearDown(self):
        self._trunk = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._trunk = Trunk(1, "", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._trunk = Trunk(1, "Trunk", Colour(255, 255, 255), "", {"Length": 3, "Width": 5}, True, True)

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._trunk = Trunk(1, "Trunk", Colour(255, 255, 255), "Audi", {"Length": -3, "Width": -5}, True, True)

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._trunk = Trunk(-1, "Trunk", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._trunk.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._trunk.part_id = 1000
        self.assertEqual(self._trunk.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised if you try to set the part ID to a negative number using the part ID
        setter"""
        with self.assertRaises(ValueError):
            self._trunk.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._trunk.name, "Trunk")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._trunk = Trunk(1, "Engine", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)
        self._trunk.name = "Trunk"
        self.assertEqual(self._trunk.name, "Trunk")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if you try to set the part name to an empty string using the part name
        setter"""
        with self.assertRaises(ValueError):
            self._trunk.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._trunk.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._trunk.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._trunk.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._trunk.colour), "RGB(255, 255, 255)\n"
                                                      "CMYK(0, 0, 0, 0)\n"
                                                      "#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._trunk.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._trunk.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._trunk.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._trunk.colour.blue, 0)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._trunk.colour), "RGB(0, 0, 0)\n"
                                                      "CMYK(0, 0, 0, 100)\n"
                                                      "#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._trunk.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._trunk.manufacturer = "BMW"
        self.assertEqual(self._trunk.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if you try to set the parts manufacturer to an empty string using the
        manufacture setter"""
        with self.assertRaises(ValueError):
            self._trunk.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._trunk.dimensions, {"Length": 3, "Width": 5})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._trunk.dimensions = {"Length": 1, "Width": 2}
        self.assertEqual(self._trunk.dimensions, {"Length": 1, "Width": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the parts dimensions you've set using the dimensions setter are
        a negative number"""
        with self.assertRaises(ValueError):
            self._trunk.dimensions = {"Length": -1, "Width": -2}

    def testClosedGetter(self):
        """Testing the trunk closed status is returned when you call the closed getter"""
        self.assertEqual(self._trunk.closed, True)

    def testClosedSetter(self):
        """Testing you can update the closed status by calling the closed setter"""
        self._trunk.closed = False
        self.assertEqual(self._trunk.closed, False)

    def testLockedGetterIfTrunkIsShut(self):
        """Testing the trunk can only be locked if its already shut"""
        self.assertEqual(self._trunk.locked, True)

    def testLockedGetterIfTrunkIsNotShut(self):
        """Testing the trunk can't be locked if it is not shut"""
        self._trunk = Trunk(1, "Trunk", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, False, True)
        self.assertEqual(self._trunk.locked, False)

    def testLockedSetterIfTrunkIsClosed(self):
        """Testing you can update the locked status using the locked getter, but it will only be able to be locked if
        the door is already shut"""
        self._trunk = Trunk(1, "Trunk", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, False)
        self._trunk.locked = True
        self.assertEqual(self._trunk.locked, True)

    def testLockedSetterIfTrunkIsNotClosed(self):
        """Testing you can update the locked status using the locked getter, but it will not lock the door if it is not
        shut"""
        self._trunk = Trunk(1, "Trunk", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, False, True)
        self._trunk.locked = True
        self.assertEqual(self._trunk._locked, False)

    def testTrunkObject(self):
        """Testing the trunk object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._trunk.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._trunk.name, "Trunk")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._trunk.colour), "RGB(255, 255, 255)\n"
                                                      "CMYK(0, 0, 0, 0)\n"
                                                      "#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._trunk.dimensions, {"Length": 3, "Width": 5})
        with self.subTest("Shut Status"):
            self.assertEqual(self._trunk.closed, True)
        with self.subTest("Locked Status"):
            self.assertEqual(self._trunk.locked, True)
        with self.subTest("Trunk Object"):
            self.assertEqual(self._trunk.__str__(), "Part Name: Trunk\n"
                                                    "Part ID: 1\n"
                                                    "Colour: \n"
                                                    "RGB(255, 255, 255)\n"
                                                    "CMYK(0, 0, 0, 0)\n"
                                                    "#FFFFFF\n"
                                                    "Manufacture: Audi\n"
                                                    "Length: 3 Meters\n"
                                                    "Width: 5 Meters\n"
                                                    "Trunk Shut\n"
                                                    "Trunk Locked")


if __name__ == '__main__':
    unittest.main()
