import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader


class Resume:
    def __init__(self, file, rich_gold_color, night_gray_color, pure_white_color, photo = None):
        with open(file, 'r') as f:
            self.data = json.load(f)

        # Check if the 'name' key exists and has a value
        if 'name' not in self.data or not self.data['name']:
            raise ValueError("Missing or invalid 'name' value in JSON file")
        
        self.pdf_file_name = f"{self.data['name']}_{self.data['family_name']}_CV.pdf"
        self.pdf = canvas.Canvas(self.pdf_file_name)
        self.rich_gold_color = rich_gold_color
        self.night_gray_color = night_gray_color
        self.pure_white_color = pure_white_color
        self.photo = photo

    def generate(self):
        #Set the background color
        self.pdf.setFillColor(self.pure_white_color)

        #Draw a rectangle that covers the entire page
        self.pdf.rect(0,0, letter[0], letter[1], fill=True, stroke=False)

        if self.photo:
            # Draw the photo on the top right corner
            photo_width, photo_height = (2.5*inch, 2.5*inch)
            x = letter[0] - photo_width - inch
            y = letter[1] - photo_height - inch
            self.pdf.drawImage(ImageReader(self.photo), x, y, width=photo_width, height=photo_height, preserveAspectRatio=True)

        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica-Bold', 18)
        self.pdf.drawString(240, 800, 'RESUME')

        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 14)
        self.pdf.drawString(50, 750, 'Name: ' + self.data['name'])
        self.pdf.drawString(50, 735, 'Family Name: ' + self.data['family_name'])
        self.pdf.drawString(50, 720, 'Birthday: ' + self.data['birthday'])
        self.pdf.drawString(50, 705, 'Sex: ' + self.data['sex'])
        self.pdf.drawString(50, 690, 'Phone: ' + self.data['phone'])
        self.pdf.drawString(50, 675, 'Email: ' + self.data['email'])
        self.pdf.drawString(50, 660, 'Address: ' + self.data['adress'])

        y_offset = 600
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 16)
        self.pdf.drawString(50, y_offset, 'Experience:')
        y_offset -= 15
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 14)
        for exp in self.data['experience']:
            self.pdf.drawString(70, y_offset, 'Title: ' + exp['title'])
            self.pdf.drawString(70, y_offset - 15, 'Description: ' + exp['description'])
            self.pdf.drawString(70, y_offset - 30, 'Company: ' + exp['company'])
            self.pdf.drawString(70, y_offset - 45, 'Start Date: ' + exp['date_start'])
            self.pdf.drawString(70, y_offset - 60, 'End Date: ' + exp['date_end'])
            y_offset -= 75

        y_offset -= 15
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 16)
        self.pdf.drawString(50, y_offset, 'Studies:')
        y_offset -= 15
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 14)
        for study in self.data['studies']:
            self.pdf.drawString(70, y_offset, 'Title: ' + study['title'])
            self.pdf.drawString(70, y_offset - 15, 'Description: ' + study['description'])
            self.pdf.drawString(70, y_offset - 30, 'School: ' + study['school'])
            self.pdf.drawString(70, y_offset - 45, 'Start Date: ' + study['date_start'])
            self.pdf.drawString(70, y_offset - 60, 'End Date: ' + study['date_end'])
            y_offset -= 75

        y_offset -= 15
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 16)
        self.pdf.drawString(50, y_offset, 'Hobbies:')
        y_offset -= 15
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 14)
        for hobby in self.data['hobbies']:
            self.pdf.drawString(70, y_offset, hobby['hobby'])
            y_offset -= 15

        y_offset -= 15
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 16)
        self.pdf.drawString(50, y_offset, 'Skills:')
        y_offset -= 15
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 14)
        for skill in self.data['skills']:
            self.pdf.drawString(70, y_offset, skill['skill'])
            y_offset -= 15

        y_offset -= 15
        self.pdf.setFillColor(self.rich_gold_color)
        self.pdf.setFont('Helvetica', 16)
        self.pdf.drawString(50, y_offset, 'Languages:')
        y_offset -= 15
        self.pdf.setFillColor(self.night_gray_color)
        self.pdf.setFont('Helvetica', 14)
        for language in self.data['languages']:
            self.pdf.drawString(70, y_offset, language['language'])
            y_offset -= 15

        self.pdf.save()

<<<<<<< HEAD
resume = Resume('json/candidate.json', HexColor("#D4AF37"), HexColor("#404040"), HexColor("#FFFFFF"))
=======
resume = Resume('json/candidate.json')
>>>>>>> origin
resume.generate()