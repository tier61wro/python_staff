from dataclasses import dataclass

class SimpleBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book_first = SimpleBook("Fahrenheit 451", "Bradbury")
print(f'{type(book_first)}')

@dataclass
class DataBook:
    title: str
    author: str

from collections import namedtuple
NamedTupleBook = namedtuple("NamedTupleBook", ["title", "author"])
book = NamedTupleBook("Fahrenheit 451", "Bradbury")
print(book.author)

# book.title = 'Celsius 232'

book_sec = DataBook("Fahrenheit 451", "Bradbury")
print(f'{type(book_sec)}')
# DataBook.title =