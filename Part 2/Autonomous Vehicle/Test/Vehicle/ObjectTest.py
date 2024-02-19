import unittest
from Main.Vehicle.Object import Object


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._size_of_cone = dict()
        self._size_of_cone["length"] = 5
        self._size_of_cone["width"] = 5
        self._size_of_cone["height"] = 10
        self._cone = Object("Cone", self._size_of_cone, 1, 5, 10)

    def tearDown(self):
        self._size_of_cone = None
        self._cone = None

    def testValueErrorIsRaisedIfTheObjectHasNoName(self):
        """Testing a value error is raised for an object without a name"""
        with self.assertRaises(ValueError):
            Object(None, self._size_of_cone, 1, 5, 10)

    def testValueErrorIsRaisedIfAnyOfTheObjectDimensionsAreNegative(self):
        """Testing a value error is raised if any of the objects dimensions are negative"""
        with self.assertRaises(ValueError):
            self._size_of_cone = dict()
            self._size_of_cone["length"] = -5
            self._size_of_cone["width"] = -5
            self._size_of_cone["height"] = -10
            self._cone = Object("Cone", self._size_of_cone, 1, 5, 10)

    def testValueErrorIsRaisedIfTheObjectIsANegativeNumberOfMetersAway(self):
        """Testing a value error is raised if the object is a negative number of meters away"""
        with self.assertRaises(ValueError):
            self._cone = Object("Cone", self._size_of_cone, 1, -5, 10)

    def testValueErrorIsRaisedIfTheObjectIsANegativeNumberOfSecondsAway(self):
        """Testing a value error is raised if the object is a negative number of seconds away"""
        with self.assertRaises(ValueError):
            self._cone = Object("Cone", self._size_of_cone, 1, 5, -10)

    def testObjectNameGetter(self):
        """Testing the object name is returned when you call the name getter"""
        self.assertEqual(self._cone.name, "Cone")

    def testObjectNameSetter(self):
        """Testing if you can update the name of the object by calling the name setter"""
        self._cone = Object("Rubbish", self._size_of_cone, 1, 5, 10)
        self._cone.name = "Cone"
        self.assertEqual(self._cone.name, "Cone")

    def testValueErrorIsRaisedIfTheObjectHasNoNameSetWithTheNameSetter(self):
        """Testing a value error is raised when you try to update the object name to none"""
        with self.assertRaises(ValueError):
            self._cone.name = None

    def testObjectDimensionsGetter(self):
        """Testing the objects dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._cone.dimensions, {"length": 5, "width": 5, "height": 10})

    def testObjectDimensionsSetter(self):
        """Testing if you can update the dimensions of the object by calling the dimensions setter"""
        self._cone.dimensions = {"length": 10, "width": 10, "height": 5}
        self.assertEqual(self._cone.dimensions, {"length": 10, "width": 10, "height": 5})

    def testValueErrorIsRaisedIfAnyOfTheObjectDimensionsSetUsingTheDimensionsSetterAreNegative(self):
        """Testing a value error is raised when you try to update an objects dimensions to negative dimensions using
        the dimensions setter"""
        with self.assertRaises(ValueError):
            self._cone.dimensions = {"length": -10, "width": -10, "height": -5}

    def testLaneGetterIfObjectIsInTheRoad(self):
        """Testing the correct lane is returned when you call the lane getter if the object is in the road"""
        self.assertEqual(self._cone.lane_object_is_in, 1)

    def testLaneGetterIfObjectIsNotInTheRoad(self):
        """Testing the lane returned is none when you call the lane getter if the object is not in the road"""
        self._cone = Object("Cone", self._size_of_cone, -1, 5, 10)
        self.assertEqual(self._cone.lane_object_is_in, None)

    def testLaneSetter(self):
        """Testing if you can update the lane an object is in if the object is in the road by calling the lane setter"""
        self._cone.lane_object_is_in = 2
        self.assertEqual(self._cone.lane_object_is_in, 2)

    def testLaneSetterWhenObjectIsNotInTheRoad(self):
        """Testing if update the lane the object is in using the lane setter to the object not being in the road
        correctly sets the lane the object in as none"""
        self._cone.lane_object_is_in = -1
        self.assertEqual(self._cone.lane_object_is_in, None)

    def testGetDistanceToObjectIfObjectIsInTheRoad(self):
        """Testing the distance to the object is returned when you call the distance getter when the object is in the
        road"""
        self.assertEqual(self._cone.distance_to_object, 5)

    def testGetDistanceToObjectIfObjectIsNotInTheRoad(self):
        """Testing the distance to the object is none when you call the distance getter when the object is not in the
        road as it can be ignored"""
        self._cone = Object("Cone", self._size_of_cone, -1, 5, 10)
        self.assertEqual(self._cone.distance_to_object, None)

    def testDistanceToObjectSetter(self):
        """Testing you can update the distance to the object if the lane is in the road by calling the distance
        setter"""
        self._cone.distance_to_object = 10
        self.assertEqual(self._cone.distance_to_object, 10)

    def testDistanceToObjectSetterWhenTheObjectIsNotInTheRoad(self):
        """Testing the distance to the object is None if the object isn't in the road even if you try setting it
        using the distance setter"""
        self._cone = Object("Cone", self._size_of_cone, -1, 5, 10)
        self._cone.distance_to_object = 10
        self.assertEqual(self._cone.distance_to_object, None)

    def testValueErrorIsRaisedIfTheDistanceToTheObjectSetUsingTheDistanceSetterIsANegativeNumber(self):
        """Testing a value error is raised if you try to update the distance to the object to a negative number using
        the distance setter"""
        with self.assertRaises(ValueError):
            self._cone.distance_to_object = -10

    def testGetTimeUntilCollisionWithObjectAtCurrentSpeedIfTheObjectIsInTheRoad(self):
        """Testing the time until collision with the object is returned if you call the time until collision getter
        and the object is in the road"""
        self.assertEqual(self._cone.time_until_impact_with_object, 10)

    def testGetTimeUntilCollisionWithObjectAtCurrentSpeedIfTheObjectIsNotInTheRoad(self):
        """Testing the time until collision with the object is none if you call the time until collision getter when
        the object is not in the road"""
        self._cone = Object("Cone", self._size_of_cone, -1, 5, 10)
        self.assertEqual(self._cone.time_until_impact_with_object, None)

    def testTimeUntilCollisionWithObjectAtCurrentSpeedSetter(self):
        """Testing you can update the time until collision if the object is in the road using the time until
        collision setter"""
        self._cone.time_until_impact_with_object = 5
        self.assertEqual(self._cone.time_until_impact_with_object, 5)

    def testTimeUntilCollisionWithObjectAtCurrentSpeedSetterWhenTheObjectIsNotInTheRoad(self):
        """Testing you can't update the time until collision if the object is not in the road"""
        self._cone = Object("Cone", self._size_of_cone, -1, 5, 10)
        self._cone.time_until_impact_with_object = 20
        self.assertEqual(self._cone.time_until_impact_with_object, None)

    def testValueErrorIsRaisedIfTheTimeUntilCollisionWithObjectAtCurrentSpeedSetUsingTimeUntilCollisionWithObjectAtCurrentSpeedSetterIsANegativeNumber(self):
        """Testing a value error is raised when you try to set the time until collision to a negative number using
        the time until collision setter"""
        with self.assertRaises(ValueError):
            self._cone.time_until_impact_with_object = -10

    def testObject(self):
        """Testing the object 'object'"""
        with self.subTest("Name"):
            self.assertEqual(self._cone.name, "Cone")
        with self.subTest("Dimensions"):
            self.assertEqual(self._cone.dimensions, {"length": 5, "width": 5, "height": 10})
        with self.subTest("Lane"):
            self.assertEqual(self._cone.lane_object_is_in, 1)
        with self.subTest("Distance To Object"):
            self.assertEqual(self._cone.distance_to_object, 5)
        with self.subTest("Time Until Collision With Object"):
            self.assertEqual(self._cone.time_until_impact_with_object, 10)
        with self.subTest("Object"):
            self.assertEqual(self._cone.__str__(), "Object Name: Cone\n"
                                                   "Object Dimensions:\n"
                                                   "Length: 5 Meters\n"
                                                   "Width: 5 Meters\n"
                                                   "Height: 10 Meters\n"
                                                   "Object in Lane 1\n"
                                                   "Distance to object: 5 Meters\n"
                                                   "Time until impact with object at current speed: 10 Seconds")


if __name__ == '__main__':
    unittest.main()
