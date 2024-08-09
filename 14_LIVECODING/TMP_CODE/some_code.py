# fs = frozenset([1, 2, 3])
#
# print(fs)

# mv = memoryview(b'abc')
# print(len(mv))

# a = set([1, 2, 3])
# print(type(a))
# print(a[1])


# Создание множества из списка
# set_list = []
# for i in range(100):
#     # my_list = [3, 1, 4, 2, 5]
#     # my_set = set(my_list)
#     # # print(my_set)  # Вывод: {1, 2, 3, 4, 5} или другой порядок
#     my_string = "abracadabra"
#     my_set = set(my_string)
#     print(my_set)  # Вывод: {'a', 'r', 'b', 'c', 'd'} или другой порядок
#     my_set = set()

# # Создание множества из строки
# my_string = "abracadabra"
# my_set = set(my_string)
# print(my_set)  # Вывод: {'a', 'r', 'b', 'c', 'd'} или другой порядок

# my_set = set(['a', 'some', 'elem', 'here'])
# print(my_set)
#
# print(my_set[1])
# a = [1, 2]
# mt = tuple([1, 2, a])
# print(mt)
# md = {mt: 3, 'mama': 4}
# print(md)

# def modify_list(lst):
#     lst.append(4)
#
# l = [1, 2, 3]
#
# modify_list(l)
#
# print(l)
#
# def modify_var(v):
#     v = 100
#
# v = 200
# modify_var(v)
# print(v)
#
# def modify_frozen_set(v):
#     v = 100
#
# num = "12345"
# print(type(num))

# for n in num:
#     print(n)
#
# r = range(20)
# print(type(r))
t = (['a', 'b'])


#
# s = {3, t}
# l = ['a', t]
# print(l)
#
# r1 = range(20)
# r2 = range(21, 40)
# r3 = r1 + r2
# for k in r3:
#     print(k)

# d = {'t': 1, r1: 1}
# print(d)

# s = "10"
# number = int(s)
# print(number)
# try:
#     number = int(s)
# except ValueError as e:
#     print(f"ValueError: {e}")


# свой итератор

class MyOddIterator:
    def __init__(self, il):
        self.inner_list = il
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.inner_list):
            res = self.inner_list[self.index]
            self.index += 2
            print("one more odd number")
            return res
        else:
            raise StopIteration


# iterable_seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # итерируемая последовательность
# print(dir(iterable_seq))
# my_iterator = MyOddIterator(iterable_seq)  # итератор

# r = next(my_iterator)  # r=0 и "one more odd number"
# print(f'{r=}')
# for i in my_iterator:
#     print(i)  # 2 4 8 и каждый раз "one more odd number"


def my_iter_generator(some_list):
    index = 0
    while index < len(some_list):
        yield some_list[index]
        index += 2


# print("generator");
# r = range(10)
# iterator = my_iter_generator(r)

# for i in iterator:
#     print(i)  # 0 2 4 6 8


class InfiniteSquaring:
    """Класс обеспечивает бесконечное последовательное возведение в квадрат заданного числа."""

    def __init__(self, initial_number):
        # Здесь хранится промежуточное значение
        self.number_to_square = initial_number

    def __next__(self):
        # Здесь мы обновляем значение и возвращаем результат
        self.number_to_square = self.number_to_square ** 2
        return self.number_to_square

    def __iter__(self):
        """Этот метод позволяет при передаче объекта функции iter возвращать самого себя, тем самым в точности реализуя протокол итератора."""
        return self


# a = InfiniteSquaring(6)
# print(next(a))
# print(next(a))
# print(next(a))

#
# numbers = [1, 2, 3, 4, 5]
# iterator = iter(numbers)  # получаем итератор
# print(next(iterator))  # 1
# print(next(iterator))  # 2
# # и так далее, пока не закончатся элементы

# a = [1, 2, 3]
# b = [1, 2, 3]
# # b = a
# if a == b:
#     print("True1")
#
# if a is b:
#     print("True2")

# square = lambda x: x * x
#
# print(square(10))

# my_str = "1 2 3 4 5 6"
# 41636
# переделать в строку квадратов четных чисел разделенных дефисом
# join - split - map - filter

# a = my_str.split(' ')
# a = list(map(int, a))
# a = list(filter(lambda x: x % 2 == 0, a))
# a = list(map(lambda x: int(x) ** 2, a))
# a = map(str, a)
# res = "-".join(a)
# print(res)

# result = '-'.join(map(str, map(lambda x: x * x, filter(lambda x: x % 2 == 0, map(int, my_str.split())))))
# print(result)


# l = [1, 2, 3, 10]
# my_iter = l.__iter__()
# while True:
#     try:
#         i = my_iter.__next__()
#         print(i)
#     except:
#         print("This is the end")
#         break
# m = dir(l)
# print (m)

# gen = (k ** 2 for k in range(10))
#
# print(next(gen))
# print(next(gen))
# # for m in gen:
# #     print(m)
#
#
# def gen_new():
#     for i in range(3):
#         yield i*i
# g1 = gen_new()
# print(type(g1))
#
# g2 = (x * x for x in range(3))
# print(type(g2))
# if list(g1) == list(g2):
#     print("Equal")
# else:
#     print("Not Equal")
# # Not Equal
#
# myset = {1, 2, 3, 4}
# print(len(myset))
#
# d1 = dict(short='dict', longer='dictionary')
# print(len(d1))

