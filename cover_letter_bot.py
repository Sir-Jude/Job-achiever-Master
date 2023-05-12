import os
import openai
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

import json
from datetime import date
from reportlab.lib.pagesizes import letter  # for specifying PDF page size
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)  # for creating elements in PDF
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)  # for creating styles in PDF
import tkinter as tk  # for creating graphical user interfaces
from tkinter import filedialog  # for file dialog in tkinter

openai.api_key = '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'

def get_user_info():
    jsonname = input("Enter your first name: ")
    # Function to get user information
    with open(f"json/{jsonname}.json", "r") as file:
        data = json.load(file)
        return (
            data["Last Name"],
            data["First Name"],
            data["D.O.B."],
            #data["sex"],
            data["Phone"],
            data["Email"],
            data["Address"],
            data["Work Experience"],
            data["Education"],
            data["Hobbies"],
            data["Skills"],
            data["Languages"],
            data["About"],
        )


def get_job_info():
    # Function to get job information
    with open("json/job.json", "r") as file:
        data = json.load(file)
        return data["position"]


def get_recruiter_info():
    # Function to get recruiter info
    with open("json/recruiter.json", "r") as file:
        data = json.load(file)
        return (
            data["name"],
            data["surname"],
            data["company"],
            data["company_adress"],
        )


def generate_cover_letter(
    surname,
    name,
    birthday,
    phone,
    email,
    adress,
    experience,
    education,
    hobbies,
    skills,
    languages,
    short_description,
    recruiter_name,
    recruiter_surname,
    company,
    company_adress,
    position,
):
    # Function to generate a cover letter using the OpenAI API
    prompt = f"""
    Applicant name: {surname} {name}
    Applicant age: {birthday}
    Applicant address: {adress}
    Applicant phone : {phone}
    Applicant email: {email}
    Applicant past studies : {education}
    Company name: {company}
    Company adress:{company_adress}
    Hiring manager name: {recruiter_name} {recruiter_surname}
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
            {
                "role": "system",
                "content": """You are a cover letter creator for jobs.
                Based on the input you receive, you will compose the content of a cover letter for the desired job based only on the data provided.
                Don't provide any results other than the cover letter.
                Don't mention unnecessary information from my experience or education.
                Write the text of the letter in {user_language} in a style suitable for the job to which the candidate is applying.
                You don't ask questions or say anything other than the content of the cover letter."""
            },
            {
                "role": "user",
                "content": prompt,
            },
            
        ],
    )
    return response["choices"][0]["message"]["content"].strip()


def save_cover_letter_as_pdf(
    cover_letter,
    directory,
    filename,
    sender_address,
    recipient_address,
    current_date,
    subject_line,
    name,
    surname,
    email,
    phone,
    company,
    recruiter_name,
    recruiter_surname,
):
    # Function to save the cover letter as a PDF file
    file_path = os.path.join(directory, filename)

    # Create a simple document template
    doc = SimpleDocTemplate(file_path, pagesize=letter)

    # Create a style sheet
    styles = getSampleStyleSheet()

    # Set the space after the paragraph to 12 for 'Normal' style
    styles["Normal"].spaceAfter = 12

    # Create custom styles for right-aligned text
    right_aligned_style = ParagraphStyle("RightAlign")
    right_aligned_style.alignment = 2  # 2 is for right alignment

    # Create custom styles for left-aligned text
    left_aligned_style = ParagraphStyle("LeftAlign")

    # Split the sender and recipient addresses into multiple lines
    sender_address_lines = sender_address.split(", ")
    recipient_address_lines = recipient_address.split(", ")

    # Create multiple paragraphs for sender address
    sender_paragraphs = [
        Paragraph(line, right_aligned_style)
        for line in [f"{surname} {name}"] + sender_address_lines + [email, phone]
    ]

    # Create multiple paragraphs for recipient address
    recipient_paragraphs = [
        Paragraph(line, left_aligned_style)
        for line in [company, f"{recruiter_name} {recruiter_surname}"]
        + recipient_address_lines
    ]

    # Create a paragraph with the current date
    date_paragraph = Paragraph(f"{str(current_date)}", right_aligned_style)

    # Create a paragraph with the subject line
    subject_paragraph = Paragraph(subject_line, styles["Heading1"])
    subject_paragraph.spaceAfter = 12

    # Create a spacer
    spacer = Spacer(1, 12)

    # Create paragraphs with the cover letter content
    cover_letter_paragraphs = [
        Paragraph(line, styles["Normal"])
        for line in cover_letter.split("\n")
        if line.strip() != ""
    ]

    # Build the document with the elements
    elements = (
        sender_paragraphs
        + [spacer]
        + recipient_paragraphs
        + [spacer, date_paragraph, spacer, subject_paragraph, spacer]
        + cover_letter_paragraphs
    )
    doc.build(elements)


def choose_directory():
    # Function to open a dialog for the user to choose a directory
    root = tk.Tk()
    root.withdraw()  # Hides the root window
    directory = filedialog.askdirectory(
        title="Choose the directory where you want to save the cover letter"
    )
    return directory


def generate():
    # Main function
    # Get user and job info
    (
        name,
        surname,
        birthday,
        phone,
        email,
        adress,
        experience,
        education,
        hobbies,
        skills,
        languages,
        short_description,
    ) = get_user_info()
    (
        recruiter_name,
        recruiter_surname,
        company,
        company_adress,
    ) = get_recruiter_info()
    position = get_job_info()

    # Generate cover letter
    cover_letter = generate_cover_letter(
        name,
        surname,
        birthday,
        phone,
        email,
        adress,
        experience,
        education,
        hobbies,
        skills,
        languages,
        short_description,
        recruiter_name,
        recruiter_surname,
        company,
        company_adress,
        position,
    )

    sender_address = adress
    recipient_address = company_adress
    current_date = date.today()
    subject_line = f"Application for the position as {position}"

    print("\nGenerated cover letter:\n")
    print(cover_letter)

    root = tk.Tk()  # lets the user edit the cover letter
    text_widget = tk.Text(root, width=80, height=24)
    text_widget.pack()
    text_widget.insert("end", cover_letter)
    print(
        "\nPlease edit your cover letter in the opened window and close it when you're done.\n"
    )

    def on_close():
        # Function to handle the event when the window is closed
        global edited_cover_letter
        edited_cover_letter = text_widget.get("1.0", "end")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

    cover_letter = edited_cover_letter

    output_format = "PDF"

    directory = choose_directory()
    filename = f"cover_letter_{name}.{output_format.lower()}"

    # Save cover letter as PDF
    save_cover_letter_as_pdf(
        cover_letter,
        directory,
        filename,
        sender_address,
        recipient_address,
        current_date,
        subject_line,
        name,
        surname,
        email,
        phone,
        company,
        recruiter_name,
        recruiter_surname,
    )

    print(f"\nCover letter saved as '{os.path.join(directory, filename)}'")
