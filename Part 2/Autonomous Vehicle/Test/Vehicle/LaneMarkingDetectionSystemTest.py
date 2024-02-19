import unittest
from Main.Vehicle.LaneMarkingDetectionSystem import LaneMarkingDetectionSystem


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._lane_marking_detection_system = LaneMarkingDetectionSystem(5, 0)

    def tearDown(self):
        self._lane_marking_detection_system = None

    def testLeftDistanceGetter(self):
        """Testing the distance from the left lane marking is returned when you call the left distance getter"""
        self.assertEqual(self._lane_marking_detection_system.left_distance, 5)

    def testLeftDistanceSetter(self):
        """Testing you can change the distance from the left lane marking by calling the left distance setter"""
        self._lane_marking_detection_system.left_distance = 0
        self.assertEqual(self._lane_marking_detection_system.left_distance, 0)

    def testRightDistanceGetter(self):
        """Testing the distance from the right lane marking is returned when you call the right distance getter"""
        self.assertEqual(self._lane_marking_detection_system.right_distance, 0)

    def testRightDistanceSetter(self):
        """Testing you can change the distance from the right lane marking by calling the right distance setter"""
        self._lane_marking_detection_system.right_distance = 10
        self.assertEqual(self._lane_marking_detection_system.right_distance, 10)

    def testGetLaneMarkingDetectionSystemObjectForVehicleInTheLane(self):
        """Testing you can get the lane marking detection object when the vehicle is in the lane"""
        with self.subTest("Left Distance"):
            self.assertEqual(self._lane_marking_detection_system.left_distance, 5)
        with self.subTest("Right Distance"):
            self.assertEqual(self._lane_marking_detection_system.right_distance, 0)
        with self.subTest("In Lane"):
            self.assertEqual(self._lane_marking_detection_system.in_lane(), True)
        with self.subTest("Lane Marking Detection Object"):
            self.assertEqual(self._lane_marking_detection_system.__str__(),
                             "Distance from left lane marking: 5 Meters\n"
                             "Distance from right lane marking: 0 Meters\n"
                             "In Lane")

    def testGetLaneMarkingDetectionSystemObjectForVehicleNotInTheLane(self):
        """Testing you can get the lane marking detection object when the vehicle is not in the lane"""
        self._lane_marking_detection_system.right_distance = -10
        with self.subTest("Left Distance"):
            self.assertEqual(self._lane_marking_detection_system.left_distance, 5)
        with self.subTest("Right Distance"):
            self.assertEqual(self._lane_marking_detection_system.right_distance, -10)
        with self.subTest("In Lane"):
            self.assertEqual(self._lane_marking_detection_system.in_lane(), False)
        with self.subTest("Lane Marking Detection Object"):
            self.assertEqual(self._lane_marking_detection_system.__str__(),
                             "Distance from left lane marking: 5 Meters\n"
                             "Distance from right lane marking: -10 Meters\n"
                             "Not In Lane")

    def testInLaneForVehicleInLane(self):
        """Testing if the vehicle is in the lane the in lane function returns true"""
        self.assertEqual(self._lane_marking_detection_system.in_lane(), True)

    def testInLaneForVehicleNotInLane(self):
        """Testing if the vehicle is not in the lane the in lane function returns false"""
        self._lane_marking_detection_system = LaneMarkingDetectionSystem(5, -10)
        self.assertEqual(self._lane_marking_detection_system.in_lane(), False)


if __name__ == '__main__':
    unittest.main()
