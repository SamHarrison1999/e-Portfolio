import unittest

from Main.Colour.Colour import Colour
from Main.Vehicle.Engine import Engine
from Main.Vehicle.EngineMode import EngineMode


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._engine = Engine(1, "Engine", Colour(255, 255, 255), "Audi",
                              {"Length": 3, "Width": 5}, 2, 250, 12, 8, EngineMode.Sport)

    def tearDown(self):
        self._engine = None

    def testValueErrorIsRaisedIfThePartHasNoName(self):
        """Testing a value error is raised if the part as no name"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "", Colour(255, 255, 255), "Audi",
                                  {"Length": 3, "Width": 5}, 2, 250, 12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfThePartHasNoManufacture(self):
        """Testing a value error is raised if the part has no manufacture"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "Engine", Colour(255, 255, 255), "",
                                  {"Length": 3, "Width": 5}, 2, 250, 12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfThePartHasInvalidDimensions(self):
        """Testing a value error is raised if the part has invalid dimensions"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "Engine", Colour(255, 255, 255), "Audi",
                                  {"Length": -3, "Width": -5}, 2, 250, 12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfThePartIDIsANegativeNumber(self):
        """Testing a value error is raised if the part ID number is a negative number"""
        with self.assertRaises(ValueError):
            self._engine = Engine(-1, "Engine", Colour(255, 255, 255), "Audi",
                                  {"Length": 3, "Width": 5}, 2, 250, 12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfTheEngineSizeIsANegativeNumber(self):
        """Testing a value error is raised if the engine size is a negative number"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "Engine", Colour(255, 255, 255), "Audi",
                                  {"Length": 3, "Width": 5}, -2, 250, 12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfTheHorsePowerIsANegativeNumber(self):
        """Testing a value error is raised if the horsepower the engine produces is a negative number"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "Engine", Colour(255, 255, 255), "Audi",
                                  {"Length": 3, "Width": 5}, 2, -250, 12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfTheNumberOfCylindersIsANegativeNumber(self):
        """Testing a value error is raised if the number of cylinders is a negative number"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "Engine", Colour(255, 255, 255), "Audi",
                                  {"Length": 3, "Width": 5}, 2, 250, -12, 8, EngineMode.Sport)

    def testValueErrorIsRaisedIfTheNumberOfValvesIsANegativeNumber(self):
        """Testing a value error is raised if the number of valves is a negative number"""
        with self.assertRaises(ValueError):
            self._engine = Engine(1, "Engine", Colour(255, 255, 255), "Audi",
                                  {"Length": 3, "Width": 5}, 2, 250, 12, -8, EngineMode.Sport)

    def testPartIDGetter(self):
        """Testing the part ID is returned when you call the part ID getter"""
        self.assertEqual(self._engine.part_id, 1)

    def testPartIDSetter(self):
        """Testing if you can update the part ID by calling the part ID setter"""
        self._engine.part_id = 1000
        self.assertEqual(self._engine.part_id, 1000)

    def testValueErrorIsRaisedIfYouSetThePartIDToANegativeNumberUsingThePartIDSetter(self):
        """Testing a value error is raised if the engines part ID is a negative number"""
        with self.assertRaises(ValueError):
            self._engine.part_id = -1

    def testPartNameGetter(self):
        """Testing the part name is returned when you call the part name getter"""
        self.assertEqual(self._engine.name, "Engine")

    def testPartNameSetter(self):
        """Testing if you can update the part name by calling the part name setter"""
        self._engine = Engine(1, "Chassis", Colour(255, 255, 255), "Audi",
                              {"Length": 3, "Width": 5}, 2, 250, 12, 8, EngineMode.Sport)
        self._engine.name = "Engine"
        self.assertEqual(self._engine.name, "Engine")

    def testValueErrorIsRaisedIfYouSetThePartNameAsAnEmptyStringUsingThePartNameSetter(self):
        """Testing a value error is raised if the engine has no part name"""
        with self.assertRaises(ValueError):
            self._engine.name = ""

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._engine.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._engine.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._engine.colour.blue, 255)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._engine.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")

    def testColourSetter(self):
        """Testing you can change the colour of the part by calling the colour setter"""
        self._engine.colour = Colour(0, 0, 0)
        with self.subTest("Red"):
            self.assertEqual(self._engine.colour.red, 0)
        with self.subTest("Green"):
            self.assertEqual(self._engine.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._engine.colour.blue, 0)
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._engine.colour), "RGB(0, 0, 0)\nCMYK(0, 0, 0, 100)\n#000000")

    def testManufacturerGetter(self):
        """Testing the part manufacturer is returned when you call the manufacturer getter"""
        self.assertEqual(self._engine.manufacturer, "Audi")

    def testManufacturerSetter(self):
        """Testing you can update the part's manufacturer by calling the manufacturer setter"""
        self._engine.manufacturer = "BMW"
        self.assertEqual(self._engine.manufacturer, "BMW")

    def testValueErrorIsRaisedIfYouSetThePartManufactureAsAnEmptyStringUsingThePartManufactureSetter(self):
        """Testing a value error is raised if the engine has no manufacturer"""
        with self.assertRaises(ValueError):
            self._engine.manufacturer = ""

    def testPartDimensionsGetter(self):
        """Testing the parts dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._engine.dimensions, {"Length": 3, "Width": 5})

    def testPartDimensionsSetter(self):
        """Testing you can update the parts dimensions by calling the dimensions setter"""
        self._engine.dimensions = {"Length": 1, "Width": 2}
        self.assertEqual(self._engine.dimensions, {"Length": 1, "Width": 2})

    def testValueErrorIsRaisedIfYouSetAnyOfThePartDimensionsAsANegativeNumberUsingThePartManufactureSetter(self):
        """Testing a value error is raised if any of the engines dimensions are below zero"""
        with self.assertRaises(ValueError):
            self._engine.dimensions = {"Diameter": -1, "Radius": -2}

    def testSizeGetter(self):
        """Testing the engine size is returned when you call the size getter"""
        self.assertEqual(self._engine._size, 2)

    def testSizeSetter(self):
        """Testing you can update the engine size by calling the size setter"""
        self._engine.size = 1.5
        self.assertEqual(self._engine._size, 1.5)

    def testValueErrorIsRaisedIfTheEngineSizeSetUsingTheSizeSetterIsBelowZero(self):
        """Testing a value error is raised if the engine size is below zero"""
        with self.assertRaises(ValueError):
            self._engine.size = -1

    def testHorsePowerGetter(self):
        """Testing the horsepower is returned when you call the horsepower getter"""
        self.assertEqual(self._engine._horse_power, 250)

    def testHorsePowerSetter(self):
        """Testing you can update the horsepower by calling the horsepower setter"""
        self._engine.horse_power = 200
        self.assertEqual(self._engine.horse_power, 200)

    def testValueErrorIsRaisedIfTheHorsePowerSetUsingTheHorsePowerSetterIsBelowZero(self):
        """Testing a value error is raised if the engines horsepower is below zero"""
        with self.assertRaises(ValueError):
            self._engine.horse_power = -200

    def testCylindersGetter(self):
        """Testing the number of cylinders are returned when you call the cylinders getter"""
        self.assertEqual(self._engine.cylinders, 12)

    def testCylinderSetter(self):
        """Testing you can update the number of cylinders by calling the cylinders setter"""
        self._engine.cylinders = 8
        self.assertEqual(self._engine.cylinders, 8)

    def testValueErrorIsRaisedIfNumberOfCylindersSetUsingTheCylindersSetterIsBelowZero(self):
        """Testing a value error is raised if the number of cylinders in the engine is below zero"""
        with self.assertRaises(ValueError):
            self._engine.cylinders = -8

    def testValvesGetter(self):
        """Testing the number of valves are returned when you call the valves getter"""
        self.assertEqual(self._engine.valves, 8)

    def testValvesSetter(self):
        """Testing you can update the number of valves by calling the valves setter"""
        self._engine.valves = 12
        self.assertEqual(self._engine.valves, 12)

    def testValueErrorIsRaisedIfNumberOfValvesSetUsingTheValvesSetterIsBelowZero(self):
        """Testing a value error is raised if the number of valves in the engine is below zero"""
        with self.assertRaises(ValueError):
            self._engine.valves = -12

    def testEngineModeGetter(self):
        """Testing the engine mode is returned when you call the mode getter"""
        self.assertEqual(self._engine.mode, EngineMode.Sport)

    def testEngineModeSetter(self):
        """Testing you can update the engine mode by calling the mode setter"""
        self._engine.mode = EngineMode.Economical
        self.assertEqual(self._engine.mode, EngineMode.Economical)

    def testEngineObject(self):
        """Testing the Engine object"""
        with self.subTest("Part ID"):
            self.assertEqual(self._engine.part_id, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._engine.name, "Engine")
        with self.subTest("Part Colour"):
            self.assertEqual(str(self._engine.colour), "RGB(255, 255, 255)\nCMYK(0, 0, 0, 0)\n#FFFFFF")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._engine.dimensions, {"Length": 3, "Width": 5})
        with self.subTest("Engine Size"):
            self.assertEqual(self._engine.size, 2)
        with self.subTest("Horse Power"):
            self.assertEqual(self._engine.horse_power, 250)
        with self.subTest("Number of cylinders"):
            self.assertEqual(self._engine.cylinders, 12)
        with self.subTest("Number of valves"):
            self.assertEqual(self._engine.valves, 8)
        with self.subTest("Engine Mode"):
            self.assertEqual(self._engine.mode.name, "Sport")
        with self.subTest("Engine Object"):
            self.assertEqual(self._engine.__str__(), "Part Name: Engine\n"
                                                     "Part ID: 1\n"
                                                     "Colour: \n"
                                                     "RGB(255, 255, 255)\n"
                                                     "CMYK(0, 0, 0, 0)\n"
                                                     "#FFFFFF\n"
                                                     "Manufacture: Audi\n"
                                                     "Length: 3 Meters\n"
                                                     "Width: 5 Meters\n"
                                                     "Engine Size: 2L\n"
                                                     "Break Horse Power: 250\n"
                                                     "Number of Cylinders: 12\n"
                                                     "Number of Valves: 8\n"
                                                     "Mode: Sport")


if __name__ == '__main__':
    unittest.main()
