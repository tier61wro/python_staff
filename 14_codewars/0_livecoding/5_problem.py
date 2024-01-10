import codewars_test as test
from typing import List


def delete_nth_my(order: List, max_e: int) -> List:
    order_dict = {}
    arr_out = []
    for el in order:
        if el_count := order_dict.get(el, None):
            order_dict[el] = el_count + 1
        else:
            order_dict[el] = 1
        if order_dict[el] <= max_e:
            arr_out.append(el)
    return arr_out


# GPT remarks
def delete_nth(order: List[int], max_e: int) -> List[int]:
    count_dict = {}
    arr_out = []
    for el in order:
        count_dict[el] = count_dict.get(el, 0) + 1
        if count_dict[el] <= max_e:
            arr_out.append(el)
    return arr_out


test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])