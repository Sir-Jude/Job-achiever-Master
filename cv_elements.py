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