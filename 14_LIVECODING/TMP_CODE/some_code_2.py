# d1 = {'a':1, 'b':2}
#
# d2 = {'c': 3}
# d2.update(d1)
# print(d2)
#
# from collections import Counter
#
# # str = 'mama mila'
#
# # Подсчитываем количество каждой буквы в строке
# letter_counter = Counter(str)
#
# # Сортируем по количеству в порядке убывания
# sorted_letter_counter = letter_counter.most_common()
# print(sorted_letter_counter)
#
#
# from datetime import datetime
# current_time = datetime.now()
# print(current_time)
# readable_date = current_time.strftime('%Y-%m-%d %H:%M:%S')
# print(readable_date)
#
#
#
# # class Person:
# #     @staticmethod
# #     def get_average(attribute):
# #         attributes = {
# #             'height': 178,
# #             'weight': 88,
# #         }
# #         return attributes.get(attribute, None)
# #
# # p = Person()
# # print(p.get_average('height'))
#
# # class Person:
# #     def __init__(self, name):
# #         print("init was called")
# #         self.name = name
# #
# #     @classmethod
# #     def person_with_age(cls, name):
# #         instance = cls(name)
# #         instance.age = 20
# #         return instance
# #
# # p = Person.person_with_age('vasja')
# #
# # print(p.age)
#
#
# # class Person:
# #     def __init__(self, name, surname):
# #         self.name = name
# #         self.surname = surname
# #
# #     @property
# #     def fullname(self):
# #         return f"{self.name} {self.surname}"
# #
# #     @fullname.setter
# #     def fullname(self, value):
# #         name, surname = value.split()
# #         self.name = name
# #         self.surname = surname
# #
# # p = Person('Ivan', 'Dorn')
# # print(p.fullname)  # Вывод: Ivan Dorn
# # p.fullname = 'Ivan Ivanov'
# # print(p.fullname)  # Вывод: Ivan Ivanov
#
#
# # class Person:
# #     def __init__(self, name):
# #         self._name = name
# #
# #     @property
# #     def name(self):
# #         return self._name
# #
# #     @name.setter
# #     def name(self, value):
# #         self._name = value
# #
# # p = Person('Ivan')
# #
# #
# # print(p.name)
# # p.name = 'Petr'
# # print(p.name)
#
# # class Person():
# #     def __init__(self, h, w):
# #         self.height = h
# #         self.weight = w
# #
# #     @property
# #     def bmi(self):
# #         return self.weight / self.height ** 2
# #
# # p = Person(1.79, 91)
# # print(p.bmi)
#
# # from abc import ABC, abstractmethod
# # class Animal(ABC):
# #     @abstractmethod
# #     def make_sound(self):
# #         return "some sound"
# #
# # class Dog(Animal):
# #     def make_sounda(self):
# #         return "Woof"
# #
# # class Cat(Animal):
# #     def make_sound(self):
# #         return "Meow"
#
# # l = Dog()
# # print(Animal.mro())
# # print(a.weight)
# # print(l.make_sound())
# # print(l.__dict__)
#
#
# class SensetiveField:
#     def __init__(self):
#         self._value = 42
#
#     def __get__(self, obj, obj_type = None):
#         print(f'{obj}')
#         print("sensitive data access")
#         return self._value
#
# class BankAccount:
#     account_sum = SensetiveField()
#
#
# a = BankAccount()
# print(a.account_sum)
#
#
#
# # class Person:
# #     @staticmethod
# #     def some_method(fa, sa):
# #         print(f"{fa}---{sa}")
# #
# #
# # Person.some_method(1, 2)
# # p = Person
# # p.some_method('22', '33')
#
#
# class OddNumbers:
#     def __init__(self, seq):
#         self.ind = 0
#         self.seq = seq
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.ind < len(self.seq):
#
#             index = self.ind
#             print(f'current index{index}')
#             self.ind += 2
#             return self.seq[index]
#         else:
#             raise StopIteration
#
#
# l = [i for i in range(11)]
# print(l)
#
# for n in OddNumbers(l):
#     print(f'{n=}')
#
#
# def create_konvert1(index, *args, **kwargs):
#     full_address = f'{index} '
#     for np in args:
#         full_address += f"{np} "
#
#     for k, v in kwargs.items():
#         full_address += f"{k}: {v} "
#
#     return full_address
#
#
# # def create_konvert(index, *args, **kwargs):
# #     name = " ".join(args)
# #     addr = " ".join(f"{k}:{v}" for k, v in kwargs.items())
# #     full_address = f'{index} {name} {addr}'
# #
# #     return full_address
# #
# # res = create_konvert('053200', 'Лунаида', 'Коновалова', street='Broadway', house='10', flat='1')
# # print(f"---{res}---")
# #
# # def ret_sort(word: str) -> str:
# #     return ''.join(([*word]).sort())
# #     # # l = word.split('')
# #     # l = [*word]
# #     # l.sort()
# #     # return ''.join(l)
# # from collections import Counter
# #
# # def is_anagram(f, s):
# #     return Counter(f) == Counter(s)
# #
# # print(is_anagram(f='listen', s='silent1'))
#
#
# print('===============================')
# # def some_function(name='Zenek', age=45):
# #     print(f'name = {name}')
# #     print(f'age = {age}')
#
#
# def some_function(name: str = 'zenek', age: int = '45'):
#     '''
#     :param name: - name of user
#     :param age: - age of user years
#     :return:
#     '''
#     print(f'name = {name}')
#     print(f'age = {age}')
#     return f"{name} {age}", '4'
#
# some_function('Sasha', 39)
# #
# some_function(name='Sasha', age=39)
# #
# some_function('Sasha',  age=39)
# #
# a, b = some_function()
#
# print(a)
# print(b)

