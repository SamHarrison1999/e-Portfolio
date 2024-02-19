import re
from Main.Vehicle.Contact import Contact
from Main.Vehicle.Message import Message
from Main.Utils.Utils import is_null_or_white_space

# Regex for UK phone numbers
PHONE_REGEX = re.compile(
    r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\('
    r'?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?#(\d{4}|\d{3}))?$')


class Phone:
    def __init__(self, phone_number: str, emergency_contact: Contact, contacts: list[Contact], messages: list[Message])\
            -> None:
        """
        Constructor for a phone object
        :parameter Phone self: The phone object
        :parameter str phone_number: The drivers phone number
        :parameter Contact emergency_contact: The drivers emergency contact
        :parameter list[Contact] contacts: A list of all the contacts on the drivers phone
        :parameter list[Message] messages: A list of all the text messages on the drivers phone
        :raises ValueError: If the phone number isn't valid
        :returns: None
        """
        # If contact number isn't a valid United Kingdom number throw an error
        if is_null_or_white_space(phone_number) or not PHONE_REGEX.search(phone_number):
            raise ValueError("phone number is not valid")
        else:
            self._phone_number = phone_number
        self._emergency_contact = emergency_contact
        # If your have no contacts your contacts list is an empty list
        if contacts:
            self._contacts = contacts
        else:
            self._contacts = []
        # If you have no messages your messages list is an empty list
        if messages:
            self._messages = messages
        else:
            self._messages = []

    def __str__(self) -> str:
        """
        Returns the phone object as a string
        :parameter Phone self: The phone object
        :returns: The phone object as a string
        """
        return (f"Phone Number: {self._phone_number}\nEmergency Contact:\n{self._emergency_contact}\n" + "Contacts:\n"
                + "" + f''.join(f"Contact {contact_number + 1}:\n{contact}\n"
                                for contact_number, contact in enumerate(self._contacts)) + "Messages:" +
                "" + f''.join(f"\nMessage {message_number + 1}:\n{message}"
                              for message_number, message in enumerate(self._messages)))

    @property
    def phone_number(self) -> str:
        """
        Returns the drivers phone number
        :parameter Phone self: The phone object
        :returns: The drivers phone number
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str) -> None:
        """
        Set the drivers phone number
        :parameter Phone self: The phone object
        :parameter str phone_number: The drivers phone number
        :raises ValueError: If the phone number isn't valid
        :returns: None
        """
        # If contact number isn't a valid United Kingdom number throw an error
        if is_null_or_white_space(phone_number) or not PHONE_REGEX.search(phone_number):
            raise ValueError("phone number is not valid")
        else:
            self._phone_number = phone_number

    @property
    def emergency_contact(self) -> Contact:
        """
        Returns the drivers emergency contact
        :parameter Phone self: The phone object
        :returns: The drivers emergency contact
        """
        return self._emergency_contact

    @emergency_contact.setter
    def emergency_contact(self, emergency_contact: Contact) -> None:
        """
        Set the drivers emergency contact
        :parameter Phone self: The phone object
        :parameter Contact emergency_contact: The drivers emergency contact
        :returns: None
        """
        self._emergency_contact = emergency_contact

    @property
    def contacts(self) -> list[Contact]:
        """
        Returns a list of all the contacts on the drivers phone
        :parameter Phone self: The phone object
        :returns: A list of all the contacts on the drivers phone
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts: list[Contact]) -> None:
        """
        Sets a list of all the contacts on the drivers phone
        :parameter Phone self: The phone object
        :parameter list[Contact] contacts: A list of all the contacts on the drivers phone
        :returns: None
        """
        # If your have no contacts your contacts list is an empty list
        if contacts:
            self._contacts = contacts
        else:
            self._contacts = []

    @property
    def messages(self) -> list[Message]:
        """
        Returns a list of all the text messages on the drivers phone
        :parameter Phone self: The phone object
        :returns:  A list of all the text messages on the drivers phone
        """
        return self._messages

    @messages.setter
    def messages(self, messages: list[Message]) -> None:
        """
        Sets a list of all the text messages on the drivers phone
        :parameter Phone self: The phone object
        :parameter list[Message] messages: A list of all the text messages on the drivers phone
        :returns: None
        """
        # If you have no messages your messages list is an empty list
        if messages:
            self._messages = messages
        else:
            self._messages = []

    @staticmethod
    def call_emergency_services() -> str:
        """
        Calls emergency services in the event of a crash or the drivers vitals flat-lining
        Returns:
            A String saying calling emergency services
        """
        return "Calling Emergency Services"

    def call_emergency_contact(self) -> str:
        """
        Calls Emergency Contact in the event of a crash or the drivers vitals flat-lining
        Returns:
            A String saying calling your emergency contact with the emergency contacts information
        """
        return f"Calling Emergency Contact\n{self._emergency_contact}"
