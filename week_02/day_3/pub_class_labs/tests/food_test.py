import unittest
from src.food import Food
from src.customer import Customer

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.food = Food("Nachos", 6.00, 6)
        self.customer = Customer("Roland", 18, 20)
        self.customer.drunkenness = 9

    def test_rejuvenation_level