from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import pandas as pd
import os
from datetime import datetime
import schedule
import time

# Define the scope for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Authenticate and return Gmail API service."""
    print("Attempting to authenticate...")  # Debugging step
    creds = None

    # Check if token.json exists (to avoid re-authentication)
    if os.path.exists('token.json'):
        print("Found token.json, loading credentials...")
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Refresh or obtain new credentials if none are valid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            print("Credentials not found or invalid. Starting browser authentication...")
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    print("Authentication successful!")  # Debugging step
    return build('gmail', 'v1', credentials=creds)

def read_student_data():
    """Read student data from a CSV file."""
    file_name = 'students.csv'
    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found!")
        return None
    
    try:
        students = pd.read_csv(file_name)
        print("Read Students csv as:\n")
        print(students)
        return students
    except Exception as e:
        print(f"Error reading {file_name}: {e}")
        return None

def send_email(service, sender, to, subject, body):
    """Send an email using the Gmail API."""
    from email.mime.text import MIMEText
    import base64

    print(f"Sending email to {to}...")  # Debugging step
    message = MIMEText(body)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Encode the message in base64
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        print(f"Email sent successfully to {to} with message ID: {message['id']}")
    except Exception as e:
        print(f"Error sending email to {to}: {e}")

def check_and_send_emails():
    """Check birthdays and send emails."""
    students = read_student_data()
    if students is None:
        return

    # Get today's date in MM-DD format
    today = datetime.now().strftime('%m-%d')

    # Filter students with today's birthday
    students['DOB'] = pd.to_datetime(students['DOB'], errors='coerce')  # Handle invalid dates
    birthday_students = students[students['DOB'].dt.strftime('%m-%d') == today]
    print(birthday_students)
    
    # Authenticate Gmail API
    service = authenticate_gmail()
    sender = "utkarshraj130@gmail.com"  # Replace with your email

    # Send emails to students with birthdays today
    for _, student in birthday_students.iterrows():
        print(f"Sending mail to {student}")
        name = student['Name']
        email = student['Email']
        roll_number = student['Roll Number']
        subject = "Happy Birthday! 🎉"
        body = f"""
        Dear {name},

        Wishing you a very Happy Birthday! 🎂

        On this special day, we also invite you to take part in our self-discovery exercises, such as personality tests. These exercises are designed to help you understand yourself better and take the first step toward a fulfilling life.

        Click the link below to get started:
        [Self-Discovery Exercises](https://example.com/self-discovery)

        Have a fantastic day ahead!

        Best regards,
        Prof. Pradeep
        """
        send_email(service, sender, email, subject, body)

def schedule_email_check():
    """Schedule the email check function to run daily."""
    schedule.every().day.at("08:00").do(check_and_send_emails)  # Adjust time as needed
    print("Scheduler is running. Waiting for the next task...")

    while True:
        schedule.run_pending()
        print("Running again")
        time.sleep(10)

if __name__ == '__main__':
    print("Starting the Birthday Email Scheduler...")
    
    # Test the function once before starting the scheduler
    print("Running the birthday email check manually for testing...")
    check_and_send_emails()
    
    # Start the scheduler
    schedule_email_check()