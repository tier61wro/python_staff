# массив из N+1 целых чисел, который содержит элементы в диапазоне [1, N].
from typing import List

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

# print(find_numbers(numbers_list))
print(find_numbers_count(numbers_list))