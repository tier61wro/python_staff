'''
11.10.20
Create a function that returns the name of the winner in a fight between two fighters.
Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.
Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
'''

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    dc_f = (fighter1.health - 1) // fighter2.damage_per_attack
    dc_s = (fighter2.health - 1) // fighter1.damage_per_attack
    print(f'dc_f = {dc_f}, dc_s = {dc_s}')
    if dc_f > dc_s:
        return fighter1.name
    elif dc_f < dc_s:
        return fighter2.name
    else:
        if first_attacker == fighter1.name:
            return fighter1.name
        else:
            return fighter2.name



# res = declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")
#test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
res = declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry")

print(res)
