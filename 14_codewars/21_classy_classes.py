'''
https://www.codewars.com/kata/55a144eff5124e546400005a/train/python

Task

Your task is to complete this Class, the Person class has been created.
You must fill in the Constructor method to accept a name as string and an age as number,
complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person
    def __init__(name,age)
        self.info="#{name}s age is #{age}"

Reference: https://docs.python.org/3/tutorial/classes.html

----
https://www.codewars.com/kata/55a144eff5124e546400005a/solutions/python
----
можно было сразу без свойств
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

'''
import codewars_test as test

class Person:
    def __init__(self, name, age):
        self._info = f'{name}s age is {age}'

    @property
    def info(self):
        return self._info

    # @info.setter
    # def info(self, info):
    #     self._info = info


names = ["john", "matt", "alex", "cam"]
ages = [16, 25, 57, 39]


for i in range(4):
    name, age = names[i], ages[i]
    person = Person(name, age)
    test.it("Testing for %s and %s" % (repr(name), age))
    test.assert_equals(person.info, name + "s age is " + str(age))