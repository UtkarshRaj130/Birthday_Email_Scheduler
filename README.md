# 🎉 Automated Birthday Emailer using Gmail API (Linux + Python + Cron)

This project sends **automated birthday emails** every morning at 8 AM to students listed in a CSV file.  
It uses the **Gmail API**, **Python**, and **cron** (on Linux) to run daily with almost no system resource usage.

---

## ✨ Features

- Automatically sends birthday wishes
- Uses Gmail API (secured and authenticated)
- Lightweight: scheduled with cron, no background process needed
- Easy to set up and extend

---

## 📁 Project Structure

```
birthday-mailer/
├── birthday_mailer.py         # Main script that sends birthday emails
├── students.csv               # List of students with name, email, DOB
├── credentials.json           # Gmail API credentials (downloaded from Google Cloud)
├── token.json                 # Auto-generated on first authentication (stores access token)
├── requirements.txt           # Required Python libraries
└── log.txt                    # (Optional) Logs cron output for debugging
```

---

## ⚙️ Prerequisites

- A **Google account** (Gmail)
- A Linux system (Ubuntu/Debian/Arch etc.)
- Python 3.7 or higher
- Basic internet connection

---

## 🚀 Step-by-Step Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/birthday-mailer.git
cd birthday-mailer
```

### 2. Set Up a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

#### 📦 `requirements.txt` contents:
```
google-auth
google-auth-oauthlib
google-api-python-client
pandas
```

---

## 📧 Setting Up Gmail API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Gmail API** from “APIs & Services”
4. Go to **Credentials** and click **Create Credentials → OAuth Client ID**
5. Choose:
   - **Application type**: Desktop app
   - **Name**: Birthday Mailer
6. Download the `credentials.json` file and place it inside the project directory.

---

## 👤 First-Time Authentication

Run the script once manually to authenticate your Google account:

```bash
python birthday_mailer.py
```

- A browser will open asking you to log in and allow permissions.
- A `token.json` file will be created to store your login token for future runs.
- From now on, **no manual login needed** unless the token expires (usually years).

---

## 🧪 Test it Manually (Optional)

You can manually test it by running:

```bash
python birthday_mailer.py
```

If a birthday matches today’s date in `students.csv`, a mail will be sent.

---

## 🕗 Set Up Cron to Run Every Day at 8 AM

1. Open your crontab:

```bash
crontab -e
```

2. Add the following line to schedule it daily at 8 AM:

```bash
0 8 * * * /path/to/your/project/venv/bin/python /path/to/your/project/birthday_mailer.py >> /path/to/your/project/log.txt 2>&1
```

> Replace `/path/to/your/project/` with the **full absolute path** to the project folder on your system.

---

## 🧾 students.csv Format

This file should have 3 columns:

| Name         | Email               | DOB        |
|--------------|---------------------|------------|
| Alice Smith  | alice@example.com   | 2002-06-05 |
| Bob Johnson  | bob@example.com     | 2003-08-21 |

> ✅ **DOB format must be `YYYY-MM-DD`**

---

## 🛠 Notes

- `token.json` is automatically refreshed silently once created.
- If you ever change Gmail accounts or scopes, delete `token.json` and run the script again.
- The Gmail account must allow access to **less secure apps** or use **OAuth 2.0** as configured.

---

## 📜 License

MIT License

---

## 👨‍🏫 Project By

- Utkarsh Raj  
- Purpose: Automated self-awareness initiative via birthday wishes

---

## 🙋 FAQ

**Q: Will this run every day?**  
Yes, once cron is set, it silently runs at 8 AM every day.

**Q: Will I be asked to log in every time?**  
No, only the first time. After that, `token.json` handles authentication.

**Q: Can I use this on Windows?**  
Not directly with cron. But you can use Task Scheduler instead.

---

Happy Automating! 🥳