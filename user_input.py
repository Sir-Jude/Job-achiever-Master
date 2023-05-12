import json
import re
from os import system as clear_terminal

# This pattern checks that a date follows one of these format's: DD.MM.YYYY, MM.YYYY and YYYY
RE_DATE_PATTERN = r"^(?:(?:0?[1-9]|[12][0-9]|3[01])\.(?:0?[1-9]|1[0-2])\.(?:19|20)\d{2})$|^(?:(?:0?[1-9]|1[0-2])\.(?:19|20)\d{2})$|^(?:19|20)\d{2}$"
# This pattern checks for DOB
RE_DOB_PATTERN = r"\d{1,2}.\d{1,2}.\d{4}"
# This pattern checks for email addresses
RE_EMAIL_PATTERN = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
# This pattern checks for phone numbers
# Could get a better one that is more forgiving
RE_PHONE_PATTERN = r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$"


class User:
    """
    A class to get User details.

    Methods:
    --------
        get_first_name(): gets a users first name
        get_last_name(): gets a users last name
        get_DOB(): gets a users DOB
        get_email(): gets a users email
        get_phone_number(): gets a users phone number
        get_address(): gets a users address
        get_languages(): gets a users spoken languages
        get_hobbies(): gets a users hobbies
        get_skills(): gets a users skills
        get_about_user(): gets a brief description of the user
        get_date(): gets a date is used in other methods
        get_experience(): gets a users work experience
            - Company
            - Start date
            - End date
            - Job Title
            - Job Description
        get_education(): gets a users education
            - School name
            - Type of Education
            - Name of the Course
            - Start date
            - End date
            - Course Description
        get_info(): calls all the other methods and an populates the class __init__
        json_info(): returns json formatted info that has been collected 
    """

    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.DOB = None
        self.email = None
        self.phone = None
        self.address = None
        self.language = {}
        self.hobbies = None
        self.skills = None
        self.about_user = None
        self.experience = []
        self.education = []

    def get_first_name(self) -> str:
        """Takes a users first name"""
        return input("First Name: ")

    def get_last_name(self) -> str:
        """Takes a users Last name"""
        return input("Last Name : ")

    def get_DOB(self) -> str:
        """
        Takes a users Date of Birth and checks
        that its valid against a regex pattern.
        """
        while True:
            dob_str = input("Date of Birth (DD.MM.YYYY): ")
            if re.match(RE_DOB_PATTERN, dob_str):
                return dob_str
            else:
                print("Invalid input you must enter DD.MM.YYYY")

    def get_email(self) -> str:
        """
        Takes a users Email address and checks
        that its valid against a regex pattern.
        """
        while True:
            email = input("Email: ")
            if re.match(RE_EMAIL_PATTERN, email):
                return email
            else:
                print("Invalid email address please give a valid email address.")

    def get_phone_number(self) -> str:
        """
        Takes a users phone number and checks
        that its valid against a regex pattern.
        """
        while True:
            phone_num = input("Phone Number: ")
            if re.match(RE_PHONE_PATTERN, phone_num):
                return phone_num
            else:
                print("Invalid Phone Number please enter a valid Phone Number.")

    def get_address(self) -> str:
        """Takes a users address."""
        return input("Enter your address: ")

    def get_languages(self) -> dict:
        """Takes a users spoken languages and there language level."""
        languages = {}
        while True:
            language = input("Please enter one language you speak or type 'No' to exit: ").capitalize()
            if language == "No":
                return languages
            language_level = input(f"What level do you speak {language} at (e.g. Native, B1): ")
            languages[language] = language_level


    def get_hobbies(self) -> str:
        """Takes a users hobbies."""
        hobbies = input("Enter your hobbies or type 'No' to move on: ")
        if hobbies == "No" or "":
            return None
        else: 
            return hobbies
        
    def get_skills(self) -> str:
        """Takes a users skills."""
        skills = input("Enter your skills or type 'No' to move on: ")
        if skills.capitalize() == "No":
            return None
        else:
            return skills
    
    def get_about_user(self) -> str:
        """Takes in info a user wants to provide about them self."""
        return input("Give a brief description about your self: ")

    def get_date(self) -> str:
        """
        Takes in a date as DD.MM.YYYY, MM.YYYY or YYYY
        checks that its valid against a regex pattern.
        A user can skip this by typing 'No' which will return None.
        """
        while True:
            date = input("Formats: DD.MM.YYYY, MM,YYYY or YYYY: ")
            if re.match(RE_DATE_PATTERN, date):
                return date
            elif date.lower() == "No":
                return None
            else:
                print("Invalid Date please enter a valid date.\n Or enter 'No'.")

    def get_experience(self) -> dict:
        """
        Takes in information about a users work experience.

        Returns a Dict with the following:
            - Company
            - Start date
            - End date
            - Job Title
            - Job Description
        """
        company_name = input("Name of the Company: ")
        print("Start date")
        start_date = self.get_date()
        print("End date")
        end_date = self.get_date()
        job_title = input("Job Title: ")
        job_description = input("Give a brief description of you job: ")
        return {
            "Company": company_name,
            "Start date": start_date,
            "End date": end_date,
            "Job Title": job_title,
            "Job Description": job_description,
        }

    def get_education(self) -> dict:
        """
        Takes in information about a users Education.

        Returns a Dict with the following:
            - School name
            - Type of Education
            - Name of the Course
            - Start date
            - End date
            - Course Description
        """
        school_name = input("Name of the School: ")
        education_type = input("What type of Education (e.g. Degree, Apprenticeship): ")
        course_name = input("Name of the course: ")
        print("Start date")
        start_date = self.get_date()
        print("End date")
        end_date = self.get_date()
        education_description = input("Give a brief description of what you learnt: ")
        return {
            "School name": school_name,
            "Type of Education": education_type,
            "Name of the Course": course_name,
            "Start date": start_date,
            "End date": end_date,
            "Course Description": education_description,
        }

    def get_info(self) -> str:
        """
        Calls the other methods that get info
        and populates the __init__ of the User class.

        add_education and add_experience are both in a loop
        to allow the user to add as much or as little as they
        like they also use .append() as they are appending to a
        list.
        """
        self.first_name = self.get_first_name()
        clear_terminal("clear")
        self.last_name = self.get_last_name()
        clear_terminal("clear")
        self.DOB = self.get_DOB()
        clear_terminal("clear")
        self.email = self.get_email()
        clear_terminal("clear")
        self.phone = self.get_phone_number()
        clear_terminal("clear")
        self.address = self.get_address()
        clear_terminal("clear")
        self.language = self.get_languages()
        clear_terminal("clear")
        self.hobbies = self.get_hobbies()
        clear_terminal("clear")
        self.skills = self.get_skills()
        clear_terminal("clear")
        self.about_user = self.get_about_user()
        clear_terminal("clear")

        while True:
            add_experience = input(
                "Would you like to add your work experience (Y,N):"
            ).lower()
            if add_experience == "n":
                break
            elif add_experience == "y":
                self.experience.append(self.get_experience())
        
        clear_terminal("clear")

        while True:
            add_education = input("Would you like to add your education (Y,N):").lower()
            if add_education == "n":
                break
            elif add_education == "y":
                self.education.append(self.get_education())
        
        clear_terminal("clear")



    def dict_info(self) -> dict:
        """Returns dict formatted user info"""
        info_dict = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "D.O.B.": self.DOB,
            "Email": self.email,
            "Phone": self.phone,
            "Address": self.address,
            "Languages": self.language,
            "Hobbies": self.hobbies,
            "Skills": self.skills,
            "About": self.about_user,
            "Work Experience": self.experience,
            "Education": self.education,
        }
        return info_dict

    def json_info(self) -> str:
        """Returns json formatted user info"""
        return json.dumps(self.dict_info(), indent=4)
    
    def save_json(self) -> None:
        """Creates a json file continuing the the info that has been collected in a file called user.json in the json folder."""
        json_data = self.json_info()
        with open(f"json/{self.first_name}.json", "w") as file:
            file.write(json_data)


# for testing purposes
if __name__ == "__main__":
    test = User()
    test.get_info()

    test.save_json()

    # reading the user.json file that was created and printing it out
    with open(f"json/{test.first_name}.json", "r") as file:
        formatted_json = json.load(file)
    
    print(json.dumps(formatted_json, indent=4))


