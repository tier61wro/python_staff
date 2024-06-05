'''
train_date: 14.06.2022
kata link: https://www.codewars.com/kata/55cd4ce59382498cbd000080
points: 7 kyu
type: OOP
-------------
DESCRIPTION:
Class conundrum - Bug Fixing #7
Oh no! Timmy's List Class has broken!
Can you help timmy and fix his class?
Timmy has a List class he has created, this is used for type strict arrays (which timmy calls Lists).

When timmy calls the Count property of the list it still remains at 0 when adding items.

Also it fails when timmy trys to chain the adds e.g.

my_list.add(0).add(1)
-------------
TRANSLATION:
помогите Тимми починить код, так чтобы возвращалось правильное количество элементов и чтобы работали цепочки добавления типа:
my_list.add(0).add(1)
-------------
===TRAINED====
по сути из функции add возвращалось не правильное значение
должен был быть self а  был item
крутой момент, чтобы узнать конкретное название типа которое пришло к нам на вход
делаем вот так
self.type.__name__
-------------
'''

import codewars_test as test


class List:
    def __init__(self, type_in):
        self.type = type_in
        self.items = []
        self.count = 0

    def add(self, item):
        if type(item) != self.type:
            return f"This item is not of type: {self.type.__name__}"
        self.items.append(item)
        self.count += 1
        return self

#===TESTS====
my_list = List(str)

test.assert_equals(my_list.add('Hello').count, 1, 'How many items in the List?')
test.assert_equals(my_list.add(5), "This item is not of type: str", 'Wrong type added')
test.assert_equals(my_list.add(' ').add('World!').count, 3, 'How many items in the List?')