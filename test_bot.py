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

adviser = app_classes.Adviser_Bot(candidate, recrutier, job, "english")
print(adviser.show_user_input())
print("==============================================================================")
print()
print("SHORT DESCRIPTION FOR CV:")
print(adviser.generate_cv_short_description())
print("==============================================================================")
time.sleep(2)
print()
print("COVER LETTER:")
print(adviser.generate_letter())

# A fake interview
interview = "Recrutier: Tell me something about yourself\n"
interview += "Candidate: I am Adrian and I'm working for more than 15 years in webdesign area.\n"
interview += "Recrutier: How did you hear about this position?\n"
interview += "Candidate: After I search for a while for a good job on internet, I found your job proposal on stepstone.de\n"
interview += "Recrutier: Why did you decide to apply for this position?\n"
interview += "Candidate: I'm very passionate about Python and programing. In fact, I have some experience achieved doin some projects in my Python cours.\n"
interview += "Recrutier: What are your biggest strengths?\n"
interview += "Candidate: I am a logical and detail-oriented person. Even when I'm at intermediate level at english, I'm a good comunicator and team player.\n"
interview += "Recrutier: What is your biggest weakness?\n"
interview += "Candidate: Well, as a recent graduate of DCI, I'd say my biggest weakness is the lack of real-life work experience. I am, however, willing to do my best and catch up as fast as I can.\n"
interview += "Recrutier: Why should we hire you?\n"
interview += "Candidate: I just think I meet your requirements for this job.\n"
interview += "Recrutier: What are your salary requirements?\n"
interview += "Candidate: My salary expectation is around $70,000 annually.\n"
interview += "Recrutier: Do you have any questions for us?\n"
interview += "Candidate: What is the next step in the hiring process?\n"
interview += "Recrutier: Well, if you'll be chosen, than you'll receive a trial period contract.\n"
interview += "Candidate: Thank you for the interview oportunity.\n"
interview += "Recrutier: Wellcome. Have a good day.\n"
print("==============================================================================")
time.sleep(2)
print()
print("INTERVIEW ANALYSE:")
print(adviser.analize_interview(interview))