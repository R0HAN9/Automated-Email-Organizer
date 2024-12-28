# email_utils.py
from app.config import GMAIL_API_SERVICE, OUTLOOK_API_SERVICE
from app.models.email_model import Email


async def get_gmail_emails():
    # This function should implement logic to fetch emails from Gmail
    # Return a list of Email objects
    emails = []
    # Sample email data for demonstration
    emails.append(Email("work@example.com", "Work Email #1", "work"))
    emails.append(Email("personal@example.com",
                  "Personal Email #1", "personal"))
    emails.append(Email("social@example.com", "Social Email #1", "social"))
    return emails
