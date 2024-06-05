'''
kata link: https://www.codewars.com/kata/5121303128ef4b495f000001
points: 7 kyu
type: OOP
----
The following code could use a bit of object-oriented artistry.
While it's a simple method and works just fine as it is, in a larger system it's best to organize methods into classes/objects.
(Or, at least, something similar depending on your language)
Refactor the following code so that it belongs to a Person class/object.
Each Person instance will have a greet method.
The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call.
Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'

----
Нужно написать клаас Person такой чтобы у него при инициализации объекта задавался атрибут имя
joe = Person('Joe')
у объекта класса должно быть свойство name
joe.name          # should == 'Joe'
так же должен быть метод greet который позволяет здороваться с заданным именем по формуле:
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
'''
import codewars_test as test

# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.


class Person:
    def __init__(self, my_name):
        self.my_name = my_name

    @property
    def name(self):
        return self.my_name

    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.my_name}'


jack = Person("Jack")
jill = Person("Jill")

test.assert_equals(jack.greet("Jill"), "Hello Jill, my name is Jack")
test.assert_equals(jack.greet("Mary"), "Hello Mary, my name is Jack")

test.assert_equals(jill.greet("Jack"), "Hello Jack, my name is Jill")
test.assert_equals(jill.name, 'Jill', "Person's name could not be retrieved")
