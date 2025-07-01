# config.py
import os

# Gmail OAuth2 credentials
GMAIL_CLIENT_ID = os.getenv("GMAIL_CLIENT_ID", "your-gmail-client-id")
GMAIL_CLIENT_SECRET = os.getenv("GMAIL_CLIENT_SECRET", "your-gmail-client-secret")
GMAIL_REDIRECT_URI = os.getenv("GMAIL_REDIRECT_URI", "http://localhost:8080/callback")

# Outlook OAuth2 credentials
OUTLOOK_CLIENT_ID = os.getenv("OUTLOOK_CLIENT_ID", "your-outlook-client-id")
OUTLOOK_CLIENT_SECRET = os.getenv("OUTLOOK_CLIENT_SECRET", "your-outlook-client-secret")
OUTLOOK_REDIRECT_URI = os.getenv("OUTLOOK_REDIRECT_URI", "http://localhost:8080/callback")

# Token storage paths
GMAIL_TOKEN_PATH = os.getenv("GMAIL_TOKEN_PATH", "tokens/gmail_token.json")
OUTLOOK_TOKEN_PATH = os.getenv("OUTLOOK_TOKEN_PATH", "tokens/outlook_token.json")

# API service configurations (placeholders)
GMAIL_API_SERVICE = None
OUTLOOK_API_SERVICE = None

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "emailOrganizer")

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
