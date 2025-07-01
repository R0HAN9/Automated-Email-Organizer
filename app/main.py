# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.services.email_service import fetch_sorted_emails
from app.routers.email_router import router as email_router

app = FastAPI(title="Email Organizer", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_path = Path(__file__).parent / "static"
if static_path.exists():
    app.mount("/static", StaticFiles(directory=static_path), name="static")

# Set up Jinja2 templates
templates_path = Path(__file__).parent / "templates"
if templates_path.exists():
    templates = Jinja2Templates(directory=templates_path)
else:
    templates = None

# Include routers
app.include_router(email_router, prefix="/api", tags=["emails"])


@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    if templates:
        return templates.TemplateResponse("index.html", {"request": request})
    else:
        return HTMLResponse("""
        <html>
            <head><title>Email Organizer</title></head>
            <body>
                <h1>Email Organizer</h1>
                <p>API is running! Visit <a href="/docs">/docs</a> for API documentation.</p>
                <p>API endpoints:</p>
                <ul>
                    <li><a href="/api/emails/gmail">Gmail Emails</a></li>
                    <li><a href="/emails/sorted">Sorted Emails</a></li>
                </ul>
            </body>
        </html>
        """)


@app.get("/emails/sorted")
async def get_sorted_emails():
    """Get sorted emails from all sources"""
    sorted_emails = await fetch_sorted_emails()
    return {"sorted_emails": sorted_emails}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Email Organizer API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
