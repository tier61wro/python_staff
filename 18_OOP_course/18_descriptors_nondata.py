class StringD:
    def __init__(self, value=None):
        # if isinstance(value, str):
        #     self.set(value)
        # else:
        #     raise AttributeError('wrong attribute, must be string')
        if value:
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


class Person_simple:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        print('name getter called')
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        return self._name

    @property
    def surname(self):
        print('surname getter called')
        return self._name

    @surname.setter
    def surname(self, value):
        self._surname = value
        return self._surname


class Person_desc:
    def __init__(self, name, surname):
        self.name = StringD(name)
        print(f'descriptor attr is {type(self.name)}')
        self.surname = StringD(surname)


p_s = Person_simple('ivan', 'ivanov')
p_d = Person_desc('sasha', 'smirnov')

from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        print("get was called")
        print(f'self = {self}')
        print(f'instance = {instance}')
        print(f'owner_class = {owner_class}')
        return int(time())


class MyTime:
    epoch = Epoch()


m = MyTime()


class Someclass:
    def somefunction(self, jopa):
        print('called')

s=Someclass()


def somefunction(mama, jopa):
    print('called')


from random import choice

class Choice:
    def __init__(self, *choice):
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)


class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')

# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])
#
#     @property
#     def number(self):
#         return choice(range(1, 7))
#
#     @property
#     def flip(self):
#         return choice(['Head', 'Tails'])


d = Game()

