'''
train_date: 02.06.2022
kata link: https://www.codewars.com/kata/55ddcef532f8678af1000006
points: 7 kyu
type: OOP
-------------
DESCRIPTION:

Continuation to Python's Dynamic Classes #1 Kata.

- That name changing function is awesome! - Timmy heard from his boss -
but would it not be possible to hide somehow that function in classes itself?

Timmy was thinking about it for while than decided to contact with his guru - you - and ask about it.
You offered him to build class that could be inherited,
and could provide some class method to modify name of already existing classes. The new class should be named as

ReNameAbleClass
and the special one method should be

change_class_name
Like before, be sure that new solution will allow only names with alphanumeric chars (upper & lower letters plus digits),
 but starting only with upper case letter.

Moreover, for testing purposes, he want new class to have

__str__
method which will be returning string like "Class name is: MyClass" for MyClass.



Too easy? Check Python's Dynamic Classes #3 Kata and make sure that solved Python's Dynamic Classes #1 Kata.
-------------
TRANSLATION:
-------------
===TRAINED====
-------------
'''

import codewars_test as test


class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        pass

    @classmethod
    def __str__(cls):
        pass

#===TESTS====

class MyClass(ReNameAbleClass):
    pass;


myObject = MyClass()
test.assert_equals(str(myObject), "Class name is: MyClass", "Original class name shouldn't be changed yet...");

myObject.change_class_name("UsefulClass");
test.assert_equals(str(myObject), "Class name is: UsefulClass", "New class name should be as boss wanted to!");

myObject.change_class_name("SecondUsefulClass");
test.assert_equals(str(myObject), "Class name is: SecondUsefulClass", "New class name should be as boss wanted to!");

