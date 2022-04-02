'''
kata link:
https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python
point: 7 kyu
----
Define a method/function that removes from a given array of integers all the values contained in a second array.

[1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3] -> [2, 2, 4]
----
создайте класс и
напишите метод/функцию, который удаляет из заданного массива чисел все числа которые содержатся во втором массиве
----
Дополнительно:
сделайте тоже самое - но remove_ должен быть staticmethod
----
Дополнительно:
сделайте тоже самое - но remove_ должен быть реализован через lambda, без объявления функции через def
'''
import codewars_test as test


# class List:
#     def remove_(self, integer_list, values_list):
#         return [x for x in integer_list if x not in values_list]

# class List:
#     @staticmethod
#     def remove_(integer_list, values_list):
#         return [x for x in integer_list if x not in values_list]


class List(object):
        remove_= lambda self, i, v: [x for x in i if x not in v]



test.describe("Example Tests")
l = List()

integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
test.assert_equals(l.remove_(integer_list, values_list), [2, 2, 4])

integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
values_list  = [1, 3, 4, 2]
test.assert_equals(l.remove_(integer_list, values_list), [5, 6 ,7 ,8])

integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
values_list  = [2, 4, 3]
test.assert_equals(l.remove_(integer_list, values_list), [8, 7, 6, 5, 1])