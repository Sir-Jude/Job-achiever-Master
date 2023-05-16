import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
import tkinter as tk
from tkinter import filedialog
import textwrap


class Resume:
    def __init__(self, file, rich_gold_color, night_gray_color, pure_white_color):

        # Open JSON file in reader mode
        with open(file, 'r') as f:
            self.data = json.load(f)

        # Check if the 'name' key exists and has a value
        if 'name' not in self.data or not self.data['name']:
            raise ValueError("Missing or invalid 'name' value in JSON file")
        
        # Create a PDF file
        self.pdf_file_name = f"pdfs/{self.data['name']}_{self.data['surname']}_CV.pdf"
        self.pdf = canvas.Canvas(self.pdf_file_name)

        self.rich_gold_color = rich_gold_color
        self.night_gray_color = night_gray_color
        self.pure_white_color = pure_white_color

    # Create a genarate method to generate a CV
    def generate(self):

        # Set the background color
        self.pdf.setFillColor(self.pure_white_color)

        # Draw a rectangle that covers the entire page
        self.pdf.rect(0,0, letter[0], letter[1], fill=True, stroke=False)

        # Set up font color and style for RESUME
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica-Bold', 16)
        self.pdf.drawString(240, 800, 'RESUME')

        # Upload a photo 
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path:
            photo = ImageReader(file_path)
            self.pdf.drawImage(photo, 400, 645, width=1.5*inch, height=1.7*inch)

        # Set up parameters for personal information section
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 12)
        self.pdf.drawString(50, 750, 'Name:')
        self.pdf.drawString(130, 750, self.data['name'])
        self.pdf.drawString(50, 735, 'Family Name:')
        self.pdf.drawString(130, 735, self.data['surname'])
        self.pdf.drawString(50, 720, 'Birthday:')
        self.pdf.drawString(130, 720, self.data['birthday'])
        self.pdf.drawString(50, 705, 'Sex:')
        self.pdf.drawString(130, 705, self.data['sex'])
        self.pdf.drawString(50, 690, 'Phone:')
        self.pdf.drawString(130, 690, self.data['phone'])
        self.pdf.drawString(50, 675, 'Email:')
        self.pdf.drawString(130, 675, self.data['email'])
        self.pdf.drawString(50, 660, 'Address:')
        self.pdf.drawString(130, 660, self.data['address'])
        self.pdf.drawString(50, 645, 'Language:')
        self.pdf.drawString(130, 645, self.data['user_language'])
        self.pdf.drawString(50, 630, 'Motivation:')
        y_offset = 630
        motivation = self.data['short_description']
        wrapped_text = textwrap.fill(motivation, 77)
        lines = wrapped_text.split('\n')
        for line in lines:
            self.pdf.drawString(130, y_offset, line)
            y_offset -= 15
                            
        # Set up parameters for Experience section
        y_offset -= 30 
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 14)
        self.pdf.drawString(240, y_offset, 'Experience:')
        y_offset -= 50
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 12)
        for exp in self.data['experience']:
            self.pdf.drawString(50, y_offset, 'Title:')
            self.pdf.drawString(130, y_offset, exp['title'])
            self.pdf.drawString(50, y_offset - 15, 'Description:')
            description = exp['description']
            wrapped_text = textwrap.fill(description, 77)  # Wrap description text to 80 characters per line
            lines = wrapped_text.split('\n')  # Split the wrapped text into lines
            for line in lines:
                self.pdf.drawString(130, y_offset - 15, line)
                y_offset -= 15  # Decrease the y_offset for each line
            self.pdf.setFillColor(self.night_gray_color)
            self.pdf.setFont('Helvetica', 12)
            self.pdf.drawString(50, y_offset - 30, 'Company:')
            self.pdf.drawString(130, y_offset - 30, exp['company'])
            self.pdf.drawString(50, y_offset - 45, 'Start Date:')
            self.pdf.drawString(130, y_offset - 45, exp['date_start'])
            self.pdf.drawString(50, y_offset - 60, 'End Date:')
            self.pdf.drawString(130, y_offset - 60, exp['date_end'])
            y_offset -= 75

        #Set up parameters for Education section
        y_offset -= 30
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 14)
        self.pdf.drawString(240, y_offset, 'Education:')
        y_offset -= 50
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 12)
        for study in self.data['education']:
            self.pdf.drawString(50, y_offset, 'Title:')
            self.pdf.drawString(130, y_offset, study['title'])
            self.pdf.drawString(50, y_offset - 15, 'Description:')
            description = exp['description']
            wrapped_text = textwrap.fill(description, 77)  # Wrap description text to 80 characters per line
            lines = wrapped_text.split('\n')  # Split the wrapped text into lines
            for line in lines:
                self.pdf.drawString(130, y_offset - 15, line)
                y_offset -= 15  # Decrease the y_offset for each line
            #self.pdf.drawString(130, y_offset - 15, study['description'])
            self.pdf.drawString(50, y_offset - 30, 'School:')
            self.pdf.drawString(130, y_offset -30, study['school'])
            self.pdf.drawString(50, y_offset - 45, 'Start Date:')
            self.pdf.drawString(130, y_offset - 45, study['date_start'])
            self.pdf.drawString(50, y_offset - 60, 'End Date:')
            self.pdf.drawString(130, y_offset - 60, study['date_end'])
            y_offset -= 75

        #Set up parameters for Hobbies section
        y_offset -= 30
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 14)
        self.pdf.drawString(240, y_offset, 'Hobbies:')
        y_offset -= 50
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 12)
        for hobby in self.data['hobbies']:
            self.pdf.drawString(50, y_offset, hobby['hobby'])
            y_offset -= 17

        #Set up parameters for Skills section
        y_offset -= 30
        # Check if there is enough space on the current page
        if y_offset < 100:
            self.pdf.showPage()  # Create a new page
            y_offset = 750  # Reset the y_offset for the new page
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 14)
        self.pdf.drawString(240, y_offset, 'Skills:')
        y_offset -= 50
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 12)
        for skill in self.data['skills']:
            # Check if there is enough space on the current page
            if y_offset < 60:
                self.pdf.showPage()  # Create a new page
                y_offset = 750  # Reset the y_offset for the new page
            self.pdf.drawString(50, y_offset, skill['skill'])
            y_offset -= 17

        #Set up parameters for Languages section
        y_offset -= 30
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 14)
        self.pdf.drawString(240, y_offset, 'Languages:')
        y_offset -= 50
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 12)
        for language in self.data['languages']:
            self.pdf.drawString(50, y_offset, language['language'])
            y_offset -= 17

        self.pdf.save()
