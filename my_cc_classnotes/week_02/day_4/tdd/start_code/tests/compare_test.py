import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_3_5_returns_3_is_less_than_5(self):
        self.assertEqual("3 is less than 5", compare(3, 5))

    def test_compare_4_4_returns_numbers_are_the_same(self):
        self.assertEqual("Numbers are the same!", compare(4, 4))