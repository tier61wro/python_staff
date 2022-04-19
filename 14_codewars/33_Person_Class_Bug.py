'''
train_date: 16.04.2022
kata link: https://www.codewars.com/kata/513f887e484edf3eb3000001/train/python
points: 7 kyu
type: OOP
-------------
DESCRIPTION:

The following code was thought to be working properly,
however when the code tries to access the age of the person instance it fails.

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)

For this exercise you need to fix the code so that it works correctly.
-------------
TRANSLATION:
исправьте код так чтобы он работал корректно
лучше используя декоратор property
-------------
===TRAINED====
property
-------------
'''

import codewars_test as test


class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


matz = Person('Yukihiro', 'Matsumoto', 47)
test.assert_equals(matz.full_name, 'Yukihiro Matsumoto')
test.assert_equals(matz.age, 47)

joe = Person('Joe', 'Smith', 30)
test.assert_equals(joe.full_name, 'Joe Smith')
test.assert_equals(joe.age, 30)