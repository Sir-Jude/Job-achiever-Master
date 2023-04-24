import os
import app_classes
import app_functions
import time

candidate = app_classes.Candidate("Adrian", "Radu", "11.03.1977", "male", "0123456789", "adrian@email.de", "Ritterstr. 11b, 39124 Magdeburg")
experience_1 = app_classes.Experience("Webdesigner", "Responsable for mentenance of the company websites.", "IATOM", "10.10.2010", "23.09.2022")
candidate.add_experience(experience_1)
experience_2 = app_classes.Experience("Art Director", "Cration and implementing of web ads.", "Stream Line", "01.01.2000", "10.10.2010")
candidate.add_experience(experience_2)
experience_3 = app_classes.Experience("Janitor", "Cleaning of office rooms.", "Amazon", "01.01.1998", "01.01.2000")
candidate.add_experience(experience_3)
study_1 = app_classes.Study("Python Backend Programming", "Cours", "DCI", "15.12.2022", "10.01.2024")
candidate.add_studies(study_1)
study_2 = app_classes.Study("Graphic designer", "Barcelors degree", "University of Arts - Nicolae Grigorescu - Bucharest", "01.09.1995", "01.01.2000")
candidate.add_studies(study_2)
candidate.add_hobbies("music")
candidate.add_hobbies("reading")
candidate.add_skills("English (B1 - lower intermediate)")
candidate.add_skills("Python, PHP, mySQL")

recrutier = app_classes.Recrutier("Nicolas", "Tesla", "male", "Dataport AöR", "CEO", "Berlinerstr. 11b, 39124 Berlin")

job_description = """
IHR AUFGABENFELD
- In unserem bevorzugten Techstack entwickeln und implementieren Sie OpenSource-Bausteine für die Phoenix-Produktfamilie.
- In agilen Entwicklungsmethoden fühlen Sie sich zu Hause und treiben im Team die Softwareentwicklung nebst Deployment und Betrieb voran.
- Ihre Arbeitsweise orientiert sich am Clean Code und Sie sichern die Qualität Ihrer Ergebnisse durch Softwaretests.
DAS BRINGEN SIE MIT
- Erfahrung in der Systemadministration komplexer Lösungen
- Breite Kenntnisse in IT-Systemen, Applikationen/Software/Netzwerk
- Know-how in Open-Source-Lösungen
- Erfahrung mit den vorhandenen Applikationen sind hilfreich:
- Datenbanken, Containertechnologien, Microservices, Terraform, Ansible, Python
"""
job = app_classes.Job("DevOps Engineer - Open Source", job_description, "www.stepstone.de")

adviser = app_classes.Adviser_Bot(candidate, recrutier, job, "german")
print(adviser.show_user_input())
print()
print("SHORT DESCRIPTION FOR CV:")
print(adviser.generate_cv_short_description())
time.sleep(2)
print()
print("COVER LETTER:")
print(adviser.generate_letter())