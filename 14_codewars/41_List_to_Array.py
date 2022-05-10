'''
train_date: 05.05.2022
kata link: https://www.codewars.com/kata/557dd2a061f099504a000088
points: 7 kyu
type: OOP
-------------
DESCRIPTION:


Linked lists are data structures composed of nested or chained objects, each containing
a single value and a reference to the next object.

Here's an example of a list:

class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

LinkedList(1, LinkedList(2, LinkedList(3)))

Write a function listToArray (or list_to_array in Python) that converts a list to an array, like this:

[1, 2, 3]

Assume all inputs are valid lists with at least one value. For the purpose of simplicity,
all values will be either numbers, strings, or Booleans.

-------------
TRANSLATION:
Связанные структуры это структуры составленные из нескольких вложенных или связанных цепью объектов,
каждый содержит единичное значение и ссылку на следующий объект
напишите функцию которая будет принимать на вход связанные объект и возвращать назад массив
-------------
===TRAINED====
сам написал рекурсивную функцию :)

решение по красоте:
def list_to_array(lst):
    return ([lst.value] + list_to_array(lst.next)) if lst else []

-------------
'''

import codewars_test as test


class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def list_to_array(node):
    arr_back = []

    def req_fun(n):
        arr_back.append(n.value)
        if n.next:
            req_fun(n.next)

    req_fun(node)
    return arr_back


#===TESTS====

u = LinkedList(1)
test.assert_equals(list_to_array(u), [1])

u = LinkedList(4, LinkedList(25, LinkedList(30)))
test.assert_equals(list_to_array(u), [4, 25, 30])

u = LinkedList(2, LinkedList(40, LinkedList(43, LinkedList(25, LinkedList(125)))))
test.assert_equals(list_to_array(u), [2, 40, 43, 25, 125])
