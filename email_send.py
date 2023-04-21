from email.message import EmailMessage
import ssl
import smtplib

email_sender = "jude.smiley.python@gmail.com"

email_password = "yixc lqff lkzg lsvp"

email_receiveer = "jude.smiley.python@gmail.com"

subject = "Test email"
body = """Hi,
this is a test email

Regards"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiveer
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiveer, em.as_string())