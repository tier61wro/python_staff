#Напишите функцию `binary_search`,
# которая принимает отсортированный массив `arr` и значение `target`, и возвращает индекс `target` в массиве `arr`. Если `target` не найден, функция должна вернуть `-1`.

# - `arr`: отсортированный список целых чисел (например, `[1, 20, 33, 41, 52, 64, 70, 81, 96, 119]`)
# - `target`: целое число, которое нужно найти в списке

#Выходные данные:
#Индекс `target` в массиве `arr`, если `target` присутствует в массиве
#`-1`, если `target` отсутствует в массиве

import unittest
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

list_in = [1, 20, 33, 41, 52, 64, 70, 81, 96, 119]

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


class Test(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search(list_in, 52), 4)

    def test_notfound(self):
        self.assertEqual(binary_search(list_in, 0), -1)

    def test_empty_arr(self):
        self.assertEqual(binary_search([], 2), -1)

    def test_single_found(self):
        self.assertEqual(binary_search([1], 1), 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)