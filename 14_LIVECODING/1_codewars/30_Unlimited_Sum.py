
'''
train_date: 05.04.2022
kata link: https://www.codewars.com/kata/536c738e49aa8b663b000301
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Write a function sum that accepts an unlimited number of integer arguments, and adds all of them together.

The function should reject any arguments that are not integers, and sum the remaining integers.

sum(1, 2, 3)    ==>  6
sum(1, "2", 3)  ==>  4
-------------
TRANSLATION:
напишите функцию которая принимает на вход неограниченное количество целых чисел и возвращает их сумму
Функция должна отбрасывать все аргументы которые не целые и суммровать оставшиеся
-------------
===TRAINED====
подковырка в том что в условии задания требуется чтобы функция называлась sum
и если мы захотим использовать функцию sum то получится говно

красивый выход из ситуации:

from __builtin__ import sum as builtin_sum

def sum(*args):
    return builtin_sum(arg for arg in args if isinstance(arg, int))

или

s = sum
def sum(*args):
    return s(x for x in args if isinstance(x, int))

проверка числа на int
if isinstance(x, int)
можно еще вот так
if type(i) is int:

задача со * сделать это через lambda
-------------
'''

import codewars_test as test


def sum(*args):
    sum_num = 0
    for number in [x for x in args if isinstance(x, int)]:
        sum_num += number

    return sum_num




print(sum(1, 2, 3))

test.assert_equals(sum(1, 2, 3), 6)
test.assert_equals(sum(1, "2", 3), 4)