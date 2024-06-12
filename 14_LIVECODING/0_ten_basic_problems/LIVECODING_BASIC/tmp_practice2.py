import logging
from typing import List
import unittest

logging.basicConfig(level=logging.DEBUG)
list_in = [1, 2, 56, 66, 88, 100, 120]

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        logging.debug(f'{left=}, {right=}, {middle=}')
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return -1

# class Test(unittest.TestCase):
#     def test_found(self):
#         self.assertEqual(binary_search(list_in, 52), 4)
#
#     def test_notfound(self):
#         self.assertEqual(binary_search(list_in, 0), -1)

class BinarySearchTest(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search(list_in, 66), 1)


if __name__ == "__main__":
    print("we are here")
    unittest.main(verbosity=2)