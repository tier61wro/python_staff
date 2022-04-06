'''
train_date: 04.04.2022
kata link: https://www.codewars.com/kata/57a93f93bb9944516d0000c1
points: 7 kyu
type: OOP
-------------
DESCRIPTION:

In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:
>>> d = Dictionary()
>>> d.newentry('Apple', 'A fruit that grows on trees')
>>> print(d.look('Apple'))
A fruit that grows on trees
>>> print(d.look('Banana'))
Can't find entry for Banana

Good luck and happy coding!

-------------
TRANSLATION:
Вам нужно дореализовать соответствующие методы класса Dictionary (словарь)
чтобы работало создание объекта класса:
>>> d = Dictionary()
метод newentry:
>>> d.newentry('Apple', 'A fruit that grows on trees')
метод поиска значения по словарю look:
>>> print(d.look('Apple'))

class Dictionary():
    def __init__(self):
        # Your code

    def newentry(self, word, definition):
        # Your code

    def look(self, key):
        # your code
так чтобы
-------------
===TRAINED====
красивый return черерез тернарный оператор
return self[key] if key in self else "Can't find entry for " + key
-------------
'''

import codewars_test as test


class Dictionary:
    def __init__(self):
        self.d = {}

    def newentry(self, word, description):
        self.d[word] = description

    def look(self, word):
        if word in self.d.keys():
            return self.d[word]
        else:
            return f"Can't find entry for {word}"


d = Dictionary()

d.newentry("Apple", "A fruit")
test.assert_equals(d.look("Apple"), "A fruit")

d.newentry("Soccer", "A sport")
test.assert_equals(d.look("Soccer"), "A sport")
test.assert_equals(d.look("Hi"), "Can't find entry for Hi")
test.assert_equals(d.look("Ball"), "Can't find entry for Ball")

d.newentry("soccer", "a sport")
test.assert_equals(d.look("soccer"), "a sport")
