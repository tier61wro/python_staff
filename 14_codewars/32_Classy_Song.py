'''
train_date: 14.04.2022
kata link: https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Your job is to create a class called Song.
A new Song will take two parameters, title and artist.

mount_moose = Song('Mount Moose', 'The Snazzy Moose')

mount_moose.title => 'Mount Moose'
mount_moose.artist => 'The Snazzy Moose'

You will also have to create an instance method named howMany() (or how_many()).

The method takes an array of people who have listened to the song that day.
The output should be how many new listeners the song gained on that day out of all listeners.
Names should be treated in a case-insensitive manner, i.e. "John" is the same as "john".

Example

mount_moose = Song('Mount Moose', 'The Snazzy Moose')

# day 1 (or test 1)
mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']) => 5
# These are all new since they are the first listeners.

# day 2
mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']); => 2
# Luke and Amanda are new, john already listened to it the previous day

Example

mount_moose = Song('Mount Moose', 'The Snazzy Moose')

# day 1
mount_moose.how_many(['John', 'joHN', 'carl']) => 2
-------------
TRANSLATION:
Нужно создать класс Song у которого будет два атрибута title и artist
так же у объектов класса должен быть метод который принимает на вход массив из слушателей и возвращает назад
количество уникальных слушателей, не принимая во внимание регистр
-------------
===TRAINED====
красивый способ найти уникальные эелементы в массиве

вот еще красивее из чужого перешептывания
        tmp = set(map(str.lower, people))
        res = len(tmp - self._seen)
        self._seen.update(tmp)
оказывается со множествами можно вот так
In [4]: l =set([1, 2, 3])
In [5]: m = set([1])
In [6]: l - m
Out[6]: {2, 3}

-------------
'''

import codewars_test as test


class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, listeners_list):
        count = 0
        for name in set([(l.lower()) for l in listeners_list]):
            if name not in self.listeners:
                count += 1
                self.listeners.append(name)
        return count



# from solution import Song
# from preloaded import *

mount_moose = Song('Mount Moose', 'The Snazzy Moose')
# print(vars(mount_moose))

@test.describe('Sample Tests')
def test_group():
    @test.it('Test for title and artist')
    def test_case():
        test.assert_equals(mount_moose.title, 'Mount Moose')
        test.assert_equals(mount_moose.artist, 'The Snazzy Moose')

    @test.it("Given: 'John', 'Fred', 'Bob', 'Carl', 'RyAn'")
    def test_case():
        test.assert_equals(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']), 5)

    @test.it("Given: 'JoHn', 'Luke', 'AmAndA'")
    def test_case():
        test.assert_equals(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']), 2)

    @test.it("Given: 'Amanda', 'CalEb', 'CarL', 'Furgus'")
    def test_case():
        test.assert_equals(mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']), 2)

    @test.it("Given: 'JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE'")
    def test_case():
        test.assert_equals(mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']), 1)