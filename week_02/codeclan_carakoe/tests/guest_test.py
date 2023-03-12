import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Celine Dion", 60)

    def test_guest_has_name(self):
        self.assertEqual("Celine Dion", self.guest.name)

    def test_guest_can_spend(self):
        self.guest.decrease_wallet(35)
        self.assertEqual(25, self.guest.wallet)
