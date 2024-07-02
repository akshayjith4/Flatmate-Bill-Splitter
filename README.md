# Flatmate Bill Splitter

The **Flatmate Bill Splitter** is a Python program that helps flatmates split bills based on their respective periods of stay in the house. It generates a PDF report detailing each flatmate's share of the bill for a specified billing period.

## Features

- **Input Collection**: Collects bill amount, billing period, flatmates' names, and days each flatmate stayed during the billing period.
- **Bill Calculation**: Calculates each flatmate's share of the bill based on their days stayed relative to the total days stayed by all flatmates.
- **PDF Report Generation**: Generates a detailed PDF report that includes:
  - Title and period of the bill.
  - Names of flatmates and their respective amounts to be paid.
- **Automatic PDF Viewing**: Opens the generated PDF report in the default web browser after generation.

## How to Use

1. **Clone the Repository**:
   git clone https://github.com/akshayjith4/flatmate-bill-splitter.git
   cd flatmate-bill-splitter

Install Dependencies:
Ensure you have Python installed. Install required dependencies using pip:
pip install fpdf  # for PDF generation

Run the Program:
Execute main.py and follow the prompts to enter bill details and flatmates' information:

View the PDF Report:
After entering the required information, a PDF report named <period>.pdf will be generated in the files directory and opened automatically in your default web browser.
