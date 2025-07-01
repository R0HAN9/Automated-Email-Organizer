# email_utils.py
import asyncio
from app.models.email_model import Email
from app.config import GMAIL_API_SERVICE, OUTLOOK_API_SERVICE


async def get_gmail_emails():
    """Fetch emails from Gmail API"""
    try:
        # This is a mock implementation - replace with actual Gmail API calls
        emails = []
        
        # Sample email data for demonstration
        sample_emails = [
            {"sender": "boss@company.com", "subject": "Urgent: Project Deadline Tomorrow", "category": "work"},
            {"sender": "friend@personal.com", "subject": "Hey, let's catch up!", "category": "personal"},
            {"sender": "noreply@social.com", "subject": "You have 5 new notifications", "category": "social"},
            {"sender": "spam@fake.com", "subject": "Win money now! Click here!", "category": "spam"},
            {"sender": "team@work.com", "subject": "Team meeting scheduled", "category": "work"},
        ]
        
        for email_data in sample_emails:
            emails.append(Email(
                sender=email_data["sender"],
                subject=email_data["subject"],
                category=email_data.get("category")
            ))
        
        return emails
    except Exception as e:
        print(f"Error fetching Gmail emails: {e}")
        return []


async def get_outlook_emails():
    """Fetch emails from Outlook API (placeholder)"""
    # Placeholder for Outlook implementation
    return []
