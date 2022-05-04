'''
train_date: 04.05.2022
kata link: https://www.codewars.com/kata/5641275f07335295f10000d0/
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
-------------
===TRAINED====
-------------
'''

import codewars_test as test

class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        first_name = first_name
        last_name = last_name
    def get_full_name(self):
        return first_name + ' ' + last_name

#===TESTS====

import codewars_test as test
from preloaded import *
from solution import Dinglemouse

@test.describe("Basic Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(Dinglemouse('Clint', 'Eastwood').get_full_name(), 'Clint Eastwood')
        test.assert_equals(Dinglemouse('', 'Eastwood').get_full_name(), 'Eastwood')
        test.assert_equals(Dinglemouse('Clint', '').get_full_name(), 'Clint')
        test.assert_equals(Dinglemouse('', '').get_full_name(), '')