import os
import openai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO # needed to save letter as pdf

openai.api_key = "input API key"

def get_user_input():   # give info to AI to put in cover letter
    name = input("Enter your name: ")
    company = input("Enter the company name: ")
    hiring_manager = input("Enter the hiring manager's name (leave empty if unknown): ")
    age = input("Enter your age: ")
    position = input("Enter the position you are applying for: ")
    experience = input("Enter your past job experience: ")
    language = input("Enter the language for you cover letter: ")
    return name, company, hiring_manager, age, position, experience, language

def generate_cover_letter(name, company, hiring_manager, age, position, experience, language):
    prompt = f"Write a cover letter for a job application in the given {language} using the following details:\n\nApplicant name: {name}\nCompany name: {company}\nHiring manager name: {hiring_manager}\nApplicant age: {age}\nPosition: {position}\nPast job experience: {experience}\n\nCover Letter:"


    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates cover letters."},
            {"role": "user", "content": prompt}
        ],
    )

    cover_letter = response['choices'][0]['message']['content'].strip()
    return cover_letter

def save_cover_letter_as_txt(cover_letter, filename): # if user chooses to save as txt.
    with open(filename, 'w') as f:
        f.write(cover_letter)

def save_cover_letter_as_pdf(cover_letter, filename): # if user chooses to save as pdf
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)
    textobject = c.beginText(50, 750)
    for line in cover_letter.split("\n"):
        textobject.textLine(line)
    c.drawText(textobject)
    c.showPage()
    c.save()
    buffer.seek(0)
    with open(filename, "wb") as f:
        f.write(buffer.read())

def main():
    name, company, hiring_manager, age, position, experience, language = get_user_input()
    cover_letter = generate_cover_letter(name, company, hiring_manager, age, position, experience,language)
    print("\nGenerated cover letter:\n")
    print(cover_letter)

    output_format = ''
    while output_format.lower() not in ['pdf', 'txt']:
        output_format = input("\nChoose the output format (PDF or TXT): ")

    filename = f"cover_letter_{name}_{position}.{output_format.lower()}"

    if output_format.lower() == 'pdf':
        save_cover_letter_as_pdf(cover_letter, filename)
    else:
        save_cover_letter_as_txt(cover_letter, filename)

    print(f"\nCover letter saved as '{filename}'")

if __name__ == "__main__":
    main()