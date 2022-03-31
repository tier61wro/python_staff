'''
https://www.codewars.com/kata/54fe05c4762e2e3047000add
----
You are a leader of a small pirate crew.
And you have a plan.
With the help of OOP you wish to make a pretty efficient system to identify ships with a heavy booty on board.

Unfortunately for you, people weigh a lot this days, so how do you know if a ship if full of gold and not people?

You begin with writing a generic Ship class:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:

    draft - an estimate of the ship's weight based on how low it is in the water
    crew - the count of crew on board

Titanic = Ship(15, 10)

Taking into account that an average crew member on board adds 1.5 units to the draft, a ship that has a draft of more than 20 without crew is considered worthy to loot. Any ship weighing that much must have a lot of booty!

Add the method

is_worth_it

to decide if the ship is worthy to loot. For example:

Titanic.is_worth_it()
False

This Kata teaches you the very basic of method creation.

----
Вы капитан пиратского корабля и вам нужно сделать метод который будет позволять оценить стоит ли атаковать корабль или нет
метод должен возвращать True если стоит и False иначе
каждый человек дает осадку 1.5 балла
корабль считается ценным если разница между его осадкой и осадкой которую дают люди больше чем 20
'''
import codewars_test as test

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if self.draft - self.crew * 1.5 > 20:
            return True
        return False


EmptyShip = Ship(0, 0)
test.assert_equals(EmptyShip.is_worth_it(), False)