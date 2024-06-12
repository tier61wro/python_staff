# class KoreanPerson1:
#     def __init__(self, name, surname='Kim'):
#         self._name = name
#         self._surname = surname
#         self.fullname = f"{self._name} {self._surname}"
#
#
# p1 = KoreanPerson1('Ivan')
# p1._surname = 'Choi'
# print()
#
# class KoreanPerson2:
#     __surname = 'Kim'
#     def __init__(self, name):
#         self.name = name
#         self.fullname = f"{name} {self.__surname}"
#
# p2 = KoreanPerson2('Ivan')
#
# print(dir(p1))
# print(dir(p2))

# ==================
from random import random


# name = 'ivan'
# age = 13
# print(f"locals global {locals()}")
# l = locals()
# print(l.get('__name__'))
#
# def some_big_function():
#     age = 12
#     print(f"locals enclose {locals()}")
#
#     def some_function():
#         name = "ivan"
#         print(f"locals local {locals()}")
#
#     some_function()
#
# some_big_function()

# ================== показываем как сделать класс бесплодным



# class Person:
#     # def __new__(cls):
#     #     return None
#     name = 'Masha'
#
#     def __init__(self):
#         self.name = 'Ivan'
# #
# #
# p = Person()
# print(type(p))

# for name in dir(p):
#     attribute = getattr(p, name)
#     if callable(attribute):
#         print(f"{name} - метод")
#     else:
#         print(f"{name} - атрибут")
#
# delattr(Person, 'name')
# delattr(Person, '__doc__')
# print(f"p = {p.__doc__}")
#
# p = Person()
# print(dir(p))
# print(type(p))



#============
# class Person:
#     name = 'Ivan'
#     def print_name(self):
#         print(name)
#
# p = Person()
# p.print_name()

#============
# import random
# class Person:
#     @staticmethod
#     def return_rand():
#         return random.choice(list(range(1, 11)))
#
# print(Person.return_rand())

# class Person():
#     def __init__(self):
#         self._name = 'Ivan'
#         self.name = f'{self._name} Smith'
#
# p = Person()
# print(p.name)
# print(p._name)

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def create_with_custom_name(cls, original_name):
#         name_mapping = {
#             "Артем": 'ЛСДУЗ',
#             "Игорь": 'ЙФЯУ9'
#         }
#         return cls(name=name_mapping.get(original_name, "DefaultName"))
#
# # Пример использования
# person = Person.create_with_custom_name("Артем")
# print(person.name)  # Выведет: ЛСДУЗ

# p1 = Person('Anna')  # Anna
# p2 = Person.chaika_son_name('Artem')  # Relax

#  name mangling error example
class Person:
    _name = "John"
    __surname = "Doe"

p = Person()
print(p.__dict__)
print(dir(p))

print(p._name) # John
print(p.__surname) # AttributeError




class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self.name = f'{self._name} {self._surname}'
        p = Person('Oleg', 'Molchanov')
        print(p.name)# Oleg Molchanov`