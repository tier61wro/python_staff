'''
check if given string is in upper case
----
проверка того все ли буквы в заданной строке написаны в верхнем регинстре
тоесть по сути мы проверям не содержит ли строка букв в нижнем регистре
https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/solutions/python
----
ord('z')+1)
тут прибавляем единицу из-за того что
print(list(range(1,3)))
[1, 2]
----
красивое решение:
def is_uppercase(inp):
    return inp == inp.upper()
'''
import codewars_test as test

small_letters = list(map(chr, range(ord('a'), ord('z')+1)))


def is_uppercase(inp):
    for i in inp:
        if i in small_letters:
            return False
    return True

inp = 'Mama'
inp1 = 'MAMA MILA RAMU'

print(is_uppercase(inp))
print(is_uppercase(inp1))


def gen_test_case(inp, res):
    test.assert_equals(is_uppercase(inp), res, inp)

test.describe("Basic Tests")

gen_test_case("c", False)
gen_test_case("C", True)
gen_test_case("hello I AM DONALD", False)
gen_test_case("HELLO I AM DONALD", True)
gen_test_case("$%&", True)