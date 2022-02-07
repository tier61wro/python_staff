import random
import string
from random import choice
# from string import ascii_lowercase
import string

name = 'Ivan'


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def chaika_son_name(cls, name):
        n = len(name)
        son_name = ''.join(choice(string.ascii_lowercase) for i in range(n)).title()
        return cls(name=son_name)


p1 = Person('Anna')
p2 = Person.chaika_son_name('Artem')

print(p1.name)
print(p2.name)