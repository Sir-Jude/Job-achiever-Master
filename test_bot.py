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
    "Nicolas", "Tesla", "male", "Elli - a brand of the Volkswagen Group", "CEO", "Berlinerstr. 11b, 39124 Berlin"
)
recruiter.set_atitude("arogant")

job_description = """
What the candidate will do
- Actively learn and be always up-to-date with the industry trends and developments 
- You will be part of an agile and independent team with end to end responsibility for a product
- Design, build and operate scalable production systems
- Advocate for maintaining a high quality bar, making sure quality and testing are part of the development work from day one
- Contribute to the team's effectiveness and efficiency through setting an example of best SW development practices
- Contribute in one of our Communities of Practice 

What the candidate has
- Experience in developing high quality software in one of the modern programming languages (TypeScript, Python, Go, Ruby, etc.) 
- Experience in modern software development tools and systems including Git, Bash, Docker, Linux
- Experience with automated software testing, Continuous Integration and Continuous Delivery practices
- Readiness to work in cross-functional agile teams
- Knowledge in design patterns, data structures and algorithms
- Passion for continuous improvement, technical and operational excellence
- Passion and eagerness to learn different tools, technologies and practices that are needed to get the job done

Ideally the candidate has
- Experience in Typescript
- Experience with one of the leading public clouds (GCP, AWS, Azure) preferably GCP
- Experience in infrastructure provisioning tools like Terraform
- Experience in modern software development and delivery practices including Cloud Native and Microservices architecture, Everything as Code and Test Driven Development
- Experience in working in true DevOps teams where “you build it, you run it”
- Experience in EV charging field
"""
job = app_classes.Job(
    "Software Engineer Backend", job_description, "www.stepstone.de"
)

adviser = app_classes.Adviser_Bot(candidate, recruiter, job, "english")

os.system('clear')
print("==============================================================================")
print(adviser.show_user_input())
print("==============================================================================")
print()
"""input("Ready for Resume and Coer Letter? ")
os.system('clear')
print("SHORT DESCRIPTION FOR CV:")
print(adviser.generate_cv_short_description())
print("==============================================================================")
time.sleep(2)
print()
print("COVER LETTER:")
print(adviser.generate_letter())"""
input("Ready for interview? ")
os.system('clear')
# A real interview simulation:
os.system('clear')
print(f"{recruiter.name}: Welcome {candidate.name}.")
interview_on = True
while interview_on:
    user_message = input(f'{candidate.name}: ')
    bot_message = adviser.simulate_recruiter(recruiter, user_message)
    os.system('clear')
    # print interview_history
    for m in adviser.interview_history[1:]:
        if m["role"] == "assistant":
            person = recruiter.name
        else:
            person = candidate.name
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
