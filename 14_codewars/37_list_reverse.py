
'''
train_date: 25.04.2022
kata link: https://www.codewars.com/kata/55de9c184bb732a87f000055/train/python
points: 6 kyu
type: basic
-------------
DESCRIPTION:
-------------
TRANSLATION:
сделайте функцию которая делает реверс исходного массива
-------------
===TRAINED====
правильное копирование массива через copy

Александр К., [25.04.2022 13:37]
def reverse(seq):
    r = seq[::-1]
    seq = r.copy()

Александр К., [25.04.2022 13:39]
а если так - то ок

def reverse(seq):
    r = seq[::-1]
    for i, el in enumerate(r):
        seq[i] = el

Александр К., [25.04.2022 13:37]
def reverse(seq):
    r = seq[::-1]
    seq = r.copy()

Александр К., [25.04.2022 13:39]
а если так - то ок

def reverse(seq):
    r = seq[::-1]
    for i, el in enumerate(r):
        seq[i] = el

Fomin Danila, [25.04.2022 14:03]
[In reply to Александр К.]
мысли ссылками


def reverse(seq):
    r = seq[::-1]
    seq = r.copy()

a = [1, 2, 3] #   [1, 2, 3] -> a
reverse(a)  #    [1, 2, 3] -> a, seq
   … seq = r.copy()  # [3, 2, 1] -> seq, [1, 2, 3] -> a

Александр К., [25.04.2022 13:37]
def reverse(seq):
    r = seq[::-1]
    seq = r.copy()

Александр К., [25.04.2022 13:39]
а если так - то ок

def reverse(seq):
    r = seq[::-1]
    for i, el in enumerate(r):
        seq[i] = el

Fomin Danila, [25.04.2022 14:03]
[In reply to Александр К.]
мысли ссылками


def reverse(seq):
    r = seq[::-1]
    seq = r.copy()

a = [1, 2, 3] #   [1, 2, 3] -> a
reverse(a)  #    [1, 2, 3] -> a, seq
   … seq = r.copy()  # [3, 2, 1] -> seq, [1, 2, 3] -> a

Александр К., [25.04.2022 14:36]
In [1]: a = [1,2,3]

In [2]: id(a)
Out[2]: 140667101728384

In [3]: b = a

In [4]: id(b)
Out[4]: 140667101728384

In [5]: c = a[:]

In [6]: id(c)
Out[6]: 140667102110784
-------------
'''

import codewars_test as test

def reverse(seq):
    r = seq.copy()
    for i, el in enumerate(r):
        seq[len(seq) -1 - i] = el

def reverse(seq):
    r = seq.copy()
    for i, el in enumerate(r):
        seq[len(seq) -1 - i] = el

# seq = [1, 2, 3, 4, 5]
# reverse(seq)



@test.describe('Example Tests')
def example_tests():
    seq = [1, 2, 3, 4, 5]
    reverse(seq)
    test.assert_equals([5, 4, 3, 2, 1], seq)

    seq = ['?', 'you', 'are', 'how', 'world', 'hello']
    reverse(seq)
    test.assert_equals(['hello', 'world', 'how', 'are', 'you', '?'], seq)

    seq = [{'b': 2}, {'a': 1}]
    reverse(seq)
    test.assert_equals([{'a': 1}, {'b': 2}], seq)