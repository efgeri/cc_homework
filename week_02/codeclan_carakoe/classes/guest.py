class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def decrease_wallet(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount