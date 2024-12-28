# Automated Email Organizer

## Project Overview

The **Automated Email Organizer** is a web-based application that helps users manage and organize their emails by fetching them from Gmail, sorting them into categories (e.g., high priority, work-related, personal, spam), and saving them into a MongoDB database. The application utilizes OAuth2 for Gmail authentication, organizes emails based on predefined rules, and provides a clean user interface to view the results.

## Key Features

- **Fetch Emails from Gmail**: Uses OAuth2 to authenticate with Gmail API and fetch the user's emails.
- **Sort Emails**: Automatically sorts emails into different categories based on predefined keywords (e.g., work, personal, high priority, spam).
- **MongoDB Storage**: Saves emails in MongoDB for persistent storage and quick retrieval.
- **User-Friendly Interface**: Simple and intuitive UI to display sorted emails, integrated with the backend to fetch and display results.
- **Modular Code Structure**: Organized backend services and well-documented codebase.

## Technologies Used

- **Backend**: Python, FastAPI
- **Frontend**: HTML, JavaScript (Vanilla), CSS
- **Database**: MongoDB
- **Authentication**: Google OAuth2 for Gmail integration
- **Deployment**: Docker for containerization (optional)


## Installation and Setup

1. **Clone the Repository**:

git clone https://github.com/R0HAN9/Automated-Email-Organizer.git cd Automated-Email-Organizer



2. **Install Dependencies**:

Create a virtual environment and install dependencies:

python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate pip install -r requirements.txt



3. **Configure Gmail API**:

- Go to the [Google Developer Console](https://console.developers.google.com/), create a new project, and enable the Gmail API.
- Download the OAuth2 credentials (`credentials/gmail_credentials.json`) and place it in the `credentials` folder.
- Follow the instructions to configure OAuth2 consent screen and scopes.

4. **Set Up Environment Variables**:

Create a `.env` file in the root directory with the following variables:

```env
GMAIL_CLIENT_ID=your-gmail-client-id
GMAIL_CLIENT_SECRET=your-gmail-client-secret
GMAIL_REDIRECT_URI=your-redirect-uri
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=emailOrganizer


Once the application is running:

Open http://127.0.0.1:8000 in your browser.
Click the "Fetch and Sort Emails" button to fetch and sort your Gmail emails.
The sorted emails will be displayed in categories like High Priority, Work Emails, Personal Emails, and Spam Emails.



File and Code Explanation

How the Files Work Together
Frontend:

The user interacts with the UI in index.html, which displays the sorted emails.
The emails.js script fetches sorted email data from the backend when the user clicks the "Fetch and Sort Emails" button.
It dynamically updates the page with the results, displaying emails in categories like High Priority, Work Emails, Personal Emails, and Spam Emails.

Backend:

When the user triggers the email fetching process, FastAPI's endpoint /emails/gmail is invoked.
email_service.py: The fetch_emails function handles the authentication with Gmail via OAuth2 and fetches the user's emails from Gmail.
email_sorting_service.py: The sort_emails function processes the emails fetched by email_service.py and sorts them into categories based on predefined rules (such as "urgent", "meeting", "invoice").
The sorted emails are then returned as a JSON response to the frontend.

MongoDB:

mongo_helpers.py helps interact with the MongoDB database by storing the fetched and sorted emails.
email_service.py uses MongoDB helper functions to save the fetched emails into the emailOrganizer database.
OAuth2 Authentication:

When the application starts, the user is redirected to Google’s OAuth2 consent screen to authenticate and grant access to their Gmail account.
The credentials are stored in gmail_token.json, and subsequent API requests use the stored token for authentication.
File Interactions:

The frontend index.html interacts with the backend via the emails.js script. When the user clicks the button, emails.js makes a request to the FastAPI backend at http://127.0.0.1:8000/emails/gmail.
The backend (email_service.py and email_sorting_service.py) fetches, processes, and sorts the emails, sending the result back to the frontend.
MongoDB is used to persist emails, which are stored using functions in mongo_helpers.py and retrieved as needed.
Docker Integration (optional):

The project is Dockerized using the Dockerfile and docker-compose.yml to simplify deployment in different environments.
This allows you to run the app inside containers, ensuring consistency across different setups.
