import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Whatever Potter", 20.00, 35)

    def test_customer_has_name(self):
        self.assertEqual("Whatever Potter", self.customer.name)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(4.00)
        self.assertEqual(16.00, self.customer.wallet)