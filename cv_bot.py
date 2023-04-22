import openai
import os
from fpdf import FPDF
from user_input import User
import requests
from io import BytesIO
from PIL import Image

openai.api_key = "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"

start = True

while start is True:
    print("Hey man, I`m your personal CV maker. Choose the option below:")
    print()
    print("1.Generate photo")
    print("2.Upload photo")
    print()
    choice = input("Make your choice: ")
    print()
    print("Ok, u chose: ", choice)
    print()

    if choice == "1":
        description = input("Give me any description you want to generate as image: ")

        # Generate an image
        response = openai.Image.create(prompt=description, n=1, size="1024x1024")
        image_url = response["data"][0]["url"]
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

        # Logo
        pdf.image("output.png", 0, 0, 45)

        # Set the font and font size
        pdf.set_font("Arial", "B", size=20)

        # create a cell
        pdf.cell(200, 10, txt="GROUP CHARLIE ", ln=1, align="C")

        # add another cell
        pdf.cell(200, 10, txt="A very simple PDF file", ln=2, align="C")

        # add another cell
        pdf.set_font("Arial", "B", size=18)
        pdf.cell(200, 20, txt="Group members:", ln=2, align="L")
        members = [
            "Giulio",
            "Spencer",
            "Connor",
            "Kyrylo",
            "Adrian",
            "Mathias",
            "Semen",
        ]
        for member in members:
            pdf.set_font("Arial", size=16)
            pdf.cell(
                200,
                10,
                txt=member,
                border=1,
                ln=2,
                align="L",
            )

        # Save the PDF file
        pdf.output("CV.pdf", "F")

        start = False

    elif choice == "2":
        # prompt the user to provide the path of the image they want to upload
        image_path = input("Please enter the path of the image you want to upload: ")

        # open the image using PIL
        image = Image.open(image_path)

        # save the image as a PNG file
        image.save("output.png", format="PNG")

        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # Logo
        pdf.image("output.png", 0, 0, 45)

        # Set the font and font size
        pdf.set_font("Arial", "B", size=20)

        # create a cell
        pdf.cell(200, 10, txt="GROUP CHARLIE ", ln=1, align="C")

        # add another cell
        pdf.cell(200, 10, txt="A very simple PDF file", ln=2, align="C")

        # add another cell
        pdf.set_font("Arial", "B", size=18)
        pdf.cell(200, 20, txt="Group members:", ln=2, align="L")
        members = [
            "Giulio",
            "Spencer",
            "Connor",
            "Kyrylo",
            "Adrian",
            "Mathias",
            "Semen",
        ]
        for member in members:
            pdf.set_font("Arial", size=16)
            pdf.cell(
                200,
                10,
                txt=member,
                border=1,
                ln=2,
                align="L",
            )

        # Save the PDF file
        pdf.output("CV.pdf", "F")

        start = False
