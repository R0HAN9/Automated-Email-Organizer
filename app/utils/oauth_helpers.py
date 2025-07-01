# oauth_helper.py
import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from app.config import GMAIL_TOKEN_PATH, GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_oauth2_credentials():
    """Get OAuth2 credentials for Gmail API"""
    creds = None
    
    # Load existing credentials
    if os.path.exists(GMAIL_TOKEN_PATH):
        try:
            creds = Credentials.from_authorized_user_file(GMAIL_TOKEN_PATH, SCOPES)
        except Exception as e:
            print(f"Error loading credentials: {e}")
    
    # If credentials are invalid or missing, get new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}")
                creds = None
        
        if not creds:
            try:
                # Create credentials dict for OAuth flow
                client_config = {
                    "installed": {
                        "client_id": GMAIL_CLIENT_ID,
                        "client_secret": GMAIL_CLIENT_SECRET,
                        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "redirect_uris": ["http://localhost"]
                    }
                }
                
                flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
                creds = flow.run_local_server(port=0)
                
                # Save credentials
                os.makedirs(os.path.dirname(GMAIL_TOKEN_PATH), exist_ok=True)
                with open(GMAIL_TOKEN_PATH, 'w') as token:
                    token.write(creds.to_json())
                    
            except Exception as e:
                print(f"Error during OAuth flow: {e}")
                return None
    
    return creds
