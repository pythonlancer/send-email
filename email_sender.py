#import the necessary libraries
import smtplib
from email.message import EmailMessage
import os
import csv
import logging
import time
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

# ------------------------
# Configure Logging
# ------------------------
logging.basicConfig(
    filename="email.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------------
# Load Recipients from CSV
# ------------------------
def load_recipients(file_path):
    with open(file_path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# ------------------------
# Send Bulk Emails
# ------------------------
def send_bulk_emails(csv_file):
    recipients = load_recipients(csv_file)

    # Establish a secure SSL connection to the SMTP server, authenticate with credentials, send the composed email from sender to recipient, confirm successful delivery, and properly close the connection
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.ehlo()  # Identify client to the SMTP server
        server.starttls()  # Upgrade the connection to a secure TLS-encrypted channel
        server.ehlo()  # Re-identify after starting TLS (recommended)
        server.login(f'{EMAIL_USER}',f'{EMAIL_PASS}')  # Please replace the username & password with your smtp login details in the .env file

        for recipient in recipients:
            try:
                # Create and configure an email message object by setting sender details, recipient information, reply-to address, subject line, and plain-text body content for sending via SMTP
                email = EmailMessage()
                email["From"] = f"Python Lancer Dev Team <{EMAIL_USER}>"
                email["To"] = recipient['email']
                email["Reply-To"] = EMAIL_USER
                email["Subject"] = "Python Mad skills with our Dev Team"
                to_addr = recipient['email']
                body = f"""
Hiya {recipient['first_name']},

Are you ready to learn Python mad skills that could potentially land you a good paying job?

Join our dev team today and start building real-world projects immediately.

Talk soon,
Python Lancer Dev Team
"""
                email.set_content(body)
                server.sendmail(f'{EMAIL_USER}', f'{to_addr}', email.as_string())
                logging.info(f"Email sent to {recipient['email']}")
                print(f"Sent to {recipient['email']}")

                time.sleep(2)  # Rate limiting (2 seconds between emails)
            except Exception as e:
                logging.error(f"Failed to send to {recipient['email']} - {e}")
                print(f"Failed for {recipient['email']}")

    print("Bulk email process completed.")

# ------------------------
# Run The Script
# ------------------------
if __name__ == "__main__":
    send_bulk_emails("recipients.csv")




