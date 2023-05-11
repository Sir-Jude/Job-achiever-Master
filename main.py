# imports
# (here we imports all the modules)
# import app_classes
# import app_functions
import os
from cv_bot import Resume
from email_package import Email

# MENU
class Menu:
    def __init__(self) -> None:
        self.candidate = "empty"
        self.recriutier = "empty"
        self.job = "empty"
        self.cv = "empty"
        self.cover_letter = "empty"
        self.interview = "empty"
        self.interview_analyse = "empty"

    def home(self):
        os.system('clear')
        print("""Job Achiever Master
===========================""")
        home_menu = f"""
[1] Candidate info ({self.candidate})
[2] Job ({self.job})
[3] CV ({self.cv})
[4] Cover letter ({self.cover_letter})
[5] Email sender
[6] Interviews ({self.interview})
[7] Interview analyse ({self.interview_analyse})
[x] Exit
> """
        # app_functions.input_strict(home_menu, ["1","2","3","4","5","x"], "clear")

def main():
    # 1) "Candidate info"
    # (which collects all the inputs for the personal info and the job.
    # Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)

    # 2) "Job"
    # Look for jobs on popular website like LInkedin, Stepstones, etc... (usng their API?)

    # 3) "CV"
    # Create the CV
    cv = Resume("candidate.json")
    cv.generate()
    # 4) "Cover letter"
    # Writes the cover letter

    # 5) "Email"
    # Send the email, attaching cover letter and CV
    email = Email(
        "jude.smiley.python@gmail.com", # sender
        ["jude.smiley.python@gmail.com"], # list of receivers
        "Test with class and methods") # object
    
    password = email.password("email_pass.txt") # app password

    body = email.body("email_test.txt") # text of the email 

    attachments = email.attachments(["candidate.pdf"]) # cv and cover letter

    email.send(password, body, attachments) # Send the email

    # 6) "Interview"
    # Prepare for the job interview

    # 7) "Interview analyse"
    # Give a feedback about the interview

    # Testing if this file is running properly

if __name__ == '__main__':
    menu = Menu().home()
    main()
    