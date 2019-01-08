#!/usr/bin/env pythoclass Person3:
class Person3:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set(self, name, age):
        self.name = name
        self.age = age

class Student2(Person3):
    course = 1
    def __init__(self, name, age, course):
        self.course = course
        super().__init__(name, age)
    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

user = Student2('Igor', 25)
print(user.name, user.age)
#работает

user = Student2('Igor', 25, 6)
print(user.name, user.age, user.course)
# не работает, в чем проблема?
