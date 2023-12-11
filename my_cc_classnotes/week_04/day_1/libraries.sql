DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS libraries;

CREATE TABLE libraries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    library_id INT REFERENCES libraries(id) ON DELETE CASCADE
    );

INSERT INTO libraries (name, location)
VALUES ('Library of Congress', 'Washington D.C.');

INSERT INTO libraries (name, location)
VALUES ('British Library', 'London');

INSERT INTO libraries (name, location)
VALUES ('Royal Danish Library', 'Copenhagen');

INSERT INTO libraries (name, location)
VALUES ('Berlin State Library', 'Berlin');

INSERT INTO libraries (name, location)
VALUES ('Bibliothèque nationale de France', 'Paris');

INSERT INTO libraries (name, location)
VALUES ('Trinity College Library', 'Dublin');

INSERT INTO libraries (name, location)
VALUES ('New York Public Library', 'New York');

INSERT INTO libraries (name, location)
VALUES ('Szabo Ervin Library', 'Budapest');

INSERT INTO books (title, author, library_id)
VALUES ('The Adventures of Huckleberry Finn', 'Mark Twain', 1);

INSERT INTO books (title, author, library_id)
VALUES ('The Divine Comedy', 'Dante Alighieri', 1);

INSERT INTO books (title, author, library_id)
VALUES ('Don Quixote', 'Miguel de Cervantes', 2);

INSERT INTO books (title, author, library_id)
VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 2);

INSERT INTO books (title, author, library_id)
VALUES ('Gulliver''s Travels', 'Jonathan Swift', 7);

-- This is how you write a query to show a specific librarie's contents
-- SELECT name, title FROM libraries, books WHERE libraries.id = 2 AND books.library_id = libraries.id
-- Order BY title