import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 6)
        self.card2 = Card("Clubs", 1)
        self.card3 = Card("Diamonds", 9)
        self.cards = [self.card1, self.card2, self.card3]
        self.cardgame = CardGame()

    def test_check_for_ace_true(self):
        check_ace = self.cardgame.check_for_ace(self.card2)
        self.assertEqual(True, check_ace)
    
    def test_check_for_ace_false(self):
        check_ace = self.cardgame.check_for_ace(self.card1)
        self.assertEqual(False, check_ace)

    def test_highest_card(self):
        highest = self.cardgame.highest_card(self.card1, self.card3)
        self.assertEqual(self.card3, highest)

    def test_cards_total(self):
        total = self.cardgame.cards_total(self.cards)
        self.assertEqual("You have a total of 16", total)
