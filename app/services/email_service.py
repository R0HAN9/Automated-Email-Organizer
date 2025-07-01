# email_service.py
from app.models.email_model import Email
from app.utils.email_utils import get_gmail_emails
from app.services.email_sorting_service import sort_emails


async def fetch_sorted_emails():
    """Fetch and sort emails from Gmail"""
    try:
        # Fetch emails from Gmail
        gmail_emails = await get_gmail_emails()
        
        # Convert to dictionaries for consistent processing
        email_dicts = [email.to_dict() for email in gmail_emails]
        
        # Use the sorting service for consistent sorting logic
        sorted_emails = sort_emails(email_dicts)
        
        return sorted_emails
    except Exception as e:
        print(f"Error fetching sorted emails: {e}")
        return {
            "high_priority": [],
            "low_priority": [],
            "work_emails": [],
            "personal_emails": [],
            "spam_emails": []
        }


async def get_emails_from_gmail():
    """Wrapper function for get_gmail_emails"""
    return await get_gmail_emails()


