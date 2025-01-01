import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from app.config import GMAIL_TOKEN_PATH, GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, GMAIL_REDIRECT_URI

# Define the required scope for Gmail read-only access.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_oauth2_credentials():
    """
    Retrieves OAuth2 credentials for accessing the Gmail API.

    If a valid token exists, it loads the credentials from the token file.
    Otherwise, it initializes the OAuth2 flow to authenticate and authorize the user.
    The resulting credentials are stored in a token file for future use.

    Returns:
        Credentials: An authorized Credentials object for the Gmail API.
    """
    creds = None

    # Check if a token file exists.
    # The token file stores authorized credentials for Gmail API access.
    if os.path.exists(GMAIL_TOKEN_PATH):
        # Load credentials from the token file.
        creds = Credentials.from_authorized_user_file(GMAIL_TOKEN_PATH, SCOPES)

    # If no valid credentials are found, initiate the authentication flow.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh the token if it has expired and a refresh token is available.
            creds.refresh(Request())
        else:
            # If no valid token is available, start a new authentication flow.
            # This requires the client secrets file ('gmail_credentials.json').
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/gmail_credentials.json', SCOPES
            )
            # Run the local server for user authentication and authorization.
            creds = flow.run_local_server(port=0)

        # Save the newly obtained credentials to the token file for future use.
        with open(GMAIL_TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    # Return the authorized credentials object.
    return creds
