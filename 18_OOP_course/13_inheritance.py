# inheritance
class Person:
    default_name = 'Misha'

    def __init__(self, name = default_name):
        self.name = name

    def hello(self):
        print(f'hello from {self.name}')

class Student(Person):
    pass

s1 = Student('Ivan')
s2 = Student()