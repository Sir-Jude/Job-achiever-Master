# imports
# (here we imports all the modules)
import os
import app_classes
import app_functions
import Email

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
        app_functions.input_strict(home_menu, ["1","2","3","4","5","x"], "clear")

# 1) "Candidate info"
# (which collects all the inputs for the personal info and the job.
# Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)

# 2) "Job"
# Look for jobs on popular website like LInkedin, Stepstones, etc... (usng their API?)

# 3) "CV"
# Create the CV

# 4) "Cover letter"
# Writes the cover letter

# 5) "Email"
# Send the email, attaching cover letter and CV

# 6) "Interview"
# Prepare for the job interview

# 7) "Interview analyse"
# Give a feedback about the interview

# Testing if this file is running properly
def main():
    pass

if __name__ == '__main__':
    menu = Menu().home()
    