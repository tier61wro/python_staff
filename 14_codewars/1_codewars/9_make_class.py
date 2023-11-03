'''
#10.05.2020
class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color
Give me the power to create a similar class like this:
Animal = make_class("name", "species", "age", "health", "weight", "color")

def make_class(*args):
    return
----
если нужно получить пары из двух списков (связать их молнией)
zip(args_atr, args_val)
self.color = color
setattr(self, 'color', color)
если нужно выставить атрибут класса равный значению
setattr(self, atr, val)
'''
def make_class(*args_atr):
    class A:
        def __init__(self, *args_val):
            for i in args_val:
                print(i)
            for atr, val in zip(args_atr, args_val):
                setattr(self, atr, val)

    return A


class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color
        setattr(self, 'color', color)




Animel = make_class("name", "species", "age", "health", "weight", "color")

print(Animel)

dog1 = Animal("Bob", "Dog", 5, "good", "5""0lb", "brown")
dog2 = Animel("Bob", "Dog", 5, "good", "5""0lb", "brown")

print(dog1.color)
print(dog2)