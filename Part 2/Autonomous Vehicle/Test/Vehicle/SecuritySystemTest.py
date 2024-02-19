import unittest
from Main.Vehicle.SecuritySystem import SecuritySystem


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # Set up method is run before every test case
        self._security_system = SecuritySystem(True, False)

    def tearDown(self) -> None:
        self._security_system = None

    def testAlarmGetter(self):
        """Testing the alarm status is returned when you call the armed getter"""
        self.assertEqual(self._security_system.armed, True)

    def testAlarmIsNotActivatedIfNoAlarmStatusIsDefined(self):
        """Testing the alarm is not armed if the security system has no alarm status"""
        self._security_system = SecuritySystem(None, False)
        self.assertEqual(self._security_system.armed, False)

    def testAlarmSetter(self):
        """Testing the alarm status can be updated by calling the armed setter"""
        self._security_system.armed = False
        self.assertEqual(self._security_system.armed, False)

    def testAlarmIsNotActivatedIfNoAlarmStatusIsDefinedUsingTheArmedSetter(self):
        """Testing the alarm is not armed if you try to set the armed status to None"""
        self._security_system.armed = None
        self.assertEqual(self._security_system.armed, False)

    def testLockedGetter(self):
        """Testing the locked status is returned when you call the locked getter"""
        self.assertEqual(self._security_system.locked, False)

    def testVehicleIsNotLockedIfNoLockedStatusIsDefined(self):
        """Testing the locked status is false if the locked status is none"""
        self._security_system = SecuritySystem(True, None)
        self.assertEqual(self._security_system.locked, False)

    def testLockedSetter(self):
        """Testing if you can update the locked status by calling the locked setter"""
        self._security_system.locked = True
        self.assertEqual(self._security_system.locked, True)

    def testVehicleIsNotLockedIfNoLockStatusIsDefinedUsingTheLockedSetter(self):
        """Testing the locked status is false if you set the locked status to none"""
        self._security_system = SecuritySystem(True, True)
        self._security_system.locked = None
        self.assertEqual(self._security_system.locked, False)

    def testTriggeredGetter(self):
        """Testing the triggered status is returned when you call the triggered getter"""
        self.assertEqual(self._security_system.triggered, False)

    def testTriggeredSetter(self):
        """Testing the triggered status can be updated by calling the triggered status setter"""
        self._security_system.triggered = True
        self.assertEqual(self._security_system.triggered, True)

    def testActivateAlarm(self):
        """Testing activating the alarm"""
        self._security_system = SecuritySystem(False, True)
        self._security_system.arm_security_system()
        self.assertEqual(self._security_system.armed, True)

    def testDeactivateAlarm(self):
        """Testing deactivating the alarm"""
        self._security_system = SecuritySystem(True, True)
        self._security_system.disarm_security_system()
        self.assertEqual(self._security_system.armed, False)

    def testLockVehicle(self):
        """Testing locking the vehicle"""
        self._security_system = SecuritySystem(False, False)
        self._security_system.lock_vehicle()
        self.assertEqual(self._security_system.locked, True)

    def testUnlockVehicle(self):
        """Testing unlocking the vehicle"""
        self._security_system = SecuritySystem(False, True)
        self._security_system.unlock_vehicle()
        self.assertEqual(self._security_system.locked, False)

    def testAlarmTriggered(self):
        """Testing triggering the alarm"""
        self._security_system = SecuritySystem(True, False)
        self._security_system.alarm_triggered()
        self.assertEqual(self._security_system.triggered, True)
        self.assertEqual(self._security_system.locked, True)

    def testAlarmNotTriggeredIfAlarmIsNotActivated(self):
        """Testing triggering the alarm when the alarm is not activate"""
        self._security_system = SecuritySystem(False, False)
        self._security_system.alarm_triggered()
        self.assertEqual(self._security_system.triggered, False)
        self.assertEqual(self._security_system.locked, False)
        self.assertEqual(self._security_system.armed, False)

    def testSecuritySystemObject(self):
        """Testing security system object"""
        self._security_system = SecuritySystem(True, True)
        self.assertEqual(self._security_system.__str__(), "Alarm Status: Alarm Activated\n"
                                                          "Vehicle locked\n"
                                                          "Alarm Not Triggered")


if __name__ == '__main__':
    unittest.main()
