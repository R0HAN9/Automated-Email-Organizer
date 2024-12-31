from fastapi import APIRouter, HTTPException
from app.services.email_service import get_emails_from_gmail
from app.services.email_sorting_service import sort_emails

# Create a FastAPI router instance to define endpoints related to email operations
router = APIRouter()

@router.get("/emails/gmail")
async def fetch_and_sort_gmail_emails():
    """
    Endpoint to fetch and sort Gmail emails.

    Steps:
    1. Fetch emails from Gmail using the email service.
    2. Sort emails using predefined rules via the sorting service.
    3. Return the sorted emails in a structured response.

    Returns:
        dict: A JSON response containing sorted emails.
    
    Raises:
        HTTPException: Returns a 500 status code with an error message if any exception occurs.
    """
    try:
        # Step 1: Fetch emails from Gmail
        emails = get_emails_from_gmail()  # Calls the email service to retrieve Gmail emails

        # Step 2: Sort emails based on predefined rules
        sorted_emails = sort_emails(emails)  # Uses sorting service to categorize or organize emails

        # Step 3: Return the sorted emails
        return {"sorted_emails": sorted_emails}
    except Exception as e:
        # Handle unexpected exceptions and return a detailed error response
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/emails/outlook")
async def fetch_outlook_emails():
    """
    Endpoint to fetch emails from Outlook.

    Currently, this is a placeholder for future integration with the Outlook API.

    Returns:
        dict: A JSON response indicating the status of the Outlook API integration.
    """
    # Placeholder response for Outlook email fetching
    return {"message": "Outlook API integration coming soon."}
