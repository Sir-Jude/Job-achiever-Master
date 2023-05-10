# Import:
# - the SMTP class, to send the email
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


# Server's name (Google SMTP server)
email_server = "smtp.gmail.com"
# Standard secure SMTP port (at the day of today)
smtp_port = 587

# Sender's email address
sender = "jude.smiley.python@gmail.com"
# App's password
# ("with" makes sure we close the file once we recovered the password)
with open("email_pass.txt", "r") as file:
    psw = file.read()


# List of receivers' email addresses
receivers = ["jude.smiley.python@gmail.com"]

# Subject of the email
subject = "Test Email with Attachment"

# Read the file containing the body of the email
with open("email_test.txt", "r") as file:
    body = file.read()

# Build the object rapresenting the attachment(s)
files = ["Curriculum.txt", "email.png"]
for document in files.copy():
    with open(document, "rb") as file:
        attachment = MIMEApplication(file.read())
        attachment.add_header("Content-Disposition", "attachment", filename=document)
        files.remove(document)
        files.append(attachment)
        
# Connect to the SMTP server
print("Connecting to server...")
with SMTP(email_server, smtp_port) as smtp:
    # Encript the connection with SMTP "starttls" method
    smtp.starttls()
    # Login into email account with SMTP method "login", which require 2 arguments:
    # 1. email of the sender
    # 2. app password
    smtp.login(sender, psw)
    print("Successfully connected to server.")
    print()

    # Loop through the list of receivers
    for address in receivers:
        print(f"Sending email to: {address}...")
        # Create the message container (outer email message)
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = address
        msg["Subject"] = subject

        # Add the message body to the container
        msg.attach(MIMEText(body, "plain"))

        # Add the attachment(s) to the container
        for attachment in files:
            msg.attach(attachment)

        # Send the email
        smtp.send_message(msg)
        print(f"Email sent to: {address}.")
        print()
