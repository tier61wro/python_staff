'''
train_date: 14.05.2022
kata link: https://www.codewars.com/kata/53cf459503f9bbb774000003
points: 8 kyu
type: OOP
-------------
DESCRIPTION:
Python is now supported on Codewars!

For those of us who are not very familiar with Python,
let's handle the very basic challenge of creating a class named Python.
We want to give our Pythons a name, so it should take a name argument that we can retrieve later.

For example:

bubba = Python('Bubba')
bubba.name # should return 'Bubba'
-------------
TRANSLATION:
сделайте простой класс который будет иметь атрибут name
-------------
===TRAINED====
простое задание - по сути hello world для питона
-------------
'''

import codewars_test as test

# Create a Python class that takes a name.
# example usage: Python('Bubba')
class Python(object):
    def __init__(self, name):
        self.name = name

#===TESTS====
import codewars_test as test
# from solution import Python

@test.describe('should pass other tests')
def _():
    @test.it('should support name')
    def name_test():
        bubba = Python('Bubba')
        test.assert_equals(bubba.name, 'Bubba')