from fpdf import FPDF

pdf = FPDF()

# Add a page
pdf.add_page()

#Logo
pdf.image('logo_pb.png', 0, 0, 35)
pdf.alias_nb_pages()
# Set the font and font size
pdf.set_font("Arial", size=12)

#create a cell
pdf.cell(200, 10, txt = 'GROUP CHARLIE ', ln = 1, align = 'C')

#add another cell
pdf.cell(200, 10, txt = 'A very simple PDF file', ln = 2, align = 'C')

#add another cell
pdf.cell(200, 10, txt = 'Group members:', ln = 2, align = 'L')
members = ['Giulio', 'Spencer', 'Connor', 'Kyrylo', 'Adrian', 'Mathias', 'Semen']
for member in members:
    pdf.cell(200, 10, txt = member, ln = 10, align = 'L',)

# Save the PDF file
pdf.output('CV.pdf', 'F')


