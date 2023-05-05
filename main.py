# imports
# (here we imports all the modules)
import os
import app_classes
import app_functions

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
[2] CV ({self.cv})
[3] Job ({self.job})
[4] Cover letter ({self.cover_letter})
[5] Interviews ({self.interview})
[6] Interview analyse ({self.interview_analyse})
[x] Exit
> """
        app_functions.input_strict(home_menu, ["1","2","3","4","5","x"], "clear")

# Module Introduction
# (which collects all the inputs for the personal info and the job.
# Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)

# Module CV
# (which creates the CV)

# Module Cover letter
# (which writes the cover letter)

# Module email
# (which send the email with the cover letter and the CV)

# Module Job interview
# (which simulates the job interview)


# Testing if this file is running properly
if __name__ == '__main__':
    menu = Menu().home()
    