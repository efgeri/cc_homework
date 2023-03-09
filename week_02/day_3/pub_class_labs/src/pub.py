
from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till):
        self.drinks = [Drink("Whiskey", 6.00, 5), Drink("Beer", 4.00, 2), Drink("Wine", 5.00, 3)]
        self.name = name
        self.till = till

    def increase_till(self, amount):
        self.till += amount
    
    def check_price(self, name_drink):
        for drink in self.drinks:
            if drink.name == name_drink:
                return drink.price
            
    def check_alcohol(self, name_drink):
        for drink in self.drinks:
            if drink.name == name_drink:
                return drink.alcohol_level
            
    def purchase(self, product_name, customer):
        if customer.age >=18 and customer.drunkenness < 10:
            customer.decrease_wallet(self.check_price(product_name))
            self.increase_till(self.check_price(product_name))
            customer.increase_drunkenness(self.check_alcohol(product_name))