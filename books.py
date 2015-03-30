_list_books = []


def get_book_by_isbn(isbn):
    return _list_books[isbn]


class Book(object):

    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self._content = content
        _list_books.append(self)


    def get_isbn(self):
        return _list_books.index(self)


class Person(object):

    def __init__(self, name, date_of_birth):
        self.name = name
        self._date_of_birth = date_of_birth


class Author(Person):

    def __init__(self, name, date_of_birth):
        Person.__init__(self, name, date_of_birth)


    def get_age(self):
        return 2015 - self._date_of_birth


class Reader(Person):

    def __init__(self, name, date_of_birth):
        Person.__init__(self, name, date_of_birth)


    def is_over_40(self):
        return self._date_of_birth <= 1975


    def read_book(self, book):
        return book._content
