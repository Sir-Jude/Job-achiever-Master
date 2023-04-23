# Import:
# - the class "EmailMessage", to create an email object 
from email.message import EmailMessage

# - the module "ssl", to encript the connection
import ssl

# - the smtplib module, to send the email
import smtplib

# email address of the sender
email_sender = "jude.smiley.python@gmail.com"

# app password
email_password = "yixc lqff lkzg lsvp"

# email address of the receiver
email_receiver = "jude.smiley.python@gmail.com"

# object of the email
object = "Test email"
# text of the email
body = """Hi,
this is a test email number 2
Regards"""

# create an "EmailMessage" object
em = EmailMessage()
# email's details
em["from"] = email_sender
em["to"] = email_receiver
em["object"] = object
# use the EmailMessage method "set_content" for including the email's text
em.set_content(body)

# use the ssl method "create_default_context()"
# assign it to a variable
context = ssl.create_default_context()

# use a "with statment"
# use the smtplib method "SMTP_SSL", which requires three arguments:
# 1. the email server (for gmail)
# 2. the port (for gmail)
# 3. the context
# write "as" and create a tag for this expression
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    # use the smtp method "login", which require 2 arguments:
    # 1. the email of the sender
    # 2. password
    smtp.login(email_sender, email_password)
    # use the smtp method "sendemail" which requires 3 arguments:
    # 1. the email of the sender
    # 2. the email of the receiver
    # 3. the em object, formatted with the EmailMessage method "as_string()"
    smtp.sendmail(email_sender, email_receiver, em.as_string())
