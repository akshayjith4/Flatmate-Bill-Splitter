from flat import Bill, Flatmate
from report import PDFReport


def get_user_input():
    """Prompts the user for input and returns the collected data."""
    amount = float(input("Please enter the total bill amount: $"))
    period = input("Please enter the bill period (e.g., June 2024): ")

    name1 = input("Please enter your name: ")
    days_in_house1 = int(input(f"How many days did you, {name1}, stay in the house during the bill period? "))

    name2 = input("Please enter the name of your flatmate: ")
    days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

    return amount, period, name1, days_in_house1, name2, days_in_house2


def main():
    # Get user input
    amount, period, name1, days_in_house1, name2, days_in_house2 = get_user_input()

    # Create Bill instance with the collected amount and period
    the_bill = Bill(amount, period)
    # Create Flatmate instances with collected names and days in house
    flatmate1 = Flatmate(name1, days_in_house1)
    flatmate2 = Flatmate(name2, days_in_house2)

    # Calculate payment amounts for each flatmate
    flatmate1_payment = flatmate1.pays(the_bill, flatmate2)
    flatmate2_payment = flatmate2.pays(the_bill, flatmate1)

    # Display the payment amounts
    print(f"\n{flatmate1.name} is responsible for: ${flatmate1_payment:.2f}")
    print(f"{flatmate2.name} is responsible for: ${flatmate2_payment:.2f}")

    # Generate PDF report with the bill and flatmates' details
    pdf_report = PDFReport(filename=f"{the_bill.period}.pdf")
    pdf_report.generate(flatmate1, flatmate2, bill=the_bill)

    print(f"\nA detailed report has been generated: '{the_bill.period}.pdf'")


# Check if the script is run directly (not imported), then call main function
if __name__ == "__main__":
    main()
