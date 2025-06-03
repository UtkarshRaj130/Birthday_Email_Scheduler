#!/usr/bin/env python3

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import pandas as pd
import os
from datetime import datetime
import base64
from email.mime.text import MIMEText

# ======= CONFIGURATION =======
BASE_DIR = "/home/your_user/birthday_mailer"
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")
CSV_FILE = os.path.join(BASE_DIR, "students.csv")
SENDER_EMAIL = "utkarshraj130@gmail.com"
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
# ==============================

def authenticate_gmail():
    """Authenticate and return Gmail API service."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def read_student_data():
    """Read student data from CSV."""
    if not os.path.exists(CSV_FILE):
        print(f"ERROR: {CSV_FILE} not found.")
        return None

    try:
        students = pd.read_csv(CSV_FILE)
        return students
    except Exception as e:
        print(f"ERROR reading {CSV_FILE}: {e}")
        return None

def send_email(service, sender, to, subject, body):
    """Send an email using Gmail API."""
    message = MIMEText(body, 'plain')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        sent_msg = service.users().messages().send(
            userId="me", body={'raw': raw_message}
        ).execute()
        print(f"Email sent to {to} | Message ID: {sent_msg['id']}")
    except Exception as e:
        print(f"ERROR sending email to {to}: {e}")

def check_and_send_emails():
    """Main logic to check birthdays and send emails."""
    students = read_student_data()
    if students is None:
        return

    today = datetime.now().strftime('%m-%d')
    students['DOB'] = pd.to_datetime(students['DOB'], errors='coerce')
    birthday_students = students[students['DOB'].dt.strftime('%m-%d') == today]

    if birthday_students.empty:
        print("No birthdays today.")
        return

    service = authenticate_gmail()

    for _, student in birthday_students.iterrows():
        name = student['Name']
        email = student['Email']
        subject = "Happy Birthday! 🎉"
        body = f"""Dear {name},

Wishing you a very Happy Birthday! 🎂

On this special day, we also invite you to take part in our self-discovery exercises, such as personality tests. These exercises are designed to help you understand yourself better and take the first step toward a fulfilling life.

Click the link below to get started:
https://example.com/self-discovery

Have a fantastic day ahead!

Best regards,  
Prof. Pradeep
"""
        send_email(service, SENDER_EMAIL, email, subject, body)

if __name__ == '__main__':
    print(f"Running Birthday Mailer at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    check_and_send_emails()