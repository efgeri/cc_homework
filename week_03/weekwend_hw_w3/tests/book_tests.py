import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("And then there were none", "Agatha Christie", "crime", False)

    def test_book_has_name(self):
        self.assertEqual(self.book1.title, "And then there were none")

    def test_book_has_author(self):
        self.assertEqual(self.book1.author, "Agatha Christie")

    def test_book_has_genre(self):
        self.assertEqual(self.book1.genre, "crime")

    def test_check_out(self):
        self.book1.toggle_check_out(True)
        self.assertEqual(self.book1.checked_out, True)

    def test_check_in(self):
        self.book1.toggle_check_in(True)
        self.assertEqual(self.book1.checked_out, False)
