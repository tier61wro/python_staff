class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # def __hash__(self):
    #     return hash(self._name)
    #
    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self._name == person_obj._name

class Car:
    def __init__(self, mark):
        self._mark = mark


p1 = Person('Ivan')
p2 = Person('Ivan')
p3 = Person('Sasha')

c1 = Car('Mazda')