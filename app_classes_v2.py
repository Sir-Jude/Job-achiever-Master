import app_functions
import json

bot_request = app_functions.bot_request
bot_message = app_functions.bot_message

# PERSONS and BOTS


class Candidate:
    try:  # if the file exists colect all the candidate infos
        """
        name = data["name"]  # just a string
        surname = data["surname"]  # just a string
        birthday = data["birthday"]  # date formated string
        sex = data["sex"]  # just a string
        phone = data["phone"]  # just a string
        email = data["email"]  # just a string
        adress = data["adress"]  # just a string
        experience = data["experience"]  # list of objects (update through method)
        education = data["education"]  # list of objects (update through method)
        hobbies = data["hobbies"]  # list of strings (update through method)
        skills = data["skills"]  # list of strings (update through method)
        languages = data["languages"]  # list of strings (update through method)
        user_language = data["user_language"]  # just a string
        short_description = data["short_description"]  # just a string
        """
        with open("json/candidate.json", "r") as file:
            data = json.load(file)
            
    except FileNotFoundError:  # if the file is missing than create one
        with open("json/candidate.json", "w") as file:
            data = {
                "name": None,
                "surname": None,
                "birthday": None,
                "sex": None,
                "phone": None,
                "email": None,
                "adress": None,
                "experience": [],
                "education": [],
                "hobbies": [],
                "skills": [],
                "languages": [],
                "user_language": "english",
                "short_description": None,
            }
            file.write(json.dumps(data, indent=4))

    @classmethod
    def add_experience(cls, neu_experience):
        # feed it with a dictionary in this format
        # {'title':'Title here', 'description':'Some description here', 'company':'Name of the company', 'date_start':'dd.mm.yyyy', 'date_end':'dd.mm.yyyy'}
        cls.data["experience"].append(neu_experience)

    @classmethod
    def add_education(cls, neu_education):
        # feed it with a dictionary in this format
        # {'title':'Title here', 'description':'Some description here', 'school':'Name of the school', 'date_start':'dd.mm.yyyy', 'date_end':'dd.mm.yyyy'}
        cls.data["education"].append(neu_education)

    @classmethod
    def add_hobbies(cls, neu_hobby):
        # feed it with a dictionary in this format
        # {'hobby':'Some description here'}
        cls.data["hobbies"].append(neu_hobby)

    @classmethod
    def add_skills(cls, neu_skill):
        # feed it with a dictionary in this format
        # {'skill':'Some description here'}
        cls.data["skills"].append(neu_skill)

    @classmethod
    def add_languages(cls, neu_language):
        # feed it with a dictionary in this format
        # {'language':'Language and level'}
        cls.data["languages"].append(neu_language)

    @classmethod
    def save_infos(cls):
        # save all the colected infos with this method
        with open("json/candidate.json", "w") as file:
            file.write(json.dumps(cls.data, indent=4))


