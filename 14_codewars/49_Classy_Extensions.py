'''
train_date: 13.05.2022
kata link: https://www.codewars.com/kata/55a14aa4817efe41c20000bc
points: 8 kyu
type: OOP
-------------
DESCRIPTION:


You will be preloaded with the Animal class, so you should only edit the Cat class.
Your task is to complete the Cat class which Extends Animal
and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).
-------------
TRANSLATION:
у вас есть класс Animal который умеет создавать животное с определенными именем, вам нужно на основе этого класса
создать класс Cat, у этого класса должен быть метод speak который будет возвращать строку вида:
"Имя_кота meows.


-------------
===TRAINED====
-------------
'''

import codewars_test as test

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def speak(self):
        return f'{self.name} meows.'


#===TESTS====
test.describe('Fixed Tests')
cat = Cat('Mr Whiskers')
test.assert_equals(cat.speak(), 'Mr Whiskers meows.')
cat = Cat('Lamp')
test.assert_equals(cat.speak(), 'Lamp meows.')
cat = Cat('$$Money Bags$$')
test.assert_equals(cat.speak(), '$$Money Bags$$ meows.')