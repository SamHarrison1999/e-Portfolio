import unittest
from Main.Vehicle.Contact import Contact


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._contact = Contact("Test", "Contact", "+447123456789")

    def tearDown(self):
        self._contact = None

    def testValueErrorIsRaisedIfTheContactsFirstNameIsBlank(self):
        """Testing a value error is raised if the contacts first name is empty"""
        with self.assertRaises(ValueError):
            self._contact = Contact("", "Contact", "+447123456789")

    def testValueErrorIsRaisedIfTheContactsLastNameIsBlank(self):
        """Testing a value error is raised if the contacts last name is empty"""
        with self.assertRaises(ValueError):
            self._contact = Contact("Test", "", "+447123456789")

    def testValueErrorIsRaisedIfTheContactsPhoneNumberIsNotValid(self):
        """Testing a value error is raised if the contacts phone number isn't valid"""
        with self.assertRaises(ValueError):
            self._contact = Contact("Test", "Contact", "012345678910")

    def testFirstNameGetter(self):
        """Testing the contacts first name is returned when you call the first name getter"""
        self.assertEqual(self._contact.first_name, "Test")

    def testFirstNameSetter(self):
        """Testing if you can update the contacts first name by calling the first name setter"""
        self._contact.first_name = "New"
        self.assertEqual(self._contact.first_name, "New")

    def testValueErrorIsRaisedIfTheContactsFirstNameSetUsingTheFirstNameSetterIsBlank(self):
        """Testing a value error is raised if the contacts first name set using the first name setter is empty"""
        with self.assertRaises(ValueError):
            self._contact.first_name = ""

    def testLastNameGetter(self):
        """Testing the contacts last name is returned when you call the last name getter"""
        self.assertEqual(self._contact.last_name, "Contact")

    def testLastNameSetter(self):
        """Testing if you can update the contacts last name by calling the last name setter"""
        self._contact.last_name = "Contact 2"
        self.assertEqual(self._contact.last_name, "Contact 2")

    def testValueErrorIsRaisedIfTheContactsLastNameSetUsingTheLastNameSetterIsBlank(self):
        """Testing a value error is raised if the contacts last name set using the last name setter is empty"""
        with self.assertRaises(ValueError):
            self._contact.last_name = ""

    def testContactNumberGetter(self):
        """Testing the contacts phone number is returned when you call the phone number getter"""
        self.assertEqual(self._contact.contact_number, "+447123456789")

    def testContactNumberSetter(self):
        """Testing if you can update the contacts phone number by calling the phone number setter"""
        self._contact.contact_number = "+447987654321"
        self.assertEqual(self._contact.contact_number, "+447987654321")

    def testValueErrorIsRaisedIfTheContactsPhoneNumberSetUsingTheContactNumberSetterIsNotValid(self):
        """Testing a value error is raised if the contacts phone number set using the contact number setter isn't a
        valid number"""
        with self.assertRaises(ValueError):
            self._contact.contact_number = "012345678910"

    def testGetContactObject(self):
        """Testing you can get the contact object"""
        with self.subTest("Contact"):
            self.assertEqual(self._contact.__str__(), "First Name: Test\n"
                                                      "Last Name: Contact\n"
                                                      "Contact Number: +447123456789")
        with self.subTest("First Name"):
            self.assertEqual(self._contact.first_name, "Test")
        with self.subTest("Last Name"):
            self.assertEqual(self._contact.last_name, "Contact")
        with self.subTest("Phone Number"):
            self.assertEqual(self._contact.contact_number, "+447123456789")


if __name__ == '__main__':
    unittest.main()
