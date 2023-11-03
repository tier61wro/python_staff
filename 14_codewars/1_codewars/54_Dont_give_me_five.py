'''
train_date: 19.05.2022
kata link: https://www.codewars.com/kata/5813d19765d81c592200001a
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Don't give me five!

In this kata you get the start number and the end number of a region and should return
 the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

Examples:
1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
-------------
TRANSLATION:
у вас есть диапазон чиесел заданный первым числом и вторым числом
числа могут быть отрицательными
ваша задача посчитать сколько в указанном диапазоне чисел которые не содержат в себе числа 5
-------------
===TRAINED====
красивше через генератор
def dont_give_me_five(start,end):
    return len([num for num in range(start, end+1) if '5' not in str(num)])

-------------
'''

import codewars_test as test


def dont_give_me_five(start,end):
    res_list = []
    for x in range(start, end + 1):
        if "5" not in str(x):
            res_list.append(x)
    return len(res_list)

r = dont_give_me_five(4,6)
print(r)
#===TESTS====
import codewars_test as test
# from solution import dont_give_me_five

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(dont_give_me_five(1,9), 8)
        test.assert_equals(dont_give_me_five(4,17), 12)