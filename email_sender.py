# Import:
# - the SMTP class, to send the email
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# Google SMTP server
email_server = "smtp.gmail.com"
# Stanard secure SMTP port
smtp_port = 587                     

# sender email address
sender = "jude.smiley.python@gmail.com"      
# app's password 
email_password = "pjti yzrc zgcx uiwt"
# receiver(s) email address
receivers = [
    "jude.smiley.python@gmail.com",
    "jude.smiley.python@gmail.com"
]
# subject of the email
subject = "Test email"

body = f"""
Hi,

this is the email test number 13.

Regards"""


def send_emails(receivers, body):
    # Initiate a "SMTP" class object, which requires 2 attributes:
        # 1. the email server
        # 2. the SMTP port
    print("Connecting to server...")
    email = SMTP(email_server, smtp_port)
    # Encript the connection with SMTP "starttls" method
    email.starttls()
    # Login into email account with SMTP method "login", which require 2 arguments:
        # 1. email of the sender
        # 2. app password
    email.login(sender, email_password)
    # Send the message with the SMTP method "sendemail", which requires 3 arguments:
        # 1. the email of the sender
        # 2. the email of the receiver
        # 3. the body of the email
    print("Successfully connected to server.")
    print()
    for address in receivers:
        body
        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg["from"] = sender
        msg["to"] = address
        msg["subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # 
        filename = "email.png"
        # Open the file in python as a binary, r for read, b for binary
        attachment = open(filename, "rb")
        
        attachment_package= MIMEBase("application", "octet-stream")
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header("Content-Disposition", "attachment; filename= " + filename)
        msg.attach(attachment_package)

        text = msg.as_string()
        
        print(f"Sending email to: {address}...")
        email.sendmail(sender, address, text)
        print(f"Email sent to: {address}.")
        print()
    
    # Close off the server
    email.quit()
    
send_emails(receivers, body)

