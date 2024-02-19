from Main.Vehicle.Contact import Contact
from Main.Utils.Utils import is_null_or_white_space


class Message:
    def __init__(self, sender: Contact, receiver: Contact, message: str) -> None:
        """
        Constructor for a Message Object
        :parameter Message self: The message object
        :parameter Contact sender: The person sending the text message
        :parameter Contact receiver: The person receiving the text message
        :parameter str message: The text message being sent
        :raises ValueError: If there is no message sender or receiver or the message being sent is empty
        :returns: None
        """
        # If the message sender is empty throw an error
        if sender:
            self._sender = sender
        else:
            raise ValueError("The Sender can't be empty")
        # If the message receiver is empty throw an error
        if receiver:
            self._receiver = receiver
        else:
            raise ValueError("The receiver can't be empty")
        # If the message body is empty throw an error
        if is_null_or_white_space(message):
            raise ValueError("Can't send an empty message")
        else:
            self._message = message

    def __str__(self) -> str:
        """
        Returns the message object as a string
        :parameter Message self: The message object
        :returns: The message object as a string
        """
        return f'Sender:\n{self._sender}\nReceiver:\n{self._receiver}\nMessage:\n{self._message}'

    @property
    def sender(self) -> Contact:
        """
        Returns the message senders information
        :parameter Message self: The message object
        :returns: The person sending the text message
        """
        return self._sender

    @sender.setter
    def sender(self, sender: Contact) -> None:
        """
        Update the message sender information
        :parameter Message self: The message object
        :parameter Contact sender: The person sending the text message
        :raises ValueError: If there is no message sender
        :returns: None
        """
        # If the message sender is empty throw an error
        if sender:
            self._sender = sender
        else:
            raise ValueError("The Sender can't be empty")

    @property
    def receiver(self) -> Contact:
        """
        Returns the message receivers information
        :parameter Message self: The message object
        :returns: The person receiving the text message
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: Contact) -> None:
        """
        Update the message receivers information
        :parameter Message self: The message object
        :parameter Contact receiver: The person receiving the text message
        :raises ValueError: If there is no message receiver
        :returns: None
        """
        # If the message receiver is empty throw an error
        if receiver:
            self._receiver = receiver
        else:
            raise ValueError("The receiver can't be empty")

    @property
    def message(self) -> str:
        """
        Returns the text message being sent
        :parameter Message self: The message object
        :returns: The text message being sent
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """
        Sets the text message being sent
        :parameter Message self: The message object
        :parameter str message: The text message being sent
        :raises ValueError: If the message being sent is empty
        :returns: None
        """
        # If the message body is empty throw an error
        if is_null_or_white_space(message):
            raise ValueError("Can't send an empty message")
        else:
            self._message = message
