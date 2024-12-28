# email_service.py
from app.models.email_model import Email
from app.utils.email_utils import get_gmail_emails, get_outlook_emails


async def fetch_sorted_emails():
    # Fetch and sort emails from Gmail
    gmail_emails = await get_gmail_emails()

    # Sort emails by category
    sorted_emails = {
        "work": [],
        "personal": [],
        "social": [],
        "other": [],
    }

    for email in gmail_emails:
        if "work" in email.subject.lower():
            sorted_emails["work"].append(email)
        elif "personal" in email.subject.lower():
            sorted_emails["personal"].append(email)
        elif "social" in email.subject.lower():
            sorted_emails["social"].append(email)
        else:
            sorted_emails["other"].append(email)

    return sorted_emails
