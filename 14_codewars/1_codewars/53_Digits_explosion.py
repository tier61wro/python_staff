'''
train_date: 18.05.2022
kata link: https://www.codewars.com/kata/some_hash/
points: 7 kyu
type: Basic
-------------
DESCRIPTION:
Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
Examples
explode("312")
should return :
"333122"

-------------
TRANSLATION:
Дана строка состоящая из цифр от 0 до 9
вам нужно на основе этой строки сгенерировать строку где каждая цифра будет повторяться в соответствии со своим значением

-------------
===TRAINED====
оператор повторения *
по красоте вот так
return ''.join(c * int(c) for c in s)
потому как join умеет работать с генератором
In [2]: type((c * int(c) for c in s))
Out[2]: generator
генератор это не обязательно квадратные скобки
-------------
'''

import codewars_test as test
from sys import exit

def explode(s):
    return "".join([(d*int(d)) for d in s])


#===TESTS====
test.assert_equals(explode("312"), "333122")
test.assert_equals(explode("102269"),"12222666666999999999")
test.assert_equals(explode("0"), "")
test.assert_equals(explode("000"), "")
test.assert_equals(explode("123"), "122333")