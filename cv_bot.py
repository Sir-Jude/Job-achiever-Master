import openai
import os
from fpdf import FPDF
from user_input import User
import requests
from io import BytesIO
from PIL import Image

openai.api_key = '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'

#Generate an image
response = openai.Image.create(
  prompt="the best python programmer ever",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)

# Download the image data from the URL
response = requests.get(image_url)
image_data = BytesIO(response.content)

# Open the image data with Pillow and save it as a PNG file
image = Image.open(image_data)
image.save("output.png", format="PNG")

pdf = FPDF()

# Add a page
pdf.add_page()

#Logo
pdf.image('output.png', 0, 0, 35)

# Set the font and font size
pdf.set_font("Arial", 'B', size=20)

#create a cell
pdf.cell(200, 10, txt = 'GROUP CHARLIE ', ln = 1, align = 'C')

#add another cell
pdf.cell(200, 10, txt = 'A very simple PDF file', ln = 2, align = 'C')

#add another cell
pdf.set_font("Arial", 'B', size=18)
pdf.cell(200, 20, txt = 'Group members:', ln = 2, align = 'L')
members = ['Giulio', 'Spencer', 'Connor', 'Kyrylo', 'Adrian', 'Mathias', 'Semen']
for member in members:
    pdf.set_font('Arial', size=16)
    pdf.cell(200, 10, txt = member, border = 1, ln = 2, align = 'L',)

# Save the PDF file
pdf.output('CV.pdf', 'F')


