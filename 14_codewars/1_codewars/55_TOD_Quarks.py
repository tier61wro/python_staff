'''
train_date: 06.06.2022
kata link: https://www.codewars.com/kata/5882b052bdeafec15e0000e6
points: 7 kyu
type BASIC
-------------
DESCRIPTION:

Background
You're modelling the interaction between a large number of quarks
and have decided to create a Quark class so you can generate your own quark objects.

Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.

Your task
Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green")
and any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').

Every quark has the same baryon_number (BaryonNumber in C#): 1/3.

Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with another quark via the strong force.
When two quarks interact they exchange colors.

Example
>>> q1 = Quark("red", "up")
>>> q1.color
"red"
>>> q1.flavor
"up"
>>> q2 = Quark("blue", "strange")
>>> q2.color
"blue"
>>> q2.baryon_number
0.3333333333333333
>>> q1.interact(q2)
>>> q1.color
"blue"
>>> q2.color
"red"

-------------
TRANSLATION:
вам нужно написать класс который будет создавать Кварк
у кварка должно быть два задаваемых атрибута (color и flavor) и один постоянный baryon_number всегда равный 1/3
кроме того у кварка должен быть метод interact который позволяет ему обмениваться цветом с другим кварком
-------------
===TRAINED====
лучше делать init вот так
self.color, self.flavor, self.baryon_number = color, flavor, 1/3.
-------------
'''

import codewars_test as test

class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1/3

    def interact(self, another_quark):
        self.color, another_quark.color = another_quark.color, self.color

#===TESTS====
q1 = Quark("red", "up")
q2 = Quark("blue", "strange")

test.describe("Object initialization")
test.assert_equals(q1.color, "red")
test.assert_equals(q2.flavor, "strange")

test.describe("Class attributes")
test.assert_equals(q2.baryon_number, 1.0 / 3)

test.describe("Quarks trade colors when interacting")
q1.interact(q2)
test.assert_equals(q1.color, "blue")
test.assert_equals(q2.color, "red")