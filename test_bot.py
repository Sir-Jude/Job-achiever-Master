import os
import app_classes
import app_functions
import time

candidate = app_classes.Candidate(
    "Adrian",
    "Radu",
    "11.03.1977",
    "male",
    "0123456789",
    "adrian@email.de",
    "Ritterstr. 11b, 39124 Magdeburg",
)
experience_1 = app_classes.Experience(
    "Webdesigner",
    "Responsable for mentenance of the company websites.",
    "IATOM",
    "10.10.2010",
    "23.09.2022",
)
candidate.add_experience(experience_1)
experience_2 = app_classes.Experience(
    "Art Director",
    "Cration and implementing of web ads.",
    "Stream Line",
    "01.01.2000",
    "10.10.2010",
)
candidate.add_experience(experience_2)
experience_3 = app_classes.Experience(
    "Janitor", "Cleaning of office rooms.", "Amazon", "01.01.1998", "01.01.2000"
)
candidate.add_experience(experience_3)
study_1 = app_classes.Study(
    "Python Backend Programming", "Cours", "DCI", "15.12.2022", "10.01.2024"
)
candidate.add_studies(study_1)
study_2 = app_classes.Study(
    "Graphic designer",
    "Barcelors degree",
    "University of Arts - Nicolae Grigorescu - Bucharest",
    "01.09.1995",
    "01.01.2000",
)
candidate.add_studies(study_2)
candidate.add_hobbies("music")
candidate.add_hobbies("reading")
candidate.add_skills("English (B1 - lower intermediate)")
candidate.add_skills("Python, PHP, mySQL")

recruiter = app_classes.Recruiter(
    "Nicolas", "Tesla", "male", "Dataport AöR", "CEO", "Berlinerstr. 11b, 39124 Berlin"
)
recruiter.set_atitude("arogant")

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
job = app_classes.Job(
    "DevOps Engineer - Open Source", job_description, "www.stepstone.de"
)

adviser = app_classes.Adviser_Bot(candidate, recruiter, job, "english")

"""print("==============================================================================")
print(adviser.show_user_input())
print("==============================================================================")
print()
print("SHORT DESCRIPTION FOR CV:")
print(adviser.generate_cv_short_description())
print("==============================================================================")
time.sleep(2)
print()
print("COVER LETTER:")
print(adviser.generate_letter())"""

# A real interview simulation:
os.system('clear')
print(f"{recruiter.name}: Welcome {candidate.name}.")
interview_on = True
while interview_on:
    user_message = input(f'{candidate.name}: ')
    bot_message = adviser.simulate_recruiter(recruiter, job, user_message)
    adviser.interview_history.append(app_functions.bot_message("assistant", bot_message))
    os.system('clear')
    # print(interview_history)
    for m in adviser.interview_history[1:]:
        if adviser.interview_history.index(m)%2 == 0:
            person = candidate.name
        else:
            person = recruiter.name
        print(f'{person}: {m["content"]}')
        if m["content"] == "EXIT":
            interview_on = False


# An interview analyse
interview = ""
for m in adviser.interview_history[1:]:
    if adviser.interview_history.index(m)%2 == 0:
        person = "Candidate"
    else:
        person = "Recruiter"
    interview += f"{person}: {m['content']}\n"
print("==============================================================================")
time.sleep(2)
print()
print("INTERVIEW ANALYSE:")
print(adviser.analize_interview(interview))
