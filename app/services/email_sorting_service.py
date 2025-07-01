# email_sorting_service.py
def sort_emails(emails):
    """Sort emails by priority, category, and spam detection"""
    sorted_emails = {
        "high_priority": [],
        "low_priority": [],
        "work_emails": [],
        "personal_emails": [],
        "spam_emails": []
    }

    # Keywords for classification
    high_priority_keywords = ["urgent", "important", "asap", "critical", "deadline"]
    spam_keywords = ["win money", "prize", "free", "buy now", "click here", "limited time"]
    work_keywords = ["meeting", "project", "deadline", "office", "team", "client", "report"]
    
    for email in emails:
        subject = email.get('subject', '').lower()
        sender = email.get('sender', '').lower()
        
        # Priority sorting
        if any(keyword in subject for keyword in high_priority_keywords):
            sorted_emails["high_priority"].append(email)
        else:
            sorted_emails["low_priority"].append(email)

        # Category sorting (work/personal)
        if any(keyword in subject for keyword in work_keywords) or 'work' in sender:
            sorted_emails["work_emails"].append(email)
        else:
            sorted_emails["personal_emails"].append(email)

        # Spam detection
        if any(keyword in subject for keyword in spam_keywords):
            sorted_emails["spam_emails"].append(email)

    return sorted_emails
