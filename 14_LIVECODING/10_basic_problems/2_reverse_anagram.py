'''
реверс строки:
Срез
reversed
цикл for
'''

import unittest

def reverse_string(str_in: str) -> str:
    return str_in[::-1]


def reverse_string(str_in: str) -> str:
    letters_reverse = ['a' for i in str_in]
    length = len(letters_reverse)
    for i, l in enumerate(str_in):
        letters_reverse[length - i - 1] = l
    print(letters_reverse)


def reverse_string(str_in: str) -> str:
    result = ""
    for l in str_in:
        result = l + result
    return result

def reverse_string(str_in: str) -> str:
    return("".join(list(reversed(str_in))))


def is_palindrome(str_in: str) -> bool:
    return str_in == str_in[::-1]


def is_anagram(first: str, second: str) -> bool:
    return sorted(first) == sorted(second)

def is_anagram(first: str, second: str) -> bool:
    return set(first) == set(second)


print(is_anagram('roma', 'omar'))
print(reverse_string("brat"))


class Tests(unittest.TestCase):
    def test_normal_string(self):
        self.assertTrue(is_anagram('omar','roma'))

    def test_empty_string(self):
        self.assertTrue(is_anagram('',''))


if __name__ == '__main__':
    unittest.main(verbosity=2)
