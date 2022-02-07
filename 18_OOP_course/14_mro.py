class Person:
    def hello(self):
        print('hi from person')


class FoodMixin:
    def get_food(self):
        if not hasattr(self, 'food'):
            self.food = 'Makaroshki'
        print(f'i like {self.food}')


class Student(FoodMixin, Person):
    food = 'Pizza'


class Prof(FoodMixin, Person):
    pass


p1 = Student()
p2 = Prof()
