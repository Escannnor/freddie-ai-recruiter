from googleapiclient.discovery import build
from app.services.google_auth import get_credentials
import base64
from email.mime.text import MIMEText

def send_email(email_address, candidate_name, score):
    """
    Sends an email via Gmail API using OAuth credentials.
    """
    creds = get_credentials()
    gmail_service = build("gmail", "v1", credentials=creds)
    
    email_template = (
        f"Hi {candidate_name},\n\n"
        "Thanks for applying! Based on our initial screening, we'd like to move forward with your application.\n"
        f"Your score is: {score}\n\n"
        "Best regards,\n"
        "Freddie AI Recruiter Team"
    )

    message = MIMEText(email_template)
    message['to'] = email_address
    message['from'] = "sawdickagboke@gmail.com"
    message['subject'] = "Application Update from Freddie AI Recruiter"
    
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw_message}
    
    try:
        message = gmail_service.users().messages().send(userId="me", body=body).execute()
        print(f"Email sent to {email_address}, Message Id: {message['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")
