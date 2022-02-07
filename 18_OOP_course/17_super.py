#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#
# class Student(Person):
#     def __init__(self, name, surname):
#         super().__init__(name)
#         self._surname = surname
#
#
# class Student1(Person):
#     def __init__(self, name, surname):
#         super().__init__(name)
#         self._surname = surname



class Person:
    def __new__(cls,):

    def hello(self):
        print(f'method bound with {self}')


class Student(Person):
    def hello1(self):
        print('test')
        # super().hello()
        # print('Student obj.hello() is called')

class Asp(Student):
    pass

a = Asp()
a.hello()


getattr(Person, 'name')