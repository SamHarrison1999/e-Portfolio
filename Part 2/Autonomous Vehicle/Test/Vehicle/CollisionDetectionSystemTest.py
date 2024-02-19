import unittest

from Main.Vehicle.CollisionDetectionSystem import CollisionDetectionSystem


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # The set-up method is run before each test case
        self._collision_detection = CollisionDetectionSystem(False, False, False)

    def tearDown(self) -> None:
        self._collision_detection = None

    def testEmergencyStop(self):
        """Testing an emergency stop after a collision."""
        self._collision_detection.emergency_stop()
        with self.subTest("Testing handbrake is engaged after an emergency stop"):
            self.assertEqual(self._collision_detection.handbrake_engaged, True)
        with self.subTest("Testing hazard lights are on after an emergency stop"):
            self.assertEqual(self._collision_detection.hazard_lights_turned_on, True)

    def testCollisionOccurredGetter(self):
        """Testing the collision status is returned when you call the collision occurred getter"""
        self.assertEqual(self._collision_detection.collision_occurred, False)

    def testCollisionOccurredSetter(self):
        """Testing if you can update the collision status by calling the collision occurred setter"""
        self._collision_detection.collision_occurred = True
        self.assertEqual(self._collision_detection.collision_occurred, True)

    def testHandbrakeEngageGetter(self):
        """Testing the handbrake status is returned when you call the handbrake engaged getter"""
        self.assertEqual(self._collision_detection.handbrake_engaged, False)

    def testHandbrakeEngageSetter(self):
        """Testing if you can update the handbrake status by calling the handbrake engaged setter"""
        self._collision_detection.handbrake_engaged = True
        self.assertEqual(self._collision_detection.handbrake_engaged, True)

    def testHazardLightsTurnedOnGetter(self):
        """Testing the hazard light status is returned when you call the hazard lights turned on getter"""
        self.assertEqual(self._collision_detection.hazard_lights_turned_on, False)

    def testHazardLightsTurnedOnSetter(self):
        """Testing if you can update the hazard light status by calling the hazard lights turned on setter"""
        self._collision_detection.hazard_lights_turned_on = True
        self.assertEqual(self._collision_detection.hazard_lights_turned_on, True)

    def testCollisionDetectionGetter(self):
        """Testing if you can get the collision detection object"""
        self.assertEqual(self._collision_detection.__str__(), "No Collision Detected\n"
                                                              "Handbrake not engaged\n"
                                                              "Hazard Lights Off")


if __name__ == '__main__':
    unittest.main()
