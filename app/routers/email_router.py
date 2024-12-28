from fastapi import APIRouter, HTTPException
from app.services.email_service import get_emails_from_gmail
from app.services.email_sorting_service import sort_emails

router = APIRouter()


@router.get("/emails/gmail")
async def fetch_and_sort_gmail_emails():
    try:
        # Step 1: Fetch emails from Gmail
        emails = get_emails_from_gmail()

        # Step 2: Sort emails based on predefined rules
        sorted_emails = sort_emails(emails)

        return {"sorted_emails": sorted_emails}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/emails/outlook")
async def fetch_outlook_emails():
    # Placeholder for future Outlook API integration
    return {"message": "Outlook API integration coming soon."}
