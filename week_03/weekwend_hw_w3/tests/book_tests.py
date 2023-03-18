import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("And then there were none", "Agatha Christie", "crime")

    def test_book_has_name(self):
        self.assertEqual(self.book1.title, "And then there were none")

    def test_book_has_author(self):
        self.assertEqual(self.book1.author, "Agatha Christie")

    def test_book_has_genre(self):
        self.assertEqual(self.book1.genre, "crime")
