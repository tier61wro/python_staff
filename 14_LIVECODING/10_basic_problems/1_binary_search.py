
#Напишите функцию `binary_search`,
# которая принимает отсортированный массив `arr` и значение `target`, и возвращает индекс `target` в массиве `arr`. Если `target` не найден, функция должна вернуть `-1`.

# - `arr`: отсортированный список целых чисел (например, `[1, 20, 33, 41, 52, 64, 70, 81, 96, 119]`)
# - `target`: целое число, которое нужно найти в списке

#Выходные данные:
#Индекс `target` в массиве `arr`, если `target` присутствует в массиве
#`-1`, если `target` отсутствует в массиве


import unittest
import logging
from typing import List

logging.basicConfig(level=logging.INFO)


def binary_search(arr: List[int], target: int) -> int:
    """
    Выполняет бинарный поиск целевого значения в отсортированном массиве.

    Параметры:
    arr (List[int]): Отсортированный список целых чисел.
    target (int): Целевое значение для поиска.

    Возвращает:
    int: Индекс целевого значения в списке, или -1, если значение не найдено.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1

        # Используем логирование вместо print для отладки
        logging.debug("\n" + '-'*20)
        logging.debug(f'{middle=}, {left=}, {right=}')

    return -1


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search([1, 20, 33, 41, 52, 64, 70, 81, 96, 119], 81), 7)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 20, 33, 41, 52, 64, 70, 81, 96, 119], 299), -1)

    def test_first_element(self):
        self.assertEqual(binary_search([1, 20, 33, 41, 52, 64, 70, 81, 96, 119], 1), 0)

    def test_last_element(self):
        self.assertEqual(binary_search([1, 20, 33, 41, 52, 64, 70, 81, 96, 119], 119), 9)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 81), -1)

    def test_single_element_found(self):
        self.assertEqual(binary_search([81], 81), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([81], 1), -1)


if __name__ == '__main__':
    unittest.main(verbosity=0)
