# imports
# (here we imports all the modules)
# import app_classes
import app_functions
from cv_bot import Resume
from email_package import Email
from app_classes_v2 import Candidate, Adviser_Bot, Recruiter, Job
import cover_letter_bot

def main():
    # 0) "App window"
    # (which launches the program)

    # 1) "Candidate info"
    # (which collects all the inputs for the personal info and the job.
    # Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)

    # 2) "Job"
    # Look for jobs on popular website like LInkedin, Stepstones, etc... (usng their API?)

    # 3) "CV"
    # Create the CV
    cv = Resume("json/candidate.json")
    cv.generate()
    
    # 4) "Cover letter"
    # Writes the cover letter
    cover_letter_bot.generate()

    # 5) "Email"
    # Send the email, attaching cover letter and CV
    email = Email(
        f"{Candidate.data['email']}",  # sender
        [f"{Recruiter.data['email']}"],  # list of receivers
        f"Applying for the position of {Job.data['position']}",
    )  # object

    password = email.password("email_pass.txt")  # app password

    body = Adviser_Bot.generate_letter()  # text of the email

    attachments = email.attachments(
        [
            f"{Candidate.data['name']}_{Candidate.data['surname']}_CV.pdf"
        ]
    )  # cv and cover letter

    email.send(password, body, attachments)  # Send the email

    # 6) "Interview"
    # Prepare for the job interview

    # 7) "Interview analyse"
    # Give a feedback about the interview

    # Testing if this file is running properly


if __name__ == "__main__":
    main()
