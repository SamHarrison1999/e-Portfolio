import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Transmission import Transmission
from Main.Vehicle.TransmissionType import TransmissionType


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._transmission = Transmission(1, "Transmission", Colour(255, 255, 255), "Audi", {"Length": 3, "Width": 5},
                                          TransmissionType.MANUAL, 6, 3)

    def tearDown(self):
        self._transmission = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._transmission = Transmission(1, "", Colour(255, 255, 255), "Audi",
                                              {"Length": 3, "Width": 5}, TransmissionType.MANUAL, 6, 3)

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._transmission = Transmission(1, "Transmission", Colour(255, 255, 255), "",
                                              {"Length": 3, "Width": 5}, TransmissionType.MANUAL, 6, 3)

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._transmission = Transmission(1, "Transmission", Colour(255, 255, 255), "Audi",
                                              {"Length": -3, "Width": -5}, TransmissionType.MANUAL, 6, 3)

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._transmission = Transmission(-1, "Transmission", Colour(255, 255, 255), "Audi",
                                              {"Length": 3, "Width": 5}, TransmissionType.MANUAL, 6, 3)

    def testValueErrorIsRaisedIfTheTransmissionDoesNotHaveAnyGears(self):
        """Testing a value error is raised if the transmission doesn't have any gears"""
        with self.assertRaises(ValueError):
            self._transmission = Transmission(1, "Transmission", Colour(255, 255, 255), "Audi",
                                              {"Length": 3, "Width": 5}, TransmissionType.MANUAL, -6, 3)

    def testValueErrorIsRaisedIfTheCurrentGearIsNotAvailable(self):
        """Testing a value error is raised if the current gear doesn't exist"""
        with self.assertRaises(ValueError):
            self._transmission = Transmission(1, "Transmission", Colour(255, 255, 255), "Audi",
                                              {"Length": 3, "Width": 5}, TransmissionType.MANUAL, 6, 7)

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._transmission.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._transmission.part_id = 1000
        self.assertEqual(self._transmission.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised if you try to set the part ID to a negative number using the part ID
        setter"""
        with self.assertRaises(ValueError):
            self._transmission.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._transmission.name, "Transmission")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._transmission = Transmission(1, "Engine", Colour(255, 255, 255), "Audi",
                                          {"Length": 3, "Width": 5}, TransmissionType.MANUAL, 6, 3)
        self._transmission.name = "Transmission"
        self.assertEqual(self._transmission.name, "Transmission")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if you try to set the part name to an empty string using the part name
        setter"""
        with self.assertRaises(ValueError):
            self._transmission.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._transmission.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._transmission.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._transmission.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._transmission.colour), "RGB(255, 255, 255)\n"
                                                             "CMYK(0, 0, 0, 0)\n"
                                                             "#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._transmission.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._transmission.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._transmission.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._transmission.colour.blue, 0)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._transmission.colour), "RGB(0, 0, 0)\n"
                                                             "CMYK(0, 0, 0, 100)\n"
                                                             "#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._transmission.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._transmission.manufacturer = "BMW"
        self.assertEqual(self._transmission.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if you try to set the parts manufacturer to an empty string using the
        manufacture setter"""
        with self.assertRaises(ValueError):
            self._transmission.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._transmission.dimensions, {"Length": 3, "Width": 5})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._transmission.dimensions = {"Length": 1, "Width": 2}
        self.assertEqual(self._transmission.dimensions, {"Length": 1, "Width": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the parts dimensions you've set using the dimensions setter are
        a negative number"""
        with self.assertRaises(ValueError):
            self._transmission.dimensions = {"Length": -1, "Width": -2}

    def testTransmissionTypeGetter(self):
        """Testing the transmission type is returned when you call the transmission type getter"""
        self.assertEqual(self._transmission.transmission_type, TransmissionType.MANUAL)

    def testTransmissionTypeSetter(self):
        """Testing you can update the transmission type by calling the set transmission type function"""
        self._transmission.transmission_type = TransmissionType.AUTOMATIC
        self.assertEqual(self._transmission.transmission_type, TransmissionType.AUTOMATIC)

    def testNumberOfGearsGetter(self):
        """Testing the number of gears is returned when you call the number of gears getter"""
        self.assertEqual(self._transmission.number_of_gears, 6)

    def testNumberOfGearsSetter(self):
        """Testing you can change the number of gears by calling the number of gears setter"""
        self._transmission.number_of_gears = 5
        self.assertEqual(self._transmission.number_of_gears, 5)

    def testValueErrorIsRaisedIfTheNumberOfGearsSetUsingTheSetterIsANegativeNumber(self):
        """Testing a value error is raised if the transmission doesn't have any gears"""
        with self.assertRaises(ValueError):
            self._transmission.number_of_gears = -6

    def testCurrentGearGetter(self):
        """Testing the current gear is returned when you call the current gear getter"""
        self.assertEqual(self._transmission.current_gear, 3)

    def testCurrentGearSetter(self):
        """Testing you can change the gear by calling the current gear setter"""
        self._transmission.current_gear = 1
        self.assertEqual(self._transmission.current_gear, 1)

    def testValueErrorIsRaisedIfTheGearYourTryingToChangeToUsingTheCurrentGearSetterIsNotAvailable(self):
        """Testing a value error is raised if the current gear doesn't exist"""
        with self.assertRaises(ValueError):
            self._transmission.current_gear = 10

    def testTransmissionObject(self):
        """Testing the Transmission object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._transmission.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._transmission.name, "Transmission")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._transmission.colour), "RGB(255, 255, 255)\n"
                                                             "CMYK(0, 0, 0, 0)\n"
                                                             "#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._transmission.dimensions, {"Length": 3, "Width": 5})
        with self.subTest("Transmission Type"):
            self.assertEqual(self._transmission.transmission_type, TransmissionType.MANUAL)
        with self.subTest("Number Of Gears"):
            self.assertEqual(self._transmission.number_of_gears, 6)
        with self.subTest("Current Gear"):
            self.assertEqual(self._transmission.current_gear, 3)
        with self.subTest("Transmission Object"):
            self.assertEqual(self._transmission.__str__(),
                             "Part Name: Transmission\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(255, 255, 255)\n"
                             "CMYK(0, 0, 0, 0)\n"
                             "#FFFFFF\n"
                             "Manufacture: Audi\n"
                             "Length: 3 Meters\n"
                             "Width: 5 Meters\n"
                             "Transmission: Manual\n"
                             "Number of Gears: 6\n"
                             "Current Gear: 3")

    def testNeutral(self):
        """Testing the neutral function puts the vehicle in neutral"""
        self._transmission.neutral()
        self.assertEqual(self._transmission.current_gear, 0)

    def testReverse(self):
        """Testing the reverse function puts the vehicle in reverse"""
        self._transmission.reverse()
        self.assertEqual(self._transmission.current_gear, -1)

    def testGearUp(self):
        """Testing the gear up function"""
        self._transmission.gear_up()
        self.assertEqual(self._transmission.current_gear, 4)

    def testGearDown(self):
        """Testing the gear down function"""
        self._transmission.gear_down()
        self.assertEqual(self._transmission.current_gear, 2)


if __name__ == '__main__':
    unittest.main()
