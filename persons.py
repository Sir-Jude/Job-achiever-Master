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
        self.hobbies = [] # list of objects
        self.skills = [] # list of objects
        self.short_description = "" # just a string

    def add_experience(self, neu_experience): # feed it with one object
        self.experience.append(neu_experience)
    
    def add_studies(self, neu_studies): # feed it with one object
        self.studies.append(neu_studies)

    def add_skills(self, neu_skills): # feed it with one object
        self.skills.append(neu_skills)
    
    def set_short_description(self, short_description): # feed it with a string
        self.short_description = short_description


class Recrutier:
    # All those atributes will be used to describe the role of recrutier bot
    def __init__(self, name, family_name, sex, company, position):
        self.name = name # just a string
        self.family_name = family_name # just a string
        self.sex = sex # just a string
        self.company = company # just a string
        self.position = position # just a string
        self.atitude = "" # just a string
        self.goals = "" # just a string

    def set_atitude(self, atitude): # feed it with a string
        self.atitude = atitude

    def set_goals(self, goals): # feed it with a string
        self.goals = goals

class Adviser_Bot:
    def __init__(self):
        self.role_description = "" # The role description for our advisor