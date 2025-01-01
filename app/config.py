import os

# Replace these values with your OAuth2 credentials
# The Gmail client ID, secret, and redirect URI are required for OAuth2 authentication.
# These values are typically provided by the Google Cloud Console.
GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID", "your-gmail-client-id")
GMAIL_CLIENT_SECRET = os.getenv(
    "GMAIL_CLIENT_SECRET", "your-gmail-client-secret"
)
GMAIL_REDIRECT_URI = os.getenv("GMAIL_REDIRECT_URI", "your-redirect-uri")

# The Outlook client ID, secret, and redirect URI are required for OAuth2 authentication.
# These values are typically provided by the Microsoft Azure Portal.
OUTLOOK_CLIENT_ID = os.getenv("OUTLOOK_CLIENT_ID", "your-outlook-client-id")
OUTLOOK_CLIENT_SECRET = os.getenv(
    "OUTLOOK_CLIENT_SECRET", "your-outlook-client-secret"
)
OUTLOOK_REDIRECT_URI = os.getenv("OUTLOOK_REDIRECT_URI", "your-redirect-uri")

# Paths to store OAuth2 tokens for Gmail and Outlook.
# These token files will store the access tokens and refresh tokens for authenticated accounts.
# Ensure that these files are stored securely and are not exposed publicly.
GMAIL_TOKEN_PATH = "tokens/gmail_token.json"
OUTLOOK_TOKEN_PATH = "tokens/outlook_token.json"

# MongoDB configuration
# The MongoDB URI is used to connect to the database. By default, it connects to localhost.
# MONGODB_URI can be set to a remote database address, including authentication details.
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

# The database name within MongoDB to store email-related data.
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "emailOrganizer")
