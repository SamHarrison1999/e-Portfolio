import unittest
from Main.Vehicle.Speed import Speed


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._speed = Speed(150, 5, 70)

    def tearDown(self):
        self._speed = None

    def testValueErrorIsRaisedIfTheVehiclesCurrentSpeedIsLessThanZero(self):
        """Testing a value error is returned if the current speed is less than 0 MPH"""
        with self.assertRaises(ValueError):
            self._speed = Speed(150, 5, -70)

    def testValueErrorIsRaisedIfTheVehiclesTopSpeedIsLessThanZero(self):
        """Testing a value error is returned if the top speed is less than 0 MPH"""
        with self.assertRaises(ValueError):
            self._speed = Speed(-1, 5, 70)

    def testValueErrorIsRaisedIfTheVehiclesAccelerationIsLessThanZero(self):
        """Testing a value error is returned if the 0-60 speed is less than 0 seconds"""
        with self.assertRaises(ValueError):
            self._speed = Speed(150, -5, 70)

    def testTopSpeedGetter(self):
        """Testing the top speed is returned when you call the top speed getter"""
        self.assertEqual(self._speed.top_speed, 150)

    def testTopSpeedSetter(self):
        """Testing if you can update the top speed by calling the top speed setter"""
        self._speed.top_speed = 120
        self.assertEqual(self._speed.top_speed, 120)

    def testValueErrorIsRaisedIfTheTopSpeedSetUsingTheTopSpeedSetterIsLessThanZero(self):
        """Testing a value error is raised if the top speed set using the top speed setter is less than 0"""
        with self.assertRaises(ValueError):
            self._speed.top_speed = -1

    def testAccelerationGetter(self):
        """Testing the 0-60 speed is returned when you call the acceleration getter"""
        self.assertEqual(self._speed.acceleration, 5)

    def testAccelerationSetter(self):
        """Testing the acceleration can be updated by calling the acceleration setter"""
        self._speed.acceleration = 3.5
        self.assertEqual(self._speed.acceleration, 3.5)

    def testValueErrorIsRaisedIfTheAccelerationSetUsingTheAccelerationSetterIsLessThanZero(self):
        """Testing a value error is raised if the acceleration set using the acceleration setter is less than 0"""
        with self.assertRaises(ValueError):
            self._speed.acceleration = -1

    def testingTheCurrentSpeedIsTheTopSpeedIfTheCurrentSpeedIsGreaterThanTheTopSpeed(self):
        """Testing the current speed is the top speed if the current speed set is greater than the top speed"""
        self._speed = Speed(100, 5, 120)
        self.assertEqual(self._speed.current_speed, 100)

    def testCurrentSpeedGetter(self):
        """Testing the current speed is returned when you call the current speed getter"""
        self.assertEqual(self._speed.current_speed, 70)

    def testCurrentSpeedSetter(self):
        """Testing you can update the current speed using the current speed setter"""
        self._speed.current_speed = 50
        self.assertEqual(self._speed.current_speed, 50)

    def testingTheCurrentSpeedSetUsingTheCurrentSpeedSetterIsTheTopSpeedIfTheCurrentSpeedIsGreaterThanTheTopSpeed(self):
        """Testing the current speed is the top speed if the current speed set is greater than the top speed"""
        self._speed = Speed(100, 5, 70)
        self._speed.current_speed = 120
        self.assertEqual(self._speed.current_speed, 100)

    def testValueErrorIsRaisedIfTheCurrentSpeedSetUsingTheCurrentSpeedSetterIsLessThanZero(self):
        """Testing a value error is raised if the current speed set using the current speed setter is less than 0"""
        with self.assertRaises(ValueError):
            self._speed.current_speed = -1

    def testSpeedObject(self):
        with self.subTest("Top Speed"):
            self.assertEqual(self._speed.top_speed, 150)
        with self.subTest("Current Speed"):
            self.assertEqual(self._speed.current_speed, 70)
        with self.subTest("Acceleration"):
            self.assertEqual(self._speed.acceleration, 5)
        with self.subTest("Speed Object"):
            self.assertEqual(self._speed.__str__(), "Current Speed: 70MPH\n"
                                                    "Top Speed: 150MPH\n"
                                                    "0-60 MPH Speed: 5 seconds ")

    def testAccelerate(self):
        """Testing the accelerate speeds up the car if the current speed is less than the top speed when the
        accelerate method is called"""
        self._speed.accelerate()
        self.assertEqual(self._speed.current_speed, 71)

    def testDecelerate(self):
        """Testing the decelerate slows down the car if the current speed is greater than zero when the decelerate
        method is called"""
        self._speed.decelerate()
        self.assertEqual(self._speed.current_speed, 69)


if __name__ == '__main__':
    unittest.main()
