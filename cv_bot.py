from fpdf import FPDF

pdf = FPDF()

# Add a page
pdf.add_page()

#Logo
pdf.image('logo_pb.png', 0, 0, 35)

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


