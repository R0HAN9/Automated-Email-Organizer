def sort_emails(emails):
    sorted_emails = {
        "high_priority": [],
        "low_priority": [],
        "work_emails": [],
        "personal_emails": [],
        "spam_emails": []
    }

    high_priority_keywords = ["urgent", "important", "asap"]
    spam_keywords = ["win money", "prize", "free", "buy now"]
    work_keywords = ["meeting", "project", "deadline"]

    for email in emails:
        # Sorting by priority
        if any(keyword.lower() in email['subject'].lower() for keyword in high_priority_keywords):
            sorted_emails["high_priority"].append(email)
        else:
            sorted_emails["low_priority"].append(email)

        # Sorting by category (work/personal)
        if any(keyword.lower() in email['subject'].lower() for keyword in work_keywords):
            sorted_emails["work_emails"].append(email)
        else:
            sorted_emails["personal_emails"].append(email)

        # Sorting by spam keywords
        if any(keyword.lower() in email['subject'].lower() for keyword in spam_keywords):
            sorted_emails["spam_emails"].append(email)

    return sorted_emails
