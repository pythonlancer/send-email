#import the necessary libraries
import smtplib  # Provides SMTP client functionality for connecting to and sending emails through a mail server
from email.message import EmailMessage  # Allows you to create and structure email messages (headers, body, attachments) using the modern EmailMessage class
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

# Create and configure an email message object by setting sender details, recipient information, reply-to address, subject line, and plain-text body content for sending via SMTP
email = EmailMessage()
email["From"] = f"Python Lancer Dev Team <{EMAIL_USER}>"
to_addr, email["To"] = "edgar.owarwo@protonmail.com","edgar.owarwo@protonmail.com"
email["Reply-To"] = EMAIL_USER
email["Subject"] = "Ready to start your Python Journey?"
email.set_content("Learn to be an expert python coder in no time")

# Establish a secure SSL connection to the SMTP server, authenticate with credentials, send the composed email from sender to recipient, confirm successful delivery, and properly close the connection
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo() # Identify client to the SMTP server
    server.starttls() # Upgrade the connection to a secure TLS-encrypted channel
    server.ehlo() # Re-identify after starting TLS (recommended)
    server.login(f'{EMAIL_USER}', f'{EMAIL_PASS}') # Please replace the username & password with your smtp login details
    server.sendmail(f'{EMAIL_USER}', f'{to_addr}', email.as_string())
    print("Email sent successfully")
    server.quit()
