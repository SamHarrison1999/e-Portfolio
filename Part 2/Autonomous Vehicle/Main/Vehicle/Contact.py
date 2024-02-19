from Main.Utils.Utils import is_null_or_white_space
import re

# Regex for UK mobile numbers
PHONE_NUMBER_REGEX = re.compile(
    r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\('
    r'?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?#(\d{4}|\d{3}))?$')


class Contact:
    def __init__(self, first_name: str, last_name: str, contact_number: str) -> None:
        """
        Constructor for a contact object
        :parameter Contact self: The contact object
        :parameter str first_name: Contacts first name
        :parameter str last_name: Contacts last name
        :parameter str contact_number: Contacts phone number
        :raises ValueError: If the name is empty or the contact number isn't valid
        :returns: None
        """
        # If the contacts first name is blank throw an error
        if is_null_or_white_space(first_name):
            raise ValueError("First name can't be blank")
        else:
            self._first_name = first_name
        # If the contacts last name is blank throw an error
        if is_null_or_white_space(last_name):
            raise ValueError("Last Name can't be blank")
        else:
            self._last_name = last_name
        # If contact number isn't a valid United Kingdom mobile number throw an error
        if is_null_or_white_space(contact_number) or not PHONE_NUMBER_REGEX.search(contact_number):
            raise ValueError("contact number is not valid")
        else:
            self._contact_number = contact_number

    def __str__(self) -> str:
        """
        Returns a contact object as a string
        :parameter Contact self: The contact object
        :returns: The contact object as a string
        """
        return f'First Name: {self._first_name}\nLast Name: {self._last_name}\nContact Number: {self._contact_number}'

    @property
    def first_name(self) -> str:
        """
        Returns a contacts first name
        :parameter Contact self: The contact object
        :returns: The contacts first name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """
        Sets a contacts first name
        :parameter Contact self: The contact object
        :parameter str first_name: Contacts first name
        :raises ValueError: If the first name is empty
        :returns: None
        """
        # If the contacts first name is blank throw an error
        if is_null_or_white_space(first_name):
            raise ValueError("First name can't be blank")
        else:
            self._first_name = first_name

    @property
    def last_name(self) -> str:
        """
        Returns a contacts last name
        :parameter Contact self: The contact object
        :returns: The contacts last name
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
        Sets a contacts last name
        :parameter Contact self: The contact object
        :parameter str last_name: Contacts last name
        :raises ValueError: If the last name is empty
        :returns: None
        """
        # If the contacts last name is blank throw an error
        if is_null_or_white_space(last_name):
            raise ValueError("Last Name can't be blank")
        else:
            self._last_name = last_name

    @property
    def contact_number(self) -> str:
        """
        Returns a contacts phone number
        :parameter Contact self: The contact object
        :returns: The contacts phone number
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number: str) -> None:
        """
        Sets a contacts phone number
        :parameter Contact self: The contact object
        :parameter str contact_number: Contacts phone number
        :raises ValueError: If the contact number isn't valid
        :returns: None
        """
        # If the contacts phone number isn't a valid United Kingdom number throw an error
        if is_null_or_white_space(contact_number) or not PHONE_NUMBER_REGEX.search(contact_number):
            raise ValueError("contact number is not valid")
        else:
            self._contact_number = contact_number
