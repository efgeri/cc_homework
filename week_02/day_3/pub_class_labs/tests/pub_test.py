import unittest
from src.pub import Pub 
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("Geri's Pub", 100.00)
        self.customer1 = Customer("Bob", 20, 18)
        self.customer2 = Customer("Charlie", 100, 16)

    def test_pub_has_name(self):
        self.assertEqual("Geri's Pub", self.pub.name)

    def test_can_increase_till(self):
        self.pub.increase_till(5.00)
        self.assertEqual(105.00, self.pub.till)

    def test_can_check_price(self):
        price = self.pub.check_price("Beer")
        self.assertEqual(4.00, price)

    def test_drink_list(self):
        drinks_list_number = len(self.pub.drinks)
        self.assertEqual(3, drinks_list_number)

    def test_can_buy_drink(self):
        self.pub.purchase("Beer", self.customer1)
        self.assertEqual(16, self.customer1.wallet)
        self.assertEqual(104, self.pub.till)

    def test_cannot_buy_drink(self):
        self.pub.purchase("Whiskey", self.customer2)
        self.assertEqual(100, self.customer2.wallet)
        self.assertEqual(100, self.pub.till)

    def test_alcohol_level_increase(self):
        self.pub.purchase("Wine", self.customer1)
        self.assertEqual(3, self.customer1.drunkenness)

    def test_too_drunk(self):
        self.pub.purchase("Wine", self.customer1)
        self.pub.purchase("Beer", self.customer1)
        self.pub.purchase("Whiskey", self.customer1)
        self.pub.purchase("Wine", self.customer1)
        self.assertEqual(5, self.customer1.wallet)
        self.assertEqual(115, self.pub.till)


    