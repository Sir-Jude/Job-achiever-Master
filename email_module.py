# Import:
# - the SMTP class, to send the email
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class Email:
    # Standard secure SMTP port (at the day of today)
    SMTP_PORT = 587

    def __init__(
        self,
        sender: str,
        receivers: list,
        subject: str,
        email_server: str = "smtp.gmail.com",
    ):
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.email_server = email_server
    
    def password(self, filename):
        # App's password
        # ("with" makes sure we close the file once we recovered the password)
        with open(filename, "r") as file:
            return file.read()
        
    def attachments(self, files: list):
        # Build the object rapresenting the attachment(s)
        for document in files.copy():
            with open(document, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header("Content-Disposition", "attachment", filename=document)
                files.remove(document)
                files.append(attachment)
        return files

    def send(self, password, body, attachments):
        # Connect to the SMTP server
        print("Connecting to server...")
        with SMTP(self.email_server, self.SMTP_PORT) as smtp:
            # Encript the connection with SMTP "starttls" method
            smtp.starttls()
            # Login into email account with SMTP method "login", which require 2 arguments:
            # 1. email of the sender
            # 2. app password
            smtp.login(self.sender, password)
            print("Successfully connected to server.")
            print()

            # Loop through the list of receivers
            for address in self.receivers:
                print(f"Sending email to: {address}...")
                # Create the message container (outer email message)
                msg = MIMEMultipart()
                msg["From"] = self.sender
                msg["To"] = address
                msg["Subject"] = self.subject
            
            # Add the message body to the container
            msg.attach(MIMEText(body, "plain"))
            
            # Add the attachment(s) to the container
            for attachment in attachments:
                msg.attach(attachment)

            # Send the email
            smtp.send_message(msg)
            print(f"Email sent to: {address}.")
            print()
            