class Recruiter:
    # All the atributes inside this class will be used to describe the role of recrutier bot
    try:  # if the file exists colect all the candidate infos
        """
        name = data["name"]  # just a string
        surname = data["surname"]  # just a string
        sex = data["sex"]  # just a string
        email = data["email"]  # just a string
        position = data["position"]  # just a string
        company = data["company"]  # just a string
        company_adress = data["company_adress"]  # just a string
        atitude = data["atitude"]  # just a string
        """
        with open("json/recruiter.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:  # if the file is missing than create one
        with open("json/recruiter.json", "w") as file:
            data = {
                "name": None,
                "surname": None,
                "sex": None,
                "email": None,
                "position": None,
                "company": None,
                "company_adress": None,
                "atitude": "normal",
            }
            file.write(json.dumps(data, indent=4))

    @classmethod
    def save_infos(cls):
        # save all the colected infos with this method
        with open("json/recruiter.json", "w") as file:
            file.write(json.dumps(cls.data, indent=4))


class Adviser_Bot:
    # All the atributes inside this class will be used to feed the bot with contextual infos
    candidate = "empty"
    recruiter = "empty"
    job = "empty"
    role_description = ""
    user_input = "empty"
    user_language = "english"
    try:  # if the file exists colect all the interview mesages
        with open("json/letter.json", "r") as file:
            letter = json.load(file) # the list of interview messages
    except FileNotFoundError:  # if the file is missing than create one
        with open("json/letter.json", "w") as file:
            letter = {
                "candidate_name": None,
                "candidate_surname": None,
                "recruiter_surname": None,
                "candidate_email": None,
                "candidate_phone": None,
                "candidate_adress": None,
                "recruiter_email": None,
                "recruiter_adress": None,
                "position": None,
                "company": None,
                "mail_body": None
            }
            file.write(json.dumps(letter, indent=4))

    try:  # if the file exists colect all the interview mesages
        with open("json/letter.json", "r") as file:
            interview_history = json.load(file) # the list of interview messages
    except FileNotFoundError:  # if the file is missing than create one
        with open("json/letter.json", "w") as file:
            interview_history = []
            file.write(json.dumps(interview_history, indent=4))

    @classmethod
    def update_user_input(cls):
        try:  # if the 'candidate.json' exists colect all the candidate infos
            with open("json/candidate.json", "r") as file:
                cls.candidate = json.load(file)
                # Preformating candidate informations
                cls.candidate_dates = f"{cls.candidate['name']} {cls.candidate['surname']} ({cls.candidate['sex']}), born on {cls.candidate['birthday']}."
                cls.candidate_experience = ""
                for e in cls.candidate["experience"]:
                    cls.candidate_experience += f"\n{e['date_start']} - {e['date_end']} in {e['company']}, job title - {e['title']}, description - {e['description']}"

                cls.candidate_studies = ""
                for s in cls.candidate["education"]:
                    cls.candidate_studies += f"\n{s['date_start']} - {s['date_end']} in {s['school']}, title - {s['title']}, description - {s['description']}"

                cls.candidate_languages = ""
                for l in cls.candidate["languages"]:
                    cls.candidate_languages += f"\n{l['language']}"

                cls.candidate_hobbies = ""
                for h in cls.candidate["hobbies"]:
                    cls.candidate_hobbies += f"\n{h['hobby']}"

                cls.candidate_skills = ""
                for sk in cls.candidate["skills"]:
                    cls.candidate_skills += f"\n{sk['skill']}"

                cls.user_language = cls.candidate["user_language"]
        except FileNotFoundError:  # if the file is missing set the candidate attribute 'empty'
            cls.candidate = "empty"
            cls.user_language = "english"
        try:  # if the 'recruiter.json' exists colect all the recruiter infos
            with open("json/recruiter.json", "r") as file:
                cls.recruiter = json.load(file)
                # Preformating recrutier informations
                cls.recruiter_dates = f'{cls.recruiter["name"]} {cls.recruiter["surname"]} ({cls.recruiter["sex"]}), having "{cls.recruiter["position"]}" position by "{cls.recruiter["company"]}".'
        except FileNotFoundError:  # if the file is missing set the recruiter attribute 'empty'
            cls.recruiter = "empty"
        try:  # if the 'job.json' exists colect all the job infos
            with open("json/job.json", "r") as file:
                cls.job = json.load(file)
                # Preformating job description
                cls.job_description = f'The job was found on {cls.job["source"]} having "{cls.job["position"]}" as position.\nJob description:{cls.job["description"]}'
        except FileNotFoundError:  # if the file is missing set the job attribute 'empty'
            cls.job = "empty"
        # Concatenate all candidate preformated infos
        if cls.candidate != "empty" and cls.recruiter != "empty" and cls.job != "empty":
            cls.user_input = f"""Candidate personal dates: {cls.candidate_dates}

Candidate experience:{cls.candidate_experience}
Candidate studies:{cls.candidate_studies}
Candidate knowing languages:{cls.candidate_languages}
Candidate skills: {cls.candidate_skills}
Candidate hobbies: {cls.candidate_hobbies}

Recrutier personal infos:
{cls.recruiter_dates}

Job informations:
{cls.job_description}"""
        else:
            cls.user_input = "empty"

    @classmethod
    def show_user_input(cls):
        return cls.user_input

    @classmethod
    def generate_letter(cls):
        cls.role_description = f"""You are a cover letter creator for jobs.
Based on the input you receive, you will compose the content of a cover letter for the desired job based only on the data provided.
Don't provide any results other than the cover letter.
Don't mention unnecesary informations from my experience or education.
Write the text of the letter in {cls.user_language} in a style suitable for the job to which the candidate is applying.
You don't ask questions or say anything other than the content of the cover letter."""

        messages = [
            bot_message("system", cls.role_description),
            bot_message("user", cls.user_input),
        ]
        letter_text = bot_request(messages)
        with open("json/letter.json", "w") as file:
            letter = {
                "candidate_name": cls.candidate["name"],
                "candidate_surname": cls.candidate["surname"],
                "recruiter_surname": cls.recruiter["surname"],
                "candidate_email": cls.candidate["email"],
                "candidate_phone": cls.candidate["phone"],
                "candidate_adress": cls.candidate["adress"],
                "recruiter_email": cls.recruiter["email"],
                "recruiter_adress": cls.recruiter["company_adress"],
                "position": cls.job["position"],
                "company": cls.recruiter["company"],
                "mail_body": letter_text
            }
            file.write(json.dumps(letter, indent=4))
        return letter_text

    @classmethod
    def generate_cv_short_description(cls):
        cls.role_description = f"""You are the candidate for a given job.
You must create a strong CV opening statement in {cls.user_language} that sums up your strengths, experience and motivation to impress employers with.
The statemen created by you will be a maximum of one or two sentences and can be included manually in the CV."""

        messages = [
            bot_message("system", cls.role_description),
            bot_message("user", cls.user_input),
        ]
        return bot_request(messages)

    @classmethod
    def analize_interview(cls, interview):
        cls.role_description = f"""You are a job interview adviser.
Based on the input you receive, you will comment in {cls.user_language} on each line in the job interview.
You will sugest better answers for candidate when his are not good enough.
You don't ask questions or say anything other than the comments on the dialogs from job interview."""

        messages = [
            bot_message("system", cls.role_description),
            bot_message(
                "user", f"{cls.user_input}\n\nThe interview content:\n{interview}"
            ),
        ]
        return bot_request(messages)

    @classmethod
    def simulate_interview(cls, answer):
        cls.role_description = f"""You'll interview in {cls.user_language} a candidate for a job.
{cls.user_input}
As a recruiter for this job you have to put important questions to the candidate acording to the job description and react to his answers.
You will be focused to cover all the necesary job questions with a {cls.recruiter['atitude']} atitude."""

        messages = [
            bot_message("system", cls.role_description),
            bot_message("assistant", f"Welcome {cls.candidate['name']}."),
        ] + cls.interview_history[2:]
        messages.append(bot_message("user", answer))
        cls.interview_history = messages
        response = bot_request(messages)
        messages.append(bot_message("assistant", response))
        # save all the interview mesages
        with open("json/interview.json", "w") as file:
            file.write(json.dumps(messages, indent=4))


# JOB ELEMENTS
class Job:
    # All the atributes inside this class will be used to describe the job
    try:  # if the file exists colect all the candidate infos
        """
        position = data["position"]  # just a string
        description = data["description"]  # just a string
        source = data["source"]  # just a string
        """
        with open("json/job.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:  # if the file is missing than create one
        with open("json/job.json", "w") as file:
            data = {"position": None, "description": None, "source": None}
            file.write(json.dumps(data, indent=4))

    @classmethod
    def save_infos(cls):
        # save all the colected infos with this method
        with open("json/job.json", "w") as file:
            file.write(json.dumps(cls.data, indent=4))
