# email_service.py

# Importing the Email model for email structure and utility functions for fetching emails.
from app.models.email_model import Email
from app.utils.email_utils import get_gmail_emails, get_outlook_emails


# Async function to fetch and sort emails based on categories.
async def fetch_sorted_emails():
    # Fetch emails from Gmail asynchronously.
    gmail_emails = await get_gmail_emails()

    # Initialize a dictionary to store sorted emails by category.
    sorted_emails = {
        "work": [],      # Emails related to work.
        "personal": [],  # Emails related to personal matters.
        "social": [],    # Emails related to social updates.
        "other": [],     # Emails that do not match the above categories.
    }

    # Loop through all fetched Gmail emails and categorize them based on their subject.
    for email in gmail_emails:
        if "work" in email.subject.lower():  # Check if the email subject contains "work".
            sorted_emails["work"].append(email)
        elif "personal" in email.subject.lower():  # Check if the email subject contains "personal".
            sorted_emails["personal"].append(email)
        elif "social" in email.subject.lower():  # Check if the email subject contains "social".
            sorted_emails["social"].append(email)
        else:  # If none of the above conditions match, classify as "other".
            sorted_emails["other"].append(email)

    # Return the dictionary containing emails sorted by category.
    return sorted_emails
