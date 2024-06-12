# массив из N+1 целых чисел, который содержит элементы в диапазоне [1, N].
from typing import List
import unittest

numbers_list = [1, 1, 2, 2, 3] # N = 5

def find_numbers(numbers_list:List[int]) -> List[int]:
    seen = set()
    repeat = []
    for num in numbers_list:
        if num in seen:
            repeat.append(num)
        else:
            seen.add(num)
    return repeat


def find_numbers_count(numbers_list:List[int]) -> List[int]:
    d = {n: numbers_list.count(n) for n in numbers_list}
    return [k for k, v in d.items() if v > 1]



class Test_find(unittest.TestCase):
    def test_find_one_repeat(self):
        self.assertEqual(find_numbers_count([1, 2, 1]), [1])

    def test_find_two_repeat(self):
        self.assertEqual(find_numbers_count([1, 2, 1, 2]), [1, 2])

    def test_find_no_repeat(self):
        self.assertEqual(find_numbers_count([1, 2]), [])


if __name__ == "__main__":
    # print(find_numbers(numbers_list))
    print(find_numbers_count(numbers_list))
    unittest.main(verbosity=2)