from typing import List
l = [10, 1, 10, 33]

# def find_unique_set(list_in: list) -> list:
#     return list(set(list_in))
#
#
# def find_unique_dict(list_in: list) -> list:
#     d = {k: None for k in list_in}
#     return list(d.keys())
#
# def find_unique_list_comp(list_in: list) ->list:
#     seen = set()
#     return [l for l in list_in if l not in seen and not seen.add(l)]
#
#
# from collections import Counter
# def find_unique_counter(list_in: list) -> list:
#     return [k for k, v in Counter(l).items()]
#
#
# print(find_unique_counter(l))

# print(type(m))
# # print(find_unique(l))

# 3
# 1

# в это же задание попадает полиндром, так как по сути полиндром это когда реверсы совпадают:

m = 'mama'
print(m[::-1])

def pop_rev(str_in: str):
    rev_seq = []
    l = [*str_in]
    for i in range(len(str_in)):
        rev_seq.append(l.pop())
    return ''.join(rev_seq)

def reversed_way(str_in: str):
    res = [i for i in reversed(str_in)]
    return "".join(res)

def reverse_for(str_in):
    res = ""
    for i in str_in:
        res = i + res
    return res

# print(pop_rev(m))
# print(reversed_way(m))
print(reverse_for(m))

# 11 11

some_str = 'mama mila rama mama rama'

def words_count(str_in):
    words = str_in.split()
    words_dict = {}
    for w in words:
        words_dict[w] = words_dict.get(w, 0) + 1
    return dict(sorted(words_dict.items(), key=lambda x: x[1], reverse=True))

print(words_count(some_str))

def words_counter(str_in):
    words = str_in.split()
    words_dict = {w: words.count(w) for w in words}
    return dict(sorted(words_dict.items(), key=lambda x: x[1], reverse=True))


# words_counter(some_str)
#
# def caps(num):
#     def outer(func):
#         def inner(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return (res.upper())*num
#         return inner
#     return outer
#
# @caps(5)
# def say_hello():
#     return "hello"
#
# print(say_hello())


# class MyContext:
#     def __enter__(self):
#         self.file = open('some_file', 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with MyContext() as f:
#     f.write("hello")
#
# l = [1, 2, 3, 4, 5, 6]
#
# mid = (0 + len(l) - 1) // 2
# print(mid)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

l = fact(4)
print(l)