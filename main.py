from books import *

tolkien = Author("Tolkien", 1901)
brown = Author("Dan Brown", 1955)
tizio = Reader("Tizio", 1970)
caio = Reader("Caio", 1980)
lotr = Book(tolkien, "The lord of the rings", "Once upon a time...")
davinci_isbn = Book(brown, "Da Vinci Code", "This is Da Vinci Code").get_isbn()
davinci = get_book_by_isbn(davinci_isbn)

def print_book(reader, book):
    r_age = "over 40" if reader.is_over_40() else "under 40"
    s = "%(reader)s (%(r_age)s) reads %(book)s by %(author)s (age: %(a_age)d)"
    print(s % {
        'reader': reader.name,
        'r_age': r_age,
        'book': book.title,
        'author': book.author.name,
        'a_age': book.author.get_age()
        })
    print(reader.read_book(book))

print_book(tizio, lotr)
print_book(caio, davinci)
