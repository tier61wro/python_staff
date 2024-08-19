d1 = {'a':1, 'b':2}

d2 = {'c': 3}
d2.update(d1)
print(d2)

from collections import Counter

str = 'mama mila'

# Подсчитываем количество каждой буквы в строке
letter_counter = Counter(str)

# Сортируем по количеству в порядке убывания
sorted_letter_counter = letter_counter.most_common()
print(sorted_letter_counter)


from datetime import datetime
current_time = datetime.now()
print(current_time)
readable_date = current_time.strftime('%Y-%m-%d %H:%M:%S')
print(readable_date)



# class Person:
#     @staticmethod
#     def get_average(attribute):
#         attributes = {
#             'height': 178,
#             'weight': 88,
#         }
#         return attributes.get(attribute, None)
#
# p = Person()
# print(p.get_average('height'))

# class Person:
#     def __init__(self, name):
#         print("init was called")
#         self.name = name
#
#     @classmethod
#     def person_with_age(cls, name):
#         instance = cls(name)
#         instance.age = 20
#         return instance
#
# p = Person.person_with_age('vasja')
#
# print(p.age)


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @property
#     def fullname(self):
#         return f"{self.name} {self.surname}"
#
#     @fullname.setter
#     def fullname(self, value):
#         name, surname = value.split()
#         self.name = name
#         self.surname = surname
#
# p = Person('Ivan', 'Dorn')
# print(p.fullname)  # Вывод: Ivan Dorn
# p.fullname = 'Ivan Ivanov'
# print(p.fullname)  # Вывод: Ivan Ivanov


# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
# p = Person('Ivan')
#
#
# print(p.name)
# p.name = 'Petr'
# print(p.name)

# class Person():
#     def __init__(self, h, w):
#         self.height = h
#         self.weight = w
#
#     @property
#     def bmi(self):
#         return self.weight / self.height ** 2
#
# p = Person(1.79, 91)
# print(p.bmi)

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        return "some sound"

class Dog(Animal):
    def make_sounda(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# l = Dog()
print(Animal.mro())
# print(a.weight)
# print(l.make_sound())
# print(l.__dict__)
