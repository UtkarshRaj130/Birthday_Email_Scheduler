# Birthday Email Scheduler

This project automates the process of sending birthday emails to students using the Gmail API. The script checks for birthdays daily and sends personalized greetings. It also includes a special message encouraging students to participate in self-discovery exercises.

---

## Table of Contents
1. [Features](#features)
2. [Setup Instructions](#setup-instructions)
3. [How to Run](#how-to-run)
4. [Folder Structure](#folder-structure)
5. [CSV File Format](#csv-file-format)
6. [Tech Stack](#tech-stack)
7. [Limitations](#limitations)
8. [License](#license)

---

## Features
- Automatically sends personalized birthday emails.
- Integrates with the Gmail API for email delivery.
- Uses a CSV file (`students.csv`) to store student data.
- Includes a scheduler to run the script daily at a specified time.

---

## Setup Instructions
To run this project on your system, follow these steps:

### Step 1: Clone the Repository
1. Open your terminal or command prompt.
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/<your-username>/birthday-email-scheduler.git
    ```
3. Navigate to the project folder:
   ```bash
   cd birthday-email-scheduler
   ```

### Step 2: Install Dependencies
1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Setup Gmail API Credentials
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the **Gmail API** for the project.
4. Configure the **OAuth consent screen**.
5. Create **OAuth 2.0 credentials** and download the `credentials.json` file.
6. Place the `credentials.json` file in the root directory of the project.

---

## How to Run
### Run Once for Testing
1. Open your terminal and navigate to the project folder.
2. Run the script to manually check and send birthday emails:
   ```bash
   python main.py
   ```

### Schedule the Script
The script includes a scheduler that runs daily at 8:00 AM (default). Follow these steps to start the scheduler:
1. Open your terminal and navigate to the project folder.
2. Run the script:
   ```bash
   python main.py
   ```
   Keep the terminal open to let the scheduler run.

---

## Folder Structure
```
birthday-email-scheduler/
│
├── credentials.json         # Google OAuth 2.0 credentials
├── token.json               # Saved authentication token (auto-generated)
├── students.csv             # Sample data file for student information
├── main.py                  # Main Python script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## CSV File Format
The script expects the `students.csv` file in the following format:

| Name       | Email               | Roll Number | DOB       |
|------------|---------------------|-------------|-----------|
| John Doe   | johndoe@gmail.com   | 12345       | 2000-12-06 |
| Jane Smith | janesmith@gmail.com | 12346       | 1999-05-14 |

- **DOB** must be in `YYYY-MM-DD` format.
- The email column should contain valid email addresses.

---

## Tech Stack
- **Python**: Core programming language.
- **Google API**: Used for sending emails.
- **Pandas**: Data manipulation.
- **Schedule**: For task scheduling.

---

## Limitations
- The Gmail API limits the number of emails sent per day (500 emails for personal accounts).
- The script must be running continuously for the scheduler to work.

---