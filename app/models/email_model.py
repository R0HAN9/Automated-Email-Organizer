# email_model.py

class Email:
    """
    Represents an email with its basic attributes: sender, subject, and category.
    This class provides a structure to encapsulate email data for further processing or storage.
    """

    def __init__(self, sender, subject, category):
        """
        Initializes an Email object with sender, subject, and category information.

        Args:
            sender (str): The email address of the sender.
            subject (str): The subject of the email.
            category (str): The category assigned to the email (e.g., "Work", "Personal", "Spam").
        """
        self.sender = sender  # The email address of the sender
        self.subject = subject  # The subject line of the email
        self.category = category  # The assigned category for the email

    def to_dict(self):
        """
        Converts the Email object into a dictionary representation.
        Useful for serialization or transferring email data between different components.

        Returns:
            dict: A dictionary with the email's sender, subject, and category.
        """
        return {
            "sender": self.sender,       # Maps the sender attribute to a dictionary key
            "subject": self.subject,     # Maps the subject attribute to a dictionary key
            "category": self.category,   # Maps the category attribute to a dictionary key
        }
