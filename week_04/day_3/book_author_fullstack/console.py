import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

author_repo.delete_all()
book_repo.delete_all()

author1 = Author("J.K.", "Rowling")
author2 = Author("Stephen", "King")
author3 = Author("Toni", "Morrison")
author4 = Author("Ernest", "Hemingway")
author5 = Author("Jane", "Austen")

author_repo.save(author1)
author_repo.save(author2)
author_repo.save(author3)
author_repo.save(author4)
author_repo.save(author5)

book1 = Book("Harry Potter and the Philosopher's Stone", "Fantasy", 1997, author1)
book2 = Book("The Casual Vacancy", "Fiction", 2012, author1)
book3 = Book("The Shining", "Horror", 1977, author2)
book4 = Book("11/22/63", "Science Fiction", 2011, author2)
book5 = Book("Beloved", "Fiction", 1987, author3)
book6 = Book("Sula", "Fiction", 1973, author3)
book7 = Book("The Old Man and the Sea", "Fiction", 1952, author4)
book8 = Book("A Farewell to Arms", "Fiction", 1929, author4)
book9 = Book("Pride and Prejudice", "Romance", 1813, author5)
book10 = Book("Sense and Sensibility", "Romance", 1811, author5)

book_repo.save(book1)
book_repo.save(book2)
book_repo.save(book3)
book_repo.save(book4)
book_repo.save(book5)
book_repo.save(book6)
book_repo.save(book7)
book_repo.save(book8)
book_repo.save(book9)
book_repo.save(book10)


selected_author = author_repo.select(author1.id)
print (f"The selected author's name is: {selected_author.first_name} {selected_author.last_name}")

selected_book = book_repo.select(book2.id)
print(f"The selected book title is:{selected_book.title}, which is {selected_book.genre} genre, and it was first published in {selected_book.year}.")

author_list = author_repo.select_all()
print("Here's the current list of authors in the datbase:")
for author in author_list:
    print(f"{author.first_name} {author.last_name}")

book_list = book_repo.select_all()
print("Here's the current list of books in the datbase:")
for book in book_list:
    print(f"The book title is:{book.title}, which is {book.genre} genre, and it was first published in {book.year}.")

king_books = book_repo.book_by_author(author2)
for book in king_books:
    print(f"{book.author.first_name} has {len(king_books)} books. The book title is: {book.title}, which is {book.genre} genre, and it was first published in {book.year}.")

author4.first_name = "Taylor"
author4.last_name = "Swift"
author_repo.update(author4)

book1.title = "Harry Potter and the Goblet of Fire"
book_repo.update(book2)

author_repo.delete(author5.id)
book_repo.delete(book7.id)

