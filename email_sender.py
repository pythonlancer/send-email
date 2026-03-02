#import the necessary libraries
import smtplib  # Provides SMTP client functionality for connecting to and sending emails through a mail server
from email.message import EmailMessage  # Allows you to create and structure email messages (headers, body, attachments) using the modern EmailMessage class

# Create and configure an email message object by setting sender details, recipient information, reply-to address, subject line, and plain-text body content for sending via SMTP
email = EmailMessage()
email["From"] = "Python Lancer Dev Team <info@pythonlancer.com>"
to_addr, email["To"] = "edgar.owarwo@protonmail.com","edgar.owarwo@protonmail.com"
from_addr,email["Reply-To"] = "info@pythonlancer.com", "info@pythonlancer.com"
email["Subject"] = "Ready to start your Python Journey?"
email.set_content("Learn to be an expert python coder in no time")

# Establish a secure SSL connection to the SMTP server, authenticate with credentials, send the composed email from sender to recipient, confirm successful delivery, and properly close the connection
with smtplib.SMTP("smtp.hostinger.com", 587) as server:
    server.ehlo() # Identify client to the SMTP server
    server.starttls() # Upgrade the connection to a secure TLS-encrypted channel
    server.ehlo() # Re-identify after starting TLS (recommended)
    server.login('username', 'password') # Please replace the username & password with your smtp login details
    server.sendmail(f'{from_addr}', f'{to_addr}', email.as_string())
    print("Email sent successfully")
    server.quit()
