import unittest

from Main.Vehicle.Contact import Contact
from Main.Vehicle.InfotainmentSystem import InfotainmentSystem
from Main.Vehicle.Radio import Radio
from Main.Vehicle.Phone import Phone


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # The set-up method is run before each test case
        self._emergency_contact = Contact("Emergency", "Contact", "+447987654321")
        self._phone = Phone("+447123456789", self._emergency_contact, [], [])
        self._radio = Radio("Capital", 95.8, None)
        self._infotainment_system = InfotainmentSystem(self._phone, self._radio, "English")

    def tearDown(self) -> None:
        self._emergency_contact = None
        self._phone = None
        self._radio = None
        self._infotainment_system = None

    def testValueErrorRaisedIfTheInfotainmentSystemHasNoLanguage(self):
        """Testing a value error is raised if no language has been set"""
        with self.assertRaises(ValueError):
            self._infotainment_system = InfotainmentSystem(self._phone, self._radio, "")

    def testPhoneGetter(self):
        """Testing a phone object is returned when you call the phone getter"""
        with self.subTest("Phone Number"):
            self.assertEqual(self._infotainment_system.phone.phone_number, "+447123456789")
        with self.subTest("Emergency Contact First Name"):
            self.assertEqual(self._infotainment_system.phone.emergency_contact.first_name, "Emergency")
        with self.subTest("Emergency Contact Last Name"):
            self.assertEqual(self._infotainment_system.phone.emergency_contact.last_name, "Contact")
        with self.subTest("Emergency Contact Contact Number"):
            self.assertEqual(self._infotainment_system.phone.emergency_contact.contact_number, "+447987654321")
        with self.subTest("Contacts List"):
            self.assertEqual(self._infotainment_system.phone.contacts, [])
        with self.subTest("Messages List"):
            self.assertEqual(self._infotainment_system.phone.messages, [])

    def testPhoneSetter(self):
        """Testing if you can update the phone object by calling the phone setter"""
        self._infotainment_system.phone = Phone("+447987654321",
                                                Contact("Emergency", "Contact", "+447432674965"), [], [])
        with self.subTest("Phone Number"):
            self.assertEqual(self._infotainment_system.phone.phone_number, "+447987654321")
        with self.subTest("Emergency Contact First Name"):
            self.assertEqual(self._infotainment_system.phone.emergency_contact.first_name, "Emergency")
        with self.subTest("Emergency Contact Last Name"):
            self.assertEqual(self._infotainment_system.phone.emergency_contact.last_name, "Contact")
        with self.subTest("Emergency Contact Contact Number"):
            self.assertEqual(self._infotainment_system.phone.emergency_contact.contact_number, "+447432674965")
        with self.subTest("Contacts List"):
            self.assertEqual(self._infotainment_system.phone.contacts, [])
        with self.subTest("Messages List"):
            self.assertEqual(self._infotainment_system.phone.messages, [])

    def testRadioGetter(self):
        """Testing a radio object is returned when you call the radio getter"""
        with self.subTest("Station Name"):
            self.assertEqual(self._infotainment_system.radio.station_name, "Capital")
        with self.subTest("FM"):
            self.assertEqual(self._infotainment_system.radio.frequency_modulation, 95.8)
        with self.subTest("AM"):
            self.assertEqual(self._infotainment_system.radio.amplitude_modulation, 0)

    def testRadioSetter(self):
        """Testing if you can update the radio object by calling the radio setter"""
        self._infotainment_system.radio = Radio("Kiss", 100, None)
        with self.subTest("Station Name"):
            self.assertEqual(self._infotainment_system.radio.station_name, "Kiss")
        with self.subTest("FM"):
            self.assertEqual(self._infotainment_system.radio.frequency_modulation, 100)
        with self.subTest("AM"):
            self.assertEqual(self._infotainment_system.radio.amplitude_modulation, 0)

    def testLanguageGetter(self):
        """Testing the language is returned when you call the language getter"""
        self.assertEqual(self._infotainment_system.language, "English")

    def testLanguageSetter(self):
        """Testing if you can update the language by calling the language setter"""
        self._infotainment_system.language = "French"
        self.assertEqual(self._infotainment_system.language, "French")

    def testValueErrorRaisedIfTheInfotainmentSystemLanguageSetUsingTheLanguageSetterIsEmpty(self):
        """Testing a value error is raised if you try to set the language as no language"""
        with self.assertRaises(ValueError):
            self._infotainment_system.language = ""

    def testInfotainmentSystemObject(self):
        """Testing the infotainment system object"""
        self._infotainment_system = InfotainmentSystem(self._phone, self._radio, "English")
        self.assertEqual(self._infotainment_system.__str__(), "Phone Number: +447123456789\n"
                                                              "Emergency Contact:\n"
                                                              "First Name: Emergency\n"
                                                              "Last Name: Contact\n"
                                                              "Contact Number: +447987654321\n"
                                                              "Contacts:\n"
                                                              "Messages:\n"
                                                              "Radio:\n"
                                                              "Station Name: Capital\n"
                                                              "FM: 95.8\n"
                                                              "AM: 0Hz\n"
                                                              "Language: English")


if __name__ == '__main__':
    unittest.main()
