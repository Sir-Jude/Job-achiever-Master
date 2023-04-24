import app_functions
openai = app_functions.openai
bot_request = app_functions.bot_request
bot_message = app_functions.bot_message

# PERSONS and BOTS

class Candidate:
    def __init__(self, name, family_name, birthday, sex, phone, email, adress):
        self.name = name # just a string
        self.family_name = family_name # just a string
        self.birthday = birthday # date formated string
        self.sex = sex # just a string
        self.phone = phone # just a string
        self.email = email # just a string
        self.adress = adress # just a string
        self.experience = [] # list of objects
        self.studies = [] # list of objects
        self.hobbies = [] # list of strings
        self.skills = [] # list of strings
        self.short_description = "" # just a string

    def add_experience(self, neu_experience): # feed it with one object
        self.experience.append(neu_experience)
    
    def add_studies(self, neu_studies): # feed it with one object
        self.studies.append(neu_studies)

    def add_hobbies(self, neu_hobby): # feed it with one object
        self.hobbies.append(neu_hobby)

    def add_skills(self, neu_skills): # feed it with one object
        self.skills.append(neu_skills)
    
    def set_short_description(self, short_description): # feed it with a string
        self.short_description = short_description

class Recrutier:
    # All those atributes will be used to describe the role of recrutier bot
    def __init__(self, name, family_name, sex, company, position, company_address):
        self.name = name # just a string
        self.family_name = family_name # just a string
        self.sex = sex # just a string
        self.company = company # just a string
        self.position = position # just a string
        self.company_address = company_address # just a string
        self.atitude = "" # just a string
        self.goals = "" # just a string

    def set_atitude(self, atitude): # feed it with a string
        self.atitude = atitude

    def set_goals(self, goals): # feed it with a string
        self.goals = goals

class Adviser_Bot:
    def __init__(self, candidate, recrutier, job, language):
        self.candidate = candidate
        self.recrutier = recrutier
        self.job = job
        self.language = language

        # Preformating candidate informations
        self.candidate_dates = f'{self.candidate.name} {self.candidate.family_name} ({self.candidate.sex}), born on {self.candidate.birthday}.'
        self.candidate_experience = '' # putting all candidate experience in a string
        for e in self.candidate.experience:
            self.candidate_experience += f"\n{e.date_start} - {e.date_end} in {e.company}, job title - {e.title}, description - {e.description}"
        
        self.candidate_studies = '' # putting all candidate studies in a string
        for s in self.candidate.studies:
            self.candidate_studies += f"\n{s.date_start} - {s.date_end} in {s.school}, title - {s.title}, description - {s.description}"

        self.candidate_hobbies = ", ".join(self.candidate.hobbies) # putting all candidate hobbies in a string
        self.candidate_hobbies += "."

        self.candidate_skills = ", ".join(self.candidate.skills) # putting all candidate skills in a string
        self.candidate_skills += "."
        
        # Preformating recrutier informations
        self.recrutier_dates = f'{self.recrutier.name} {self.recrutier.family_name} ({self.recrutier.sex}), having "{self.recrutier.position}" position by "{self.recrutier.company}".'

        # Preformating job description
        self.job_description = f'The job was found on {self.job.source} having "{self.job.position}" as position.\nJob description:{self.job.description}.'

        # Roles for bot init
        self.role_description =''
        self.user_input = f"""Candidate personal dates: {self.candidate_dates}
Candidate experience:{self.candidate_experience}
Candidate studies:{self.candidate_studies}
Candidate skills: {self.candidate_skills}
Candidate hobbies: {self.candidate_hobbies}

Recrutier personal infos:
{self.recrutier_dates}

Job informations:
{self.job_description}"""

    def generate_letter(self):
        self.role_description = f"""You are a cover letter creator for jobs.
Based on the input you receive, you will compose the content of a cover letter for the desired job based only on the data provided.
Don't provide any results other than the cover letter.
Don't mention unnecesary informations from my experience or education.
Write the text of the letter in {self.language} in a style suitable for the job to which the candidate is applying.
You don't ask questions or say anything other than the content of the cover letter."""

        # Just to test the given user input
        print(self.user_input)
        print()
        messages=[
            bot_message("system", self.role_description),
            bot_message("user", self.user_input)
        ]
        return bot_request(messages)
    
    def generate_cv_short_description(self):
        self.role_description = f"""You are the candidate for a given job.
You must create a strong CV opening statement in {self.language} that sums up your strengths, experience and motivation to impress employers with.
The statemen created by you will be a maximum of one or two sentences and can be included manually in the CV."""

        # Just to test the given user input
        print(self.user_input)
        print()
        messages=[
            bot_message("system", self.role_description),
            bot_message("user", self.user_input)
        ]
        return bot_request(messages)

    def analize_interview(self, interview):
        self.role_description = f"""You are a job interview adviser.
Based on the input you receive, you will comment in {self.language} on each line in the job interview.
You will sugest better answers for candidate when his are not good enough.
You don't ask questions or say anything other than the comments on the dialogs from job interview."""
        self.user_input += f"\n\nThe interview content:\n{interview}"

        # Just to test the given user input
        print(self.user_input)
        print()
        messages=[
            bot_message("system", self.role_description),
            bot_message("user", self.user_input)
        ]
        return bot_request(messages)

    def assist_intervew(self):
        self.role_description = f"""You are a job interview adviser."""
        # Not finished yet

# CV ELEMENTS
class Experience:
    def __init__(self, title, description, company, date_start, date_end):
        self.title = title # just a string
        self.description = description # just a string
        self.company = company # just a string
        self.date_start = date_start # date formated string
        self.date_end = date_end # date formated string

class Study:
    def __init__(self, title, description, school, date_start, date_end):
        self.title = title # just a string
        self.description = description # just a string
        self.school = school # just a string
        self.date_start = date_start # date formated string
        self.date_end = date_end # date formated string

class Hobby:
    def __init__(self, description):
        self.description = description # just a string

class Skill:
    def __init__(self, description):
        self.description = description # just a string

# JOB ELEMENTS
class Job:
    def __init__(self, position, description, source):
        self.position = position # just a string
        self.description = description # just a string
        self.source = source # just a string
