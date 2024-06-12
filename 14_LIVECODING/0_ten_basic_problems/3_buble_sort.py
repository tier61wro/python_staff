from typing import List

def buble_sort(list_in: List[int]) -> List[int]:
    n = len(list_in)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_in[j] > list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j + 1], list_in[j]
    return list_in

number_list = [10, 3, 1, 2, 11]
res = buble_sort(number_list)
print(res)