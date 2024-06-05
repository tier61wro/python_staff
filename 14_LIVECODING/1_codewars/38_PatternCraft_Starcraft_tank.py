
'''
train_date: 26.04.2022
kata link: https://www.codewars.com/kata/5682e72eb7354b2f39000021
points: 6 kyu
type: OOP
-------------
DESCRIPTION:

Complete the code so that when a Tank goes into SiegeMode it cannot move and its damage goes to 20.
When it goes to TankMode it should be able to move and the damage should be set to 5.

You have 3 classes:

    Tank: has a state, canMove and damage properties
    SiegeState and TankState: has canMove and damage properties

Note: The tank initial state should be TankState.

class SiegeState:
    def __init__(self):
        pass #your code here

class TankState:
    def __init__(self):
        pass #your code here

class Tank:
    def __init__(self):
        pass #your code here

    def can_move(self):
        pass #your code here

    def damage(self):
        pass #your code here

-------------
TRANSLATION:

вам нужно написать класс который определяет состояние танка из игры старкрафт
у базового класса танка должен быть атрибут состояние
у танка может быть два состояния
- Осадный когда он не может двигаться и damage = 20
- Походный (по умолчанию) когда танк может двигаться и damage = 5
-------------
===TRAINED====
базовое ООП
TODO:
дальше можно запилить задачку как пример на
-  абстрактные классыABC (from abc import ABC)
- датаклассы
-------------
'''
from self import self

import codewars_test as test


class SiegeState():
    def __init__(self, move_param=False, d = 20):
        self.move_param = move_param
        self.d = d


class TankState:
    def __init__(self, move_param=True, d = 5 ):
        self.move_param = move_param
        self.d = d


class Tank:
    def __init__(self, state = None):
        self.state = TankState()

    def can_move(self):
        return self.state.move_param

    def damage(self):
        return self.state.d


# ===== TESTS

t = Tank()
d = t.damage()
print (f"d = {d}")

@test.describe('Basic tests')

def __():
    @test.it('Tank State')
    def _():
        tank = Tank()
        test.assert_equals(tank.can_move(), True)
        test.assert_equals(tank.damage(), 5)

    @test.it('Siege State')
    def _():
        tank = Tank()
        tank.state = SiegeState()
        test.assert_equals(tank.can_move(), False)
        test.assert_equals(tank.damage(), 20)

    @test.it('Mix State')
    def _():
        tank = Tank()
        test.assert_equals(tank.can_move(), True)
        tank.state = SiegeState()
        test.assert_equals(tank.damage(), 20)