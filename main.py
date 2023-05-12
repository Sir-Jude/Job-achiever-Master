# imports
# (here we imports all the modules)
# import app_classes

from user_input import User
import app_functions
# from cv_bot import Resume
# from email_module import Email
from app_classes_v2 import Candidate, Adviser_Bot, Recruiter, Job
# import cover_letter_bot

def main():
    # 1) "Candidate info"
    # (which collects all the inputs for the personal info and the job.
    # Please use the "input_..." functions in app_functions file to restrict and verify user inputs.)
    Candidate.data["name"] = input("Name: ")
    Candidate.data["surname"] = input("Surname: ")
    Candidate.data["birthday"] = app_functions.input_date("Birthday (dd.mm.yyyy): ")
    Candidate.data["sex"] = app_functions.input_strict("Sex (male/female): ", ["male", "female"]).lower()
    Candidate.data["phone"] = input("Phone: ")
    Candidate.data["email"] = app_functions.input_email("Email: ")
    Candidate.data["address"] = input("Address: ")
    loop = True
    while loop:
        print("Input a previous working experience.")
        new_experience = {
            "title": input("Position: "),
            "description": input("Description: "),
            "company": input("Company: "),
            "date_start": app_functions.input_date("Starting date (dd.mm.yyyy): "),
            "date_end": app_functions.input_date("Ending date (dd.mm.yyyy): ")     
        }
        Candidate.add_experience(new_experience)
        answer = app_functions.input_strict("Do you want to add a new experience? (Y/N) ", ["Y", "N"]).upper()
        if answer == "N":
            loop = False
    loop = True
    while loop:
        new_education = {
            "title": input("Position: "),
            "description": input("Description: "),
            "school": input("Institution: "),
            "date_start": app_functions.input_date("Starting date (dd.mm.yyyy): "),
            "date_end": app_functions.input_date("Ending date (dd.mm.yyyy): ")     
        }
        Candidate.add_experience(new_education)
        answer = app_functions.input_strict("Do you want to add a new education? (Y/N) ", ["Y", "N"]).upper()
        if answer == "N":
            loop = False
    loop = True
    while loop:
        new_hobby = {
            "hobby": input("Hobby: "),
        }
        Candidate.add_hobbies(new_hobby)
        answer = app_functions.input_strict("Do you want to add a new hobby? (Y/N) ", ["Y", "N"]).upper()
        if answer == "N":
            loop = False
    loop = True
    while loop:
        new_skill = {
            "skill": input("Skill: "),
        }
        Candidate.add_skills(new_skill)
        answer = app_functions.input_strict("Do you want to add a new skill? (Y/N) ", ["Y", "N"]).upper()
        if answer == "N":
            loop = False
    loop = True
    while loop:
        new_language = {
            "hobby": input("Hobby: "),
        }
        Candidate.add_languages(new_language)
        answer = app_functions.input_strict("Do you want to add a new language? (Y/N) ", ["Y", "N"]).upper()
        if answer == "N":
            loop = False
    # IMPORTANT: We should put this at the beginning...
    Candidate.data["user_language"] = input("Which language do you to use for program? ")
    Candidate.save_infos()    
    
    # 2) "Job"
    # Look for jobs on popular website like LInkedin, Stepstones, etc... (usng their API?)

    # 3) "CV"
    # Create the CV
    # cv = Resume("json/candidate.json")
    # cv.generate()
    
    # 4) "Cover letter"
    # Writes the cover letter
    # cover_letter_bot.generate()

    # 5) "Email"
    # Send the email, attaching cover letter and CV
    # email = Email(
    #     f"{Candidate.data['email']}",  # sender
    #     [f"{Recruiter.data['email']}"],  # list of receivers
    #     f"Applying for the position of {Job.data['position']}",
    # )  # object

    # password = email.password("email_pass.txt")  # app password

    # body = Adviser_Bot.generate_letter()  # text of the email

    # attachments = email.attachments(
    #     [
    #         f"{Candidate.data['name']}_{Candidate.data['surname']}_CV.pdf"
    #     ]
    # )  # cv and cover letter

    # email.send(password, body, attachments)  # Send the email

    # 6) "Interview"
    # Prepare for the job interview

    # 7) "Interview analyse"
    # Give a feedback about the interview

    # Testing if this file is running properly


if __name__ == "__main__":
    main()
