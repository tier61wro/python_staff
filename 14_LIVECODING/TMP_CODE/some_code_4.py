# l = [1, 5, 7, 10]
#
# def binary_search(l_in: list, number_in: int):
#     print(f"========{number_in}===========")
#     print(f"{l_in=}")
#     last = len(l_in) - 1
#     left, right = 0, last
#
#     while left <= right:
#
#         middle = (right + left) // 2
#         print(f"{left=} -- {right=} --  {middle=}")
#         if l_in[middle] == number_in:
#             return middle
#         elif l_in[middle] < number_in:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return -1
#
# # print(binary_search(l, 3))
# # print(binary_search(l, 1))
# print(binary_search(l, 10))
# # print(binary_search(l, 5))
# # print(binary_search(l, 100))


# def Fib_memoisation(n, memo):
#     if n <= 0:
#         return 'Введите число больше 0'
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         if n not in memo:
#             memo[n] = Fib_memoisation(n - 1, memo) + Fib_memoisation(n - 2, memo)
#             print(f"we added {n} element in memo")
#         return memo[n]
#
# memo = {}
#
# res = Fib_memoisation(10, memo)
# print(res)


# def find_unique_list_comp(list_in: list) -> list:
#     seen = set()
#     return [l for l in list_in if l not in seen and not seen.add(l)]


# seen = set(['m'])
# m = seen.add('m')
# print(m)
#
#
# r = range(10)
# print(r)
# b = [12]
# t = (10, 20, b)
# print(t[2])
# # print(hash(t))
#
# m = None
# print(type(m))

# a = (1, 2, 3)
# b = a
# b = b + (4,)
# print(a)  # Вывод: (1, 2, 3)
# print(b)  # Вывод: (1, 2, 3, 4)


# num = 0
#
# for i in range(10):
#     num += i if i % 2 else -i
#     print(f"=== {num} ===")
#
# print(num)

# a = [1, 2, 4]
# print(id(a))
# a.append(5)
# print(id(a))
# a = a + [9]
# print(a)
# print(id(a))

# def function(x):
#     x += 1
#     return x
#
#
# value = 5
# value = function(value)
# print(value)
# print(a)

# def function(x):
#     x.append(1)
#
#
# value = [0]
# function(value)
# print(value)
# print(x)


# import asyncio
#
#
# async def get_temp():
#     print("going for temp")
#     await asyncio.sleep(2)
#     print("temp done")
#
#
# async def get_press():
#     print("going for pressure")
#     await asyncio.sleep(2)
#     print("pressure done")
#
# async def main():


# def filter_even_numbers(numbers):
#     return [i for i in numbers if i % 2 == 0]
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(filter_even_numbers(l)) # [2, 4, 6, 8, 10]


# def words_counter(str_in):
#     words = str_in.split()
#     words_dict = {w: words.count(w) for w in words.split()}
#     return dict(sorted(words_dict.items(), key=lambda x: x[1], reverse=True))
#

# def words_counter(str_in):
#     words_dict = {}
#     words = str_in.split()
#     words_dict = {w: words.count(w) for w in words}
#     print(words_dict)
#     words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
#     return words_dict
#
#
#
# str_in = 'sasha mama mama papa'
# print(words_counter(str_in))

# from copy import deepcopy
# d = ['a', [0, 1]]
#
# f = deepcopy(d)
# d[1][0] = 3
# print(d)
# print(f)

# square = lambda x: x*x
# l = list(map(square, [0, 1, 2, 3]))
# even_check = lambda x: x % 2 == 0
# m = list(filter(even_check, l))
# print(l)
# print(m)


# def square_gen():
#     for i in range(10):
#         yield i*i

# l = (i*i for i in range(10))
# #
# # for k in l:
# #     print(k)

# d = {'dima':4, 'alex':5, 'ivan': 5}
#
# def get_score(num):
#     def inner():
#         return [k for k, v in d.items() if v == num]
#     return inner
#
#
# get_all_5 = get_score(5)
#
# print(get_all_5())
#
# # сделай две замкнутые функции
# #get_all_5

# import array
# arr = array.array('i', [1, 2, 3, 4])
# print(arr)


# def words_count(str_in):
#     # words = str_in.split()
#     letters_dict = {}
#     for w in str_in:
#         letters_dict[w] = letters_dict.get(w, 0) + 1
#
#
# str_in = 'mama privet'
# res = words_count(str_in)
# print(res)

# var = "False"
# print(var or 0/0)

# print(type(lambda: None))

# x = [1, 10 , 20]
# res = list(map(lambda x: x**2, x))
# print (res)

# gen = (x for x in range(10))
# print(gen)

# numbers = [1, 2, 3, 4, 5]
# class MyIterator:
#     def __init__(self, sequence):
#         self.index = 0
#         self.seq = sequence
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.seq):
#             raise StopIteration
#             self.index += 2
#         else:
#             StopIteration


# numbers = [1, 2, 3, 4, 5, 6]  # это у нас iterable
# iterator = iter(numbers)  # получаем итератор
#
# i2  = iter(iterator)
# print(next(i2))

# it = MyIterator(numbers)
# #print(next(i))
#
# for n in it:
#     print(n)

# t = ([1, 2], 3)
# t[0][1] = 10
# print(t)


# sentence = ['Pit', 'is', 'my', 'friend']
# r = [l for word in sentence for l in word]
#
# print(r)

# s = 'Python is my favorite language'
# splitted_list = s.split(maxsplit=2)
# print(splitted_list) # ['Python', 'is', 'my favorite language']




x = 10

def function():
    x = x + 5
    print(x)

function()