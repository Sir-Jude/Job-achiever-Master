import os
import app_classes

candidate = app_classes.Candidate("Adrian", "Radu", "11.03.1977", "male", "0123456789", "adrian@email.de", "Ritterstr. 11b, 39124 Magdeburg")
experience_1 = app_classes.Experience("Webdesigner", "Responsable for mentenance of the company websites.", "IATOM", "10.10.2010", "23.09.2022")
candidate.add_experience(experience_1)
experience_2 = app_classes.Experience("Art Director", "Cration and implementing of web ads.", "Stream Line", "01.01.2000", "10.10.2010")
candidate.add_experience(experience_2)
experience_3 = app_classes.Experience("Janitor", "Cleaning of office rooms.", "Amazon", "01.01.1998", "01.01.2000")
candidate.add_experience(experience_3)
study = app_classes.Study("Designer", "Barcelors degree", "University Nicolae Grigorescu - Bucharest", "01.09.1995", "01.01.2000")
candidate.add_studies(study)
candidate.add_hobbies("music")
candidate.add_hobbies("reading")
candidate.add_skills("English (B1)")
candidate.add_skills("Python")

recrutier = app_classes.Recrutier("Nicolas", "Tesla", "male", "IBM", "CEO", "Berlinerstr. 11b, 39124 Berlin")

job = app_classes.Job("Network administrator", "You must take care about all the computers in the same network in our company.", "www.stepstone.de")

adviser = app_classes.Adviser_Bot(candidate, recrutier, job)
adviser.generate_letter()

answer = app_classes.Bot_Response.generate(adviser)

print(answer)