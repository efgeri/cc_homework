from models.book import Book

book_list = [Book("And then there were none", "Agatha Christie", "crime", False), Book("The Odyssey", "Homer", "Epic poetry", True), Book("Lord of the Flies", "William Golding", "Fiction", False)]

def add_book(book):
    book_list.append(book)

def delete_book(index):
    book_list.pop(index)