import sys


# print(type(int)) # type
# print(type(type)) # type
# print(type.__class__) # type

class Person:
    pass

# print(type(object))  # <class 'type'>
# print(type(Person))  # <class 'type'>
# p1 = Person() # <class '__main__.Person'>

# создаем класс через type
print("-------------------------------")
MyNewClass = type('MyNewClassName', (), {'age': 10, 'greet': lambda self: "Hello, World!"})
print(type(MyNewClass))  # <class 'type'>
o = MyNewClass()
print(o.__class__)  # <class '__main__.MyNewClassName'>
print(type(o))  # <class '__main__.MyNewClassName'>
print(o.age)  # 10
print("-------------------------------")


# создаем мета класс через type
class MyMetaClass(type):  # <class 'type'>
    def __new__(cls, name, bases, dct):
        print(f"Creating clas {name} with MyMetaClass")
        return super().__new__(cls, name, bases, {'metaclass_name': 'MyMetaClass'})

class MyClass(metaclass=MyMetaClass):
    pass

o1 = MyClass()  # Creating clas MyClass with MyMetaClass
print(o1.metaclass_name)  # MyMetaClass

# sys.exit()
# type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Doe'} )


# try:
#     m = MyMetaClass() # так нельзя TypeError: type.__new__() takes exactly 3 arguments (0 given)
#     #
#     # print(type(m))
# except TypeError as e:
#     print(e)





####### Метакласс: #############
class SomeMeta(type):
    def __new__(cls, name, bases, args):
        args['age'] = 18
        args['greet'] = lambda self: print("hello world!")
        return super().__new__(cls, name, bases, args)


class Student(metaclass=SomeMeta):
    pass

std1 = Student()
std1.greet()

################################################################
from enum import Enum

class Color(Enum):
	RED = "#FFOOOO"
	GREEN = "#00FF00"


print(Color.RED)


red_color = Color.RED.value
# print(red_color)
col = {'RED': "#FFOOOO", 'GREEN': "#00FF00"}

print(col['RED'])
