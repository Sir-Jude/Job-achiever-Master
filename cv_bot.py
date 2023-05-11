import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch



class Resume:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.data = json.load(f)
        self.pdf = canvas.Canvas('candidate.pdf')

    def generate(self):
        self.pdf.setFont('Helvetica', 12)
        self.pdf.drawString(240, 800, 'RESUME')

        self.pdf.setFont('Helvetica', 10)
        self.pdf.drawString(50, 750, 'Name: ' + self.data['name'])
        self.pdf.drawString(50, 735, 'Family Name: ' + self.data['family_name'])
        self.pdf.drawString(50, 720, 'Birthday: ' + self.data['birthday'])
        self.pdf.drawString(50, 705, 'Sex: ' + self.data['sex'])
        self.pdf.drawString(50, 690, 'Phone: ' + self.data['phone'])
        self.pdf.drawString(50, 675, 'Email: ' + self.data['email'])
        self.pdf.drawString(50, 660, 'Address: ' + self.data['adress'])

        y_offset = 600
        self.pdf.drawString(50, y_offset, 'Experience:')
        y_offset -= 15
        for exp in self.data['experience']:
            self.pdf.drawString(70, y_offset, 'Title: ' + exp['title'])
            self.pdf.drawString(70, y_offset - 15, 'Description: ' + exp['description'])
            self.pdf.drawString(70, y_offset - 30, 'Company: ' + exp['company'])
            self.pdf.drawString(70, y_offset - 45, 'Start Date: ' + exp['date_start'])
            self.pdf.drawString(70, y_offset - 60, 'End Date: ' + exp['date_end'])
            y_offset -= 75

        y_offset -= 15
        self.pdf.drawString(50, y_offset, 'Studies:')
        y_offset -= 15
        for study in self.data['studies']:
            self.pdf.drawString(70, y_offset, 'Title: ' + study['title'])
            self.pdf.drawString(70, y_offset - 15, 'Description: ' + study['description'])
            self.pdf.drawString(70, y_offset - 30, 'School: ' + study['school'])
            self.pdf.drawString(70, y_offset - 45, 'Start Date: ' + study['date_start'])
            self.pdf.drawString(70, y_offset - 60, 'End Date: ' + study['date_end'])
            y_offset -= 75

        y_offset -= 15
        self.pdf.drawString(50, y_offset, 'Hobbies:')
        y_offset -= 15
        for hobby in self.data['hobbies']:
            self.pdf.drawString(70, y_offset, hobby['hobby'])
            y_offset -= 15

        y_offset -= 15
        self.pdf.drawString(50, y_offset, 'Skills:')
        y_offset -= 15
        for skill in self.data['skills']:
            self.pdf.drawString(70, y_offset, skill['skill'])
            y_offset -= 15

        y_offset -= 15
        self.pdf.drawString(50, y_offset, 'Languages:')
        y_offset -= 15
        for language in self.data['languages']:
            self.pdf.drawString(70, y_offset, language['language'])
            y_offset -= 15

        self.pdf.save()

# resume = Resume('candidate.json')
# resume.generate()