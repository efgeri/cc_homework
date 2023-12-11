import unittest
from src.coffe_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("Sky's Coffee Shop", 100.00)

    def test_coffee_shop_has_name(self):
        self.assertEqual("Sky's Coffee Shop", self.coffee_shop.name)

    def test_can_increase_till(self):
        self.coffee_shop.increase_till(5.99)
        expected = 105.99
        actual = self.coffee_shop.till
        self.assertEqual(expected, actual)
