import unittest
from Main.Vehicle.Steering import Steering


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # The set-up method is run before every test case
        self._steering = Steering(50)

    def tearDown(self):
        self._steering = None

    def testWheelRotationGetter(self):
        """Testing the wheel rotation is returned when you call the wheel rotation getter"""
        self.assertEqual(self._steering.wheel_rotation, 50)

    def testWheelRotationSetter(self):
        """Testing you can update the wheel rotation by calling the wheel rotation setter"""
        self._steering.wheel_rotation = 100
        self.assertEqual(self._steering.wheel_rotation, 100)

    def testTurnSteeringWheelLeft(self):
        """Testing the turn wheel left function"""
        self._steering.turn_steering_wheel_left(100)
        self.assertEqual(self._steering.wheel_rotation, -50)

    def testTurnSteeringWheelRight(self):
        """Testing the turn wheel right function"""
        self._steering.turn_steer_wheel_right(200)
        self.assertEqual(self._steering.wheel_rotation, 250)

    def testStraightenUp(self):
        """Testing straighten up method sets the wheel rotation to 0 degree"""
        self._steering.straighten_up()
        self.assertEqual(self._steering.wheel_rotation, 0)

    def testSteeringObject(self):
        """Testing thr steering object"""
        with self.subTest("Wheel Rotation"):
            self.assertEqual(self._steering.wheel_rotation, 50)
        with self.subTest("Steering Object"):
            self.assertEqual(self._steering.__str__(), "Wheel rotation: 50 degrees")


if __name__ == '__main__':
    unittest.main()
