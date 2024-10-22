import re
import time
from copy import deepcopy, copy
from datetime import datetime


class Parent:
    x = 2

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
# 2 2 2

Child1.x = 5
print(Parent.x, Child1.x, Child2.x)

# 2 5 2

Parent.x = 8
print(Parent.x, Child1.x, Child2.x)

#8 5 8

# t1 = ('a', [1, 2, 3], 'b')
# t2 = ('a', 'b', ['c'])
t2 = [1]
# print(dir(t2))
# print(t2.__hash__())

#
# a = range(20)
#
# print(a[10])



# def outer(x):
#     def inner():
#         res = id(x)
#         print(res)
#         return res
#     return inner
#
# o = outer(10)
#
# o()
# a = o.__closure__[0].cell_contents
# print(id(a))


# дан словарь
d = {'dima':4, 'alex':5, 'ivan': 5}
# сделай две замкнутые функции
# get_all_4
# get_all_5

# def some_function(n):
#     def inner():
#         for k, v in d.items():
#             if v == n:
#                 print(k)
#     return inner
#
# get_all_5 = some_function(5)
# get_all_5()

def sum_numbers(*args): # тут у нас упаковка кучи входящих переменных в тапл args
    print(sum(args))


sum_numbers(10, 10, 10, 20)
l = [10, 20, 20]
sum_numbers(*l)



print ([*'mama']) # распаковали в ['m', 'a', 'm', 'a']
print([1, *[2, 3]]) # упаковали в [1, 2, 3]


start = time.time()
print(start)

a = 10
k = 1 if a > 8 else 0 # k=1 или k=0, сначала то что будет при true а не условие как в perl

current_time = datetime.now()


keys = ['luna', 'mama', 'kot']
val = [4, 4, 3]
d2= dict([(23, 34), (56, 87)])
d= dict(zip(keys, val))
print(d2)


class ForeverYoung:
    def __init__(self, age):
        self.age = age

    def __add__(self, obj):
        if self.age > 30:
            return 30
        else:
            return self.age + obj

    def __str__(self):
        return self.age

p1 = ForeverYoung(40)

print(p1 + 5)
l1 = [1, 2, 3]
l2 = deepcopy(l1) # поверхностное копирование
l2 = copy(l1)

if l1 == l2:
    print(True)

str = 'Masha is pretty girl'

# if m := re.search(r'(\d+)', "Masha is 10 years"):
#     print(m.group(1))

#
# values = [1, 1, 1, 1, 1]
#
# while (n := len(values)) > 0:
#     print(f"left {n}")
#     print(values.pop())
#
# class Person:
#     pass
# print(type(Person))
# o = Person()
#
# print(type(o))
# print("aa")
# if __name__ == '__main__':
#     # PythonistClass = type('Pythonist', (), {})
#     # print(PythonistClass)
#     # o = PythonistClass()
#     # print(type(PythonistClass))
#     class Person:
#         pass
#     Student = type('Student', (Person,), {'age': 30})
#     print(type(Student))
#     print(Student.__mro__)
#     print(Student.mro())
#
#     o = Student()
#     o.mro()



class ContManager:
    def __enter__(self):
        print("cont manager was called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("end of manager")

with ContManager():
    print("we make smth")
#
# scores = {'Bill': 5, 'Mary': 4, 'Steve': 5}
#
# def get_scores(num):
#     def inner():
#         return [k for k, v in scores.items() if v == 5]
#     return inner
#
# give_me_5 = get_scores(5)
# l = give_me_5()
# print(l)

class MetaPerson(type):
    def __new__(cls, name, bases, dct):
        pass

