from db.run_sql import run_sql
import repositories.author_repository as author_repo

from models.author import Author
from models.book import Book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def save(book):
    sql = "INSERT INTO books (title, genre, year, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.year, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['year'], author, row['id'])
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        author = author_repo.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['year'], author, result['id'])
    return book


def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(book):
    sql = "UPDATE books SET (title, genre, year, author_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.year, book.author.id, book.id]
    run_sql(sql, values)

def book_by_author(author):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['genre'], row['year'], author, row['id'] )
        books.append(book)
    return books