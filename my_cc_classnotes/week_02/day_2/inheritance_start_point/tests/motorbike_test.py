import unittest

from classes.motorbike import Motorbike

class TestMotorbike(unittest.TestCase):

    def setUp(self):
        self.motorbike = Motorbike()

    def test_motorbike_can_start_engine(self):
        self.assertEqual("Vrrmmm (I'm a motorbike), HELL YEAH!", self.motorbike.start_engine()) # MODIFIED