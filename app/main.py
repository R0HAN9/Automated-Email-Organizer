from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.services.email_service import fetch_sorted_emails

# Initialize the FastAPI application
app = FastAPI()

# Mount static files
# Static files such as CSS, JavaScript, and images are served from the "static" directory.
# These files can be accessed via the "/static" URL path.
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Set up Jinja2 templates
# Jinja2 is used for rendering HTML templates from the "templates" directory.
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    """
    Render the home page.
    - The home page is an HTML file served via Jinja2 templates.
    - The `request` parameter is required for template rendering in Jinja2.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/emails/gmail")
async def get_sorted_emails():
    """
    Fetch and return sorted Gmail emails.
    - Calls the `fetch_sorted_emails` service to fetch and categorize Gmail emails.
    - Returns the sorted emails in JSON format.
    """
    sorted_emails = await fetch_sorted_emails()  # Fetch sorted emails from the service
    return {"sorted_emails": sorted_emails}
