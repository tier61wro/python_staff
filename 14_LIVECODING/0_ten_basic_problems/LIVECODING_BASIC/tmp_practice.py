#Напишите функцию `binary_search`,
# которая принимает отсортированный массив `arr` и значение `target`, и возвращает индекс `target` в массиве `arr`. Если `target` не найден, функция должна вернуть `-1`.

# - `arr`: отсортированный список целых чисел (например, `[1, 20, 33, 41, 52, 64, 70, 81, 96, 119]`)
# - `target`: целое число, которое нужно найти в списке

#Выходные данные:
#Индекс `target` в массиве `arr`, если `target` присутствует в массиве
#`-1`, если `target` отсутствует в массиве

from typing import List
import logging

l = [1, 20, 33, 41, 52, 64, 70, 81, 96, 119]

def binary_search(arr: List[int], target: int)-> int:
    '''
    :param arr - sorted list
    :param target - number which we try to find
    :return: index of target element, -1 if not find
    '''
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1
        logging.debug("-" * 10)
        logging.debug(f'{middle=} {left=} {right=}')
    return -1


logging.basicConfig(level=logging.DEBUG)

print(binary_search(l, 299))

