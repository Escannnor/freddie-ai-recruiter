import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/gmail.send"
]

def get_credentials():
    """
    Authenticate the user and return credentials.
    This function uses the client_secret.json file and stores tokens in token.pickle.
    """
    creds = None
    token_file = "token.pickle"
    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(token_file, "wb") as token:
            pickle.dump(creds, token)
    return creds
