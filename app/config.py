import os

# Replace these values with your OAuth2 credentials
GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID", "your-gmail-client-id")
GMAIL_CLIENT_SECRET = os.getenv(
    "GMAIL_CLIENT_SECRET", "your-gmail-client-secret")
GMAIL_REDIRECT_URI = os.getenv("GMAIL_REDIRECT_URI", "your-redirect-uri")

OUTLOOK_CLIENT_ID = os.getenv("OUTLOOK_CLIENT_ID", "your-outlook-client-id")
OUTLOOK_CLIENT_SECRET = os.getenv(
    "OUTLOOK_CLIENT_SECRET", "your-outlook-client-secret")
OUTLOOK_REDIRECT_URI = os.getenv("OUTLOOK_REDIRECT_URI", "your-redirect-uri")

# For OAuth2 Tokens (ensure token.json is created and accessible)
GMAIL_TOKEN_PATH = "tokens/gmail_token.json"
OUTLOOK_TOKEN_PATH = "tokens/outlook_token.json"

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "emailOrganizer")
