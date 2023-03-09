class CompoundInterest:
    def __init__(self, principal, percentage, years):
        self.principal = principal
        self.percentage = percentage
        self.years = years

    def calculate_compound(self):
        return round(self.principal * pow((1 + self.percentage/100/12), 12 * self.years), 2)
