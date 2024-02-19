import unittest
from unittest import mock

from Main.People.Person import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._driver = Driver("admin", "Qwerty1!", {"heart rate": 100, "blood pressure": 50, "pulse": 30})
        self._passenger = Passenger({"heart rate": 100, "blood pressure": 50, "pulse": 30})

    def tearDown(self):
        self._driver = None
        self._passenger = None

    def testValueErrorIsRaisedIfTheUsernameIsEmpty(self):
        """Testing a value error is raised if the username is empty"""
        with self.assertRaises(ValueError):
            self._driver = Driver("", "Qwerty1!", {"heart rate": 100, "blood pressure": 50, "pulse": 30})

    def testValueErrorIsRaisedIfThePasswordDoesNotMeetThePasswordRequirements(self):
        """Testing a value error is raised if the password doesn't meet the password requirements"""
        with self.assertRaises(ValueError):
            self._driver = Driver("admin", "password", {"heart rate": 100, "blood pressure": 50, "pulse": 30})

    def testValueErrorIsRaisedIfAnyOfTheDriversVitalsAreBelowZero(self):
        """Testing a value error is raised if any of the drivers vitals are below zero"""
        with self.assertRaises(ValueError):
            self._driver = Driver("admin", "Qwerty1!", {"heart rate": -100, "blood pressure": -50, "pulse": -30})

    def testUsernameGetter(self):
        """Testing the drivers username is returned when you call the username getter"""
        self.assertEqual(self._driver.username, "admin")

    def testUsernameSetter(self):
        """Testing you can update the drivers username by calling the username setter"""
        self._driver.username = "driver"
        self.assertEqual(self._driver.username, "driver")

    def testValueErrorIsRaisedIfTheUsernameSetUsingTheUsernameSetterIsEmpty(self):
        """Testing a value error is raised if you try to set the username to an empty string using the username
        setter"""
        with self.assertRaises(ValueError):
            self._driver.username = ""

    def testPasswordGetter(self):
        """Testing the password is returned when you call the password getter"""
        self.assertEqual(self._driver.password, "Qwerty1!")

    def testPasswordSetter(self):
        """Testing you can update the drivers password by calling the password setter"""
        self._driver.password = "Password1!"
        self.assertEqual(self._driver.password, "Password1!")

    def testValueErrorIsRaisedIfThePasswordSetUsingThePasswordSetterDoesNotMeetThePasswordRequirements(self):
        """Testing a value error is raised if password doesn't meet the password requirements"""
        with self.assertRaises(ValueError):
            self._driver.password = "password"

    def testDriverVitalsGetter(self):
        """Testing the vitals are returned when you call the vitals getter"""
        self.assertEqual(self._driver.vitals, {"heart rate": 100, "blood pressure": 50, "pulse": 30})

    def testDriverVitalsSetter(self):
        """Testing you can update the vitals by calling the vitals setter"""
        self._driver.vitals = {"heart rate": 10}
        self.assertEqual(self._driver.vitals, {"heart rate": 10})

    def testValueErrorIsRaisedIfAnyOfTheDriversVitalsSetUsingTheVitalsSetterAreBelowZero(self):
        """Testing a value error is raised if any of the driver vitals are below zero"""
        with self.assertRaises(ValueError):
            self._driver.vitals = {"heart rate": -10}

    def testDriverObject(self):
        """Testing the driver object"""
        with self.subTest("Username"):
            self.assertEqual(self._driver.username, "admin")
        with self.subTest("Password"):
            self.assertEqual(self._driver.password, "Qwerty1!")
        with self.subTest("Vitals"):
            self.assertEqual(self._driver.vitals, {"heart rate": 100, "blood pressure": 50, "pulse": 30})
        with self.subTest("Driver Object"):
            self.assertEqual(self._driver.__str__(), "Driver:\nUsername: admin\nPassword: Qwerty1!\n"
                                                     "heart rate: 100\nblood pressure: 50\npulse: 30")

    @mock.patch('getpass.getpass')
    @mock.patch('getpass.getuser')
    def testLogin(self, getuser, getpw):
        getuser.return_value = "admin"
        getpw.return_value = "Qwerty1!"
        self.assertEqual(True, self._driver.login())

    def testValueErrorIsRaisedIfAnyOfThePassengersVitalsAreBelowZero(self):
        """Testing a value error is raised if any of the passengers vitals are below zero"""
        with self.assertRaises(ValueError):
            self._passenger = Passenger({"heart rate": -100, "blood pressure": -50, "pulse": -30})

    def testPassengerVitalsGetter(self):
        """Testing the vitals are returned when you call the vitals getter"""
        self.assertEqual(self._passenger.vitals, {"heart rate": 100, "blood pressure": 50, "pulse": 30})

    def testPassengerVitalsSetter(self):
        """Testing you can update the vitals by calling the vitals setter"""
        self._passenger.vitals = {"heart rate": 10}
        self.assertEqual(self._passenger.vitals, {"heart rate": 10})

    def testValueErrorIsRaisedIfAnyOfThePassengersVitalsSetUsingTheVitalsSetterAreBelowZero(self):
        """Testing a value error is raised if any of the passengers vitals are below zero"""
        with self.assertRaises(ValueError):
            self._passenger.vitals = {"heart rate": -10}

    def testPassengerObject(self):
        """Testing the driver object"""
        with self.subTest("Vitals"):
            self.assertEqual(self._passenger.vitals, {"heart rate": 100, "blood pressure": 50, "pulse": 30})
        with self.subTest("Passenger Object"):
            self.assertEqual(self._passenger.__str__(), "Passenger:\nheart rate: 100\nblood pressure: 50\npulse: 30")


if __name__ == '__main__':
    unittest.main()
