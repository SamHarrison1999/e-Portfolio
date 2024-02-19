from Contact import Contact
from Utils import is_null_or_white_space


class Message:
    def __init__(self, sender: Contact, receiver: Contact, message_body: str):
        """
        Constructor for a Message Object
        Parameters:
            self (Message): Message object
            sender (Contact): The person sending the text message
            receiver (Contact): The person receiving the text message
            message_body (str): The text message being sent
        Returns:
            None
        """
        # If the message sender is empty throw an error
        if sender:
            self.__sender = sender
        else:
            raise ValueError("The Sender can't be empty")
        # If the message receiver is empty throw an error
        if receiver:
            self.__receiver = receiver
        else:
            raise ValueError("The receiver can't be empty")
        # If the message body is empty throw an error
        if is_null_or_white_space(message_body):
            raise ValueError("Can't send an empty message")
        else:
            self.__message_body = message_body

    def __str__(self):
        """
        Returns the Message Object as a string
        Parameters:
            self (Message): Message Object
        Returns:
            the Message Object as a string
        """
        return f'Sender: \n{self.__sender}\nReceiver: \n{self.__receiver}\nMessage Body: {self.__message_body}'

    @property
    def sender(self):
        """
        Return the person sending the message
        Parameters:
            self (Message): Message object
        Returns:
            self.__sender (Contact): The person sending the text message
        """
        return self.__sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the person sending the message
        Parameters:
            self (Message): Message object
            sender (Contact): The person sending the text message
        Returns:
            None
        """
        # If the message sender is empty throw an error
        if sender:
            self.__sender = sender
        else:
            raise ValueError("The Sender can't be empty")

    @property
    def receiver(self):
        """
        Return the person receiving the message
        Parameters:
            self (Message): Message object
        Returns:
            self.__receiver (Contact): The person receiving the text message
        """
        return self.__receiver

    @receiver.setter
    def receiver(self, receiver):
        """
        Sets the person receiving the message
        Parameters:
            self (Message): Message object
            self.__receiver (Contact): The person receiving the text message
        Returns:
            None
        """
        # If the message receiver is empty throw an error
        if receiver:
            self.__receiver = receiver
        else:
            raise ValueError("The receiver can't be empty")

    @property
    def message_body(self):
        """
        Returns the text message being sent
        Parameters:
            self (Message): Message object
        Returns:
            self.__message_body (str): The text message being sent
        """
        return self.__message_body

    @message_body.setter
    def message_body(self, message_body):
        """
        Sets the text message being sent
        Parameters:
            self (Message): Message object
            message_body (str): The text message being sent
        Returns:
            None
        """
        # If the message body is empty throw an error
        if is_null_or_white_space(message_body):
            raise ValueError("Can't send an empty message")
        else:
            self.__message_body = message_body


def main():
    sender = Contact("Message", "Sender", "+447123456789")
    receiver = Contact("Message", "Receiver", "+447987654321")
    message = Message(sender, receiver, "Test Text Message")
    print(message)


if __name__ == "__main__":
    main()
