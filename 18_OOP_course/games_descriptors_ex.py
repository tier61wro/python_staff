from random import choice


class Game:
    def __init__(self, *choice_list):
        self.choice_list = choice_list

    def __get__(self, instance, owner_class):
        return choice(self.choice_list)


class GameChoice:
    flip = Game('Heads', 'Tails')
    number = Game(1, 2, 3, 4, 5, 6)

d = GameChoice()