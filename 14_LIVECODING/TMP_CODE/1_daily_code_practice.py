import asyncio
import string
import time
from datetime import datetime


class MyException(Exception):
    pass


try:
    raise MyException("some error")
except MyException as err:
    print(err)


class MyIteratiorClass:
    def __init__(self, l_in):
        self.i = 0
        self.l = l_in

    def __iter__(self):
        return self  # тут мы именно объект возвращаем

    def __next__(self):
        if self.i < len(self.l):
            res = self.l[self.i]
            self.i += 1
            return res
        else:
            raise StopIteration


l = [1, 3, 10, 12]


# my_iter_obj = MyIteratiorClass(l)
# print(next(my_iter_obj))
# print(next(my_iter_obj))
# print(next(my_iter_obj))
# print(next(my_iter_obj))
#
my_str = "1 2 3 4 5 6"
no_space = list(map(int, filter(lambda x: x != ' ', my_str)))
print(no_space)
# odd_number = list(filter(lambda x: int(x)*int(x) if int(x) % 2 == 0 else None, [*no_space]))
# print(odd_number)
print('-'.join([str(x*x) for x in no_space if x % 2 == 0]))

# n = 123
# m = [*n]
# print(m)
print("==================")
# result = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5]))
# print(result)
#
# # a = "8 11 2 -1 42"
# a = input()
# print(max([int(i) for i in a.split(" ")]))

# def solution(year: int) -> bool:
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     return False
#
# print(solution(int(input())))
#
# print("=============")


# def solution(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n <= 2:
#         return 1
#     else:
#         return solution(n-1) + solution(n-2)

# def solution(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
#
#
# print(solution(int(input())))


# def solution(a_string: str) -> bool:
#     # put your python code here
#     pass
#
# print(solution(input()))

def solution(a_string: str) -> bool:
    l = [i for i in a_string.lower() if i not in string.punctuation and i != ' ']
    l_rev = l[::-1]
    if ''.join(l) == ''.join(l_rev):
        return True
    else:
        return False

# print(solution(input()))


# def caps(func):
#     def wrapper(*args):
#         res = func(*args).upper()
#         return res
#     return wrapper
#
# @caps
# def gen_message(mess):
#     return mess
#
# res = gen_message(mess = 'mama')
# print(res)


import pandas as pd; print(10)
# pd.set_option('display.max_rows', 5)

# from learntools.core import binder; binder.bind(globals())
# from learntools.pandas.creating_reading_and_writing import *
# print("Setup complete.")
# print(list(filter(lambda x: x % 2 == 1, [1, 2, 10])))

# a = [10, 20]
# # b = [i for i in a]
# b = a
# a.append(30)
# print(a)
# print(b)

# print(0.0 and "mama" and "papa")  # []
# print("mama" and "papa" and [])  # []
# # print('' and "mama")
# print(0.0 or "mama" or "papa")  # []

# l = [1, 2, 3]
# m = [4, 5, 6]
# n = [4, 5, 6]
# p = zip(l, m)
# print(dict(p))

# a = [1, 2, 3]
#
# def list_fun(l):
#     if l is a:
#         print("same")


# list_fun(a)
#
# number = 5
# def elem_fun(m):
#     if m is number:
#         print("same again")
#     else:
#         print("no")
#
# elem_fun(number)  # same again


# def some(m, l = []):
#     l.append(m**2)
#     print(l)
#
#
# some(3)
# some(10)
#
# def create_profile(username, age=30, language="Python"):
#     print(f"Username: {username}, Age: {age}, Favorite Language: {language}")
#
# create_profile(username='mama', age=40, language='german')


# class Person:
#     name = "Ivan"
#
# p = Person()
# print(p.name)
# p.name = 'Sasha'
# print(p.name)
# Person.name = 'Vasya'
# print(p.name)
# print(Person.name)
# print(Person.__dict__)

class MyClass:
    name = 12

    def __str__(self):
        return str(self.name)

    # def __repr__(self):
    #     return str(self.name)

    def __hash__(self):
        return 10

#
# s = MyClass()
# print(s)  # Теперь печатает 12
#
# m = [s, 10]
# print(m[0])
# print(m)  # Печатает {12, 10}

