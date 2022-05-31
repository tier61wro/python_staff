'''
train_date: 01.06.2022
kata link: https://www.codewars.com/kata/55ddb0ea5a133623b6000043
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:

- Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!

Tim sighed, he already knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to SecondUsefulClass,

and went off. Although Timmy had no idea why changing name is so important for his boss, he realized,
that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function,
which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that,
that Timmy yet has to learn them.

-------------
TRANSLATION:
-------------
===TRAINED====
-------------
'''

import codewars_test as test

def class_name_changer(cls, new_name):
    pass;

#===TESTS====
class MyClass:
    pass

myObject = MyClass();
test.assert_equals(MyClass.__name__, "MyClass")

class_name_changer(MyClass, "UsefulClass");
test.assert_equals(MyClass.__name__, "UsefulClass")

class_name_changer(MyClass, "SecondUsefulClass");
test.assert_equals(MyClass.__name__, "SecondUsefulClass")