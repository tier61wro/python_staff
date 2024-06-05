'''
train_date: 06.05.2022
kata link: https://www.codewars.com/kata/55be95786abade3c71000079
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Linked Lists - Push & BuildOneTwoThree

Write push() and buildOneTwoThree() functions to easily update and initialize linked lists.
Try to use the push() function within your buildOneTwoThree() function.

Here's an example of push() usage:

var chained = null
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null

The push function accepts head and data parameters, where head is either a node object or null/None/nil.
Your push implementation should be able to create a new linked list/node when head is null/None/nil.

The buildOneTwoThree function should create and return a linked list with three nodes: 1 -> 2 -> 3 -> null
-------------
TRANSLATION:
-------------
===TRAINED====
-------------
'''

import codewars_test as test


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):


# Your code goes here.

def build_one_two_three():
# Your code goes here.

#===TESTS====

@test.describe("Fixed tests")
def fxd():
    @test.it("tests for inserting a node before another node.")
    def f():
        test.assert_equals(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
        test.assert_equals(push(None, 1).next, None, "Should be able to create a new linked list with push().")
        test.assert_equals(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
        test.assert_equals(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")

    @test.it("tests for building a linked list.")
    def f():
        test.assert_equals(build_one_two_three().data, 1, "Value at index 0 should be 1.")
        test.assert_equals(build_one_two_three().next.data, 2, "Value at index 1 should be 2.")
        test.assert_equals(build_one_two_three().next.next.data, 3, "Value at index 2 should be 3.")
        test.assert_equals(build_one_two_three().next.next.next, None, "Value at index 3 should be null.")