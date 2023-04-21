class User:
    """
    A class to get User details.

    """
    def __init__(self) -> None:
        self.first_name = None
        self.last_name  = None
        self.DOB        = None
        self.email      = None
        self.phone      = None
        self.experience = []
        self.education  = []


    def get_first_name(self) -> str:
        """Takes a users first name"""
        return input('First Name: ')

    def get_last_name(self) -> str:
        """Takes a users Last name"""
        return input('Last Name : ')

    def get_DOB(self) -> str:
        """Takes a users Date of Birth"""
        return input('Date of Birth (DD.MM.YYYY): ')
    
    def get_email(self) -> str:
        """Takes a users Email address"""
        return input('Email: ')
    
    def get_phone_number(self) -> str:
        """Takes a users phone number"""
        return input('Phone Number: ')

    def get_experience(self) -> dict:
        """Takes in information about a users work experience"""
        company_name = input('Name of the Company: ')
        start_date = input('Start date: ')
        end_date = input('End date: ')
        job_title = input('Job Title: ')
        job_description = input('Give a brief description of you job: ')
        return {"Company": company_name,
                "Start date": start_date,
                "End date": end_date,
                "Job Title": job_title,
                "Job Description": job_description
                }   

        
    def get_education(self) -> dict:
        """Takes in info about a users Education"""
        school_name = input('Name of the School: ')
        education_type = input('What type of Education (e.g. Degree, Apprenticeship): ')
        course_name = input('Name of the course: ')
        start_date = input('Start date: ')
        end_date = input('End date: ')
        education_description = input('Give a brief description of what you learnt: ')
        return {"School name": school_name,
                "Type of Education": education_type,
                "Name of the Course": course_name,
                "Start date": start_date,
                "End date": end_date,
                "Course Description": education_description
                }
    
    def get_info(self):
        """Returns a """
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.DOB = self.get_DOB()
        self.email = self.get_email()
        self.phone = self.get_phone_number()

        while True:
            add_experience = input('Would you like to add your work experience (Y,N):').lower()
            if add_experience == 'n':
                break
            elif add_experience == 'y':
                self.experience.append(self.get_experience())

        while True:
            add_education = input('Would you like to add your education (Y,N):').lower()
            if add_education == 'n':
                break
            elif add_education == 'y':
                self.education.append(self.get_education())
