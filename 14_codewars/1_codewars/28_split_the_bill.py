'''
train_date: 03.04.2022
kata link: https://www.codewars.com/kata/5641275f07335295f10000d0/
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
It's tricky keeping track of who is owed what when spending money in a group. Write a function to balance the books.

The function should take one parameter: an object/dict with two or more name-value pairs which represent the members of the group and the amount spent by each.
The function should return an object/dict with the same names, showing how much money the members should pay or receive.

Further points:

The values should be positive numbers if the person should receive money from the group, negative numbers if they owe money to the group.
If value is a decimal, round to two decimal places.

Translations and comments (and upvotes!) welcome.
Example

3 friends go out together: A spends £20, B spends £15, and C spends £10.
The function should return an object/dict showing that A should receive £5, B should receive £0, and C should pay £5.
-------------
TRANSLATION:
вы сходили с группой друзей в ресторан и чтобы заплатить по счету каждый скинулся сколько мог.
нужно написать функцию которая позволяет рассчитать сколько нужно вернуть/забрать денег каждому из друзей, чтобы в
итоге все заплатили поровну
Значения должны быть положительными если человек должен получить деньги и отрицательными если отдать
Если значение дробное - округляем до двух знаков после запятой
group = {
    'A': 20,
    'B': 15,
    'C': 10
}

split_the_bill(group) # returns {'A': 5, 'B': 0, 'C': -5}
-------------
===TRAINED====
# округление
# round(sum(x.values())/len(x), 2)

# пройтись по паре ключ-значение в словаре:
# for k, v in x.items():
-------------
'''


import codewars_test as test

def split_the_bill(x):
    result_dict = {}
    average_sum = round(sum(x.values())/len(x), 2)
    for k, v in x.items():
        result_dict[k] = round(v - average_sum, 2)
    return result_dict


print(split_the_bill({'A': 1, 'B': 1, 'C': 3}))

# {'A': -0.67, 'B': -0.67, 'C': 1.33}
# test.assert_equals(split_the_bill({'A': 20, 'B': 15, 'C': 10}), {'A': 5, 'B': 0, 'C': -5})
# test.assert_equals(split_the_bill({'A': 40, 'B': 25, 'X': 10}), {'A': 15, 'B': 0, 'X': -15})