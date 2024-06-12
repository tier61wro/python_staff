from typing import List
import logging

logging.basicConfig(level = logging.DEBUG)


def buble_sort(list_in: List[int]) -> int:
    n = len(list_in)
    for i in range(n):
        logging.debug(f"======={i}=======")
        for j in range(n - i - 1):
            logging.debug(f"{j=}")
            logging.debug(f'before {list_in=}')
            if list_in[j] > list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j + 1], list_in[j]
            logging.debug(f'after {list_in=}')

    return list_in

l = [4, 10, 2, 12, 11]

print(buble_sort(l))
