import unittest
from Main.Vehicle.Contact import Contact
from Main.Vehicle.Message import Message


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._sender = Contact("Message", "Sender", "+447123456789")
        self._receiver = Contact("Message", "Receiver", "+447987654321")
        self._message = Message(self._sender, self._receiver, "Test Text Message")

    def tearDown(self):
        self._sender = None
        self._receiver = None
        self._message = None

    def testValueErrorIsRaisedIfTheMessageSenderIsEmpty(self):
        """Testing a value error is raised if there is no message sender"""
        with self.assertRaises(ValueError):
            Message(None, Contact("Message", "Receiver", "+447987654321"), "Test Text Message")

    def testValueErrorIsRaisedIfTheMessageReceiverIsEmpty(self):
        """Testing a value error is raised if there is no message receiver"""
        with self.assertRaises(ValueError):
            Message(Contact("Message", "Sender", "+447123456789"), None, "Test Text Message")

    def testValueErrorIsRaisedIfTheMessageToBeSentIsSetIsEmpty(self):
        """Testing a value error is raised if there is no message"""
        with self.assertRaises(ValueError):
            Message(Contact("Message", "Sender", "+447123456789"),
                    Contact("Message", "Receiver", "+447987654321"), None)

    def testMessageSenderGetter(self):
        """Testing the message sender getters"""
        with self.subTest("First Name"):
            self.assertEqual(self._message.sender.first_name, "Message")
        with self.subTest("Last Name"):
            self.assertEqual(self._message.sender.last_name, "Sender")
        with self.subTest("Contact Number"):
            self.assertEqual(self._message.sender.contact_number, "+447123456789")

    def testMessageSenderSetter(self):
        """Testing the message sender setters"""
        self._sender = Contact("Message", "Sender", "+447123456789")
        self._receiver = Contact("Message", "Receiver", "+447987654321")
        self._message = Message(self._sender, self._receiver, "Test Text Message")
        self._message.sender = Contact("New", "Sender", "+447543765087")
        with self.subTest("First Name"):
            self.assertEqual(self._message.sender.first_name, "New")
        with self.subTest("Last Name"):
            self.assertEqual(self._message.sender.last_name, "Sender")
        with self.subTest("Contact Number"):
            self.assertEqual(self._message.sender.contact_number, "+447543765087")

    def testValueErrorIsRaisedIfTheMessageSenderIsSetToAnEmptyContactUsingTheMessageSenderSetter(self):
        """Testing a value error is raised if there is no message sender"""
        with self.assertRaises(ValueError):
            self._message.sender = None

    def testMessageReceiverGetter(self):
        """Testing the message receiver getters"""
        with self.subTest("First Name"):
            self.assertEqual(self._message.receiver.first_name, "Message")
        with self.subTest("Last Name"):
            self.assertEqual(self._message.receiver.last_name, "Receiver")
        with self.subTest("Contact Number"):
            self.assertEqual(self._message.receiver.contact_number, "+447987654321")

    def testMessageReceiverSetter(self):
        """Testing the message receiver setters"""
        self._message.receiver = Contact("New", "Receiver", "+447543765087")
        with self.subTest("First Name"):
            self.assertEqual(self._message.receiver.first_name, "New")
        with self.subTest("Last Name"):
            self.assertEqual(self._message.receiver.last_name, "Receiver")
        with self.subTest("Contact Number"):
            self.assertEqual(self._message.receiver.contact_number, "+447543765087")

    def testValueErrorIsRaisedIfTheMessageReceiverIsSetToAnEmptyContactUsingTheMessageReceiverSetter(self):
        """Testing a value error is raised if there is no message receiver"""
        with self.assertRaises(ValueError):
            self._message.receiver = None

    def testMessageGetter(self):
        """Testing the message is returned when you call the message getter"""
        self.assertEqual(self._message.message, "Test Text Message")

    def testMessageSetter(self):
        """Testing the message can be updated by calling the message setter"""
        self._message.message = "Updated Test Text Message"
        self.assertEqual(self._message.message, "Updated Test Text Message")

    def testValueErrorIsRaisedIfTheMessageToBeSentIsSetIsEmptyUsingTheMessageSetter(self):
        """Testing a value error is raised if there is no message"""
        with self.assertRaises(ValueError):
            self._message.message = ""

    def testGetMessageObject(self):
        """Testing the message object"""
        with self.subTest("Message"):
            self.assertEqual(self._message.__str__(), "Sender:\n"
                                                      "First Name: Message\n"
                                                      "Last Name: Sender\n"
                                                      "Contact Number: +447123456789\n"
                                                      "Receiver:\n"
                                                      "First Name: Message\n"
                                                      "Last Name: Receiver\n"
                                                      "Contact Number: +447987654321\n"
                                                      "Message:\n"
                                                      "Test Text Message")
        with self.subTest("Message Sender First Name"):
            self.assertEqual(self._message.sender.first_name, "Message")
        with self.subTest("Message Sender Last Name"):
            self.assertEqual(self._message.sender.last_name, "Sender")
        with self.subTest("Message Sender Phone Number"):
            self.assertEqual(self._message.sender.contact_number, "+447123456789")
        with self.subTest("Message Receiver First Name"):
            self.assertEqual(self._message.receiver.first_name, "Message")
        with self.subTest("Message Receiver Last Name"):
            self.assertEqual(self._message.receiver.last_name, "Receiver")
        with self.subTest("Message Receiver Phone Number"):
            self.assertEqual(self._message.receiver.contact_number, "+447987654321")
        with self.subTest("Message Sent"):
            self.assertEqual(self._message.message, "Test Text Message")


if __name__ == '__main__':
    unittest.main()
