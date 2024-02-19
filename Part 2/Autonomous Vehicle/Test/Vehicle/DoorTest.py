import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Door import Door


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._door = Door(1, "Door", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)

    def tearDown(self):
        self._door = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._door = Door(1, "", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._door = Door(1, "Door", Colour(255, 255, 255), "", {"Length": 3, "Width": 5}, True, True)

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._door = Door(1, "Door", Colour(255, 255, 255), "Audi", {"Length": -3, "Width": -5}, True, True)

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._door = Door(-1, "Door", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)

    def testLockingDoorWhenItsNotShut(self):
        self._door = Door(1, "Door", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, False, True)
        self.assertEqual(self._door.locked, False)

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._door.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._door.part_id = 1000
        self.assertEqual(self._door.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised if the doors ID is a negative number"""
        with self.assertRaises(ValueError):
            self._door.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._door.name, "Door")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._door = Door(1, "Engine", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)
        self._door.name = "Door"
        self.assertEqual(self._door.name, "Door")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if the door has no part name"""
        with self.assertRaises(ValueError):
            self._door.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._door.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._door.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._door.colour.blue, 255)
        with self.subTest("Colour"):
            self.assertEqual(str(self._door.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._door.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._door.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._door.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._door.colour.blue, 0)
        with self.subTest("Colour"):
            self.assertEqual(str(self._door.colour), "RGB(0, 0, 0)\nCMYK(0, 0, 0, 100)\n#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._door.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._door.manufacturer = "BMW"
        self.assertEqual(self._door.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if the door has no manufacturer"""
        with self.assertRaises(ValueError):
            self._door.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._door.dimensions, {"Length": 3, "Width": 5})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._door.dimensions = {"Length": 1, "Width": 2}
        self.assertEqual(self._door.dimensions, {"Length": 1, "Width": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the door dimensions are below zero"""
        with self.assertRaises(ValueError):
            self._door.dimensions = {"Diameter": -1, "Radius": -2}

    def testClosedGetter(self):
        """Testing the door closed status is returned when you call the closed getter"""
        self.assertEqual(self._door._closed, True)

    def testClosedSetter(self):
        """Testing you can update the closed status by calling the closed setter"""
        self._door.closed = False
        self.assertEqual(self._door._closed, False)

    def testLockedGetterIfDoorIsShut(self):
        """Testing the door can only be locked if its already shut"""
        self.assertEqual(self._door._closed, True)

    def testLockedGetterIfDoorIsNotShut(self):
        """Testing the door can't be locked if it is not shut"""
        self._door.closed = False
        self.assertEqual(self._door._closed, False)

    def testLockedSetterIfDoorIsClosed(self):
        """Testing you can lock the door if its already closed"""
        self._door.locked = True
        self.assertEqual(self._door._locked, True)

    def testLockedSetterIfDoorIsNotClosed(self):
        """Testing you can't lock the door if it is not closed"""
        self._door = Door(1, "Door", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5}, True, True)
        self._door.closed = False
        self._door.locked = True
        self.assertEqual(self._door._locked, False)

    def testDoorObject(self):
        """Testing the Door object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._door.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._door.name, "Door")
        with self.subTest("Colour"):
            self.assertEqual(str(self._door.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")
        with self.subTest("Dimensions"):
            self.assertEqual(self._door.dimensions, {"Length": 3, "Width": 5})
        with self.subTest("Shut Status"):
            self.assertEqual(self._door.closed, True)
        with self.subTest("Locked Status"):
            self.assertEqual(self._door.locked, True)
        with self.subTest("Door Object"):
            self.assertEqual(self._door.__str__(), "Part Name: Door\n"
                                                   "Part ID: 1\n"
                                                   "Colour: \n"
                                                   "RGB(255, 255, 255)\n"
                                                   "CMYK(0, 0, 0, 0)\n"
                                                   "#FFFFFF\n"
                                                   "Manufacture: Audi\n"
                                                   "Length: 3 Meters\n"
                                                   "Width: 5 Meters\n"
                                                   "Door Shut\n"
                                                   "Door Locked")


if __name__ == '__main__':
    unittest.main()
