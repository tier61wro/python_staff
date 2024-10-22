# показывем отличие метакласса от класса

class Person:
    def __init__(self):
        self.mammals_type = 'Human'


class Student(Person):
    def __init__(self, age):
        super().__init__()
        self.age = age

# Использование
s1 = Student(18)
print(s1.age) # 19

class MetaPerson(type):
    def __new__(cls, name, bases, dct):
        dct['mammals_type'] = 'Human'
        return super().__new__(cls, name, bases, dct)


class MStudent(metaclass=MetaPerson):
    def __init__(self, age):
        self.age = age

s2 = MStudent(19)
print(s2.age) # 19
