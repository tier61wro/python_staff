
'''
train_date: 16.04.2022
kata link: https://www.codewars.com/kata/566d5e2e57d8fae53c00000c
points: 6 kyu
type: basic
-------------
DESCRIPTION:
After yet another dispute on their game the Bingo Association decides to change course and automate the game.

Can you help the association by writing a method to create a random Bingo card?

Task:

    Finish method:
    def get_bingo_card()

A Bingo card contains 24 unique and random numbers according to this scheme:

    5 numbers from the B column in the range 1 to 15
    5 numbers from the I column in the range 16 to 30
    4 numbers from the N column in the range 31 to 45
    5 numbers from the G column in the range 46 to 60
    5 numbers from the O column in the range 61 to 75


The card must be returned as an array of Bingo style numbers:
[ "B14", "B12", "B5", "B6", "B3", "I28", "I27", ... ]

The numbers must be in the order of their column: B, I, N, G, O. Within the columns the order of the numbers is random.

-------------
TRANSLATION:
Вам нужно сгенерировать массив который будет определять собой карточку для лотереи по следующим правилам:

A Bingo card contains 24 unique and random numbers according to this scheme:
Лотерейная карточка содержит 24 уникальных и различных числа по следующей схеме:
    5 цифр колонки B в интервале от 1 до 15
    5 цифр колонки I в интервале от 16 до 30
    4 цифр колонки N в интервале от 31 до 45
    5 цифр колонки G в интервале от 46 до 60
    5 цифр колонки O в интервале от 61 до 75
пример карточки:
['B1', 'B6', 'B3', 'B12', 'B15',
'I20', 'I16', 'I18', 'I26', 'I19',
'N40', 'N32', 'N37', 'N41',
'G57', 'G48', 'G58', 'G47', 'G46',
'O73', 'O63', 'O71', 'O70', 'O68']
-------------
===TRAINED====
удаление элемента из массива по индексу
del card[12]
итерирование по массиву вместе с индексом
for id, l in enumerate(letters):

==== КРАСОТА ====
import random

def get_bingo_card():
    b = ['B' + str(n) for n in random.sample(range(1, 16), 5)]
    i = ['I' + str(n) for n in random.sample(range(16, 31), 5)]
    n = ['N' + str(n) for n in random.sample(range(31, 46), 4)]
    g = ['G' + str(n) for n in random.sample(range(46, 61), 5)]
    o = ['O' + str(n) for n in random.sample(range(61, 76), 5)]
    return b + i + n + g + o
-------------
'''
import codewars_test as test

from random import choice


def get_bingo_card():
    card = []
    letters = [l for l in 'bingo'.upper()]
    b_n = [1, 16, 31, 46, 61, 76]
    for id, l in enumerate(letters):
        for n in range(1, 6):
            while True:
                el = f'{l}{choice(range(b_n[id], b_n[id + 1]))}'
                if el not in card:
                    card.append(el)
                    break

    del card[12]
    return card


card = get_bingo_card()
print(card)


def get_column(card, p):
    r = []
    for i in card:
        if i[0] == p:
            r.append(i)
    return r


def get_column_order(card):
    r = ''
    for i in card:
        if r == '' or r[-1] != i[0]:
            r = r + i[0]
    return r


def numbers_are_in_range(column, min, max):
    for i in column:
        v = int(i[1:])
        if v < min or v > max:
            return False
    return True


def numbers_are_random(card):
    v = int(card[0][1:])
    for i in range(1, 24):
        v1 = int(card[i][1:])
        if v1 < v:
            return True
        v = v1
    return False


test.it("Bingo card:")

test.assert_equals(len(card), 24, "Has 24 numbers")
test.assert_equals(len(set(card)), 24, "Each number on card is unique")
test.assert_equals(len(get_column(card, 'B')), 5, "Column 'B' contains 5 items")
test.assert_equals(len(get_column(card, 'I')), 5, "Column 'I' contains 5 items")
test.assert_equals(len(get_column(card, 'N')), 4, "Column 'N' contains 4 items")
test.assert_equals(len(get_column(card, 'G')), 5, "Column 'G' contains 5 items")
test.assert_equals(len(get_column(card, 'O')), 5, "Column 'O' contains 5 items")
test.assert_equals(get_column_order(card), 'BINGO', "Numbers are ordered by column")
test.assert_equals(numbers_are_in_range(get_column(card, 'B'), 1, 15), True,
                   "Numbers of column 'B' are between 1 and 15")
test.assert_equals(numbers_are_in_range(get_column(card, 'I'), 16, 30), True,
                   "Numbers of column 'I' are between 16 and 30")
test.assert_equals(numbers_are_in_range(get_column(card, 'N'), 31, 45), True,
                   "Numbers of column 'N' are between 31 and 45")
test.assert_equals(numbers_are_in_range(get_column(card, 'G'), 46, 60), True,
                   "Numbers of column 'G' are between 46 and 60")
test.assert_equals(numbers_are_in_range(get_column(card, 'O'), 61, 75), True,
                   "Numbers of column 'O' are between 61 and 75")
test.assert_equals(numbers_are_random(card), True, "Numbers are random within the columns")

