import webbrowser
from fpdf import FPDF
import os

class PDFReport:
    """
    Generates a PDF report that contains information about the flatmates' names, days in the house, and the due amount.
    """

    def __init__(self, filename):
        """
        Initializes the PDFReport with a filename.

        :param filename: The name of the PDF file to be created.
        """
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """
        Generates the PDF report with the billing information for the flatmates.

        :param flatmate1: The first flatmate object.
        :param flatmate2: The second flatmate object.
        :param bill: The Bill object containing the total amount and period.
        """
        # Calculate the payment amounts for each flatmate
        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pays = str(round(flatmate2.pays(bill, flatmate1), 2))

        # Create a PDF document
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add an image to the PDF
        pdf.image("files/house.png", w=40, h=40)

        # Set title font and add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates' Bill", border=0, align="C", ln=1)

        # Set period label font and add the period
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.ln(20)

        # Add Flatmate 1 information
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=f"{flatmate1.name} pays:", border=0)
        pdf.cell(w=150, h=25, txt=f"${flatmate1_pays}", border=0, ln=1)

        # Add Flatmate 2 information
        pdf.cell(w=100, h=25, txt=f"{flatmate2.name} pays:", border=0)
        pdf.cell(w=150, h=25, txt=f"${flatmate2_pays}", border=0, ln=1)

        # Save the PDF to a file
        os.chdir("files")
        pdf.output(self.filename)

        # Open the PDF file in the default web browser
        webbrowser.open(self.filename)
