# email_model.py
class Email:
    def __init__(self, sender, subject, category):
        self.sender = sender
        self.subject = subject
        self.category = category

    def to_dict(self):
        return {
            "sender": self.sender,
            "subject": self.subject,
            "category": self.category,
        }
