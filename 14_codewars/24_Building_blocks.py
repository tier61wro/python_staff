'''
https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

----
Write a class Block that creates a block (Duh..)
##Requirements
The constructor should take an array as an argument,
this will contain 3 integers of the form [w, l, h] from which the Block should be created.
Define these methods:

`get_width()` return the w of the `Block`
`get_length()` return the l of the `Block`
`get_height()` return the h of the `Block`
`get_volume()` return the volume of the `Block`
`get_surface_area()` return the surface area of the `Block`

# Examle:

    b = Block([2,4,6]) -> create a `Block` object with a w of `2` a l of `4` and a h of `6`
    b.get_width() -> return 2
    b.get_length() -> return 4
    b.get_height() -> return 6
    b.get_volume() -> return 48
    b.get_surface_area() -> return 88
----
нужно написать класс который будет создавать объект параллелепипеда (Block)
конструктор должен принимать на вход три элемента [w, l, h] которые задают длину, ширину, высоту
так же надо определить три метода которые будут возвращать эти параметры
`get_width()` возвращает w `Block`
`get_length()` возвращает l `Block`
`get_height()` возвращает h `Block`
и два доп метода
`get_volume()` возвращает объем `Block`
`get_surface_area()` возвращает площадь `Block`
'''


import codewars_test as test


class Block:
    def __init__(self, params):
        (self.w, self.l, self.h) = params

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

    def get_length(self):
        return self.l

    def get_volume(self):
        return self.w * self.l * self.h

    def get_surface_area(self):
        return 2*(self.l * self.w + self.w * self.h + self.h * self.l)


block1 = Block([2, 2, 2])


test.assert_equals(block1.get_width(), 2)
test.assert_equals(block1.get_length(), 2)
test.assert_equals(block1.get_height(), 2)
test.assert_equals(block1.get_volume(), 8)
test.assert_equals(block1.get_surface_area(), 24)