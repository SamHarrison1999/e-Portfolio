import unittest
from Main.Vehicle.Sensor import Sensor


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._sensor = Sensor("Object Sensor")

    def tearDown(self):
        self._sensor = None

    def testValueErrorRaiseIfTheSensorHasNoType(self):
        """Testing value error is raised if the sensor has no type"""
        with self.assertRaises(ValueError):
            self._sensor = Sensor("")

    def testSensorTypeGetter(self):
        """Testing the sensor type is returned when you call the sensor type getter"""
        self.assertEqual(self._sensor.sensor_type, "Object Sensor")

    def testSensorTypeSetter(self):
        """Testing the sensor can be updated by calling the set sensor type function"""
        self._sensor.sensor_type = "Sign Sensor"
        self.assertEqual(self._sensor.sensor_type, "Sign Sensor")

    def testValueErrorRaiseIfTheSensorTypeSetUsingTheTypeSetterIsEmpty(self):
        """Testing a value error is raised if the sensor type set using the set sensor type function and providing no
        type"""
        with self.assertRaises(ValueError):
            self._sensor.sensor_type = ""

    def testGetSensorObject(self):
        """Testing a sensor object"""
        with self.subTest("Sensor Type"):
            self.assertEqual(self._sensor.sensor_type, "Object Sensor")
        with self.subTest("Sensor Object"):
            self.assertEqual(self._sensor.__str__(), "Sensor: Object Sensor")


if __name__ == '__main__':
    unittest.main()
