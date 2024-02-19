from collections import OrderedDict
import re
from Utils import is_null_or_white_space
from Contact import Contact
from Message import Message


class Phone:
    def __init__(self, phone_number: str, emergency_contact: OrderedDict[str, str], contacts: list[Contact],
                 messages: list[Message]):
        """
        Constructor for a Phone Object
        Parameters:
            self (Phone): The Phone Object
            phone_number (str): The drivers phone number
            emergency_contact (OrderedDict[str, str]): The drivers emergency contact
            contacts (list[Contact]): A list of all the contacts on the drivers phone
            messages (list[Message]): A list of all the text messages on the drivers phone
        Returns:
            None
        """
        # If contact number isn't a valid uk number throw an error
        regex = re.compile(
            r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?#(\d{4}|\d{3}))?$')
        if is_null_or_white_space(phone_number) or not regex.search(phone_number):
            raise ValueError("phone number is not valid")
        else:
            self.__phone_number = phone_number
        self.__emergency_contact = emergency_contact
        # If your have no contacts your contacts list is an empty list
        if contacts:
            self.__contacts = contacts
        else:
            self.__contacts = []
        # If you have no messages your messages list is an empty list
        if messages:
            self.__messages = messages
        else:
            self.__messages = []

    def __str__(self):
        """
        Returns the Phone Object as a string
        Parameters:
            self (Phone): The Phone Object
        Returns:
             Formatted string of the Phone Object
        """
        return f"Phone Number: {self.__phone_number}\nEmergency Contact: " + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.emergency_contact.items()) + f"\nContacts List:" + f"".join(
            f"\n{contact}" for contact in self.__contacts) + f"\nMessages List:" + f"".join(
            f"\n{message}" for message in self.__messages)

    @property
    def phone_number(self):
        """
        Return the drivers phone number
        Parameters:
            self (Phone): The Phone Object
        Returns:
            self.__phone_number (str): The drivers phone number
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        """
        Set the drivers phone number
        Parameters:
            self (Phone): The Phone Object
            phone_number (str): The drivers phone number
        Returns:
            None
        """
        # If contact number isn't a valid uk number throw an error
        regex = re.compile(
            r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?#(\d{4}|\d{3}))?$')
        if is_null_or_white_space(phone_number) or not regex.search(phone_number):
            raise ValueError("phone number is not valid")
        else:
            self.__phone_number = phone_number

    @property
    def emergency_contact(self):
        """
        Returns the drivers emergency contact
        Parameters:
            self (Phone): The Phone Object
        Returns:
            self.__emergency_contact (OrderedDict[str, str]): The drivers emergency contact
        """
        return self.__emergency_contact

    @emergency_contact.setter
    def emergency_contact(self, emergency_contact):
        """
        Set the drivers emergency contact
        Parameters:
            self (Phone): The Phone Object
            emergency_contact (OrderedDict[str, str]): The drivers emergency contact
        Returns:
            None
        """
        self.__emergency_contact = emergency_contact

    @property
    def contacts(self):
        """
        Returns a list of all the contacts on the drivers phone
        Parameters:
            self (Phone): The Phone Object
        Returns:
            self.__contacts (list[Contact]): A list of all the contacts on the drivers phone
        """
        return self.__contacts

    @contacts.setter
    def contacts(self, contacts: list[Contact]):
        """
        Sets a list of all the contacts on the drivers phone
        Parameters:
            self (Phone): The Phone Object
            contacts (list[Contact]): A list of all the contacts on the drivers phone
        Returns:
            None
        """
        # If your have no contacts your contacts list is an empty list
        if contacts:
            self.__contacts = contacts
        else:
            self.__contacts = []

    @property
    def messages(self):
        """
        Returns a list of all the text messages on the drivers phone
        Parameters:
            self (Phone): The Phone Object
        Returns:
            self.__messages (list[Message]): A list of all the text messages on the drivers phone
        """
        return self.__messages

    @messages.setter
    def messages(self, messages):
        """
        Sets a list of all the text messages on the drivers phone
        Parameters:
            self (Phone): The Phone Object
            messages (list[Message]): A list of all the text messages on the drivers phone
        Returns:
            None
        """
        # If you have no messages your messages list is an empty list
        if messages:
            self.__messages = messages
        else:
            self.__messages = []


def main():
    emergency_contact = OrderedDict()
    emergency_contact["Name"] = "Emergency Contact"
    emergency_contact["number"] = "+447987654321"
    phone = Phone("+447123456789", emergency_contact, [], [])
    print(phone)


if __name__ == "__main__":
    main()
