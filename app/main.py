from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.services.email_service import fetch_sorted_emails

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent /
          "static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/emails/gmail")
async def get_sorted_emails():
    # Fetch sorted emails (you can add logic for Gmail, Outlook here)
    sorted_emails = await fetch_sorted_emails()
    return {"sorted_emails": sorted_emails}
