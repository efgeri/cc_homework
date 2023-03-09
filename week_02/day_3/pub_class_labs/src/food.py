class Food:
    def __init__(self, name, price, rejuvenation_level):
        self.name = name
        self.price = price
        self.rejuvenation_level = rejuvenation_level

    def check_rejuvenation (self, food):
        return food.rejuvenation_level
