# Import:
# - the SMTP class, to send the email
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


# Input the server's name (Google SMTP server)
email_server = "smtp.gmail.com"
# Standard secure SMTP port (at the day of today)
smtp_port = 587

# Input the sender's email address
sender = "jude.smiley.python@gmail.com"
# Fetch the app's password
# ("with" makes sure we close the file once we have recovered the password)
with open("email_pass.txt", "r") as file:
    psw = file.read()


# Input the list of receivers' email addresses
receivers = ["jude.smiley.python@gmail.com", "jude.smiley.python@gmail.com"]

# Write the subject of the email
subject = "Test Email with Attachment"

# Fetch the file containing the body of the email
with open("email_test.txt", "r") as file:
    body = file.read()

# Attach the document(s) to the email
filename = "email.png"
with open(filename, "rb") as file:
    attachment = MIMEApplication(file.read(), _subtype="txt")
    attachment.add_header("Content-Disposition", "attachment", filename=filename)

# Connect to the SMTP server
# ("with" makes sure we disconnect from the server after sending the email)
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

        # Add the attachment to the container
        msg.attach(attachment)

        # Send the email
        smtp.send_message(msg)
        print(f"Email sent to: {address}.")
        print()
