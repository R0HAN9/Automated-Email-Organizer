from app.config import GMAIL_API_SERVICE, OUTLOOK_API_SERVICE
from app.models.email_model import Email

async def get_gmail_emails():
    """
    Fetches emails from the Gmail API and returns them as a list of Email objects.

    Returns:
        list: A list of Email objects containing email details.
    """
    # Initialize an empty list to store Email objects.
    emails = []

    # TODO: Implement logic to integrate with Gmail API using GMAIL_API_SERVICE.
    # Example: Use GMAIL_API_SERVICE to authenticate and fetch email data.
    # For now, this function provides mock data for demonstration.

    # Sample email data simulating fetched emails.
    emails.append(Email("work@example.com", "Work Email #1", "work"))  # Example work email.
    emails.append(Email("personal@example.com", "Personal Email #1", "personal"))  # Example personal email.
    emails.append(Email("social@example.com", "Social Email #1", "social"))  # Example social email.

    # Return the list of emails.
    return emails
