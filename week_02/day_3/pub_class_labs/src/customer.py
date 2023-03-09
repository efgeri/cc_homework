class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkenness(self, amount):
        self.drunkenness += amount
    
    def rejuvenation (self, amount):
        self.drunkenness -= amount
        if self.drunkenness < 0:
            self.drunkenness = 0
    