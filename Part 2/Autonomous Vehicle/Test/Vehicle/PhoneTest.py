import unittest

from Main.Vehicle.Message import Message
from Main.Vehicle.Phone import Phone
from Main.Vehicle.Contact import Contact


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # The set-up method is run before each test case
        self._emergency_contact = Contact("Emergency", "Contact", "+447987654321")
        self._phone = Phone("+447123456789", self._emergency_contact, [self._emergency_contact], [])

    def tearDown(self):
        self._emergency_contact = None
        self._phone = None

    def testValueErrorIsRaisedIfTheContactsPhoneNumberIsNotValid(self):
        """Testing a value error is raised if the drivers phone number isn't valid"""
        with self.assertRaises(ValueError):
            self._phone = Phone("012345678910", self._emergency_contact, [self._emergency_contact], [])

    def testPhoneWithoutContacts(self):
        """Testing the contacts list is empty if not provided"""
        self._phone = Phone("+447123456789", self._emergency_contact, None, [])
        self.assertEqual(self._phone.contacts, [])

    def testPhoneWithoutMessages(self):
        """Testing the messages list is empty if not provided"""
        self._phone = Phone("+447123456789", self._emergency_contact, [], None)
        self.assertEqual(self._phone.messages, [])

    def testContactNumberGetter(self):
        """Testing the drivers phone number is returned when you call the phone number getter"""
        self.assertEqual(self._phone.phone_number, "+447123456789")

    def testContactNumberSetter(self):
        """Testing if you can update the drivers phone number by calling the phone number setter"""
        self._phone.phone_number = "+447987654321"
        self.assertEqual(self._phone.phone_number, "+447987654321")

    def testValueErrorIsRaisedIfTheContactsPhoneNumberSetUsingTheContactNumberSetterIsNotValid(self):
        """Testing a value error is raised if the drivers phone number set using the contact number setter isn't a
        valid number"""
        with self.assertRaises(ValueError):
            self._phone.phone_number = "012345678910"

    def testEmergencyContactGetter(self):
        """Testing the drivers emergency contact is returned when you call the emergency contact getter"""
        self.assertEqual(str(self._phone.emergency_contact),
                         "First Name: Emergency\n"
                         "Last Name: Contact\n"
                         "Contact Number: +447987654321")

    def testEmergencyContactSetter(self):
        """Testing if you can update the drivers emergency contact by calling the emergency contact setter"""
        self._phone.emergency_contact = Contact("New", "Contact", "+447543907631")

    def testContactsGetter(self):
        """Testing the contacts list is returned when you call the contacts getter"""
        self.assertEqual(self._phone.contacts[0], self._emergency_contact)

    def testContactsSetter(self):
        """Testing if you can update the list of contacts by calling the contacts setter"""
        self._phone.contacts = [Contact("New", "Contact", "+447543907631")]
        self.assertEqual(self._phone.contacts[0].__str__(), "First Name: New\n"
                                                            "Last Name: Contact\n"
                                                            "Contact Number: +447543907631")

    def testSettingNoContacts(self):
        """Testing the contacts list is empty if not provided"""
        self._phone.contacts = None
        self.assertEqual(self._phone.contacts, [])

    def testMessagesGetter(self):
        """Testing the message list is returned when you call the messages getter"""
        self.assertEqual(self._phone.messages, [])

    def testMessagesSetter(self):
        """Testing if you can update the list of messages by calling the messages setter"""
        self._phone = Phone("+447123456789",
                            self._emergency_contact,
                            [self._emergency_contact],
                            [Message(self._emergency_contact,
                                     Contact("Message",
                                             "Receiver",
                                             "+447123456789"),
                                     "Hi")])
        sender = Contact("Message", "Sender", "+447123456789")
        receiver = Contact("Message", "Receiver", "+447987654321")
        self._phone.messages = [Message(sender, receiver, "First Message"), Message(sender, receiver, "Second Message")]
        self.assertEqual(self._phone.messages[0].__str__().__contains__("First Message"), True)
        self.assertEqual(self._phone.messages[1].__str__().__contains__("Second Message"), True)

    def testPhoneWithoutMessagesUsingMessagesSetter(self):
        """Testing the messages list is empty if not provided"""
        self._phone.messages = None
        self.assertEqual(self._phone.messages, [])

    def testGetPhoneObject(self):
        """Testing getting the phone object"""
        with self.subTest("Phone Number"):
            self.assertEqual(self._phone.phone_number, "+447123456789")
        with self.subTest("Emergency Contact First Name"):
            self.assertEqual(self._phone.emergency_contact.first_name, "Emergency")
        with self.subTest("Emergency Contact Last Name"):
            self.assertEqual(self._phone.emergency_contact.last_name, "Contact")
        with self.subTest("Emergency Contact Contact Number"):
            self.assertEqual(self._phone.emergency_contact.contact_number, "+447987654321")
        with self.subTest("Contacts List"):
            self.assertEqual(str(self._phone.contacts[0]),
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321")
        with self.subTest("Messages List"):
            self.assertEqual(self._phone.messages, [])
        with self.subTest("Phone Object As A String"):
            self.assertEqual(self._phone.__str__(),
                             "Phone Number: +447123456789\n"
                             "Emergency Contact:\n"
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Contacts:\n"
                             "Contact 1:\n"
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Messages:")

    def testCallEmergencyServices(self):
        """Testing the call emergency services static method"""
        self.assertEqual(Phone.call_emergency_services(), "Calling Emergency Services")

    def testCallEmergencyContact(self):
        """Testing the call emergency contact method"""
        self._phone = Phone("+447123456789", self._emergency_contact, [self._emergency_contact], [])
        self.assertEqual(self._phone.call_emergency_contact(),
                         "Calling Emergency Contact\n"
                         "First Name: Emergency\n"
                         "Last Name: Contact\n"
                         "Contact Number: +447987654321")


if __name__ == '__main__':
    unittest.main()
