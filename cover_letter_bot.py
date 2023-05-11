import os
import openai
import json
import tkinter as tk # used to choose where file is saved
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO # needed to save letter as pdf

openai.api_key = "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"

def get_user_info():   # to be edited - need the user input from user_input file
     with open('candidate.json', 'r') as file:
        data = json.load(file)
    
        name = data['name']
        family_name = data['family_name']
        birthday = data['birthday']
        sex = data['sex']
        phone = data['phone']
        email = data['email']
        adress = data['adress']
        experience = data['experience']
        studies = data['studies']
        hobbies = data['hobbies']
        skills = data['skills']
        languages = data['languages']
        user_language = data['user_language']
        short_description = data['short_description']

        return name, family_name, birthday, sex, phone, email, adress, experience, studies, hobbies, skills, languages, user_language, short_description

def get_job_info(): # just for testing at the moment
    with open('recruiter.json','r') as file:
        data = json.load(file)

        recruiter_name = data['name']
        recruiter_family_name = data['family_name']
        company = data['company']
        company_adress = data['company_adress']

        return recruiter_name, recruiter_family_name, company, company_adress


def generate_cover_letter(name, family_name, birthday, sex, phone, email, adress, experience, studies, hobbies, skills, languages, user_language, short_description, recruiter_name, recruiter_family_name, company, company_adress, position = "backend developer"): #generates the cover letter 
    prompt = f"""
    Applicant name: {name} {family_name}
    Applicant age: {birthday}
    Applicant sex: {sex}
    Applicant address: {adress}
    Applicant phone : {phone}
    Applicant email: {email}
    Applicant past studies : {studies}
    Company name: {company}
    Company adress:{company_adress}
    Hiring manager name: {recruiter_name} {recruiter_family_name}
    Position: {position}
    Past job experience: {experience}
    Hobbies: {hobbies}
    Skills: {skills}
    Languages: {languages}
    Short description: {short_description}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates cover letters."},
            {"role": "user", "content": "Given the following details, please generate a cover letter."},
            {"role": "assistant", "content": prompt}
        ],
    )

    cover_letter = response['choices'][0]['message']['content'].strip()
    return cover_letter

def save_cover_letter_as_txt(cover_letter, directory, filename): # if user chooses to save as txt.
    with open(filename, 'w') as f:
        f.write(cover_letter)


def save_cover_letter_as_pdf(cover_letter, directory, filename):    # saves file as pdf if chosen
    file_path = os.path.join(directory, filename)
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    style = styles["Normal"]

    cover_letter_lines = cover_letter.split("\n")
    cover_letter_paragraphs = []
    for index, line in enumerate(cover_letter_lines):
        cover_letter_paragraphs.append(Paragraph(line, style))
        if index < len(cover_letter_lines) - 1:
            cover_letter_paragraphs.append(Spacer(1, 12))

    doc.build(cover_letter_paragraphs)


def choose_directory(): # GUI to choose where file is saved
    root = tk.Tk()
    root.withdraw()  # Hides the root window
    directory = filedialog.askdirectory(title="Choose the directory where you want to save the cover letter")
    return directory

def main():
    name, family_name, birthday, sex, phone, email, adress, experience, studies, hobbies, skills, languages, user_language, short_description = get_user_info()
    recruiter_name, recruiter_family_name, company, company_adress = get_job_info()
    cover_letter = generate_cover_letter(name, family_name, birthday, sex, phone, email, adress, experience, studies, hobbies, skills, languages, user_language, short_description, recruiter_name, recruiter_family_name, company, company_adress)
    print("\nGenerated cover letter:\n")
    print(cover_letter)

    root = tk.Tk()                                      # lets the user edit the cover letter
    text_widget = tk.Text(root, width=80, height=24)
    text_widget.pack()
    text_widget.insert('end', cover_letter)
    print("\nPlease edit your cover letter in the opened window and close it when you're done.\n")

    def on_close():
        global edited_cover_letter
        edited_cover_letter = text_widget.get('1.0', 'end')
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

    cover_letter = edited_cover_letter

    output_format = ''
    while output_format.lower() not in ['pdf', 'txt']:
        output_format = input("\nChoose the output format (PDF or TXT): ")

    directory = choose_directory()
    filename = f"cover_letter_{name}.{output_format.lower()}"

    if output_format.lower() == 'pdf':
        save_cover_letter_as_pdf(cover_letter, directory, filename)
    else:
        save_cover_letter_as_txt(cover_letter, directory, filename)

    print(f"\nCover letter saved as '{os.path.join(directory, filename)}'")

if __name__ == "__main__":
    main()
