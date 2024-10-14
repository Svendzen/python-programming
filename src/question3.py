
class Message:
    def __init__(self, sender, recipient):
        """
        Initializes a new Message object with specified sender and recipient email addresses.
        This class is used to model an e-mail message.
        The message body is initially empty.
        """
        self.__sender = sender  # private attributes indicated by double underscore prefix
        self.__recipient = recipient
        self.__message_text = ""

    def toString(self):
        """
        Returns a string representation of the email message, including the sender, recipient, and the message text.
        """
        return f"From: {self.get_sender()}\nTo: {self.get_recipient()}\n\n{self.__message_text}"

    def get_sender(self):
        """
        Retrieves the sender's email address.
        """
        return self.__sender

    def get_recipient(self):
        """
        Retrieves the sender's email address.
        """
        return self.__recipient

    def append(self, text):
        """
        Appends a line of text to the message body followed by a newline.
        """
        self.__message_text += text + "\n"


# Example Usage
msg = Message("dev_student96@edu.co", "python_professor1337@edu.co")
msg.append("Hello worl- I mean, hello professor!")
msg.append("I hope email finds you well, or finds you at all.")
msg.append("I´m not sure yet. It depends if this Python Message class is working as intended.")
msg.append("")
msg.append("I’m currently testing this Message class I wrote, which explains the eccentric greetings and format.")
msg.append("Looking forward to hear back from you!.")
msg.append("Please restrain from using the random module while grading my code!")
msg.append("Thank you for iterating through this message.")
msg.append("")
msg.append("Best Regards,")
msg.append("dev_student96")

print(msg.toString())