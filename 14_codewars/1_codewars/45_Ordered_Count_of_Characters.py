'''
train_date: 09.05.2022
kata link: https://www.codewars.com/kata/57a6633153ba33189e000074
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Count the number of occurrences of each character and return it as a list of tuples in order of appearance.
For empty output return an empty list.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]

-------------
TRANSLATION:
посчитайте количество вхождений каждого символа и верните назад массив из таплов в порядке их появления в строке
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
-------------
===TRAINED====
у строк есть встроенная функция count, красивое решение через нее
>>> s = 'mama'
>>> s.count('m')
2

-------------
'''

import codewars_test as test


def ordered_count(inp):
    out_arr = []
    my_dict = {}
    for l in inp:
        my_dict[l] = my_dict.get(l, 0) + 1

    for k, v in my_dict.items():
        out_arr.append((k, v))
    return out_arr

#===TESTS====

test.describe("Basic Tests")


ordered_count('')

tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    test.assert_equals(ordered_count(inp), exp)