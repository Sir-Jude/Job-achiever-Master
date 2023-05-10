import json
import re

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
        self.last_name = self.get_last_name()
        self.DOB = self.get_DOB()
        self.email = self.get_email()
        self.phone = self.get_phone_number()

        while True:
            add_experience = input(
                "Would you like to add your work experience (Y,N):"
            ).lower()
            if add_experience == "n":
                break
            elif add_experience == "y":
                self.experience.append(self.get_experience())

        while True:
            add_education = input("Would you like to add your education (Y,N):").lower()
            if add_education == "n":
                break
            elif add_education == "y":
                self.education.append(self.get_education())

    def json_info(self):
        info_dict = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "D.O.B.": self.DOB,
            "Email": self.email,
            "Phone": self.phone,
            "Work Experience": self.experience,
            "Education": self.education,
        }
        return json.dumps(info_dict)


# for testing purposes
if __name__ == "__main__":
    user1 = User()
    user1.get_info()
    json_data = user1.json_info()
    parsed_data = json.loads(json_data)
    formatted_json = json.dumps(parsed_data, indent=4)
    print(formatted_json)
