#4.05.2020
"""
Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use "x=list()" instead if you need it
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
----
pop не просто выталкивает последний элемент из массива, но и возвращает его в переменную

"""

def reverse(seq):
    reversed_list = list()
    for k in range(0, len(seq)):
        reversed_list.append(seq.pop())

    return reversed_list



#seq = ['?','you','are','how','world','hello']
seq = [{'b':2},{'a':1}]

l = reverse(seq)
print(l)