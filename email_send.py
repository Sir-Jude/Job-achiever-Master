# Import:
# - the class "EmailMessage", to create an email object 
from email.message import EmailMessage

# - the module "ssl", to encript the connection
import ssl

# - the SMTP_SSL class, to send the email
from smtplib import SMTP_SSL

# email address of the sender
email_sender = "jude.smiley.python@gmail.com"

# app password
email_password = "pjti yzrc zgcx uiwt"

# email address of the receiver
email_receiver = "jude.smiley.python@gmail.com"

# object of the email
subject = "Test email"
# text of the email
body = """Hi,
this is a test email number 2
Regards"""

# create an "EmailMessage" object
em = EmailMessage()
# email's details
em["from"] = email_sender
em["to"] = email_receiver
em["Subject"] = subject
# Use EmailMessage method "set_content" for including the email's text
em.set_content(body)

# Assign ssl method "create_default_context()" to "context"
context = ssl.create_default_context()

# Initiate a "SMTP_SSL" class object, which requires three attributes:
# 1. the email server (for gmail)
# 2. the port (for gmail)
# 3. the SSL protocol
# Call a "with" statment to parse the above details
with SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    # Call SMTP_SSL method "login", which require 2 arguments:
    # 1. the email of the sender
    # 2. password
    smtp.login(email_sender, email_password)
    # Send the message with the SMTP_SSL method "sendemail", which requires 3 arguments:
    # 1. the email of the sender
    # 2. the email of the receiver
    # 3. the em object, formatted with the EmailMessage method "as_string()"
    smtp.sendmail(email_sender, email_receiver, em.as_string())