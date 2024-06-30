import sqlite3

with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    create_authors_table = """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            birth_year INTEGER NOT NULL
        )
    """
    cursor.execute(create_authors_table)
    connection.commit()


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    create_books_table = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title TEXT NOT NULL,
            author_id INTEGER,
            price FLOAT NOT NULL CHECK (price > 0),
            description TEXT,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    """
    cursor.execute(create_books_table)
    connection.commit()


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    insert_one_author = """
        INSERT INTO authors (name, birth_year)
        VALUES (?, ?)
    """
    cursor.execute(insert_one_author, ['Author One', 1950])
    authors = [
        ('Author Two', 1980),
        ('Author Three', 1975),
        ('Author Four', 1960),
        ('Author Five', 1945)
    ]
    cursor.executemany(insert_one_author, authors)
    connection.commit()


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    insert_book = """
        INSERT INTO books (title, author_id, price, description)
        VALUES (?, ?, ?, ?)
    """
    books = [
        ('Book One: рецепт', 1, 150.0, 'Description of Book One'),
        ('Book Two', 2, 200.0, 'Description of Book Two'),
        ('Book Three', 3, 250.0, 'Description of Book Three'),
        ('Book Four', 4, 300.0, 'Description of Book Four'),
        ('Book Five', 5, 350.0, 'Description of Book Five'),
        ('Book Six: рецепт', 1, 400.0, 'Description of Book Six'),
        ('Book Seven', 2, 450.0, 'Description of Book Seven'),
        ('Book Eight', 3, 500.0, 'Description of Book Eight'),
        ('Book Nine', 4, 550.0, 'Description of Book Nine'),
        ('Book Ten', 5, 600.0, 'Description of Book Ten')
    ]
    cursor.executemany(insert_book, books)
    connection.commit()


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    query = """
        SELECT * FROM books
        WHERE title LIKE '%рецепт%'
    """
    result = cursor.execute(query)
    print(result.fetchall())


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    query = """
        SELECT * FROM authors
        WHERE birth_year < 1900
    """
    result = cursor.execute(query)
    print(result.fetchall())


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    query = """
        SELECT * FROM books
        WHERE price > 100 AND author_id = 2
    """
    result = cursor.execute(query)
    print(result.fetchall())


with sqlite3.connect('book_store.sqlite3') as connection:
    cursor = connection.cursor()
    query = """
        SELECT * FROM books
        LIMIT 2 OFFSET 1
    """
    result = cursor.execute(query)
    print(result.fetchall())
