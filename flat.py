class Bill:
    """
    Represents a bill with a specified amount and period.
    """

    def __init__(self, amount, period):
        """
        Initializes the Bill object with the given amount and period.

        :param amount: Total amount of the bill.
        :param period: Period of the bill (e.g., "June 2024").
        """
        self.amount = amount  # Total amount of the bill
        self.period = period  # Period during which the bill was incurred


class Flatmate:
    """
    Represents a flatmate who lives in the flat and is responsible for paying a share of the bill.
    """

    def __init__(self, name, days_in_house):
        """
        Initializes the Flatmate object with the given name and days stayed in the house.

        :param name: Name of the flatmate.
        :param days_in_house: Number of days the flatmate stayed in the house during the bill period.
        """
        self.name = name  # Name of the flatmate
        self.days_in_house = days_in_house  # Number of days the flatmate stayed in the house

    def pays(self, bill, other_flatmate):
        """
        Calculates the amount to be paid by this flatmate based on their stay duration compared to another flatmate.

        :param bill: The Bill object containing the total amount and period.
        :param other_flatmate: The other Flatmate object to compare days stayed with.
        :return: The amount this flatmate has to pay.
        """
        total_days = self.days_in_house + other_flatmate.days_in_house  # Total days both flatmates stayed
        share = self.days_in_house / total_days  # This flatmate's share of the total days
        return share * bill.amount  # This flatmate's share of the bill amount
