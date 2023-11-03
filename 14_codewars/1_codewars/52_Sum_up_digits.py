
'''
train_date: 17.05.2022
kata link: https://www.codewars.com/kata/55da6c52a94744b379000036
points: 7 kyu
type: REGEXP
-------------
DESCRIPTION:
Given a random string consisting of numbers, letters, symbols, you need to sum up the numbers in the string.

Note:

    Consecutive integers should be treated as a single number. eg, 2015 should be treated as a single number 2015, NOT four numbers
    All the numbers should be treaded as positive integer. eg, 11-14 should be treated as two numbers 11 and 14.
    Same as 3.14, should be treated as two numbers 3 and 14
    If no number was given in the string, it should return 0

Example:

str = "In 2015, I want to know how much does iPhone 6+ cost?"

The numbers are 2015, 6

Sum is 2021.

-------------
TRANSLATION:
вам нужно написать функцию которая находит в заданное строке все цифры, а затем суммирует их и возвращает сумму
-------------
===TRAINED====
вспомнил что в питоне есть функция
re.findall - которая все совпадения закидывает в массив

то что я сделал генератором еще проще можно сделать через map
вот так:
return sum(map(int, re.findall(r'\d+', s)))
-------------
'''

import codewars_test as test
import re

str_in = "In 2015, I want to know how much does iPhone 6+ cost?"

def sum_from_string(str_in):
    return sum([int(x) for x in re.findall(r"\d+", str_in)])

#===TESTS====

r = sum_from_string(str_in)
print(r)

@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def do_basic_tests():
        test.assert_equals(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"),2021)
        test.assert_equals(sum_from_string("1+1=2"),4)
        test.assert_equals(sum_from_string("e=mc^2"),2)
        test.assert_equals(sum_from_string("aHR0cDovL3d3dy5jb2Rld2Fycy5jb20va2F0YS9uZXcvamF2YXNjcmlwdA=="),53)
        test.assert_equals(sum_from_string("a30561ff4fb19170aa598b1431b52edad1fcc3e0"),51820)
        test.assert_equals(sum_from_string("x1KT   CmZ__\rYouOY8Uqu-ETtz"), 9)
        test.assert_equals(sum_from_string("x1KT-8&*@\"CmZ__\rYouO  __Y8Uq\\u-ETtz"), 17)
        test.assert_equals(sum_from_string(""),0, "Empty string should return 0")
        test.assert_equals(sum_from_string("Hello World"),0, "String with no numbers should return 0")