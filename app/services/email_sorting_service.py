def sort_emails(emails):
    """
    Sorts a list of emails into various categories based on their subject content.

    Args:
        emails (list): A list of email dictionaries, where each dictionary contains an email's details.

    Returns:
        dict: A dictionary categorizing emails into high priority, low priority, work, personal, and spam.
    """

    # Initialize the sorted email categories.
    sorted_emails = {
        "high_priority": [],  # Emails marked as urgent or important.
        "low_priority": [],   # Emails with no high-priority keywords.
        "work_emails": [],    # Emails related to work topics such as meetings or projects.
        "personal_emails": [], # Emails not related to work; assumed to be personal.
        "spam_emails": []     # Emails detected as spam based on keywords.
    }

    # Keywords used to determine email priority and categories.
    high_priority_keywords = ["urgent", "important", "asap"]  # Indicates high-priority emails.
    spam_keywords = ["win money", "prize", "free", "buy now"] # Indicates spam emails.
    work_keywords = ["meeting", "project", "deadline"]        # Indicates work-related emails.

    # Iterate through the list of emails to classify them.
    for email in emails:
        # Check if the email subject contains any high-priority keywords.
        if any(keyword.lower() in email['subject'].lower() for keyword in high_priority_keywords):
            sorted_emails["high_priority"].append(email)
        else:
            sorted_emails["low_priority"].append(email)

        # Check if the email subject contains work-related keywords.
        if any(keyword.lower() in email['subject'].lower() for keyword in work_keywords):
            sorted_emails["work_emails"].append(email)
        else:
            sorted_emails["personal_emails"].append(email)

        # Check if the email subject contains spam keywords.
        if any(keyword.lower() in email['subject'].lower() for keyword in spam_keywords):
            sorted_emails["spam_emails"].append(email)

    # Return the dictionary containing sorted emails.
    return sorted_emails
