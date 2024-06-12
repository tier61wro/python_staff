import codewars_test as test
from typing import List


def delete_nth_reg(order: List, max_e: int) -> List:
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

# пример лябда (анонимной) функции
square = lambda x: x * x

order = [20, 37, 20, 21]
max_el = 1
# arr = [x for i, x in enumerate(order) if order[:i].count(x) < 1]

delete_nth = lambda order, max_e: [x for i, x in enumerate(order) if order[:i].count(x) < max_e]

# print(delete_nth(order, max_el))

# for i, x in enumerate(order):
#     print(f'{i} --- {x}')
#     print(order[:i])
#     print(f'freq {x} = {order[:i].count(x)}')
#     print('==============================')

# print(arr)


test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])