import re
from Utils import is_null_or_white_space


class Contact:
    def __init__(self, first_name: str, last_name: str, contact_number: str):
        """
        Constructor for Contact Object
        Parameters:
            self (Contact): Contact object
            first_name (str): Contacts first name
            last_name (str): Contacts last name
            contact_number (str): Contacts phone number
        Returns:
            None
        """
        # If first name is blank throw an error
        if is_null_or_white_space(first_name):
            raise ValueError("First name can't be blank")
        else:
            self.__first_name = first_name
        # If last name is blank throw an error
        if is_null_or_white_space(last_name):
            raise ValueError("Last Name can't be blank")
        else:
            self.__last_name = last_name
        # If contact number isn't a valid uk number throw an error
        regex = re.compile(
            r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?#(\d{4}|\d{3}))?$')
        if is_null_or_white_space(contact_number) or not regex.search(contact_number):
            raise ValueError("contact number is not valid")
        else:
            self.__contact_number = contact_number

    def __str__(self):
        """
        Returns a Contact object as a string
        Parameters:
            self (Contact): Contact object
        Returns:
            Formatted string of a Contact object
        """
        return f'First Name: {self.__first_name}\nLast Name: {self.__last_name}\nContact Number: {self.__contact_number}'

    @property
    def first_name(self):
        """
        Returns a contacts first name
        Parameters:
            self (Contact): Contact object
        Returns:
            self.__first_name (str): The contacts first name
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets a contacts first name
        Parameters:
            self (Contact): Contact object
            first_name (str): Contacts first name
        Returns:
            None
        """
        # If first name is blank throw an error
        if is_null_or_white_space(first_name):
            raise ValueError("First name can't be blank")
        else:
            self.__first_name = first_name

    @property
    def last_name(self):
        """
        Returns a contacts last name
        Parameters:
            self (Contact): Contact object
        Returns:
            self.__last_name (str): The contacts last name
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets a contacts last name
        Parameters:
            self (Contact): Contact object
            last_name (str): Contacts last name
        Returns:
            None
        """
        # If last name is blank throw an error
        if is_null_or_white_space(last_name):
            raise ValueError("Last Name can't be blank")
        else:
            self.__last_name = last_name

    @property
    def contact_number(self):
        """
        Returns a contacts phone number
        Parameters:
            self (Contact): Contact object
        Returns:
            self.__contact_number (str): The contacts phone number
        """
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        """
        Sets a contacts phone number
        Parameters:
            self (Contact): Contact object
            contact_number (str): Contacts phone number
        Returns:
            None
        """
        # If contact number isn't a valid uk number throw an error
        regex = re.compile(r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?#(\d{4}|\d{3}))?$')
        if is_null_or_white_space(contact_number) or not regex.search(contact_number):
            raise ValueError("contact number is not valid")
        else:
            self.__contact_number = contact_number


def main():
    contact = Contact("Test", "Contact", "+447123456789")
    print(contact)


if __name__ == "__main__":
    main()
