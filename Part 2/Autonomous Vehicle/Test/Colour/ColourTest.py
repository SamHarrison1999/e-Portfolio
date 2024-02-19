import unittest
from Main.Colour.Colour import Colour


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._colour = Colour(200, 200, 200)

    def tearDown(self):
        self._colour = None

    def testValueErrorIsRaisedIfRedValueIsNotValid(self):
        """Testing a value error is raised if the red value isn't between 0 and 255"""
        with self.assertRaises(ValueError):
            Colour(-10, 200, 200)

    def testValueErrorIsRaisedIfGreenValueIsNotValid(self):
        """Testing a value error is raised if the green value isn't between 0 and 255"""
        with self.assertRaises(ValueError):
            Colour(200, -10, 200)

    def testValueErrorIsRaisedIfBlueValueIsNotValid(self):
        """Testing a value error is raised if the blue value isn't between 0 and 255"""
        with self.assertRaises(ValueError):
            Colour(200, 200, -10)

    def testRGBToCMYK(self):
        """Testing converting the RGB colour to CMYK"""
        self.assertEqual(self._colour.cmyk(self._colour.red, self._colour.green, self._colour.blue), (0, 0, 0, 22))

    def testBlackToCMYK(self):
        """Testing converting black colour to CMYK"""
        self._colour = Colour(0, 0, 0)
        self.assertEqual(self._colour.cmyk(self._colour.red, self._colour.green, self._colour.blue), (0, 0, 0, 100))

    def testRGBToHex(self):
        """Testing converting the RGB colour to hexadecimal"""
        self.assertEqual(self._colour.hex_code(self._colour.red, self._colour.green, self._colour.blue), "#C8C8C8")

    def testRedValueGetter(self):
        """Testing the red value is returned when you call the red getter"""
        self.assertEqual(self._colour.red, 200)

    def testRedValueSetter(self):
        """Testing if you can update the red value by calling the red setter"""
        self._colour.red = 100
        self.assertEqual(self._colour.red, 100)

    def testValueErrorIsRaisedIfRedSetterValueIsNotValid(self):
        """Testing a value error is raised if the red value isn't between 0 and 255"""
        with self.assertRaises(ValueError):
            self._colour.red = -10

    def testGreenValueGetter(self):
        """Testing the green value is returned when you call the green getter"""
        self.assertEqual(self._colour.green, 200)

    def testGreenValueSetter(self):
        """Testing if you can update the green value by calling the green setter"""
        self._colour.green = 100
        self.assertEqual(self._colour.green, 100)

    def testValueErrorIsRaisedIfGreenSetterValueIsNotValid(self):
        """Testing a value error is raised if the green value isn't between 0 and 255"""
        with self.assertRaises(ValueError):
            self._colour.green = -10

    def testBlueValueGetter(self):
        """Testing the blue value is returned when you call the blue getter"""
        self.assertEqual(self._colour.blue, 200)

    def testBlueValueSetter(self):
        """Testing if you can update the blue value by calling the blue setter"""
        self._colour.blue = 100
        self.assertEqual(self._colour.blue, 100)

    def testValueErrorIsRaisedIfBlueSetterValueIsNotValid(self):
        """Testing a value error is raised if the blue value isn't between 0 and 255"""
        with self.assertRaises(ValueError):
            self._colour.blue = -10

    def testColourGetter(self):
        """Testing the colour is returned when you call the colour getter"""
        self.assertEqual(self._colour.__str__(), "RGB(200, 200, 200)\nCMYK(0, 0, 0, 22)\n#C8C8C8")


if __name__ == '__main__':
    unittest.main()
