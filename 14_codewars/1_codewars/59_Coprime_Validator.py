'''
train_date: 03.05.2022
kata link: https://www.codewars.com/kata/585c50e75d0930e6a7000336
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Write a program to determine if the two given numbers are coprime.
A pair of numbers are coprime if their greatest shared factor is 1.

The inputs will always be two positive integers between 2 and 99.

Examples
20 and 27:

Factors of 20: 1, 2, 4, 5, 10, 20
Factors of 27: 1, 3, 9, 27
Greatest shared factor: 1
Result: 20 and 27 are coprime
12 and 39:

Factors of 12: 1, 2, 3, 4, 6, 12
Factors of 39: 1, 3, 13, 39
Greatest shared factor: 3
Result: 12 and 39 are not coprimes
-------------
TRANSLATION:
-------------
===TRAINED====
-------------
'''
import codewars_test as test

def are_coprime(n,m):
    # Enter code here

#===TESTS====
import codewars_test as test
from solution import are_coprime

@test.describe("Coprime Validator")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(are_coprime(20, 27), True, 'The numbers were 20 and 27')
        test.assert_equals(are_coprime(12, 39), False, 'The numbers were 12 and 39')