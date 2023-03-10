import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Celine Dion")

    def test_guest_has_name(self):
        self.assertEqual("Celine Dion", self.guest.name)