# class WriteFileManager:
#     def __enter__(self):
#         self.file = open('example.txt', 'w')
#         print("Входим в контекст и открываем файл")
#         return self.file
#
#     # def __exit__(self, exc_type, exc_value, traceback):
#     #     self.file.close()
#     #     print("Выходим из контекста и закрываем файл")
#
#
#     def __exit__(self):
#         self.file.close()
#         print("Выходим из контекста и закрываем файл")
#
#
# # Использование контекстного менеджера
# with WriteFileManager() as file:
#     print("Внутри контекста")
#     file.write("Привет, мир!")  # Записываем сообщение в файл


# squares = [i ** 2 for i in range(10) if i % 2 == 0]
# num_dict = {i: i**2 for i in range(10)}
# num_set = {i for i in range(10)}
#
# print(type(num_set))
# print(type(num_dict))


# def caps_me(func):
#     def wrapper(*args, **kwargs):
#         mess = func(*args, **kwargs)
#         return mess.upper()
#     return wrapper
#
#
# def caps_or_low(param):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             mess = func(*args, **kwargs)
#             if param == 'low':
#                 return mess.lower()
#             elif param == 'caps':
#                 return mess.upper()
#         return wrapper
#     return outer
#
# #@caps_me
# @caps_or_low('caps')
# @caps_or_low('low')
# def say_hello(name: str):
#     return f"Hi dear {name}"
#
# print("==============")
# print(say_hello("Dima"))

#  декоратор кэширования

def cache_func(func):
    cache = {}
    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))
        print(f"{key=}")
        if key in cache.keys():
            print("Using cache")
            return cache[key]
        else:
            print("calculating")
            res = func(*args, **kwargs)
            cache[key] = res
            return res
    return wrapper


@cache_func
def some_calc(a: int, b: int) -> int:
    return a ** b

# print("==================")
# print(some_calc(2, 10)) #  считает
# print(some_calc(2, 10)) # берет из кэша
# print(some_calc(2, b=10)) # считает


# def some_decorate(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f"decorated func args = {args} kwargs = {kwargs}")
#         return res
#     return wrapper
#
# @some_decorate
# def some_func(a: int, b: int):
#     return a * b
#
#
# some_func(3, 4)  # decorated func args = (3, 4) kwargs = {}
# some_func(3,  b=4)  # decorated func args = (3,) kwargs = {'b': 4}



t = (1, 5 ,9, 9)

l = [1, 5, 9, 9, 9, 9]

for i, el in enumerate(l):
    print(f"{i} --- {el}")

l = set(l)
print(f'{l=}')
s1 = {(1, 2)}

s = {1, 2, 4, 4}
print(type(s))
print(s)


age = 19

#123


# match age:
#     case 19:
#         print("you are older 18")
#     case 20:
#         print("you are older 18")
#     case 21:
#         print("you are older 18")
#     case 18:
#         print("you are 18")

# print(l.index(5))
# print(t.index(1))
# print(t.count(5))

# d = {}
# # d[l] = 3
# d[t] = 4
# print(d[t])

print("---------")

def some_decorator(param1, param2):
    def outer(func):
        def wrapper(*args, **kwargs):
            print("alarm func was called")
            print(f"{param1=} {param2=}")
            func(*args, **kwargs)
        return wrapper
    return outer

@some_decorator(param1=2, param2=3)
def say_hello():
    print("Hello")

say_hello()
# print(say_hello())

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Это моя собственная ошибка")
except MyCustomError as e:
    print(e)

# l = [2, 10, 30]
# print(l[:])


d = {'Yes': [50, 21], 'No': [131, 2]}
print(type(d))
print("--------------------------")
import pandas as pd
p = pd.DataFrame({'Yes': [ 'a', 40], 'No': [131, 2]})
# print("1000" + "10")
print(p.dtypes)

# index - строки
# индексы колонок - headers
df1 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


df2 = pd.DataFrame({'s': [1, 2, 3, 4, 5]})

s1 = pd.Series([1, 2, 3, 4, 5])
print(df2)
print("--------------------------")

print(s1)

s = {'s': 10, 'm': 20}
print(s)
m = {'l': s}

b = b'abba'
print(type(b))

# a = 'two'
# print(a ** 2)


def fact(n):
    if n < 0:
        raise ValueError("bad input")
    return 1 if n == 0 else n*fact(n-1)


# Исходный список
l = [1, 2, [3, 4], 5]

# Поверхностное копирование
m = l[:]

# Проверяем, что это разные объекты
print(l is m)  # Вывод: False

# Проверяем, что вложенные объекты общие
print(l[2] is m[2])  # Вывод: True

# Изменяем вложенный объект
l[2][0] = 99

# Оба списка отражают это изменение, так как они ссылаются на один и тот же вложенный объект
print(l)  # Вывод: [1, 2, [99, 4], 5]
print(m)  # Вывод: [1, 2, [99, 4], 5]

#у тебя есть массив
l = ['alex','rik','morty']
#сделай через генератор словарь:
# {'alex': 4, 'rik':3, 'morty':5}"

print({x: l.count(x) for x  in l })

class Person:
    @staticmethod  # если тут не будет декоратора, то на строке ниже будет ошибка, типа нет self
    def goodbye():
        print('Bye')

    def hello(self):
        print("hello")

# Person().goodbye()
Person().hello()


class Person:
    sex = 'male'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.prep = 'Mrs '
        if self.sex == "male":
            self.perp = 'Mr '
        self.fulname = self.prep + self.name + ' ' + self.surname

p1 = Person('ivan', 'petrov')
p1.sex = 'hz'
print(p1.fulname)