s = {1, 2, 4}
it = iter(s)
print(next(it))
print(it.__next__())
print(it.__next__())
# print(it.__next__())


class MySet(set):
    def __init__(self, *args):
        super().__init__(args)

    # def __hash__(self):
    #     return 42

    def add_with_message(self, element):
        """Добавляет элемент и выводит сообщение."""
        self.add(element)
        print(f"{element} добавлен в множество")

    def __str__(self):
        """Переопределяет строковое представление множества."""
        return f"Элементы множества: {super().__str__()}"

# a = MySet()
# a.add_with_message(12)
# a.add_with_message(13)
# print(a)
# s = {a}
# print(s)


def gen(l):
    l.append(10)
    for i in l:
        yield i * i


l = [4, 10, 20]
m = gen(l)
# print(next(m))
# print(next(m))
#
# k = (i*i for i in l)
# print(next(k))
# print(next(k))

# class MyContext:
#     def __enter__(self):
#         self.file = open('some_tmp_file', 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
#
# with MyContext() as f:
#     f.write('some text')

# async def get_press():
#     await asyncio.sleep(3)
#     print("pressure = 861 mm")
#
# async def get_tmp():
#     await asyncio.sleep(3)
#     print("tmp = 25 c")
#
# async def main():
#     task1 = asyncio.create_task(get_press())
#     task2 = asyncio.create_task((get_tmp()))
#     await task1
#     await task2
#
# t1 = time.time()
# asyncio.run(main())
# t2 = time.time()
# print(f"all done {t2 -t1}")


# class Person:
#     def __init__(self, name):
#         print(f"name = {name}")
#         self.name = name
#
# class Student(Person):
#     def __init__(self, name, study_year):
#         super().__init__(name)
#         print(f"studied_year = {study_year}")
#         self.study_year = study_year
#
#
# alex = Student('alex', 3)

# def create_konvert_old(p_index, *args, **kwargs):
#     adress = p_index
#     body = " ".join(list(args))
#     for k, v in kwargs.items():
#         body = body + " " + f'{k} {v}'
#
#     return adress + " " + body
#
# def create_konvert(postal_code, *args, **kwargs):
#     person_name = " ".join(args)
#     addr = " ".join(f"{k} {v}" for k, v in kwargs.items())
#     return f"{postal_code} {person_name} {addr}"
#
# print(create_konvert('053200', 'Лунаида', 'Коновалова', street='Broadway', house='10', flat='1'))



# scores = {'Bill': 5, 'Mary': 4, 'Steve': 5}
#
#
#
#
# def giveme_score(target_score):
#     def inner():
#         return [k for k, v in scores.items() if v == target_score]
#     return inner
#
# giveme_5 = giveme_score(5)
# print(giveme_5())


# def caps(func):
#     def wrapper():
#         res = func()
#         return res.upper()
#     return wrapper
#
#
# #@caps()
# def say_hello():
#     return "hello world"
#
# #print(say_hello())
# print(caps(say_hello)())
#
#
# def caps(num):
#     def outer(func):
#         def wrapper():
#             res = func()
#             return (res.upper())*num
#         return wrapper
#     return outer
#
# @caps(3)
# def say_hello():
#     return "hello world"
#
# print(say_hello())

# class Person:
#     default_surname = 'Smith'
#
#     def __init__(self, name, surname=default_surname):
#         self.name = name
#         self.surname = surname
#
#     def fullname(self):
#         return f"{self.name} {self.surname}"
#
#
# # p = Person('John', 'Wolf')
# p = Person('John')
# print(p.fullname())


# class Person:
#     name = 'Bill'
#
#     # def __new__(cls, *args, **kwargs):
#     #     return None
#
#     def __init__(self):
#         return None
#
# p = Person()
#
# # print(type(p)) # <class '__main__.Person'>
#
# print(type(p)) # <class 'NoneType'>
# print(p.name)

class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def return_base_number():
        return 42

    def change_age(self):
        self.age = self.return_base_number()


p = Person(18)
print(p.age)
print(p.return_base_number())
print(Person.return_base_number())