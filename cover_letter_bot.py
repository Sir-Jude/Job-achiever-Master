import os
import json
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import tkinter as tk
from tkinter import filedialog

def load_cover_letter():
    # Function to load the cover letter from a JSON file
    with open("json/letter.json", "r") as file:
        data = json.load(file)
        return (
            data["candidate_name"],
            data["candidate_surname"],
            data["candidate_email"],
            data["candidate_address"],
            data["recruiter_surname"],
            data["recruiter_email"],
            data["recruiter_address"],
            data["position"],
            data["company"],
            data["mail_body"],
        )

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
    company,
    recruiter_surname,
):
    
    file_path = os.path.join(directory, filename)
       
       # Create a simple document template
    doc = SimpleDocTemplate(file_path, pagesize=letter)

    # Create a style sheet
    styles = getSampleStyleSheet()
    styles["Normal"].spaceAfter = 12

    # Create custom styles for right-aligned text
    right_aligned_style = ParagraphStyle("RightAlign")
    right_aligned_style.alignment = 2  # 2 is for right alignment

    # Create custom styles for left-aligned text
    left_aligned_style = ParagraphStyle("LeftAlign")

    # Create multiple paragraphs for sender address
    sender_paragraphs = [
        Paragraph(sender_address, right_aligned_style)
    ]

    # Create multiple paragraphs for recipient address
    recipient_paragraphs = [
        Paragraph(recipient_address, left_aligned_style)
    ]

    # Create a paragraph with the current date
    date_paragraph = Paragraph(str(current_date), right_aligned_style)

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

    print(f"\nCover letter saved as '{os.path.join(directory, filename)}'")


def choose_directory():
    # Function to open a dialog for the user to choose a directory
    root = tk.Tk()
    root.withdraw()  # Hides the root window
    directory = filedialog.askdirectory(
        title="Choose the directory where you want to save the cover letter"
    )
    return directory

def generate():
    # Load the cover letter
    (
        name,
        surname,
        email,
        adress,
        recruiter_surname,
        recruiter_email,
        recruiter_adress,
        position,
        company,
        cover_letter,
    ) = load_cover_letter()

    sender_address = adress
    recipient_address = recruiter_adress
    current_date = date.today().strftime("%d.%m.%Y")
    subject_line = f"Application for the position as {position}"

    print("\nLoaded cover letter:\n")

    directory = choose_directory()
    filename = f"cover_letter_{name}.pdf"

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
        company,
        recruiter_surname,
    )

    print(f"\nCover letter saved as '{os.path.join(directory, filename)}'")

