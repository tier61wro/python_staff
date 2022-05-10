'''
train_date: 08.05.2022
kata link: https://www.codewars.com/kata/597c684822bc9388f600010f
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
The code provided is supposed return a person's Full Name given their first and last names.

But it's not working properly.
Notes

The first and/or last names are never null, but may be empty.
Task

Fix the bug so we can all go home early.

-------------
TRANSLATION:
Вам нужно починить следующий кусок кода

class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        first_name = first_name
        last_name = last_name
    def get_full_name(self):
        return first_name + ' ' + last_name


так чтобы все работало
имя и фамилия могут быть пустыми,
в таком случае вместо недостающего элелемента должна быть пустая строка, без избыточных пробелов
-------------
===TRAINED====
потренировал генераторы
strip() - обрезает пробелы
>>> s = 'lesha '
>>> s.strip()
'lesha'
>>> s = ' '
>>> s.strip()
''
-------------
'''

import codewars_test as test

class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return " ".join([s for s in [self.first_name, self.last_name] if s != ''])
#===TESTS====

import codewars_test as test
# from preloaded import *
# from solution import Dinglemouse

@test.describe("Basic Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(Dinglemouse('Clint', 'Eastwood').get_full_name(), 'Clint Eastwood')
        test.assert_equals(Dinglemouse('', 'Eastwood').get_full_name(), 'Eastwood')
        test.assert_equals(Dinglemouse('Clint', '').get_full_name(), 'Clint')
        test.assert_equals(Dinglemouse('', '').get_full_name(), '')