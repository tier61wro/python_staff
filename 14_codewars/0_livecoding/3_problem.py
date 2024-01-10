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
"""

import codewars_test as test

def reverse(seq):
    print(f'START = {seq}')
    # your code here
    start = 0
    end = len(seq) - 1
    while start <  end:
        (seq[start], seq[end])  = (seq[end], seq[start])

        start += 1
        end -= 1
    print(f'END = {seq}')



seq = ['?','you','are','how','world','hello']
reverse(seq)
test.assert_equals(['hello','world','how','are','you','?'], seq)

