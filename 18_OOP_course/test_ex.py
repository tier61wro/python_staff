# name = 'Ivan'
#
# class Person:
#     name = 'Alex'
#
#     def print_name(self):
#         print(self.name)
#
#     @classmethod
#     def change_class_name(cls, name):
#         cls.name = name
#
# p = Person()
# print(Person.name)
# p.change_class_name('Igor')
# print(Person.name)
# # p.print_name()

# class Person():
#     default_name = 'Petya'
#     def __init__(self, name = default_name):
#         self.name = name
#
# p = Person('Sasha')
# # Sasha
# p = Person()
# # Petya

# class Person:
#     @staticmethod  # если тут не будет декоратора, то на строке ниже будет ошибка, типа нет self
#     def goodbye():
#         print('Bye')
#
# p1 = Person()
# p2 = Person()
# print(id(p1.goodbye)) #140218835469216
# print(id(p2.goodbye)) #140218835469216


# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#         self.name = f'{self._name} {self._surname}'
#
# p = Person('Oleg', 'Molchanov')
# print(p.name)
# # Oleg Molchanov
# from random import choice
#
# class NumbersGen():
#     @staticmethod
#     def num_gen():
#         return choice(range(1, 5))

#
# n = NumbersGen()
# print(n.num_gen())

# class Account:
#     def __init__(self, balance=0):
#         self.__balance = balance
#
#     def show_balance(self):
#         print(f"Balance: {self.__balance}")
#
# a = Account(100)
#
# print(a.__dict__)  # {'_Account__balance': 100}
# a.show_balance()  # Balance: 100
# a.__balance = 100000
# print(a.__dict__)  # {'_Account__balance': 100, '__balance': 100000}
# a.show_balance()  # Balance: 100

# ===============================
class Person:
    name = 'Dima'  # мы хотим сделать тут DIMA, так чтобы класс и все его экземпляры изменились

    @classmethod
    def name_upper(cls):
        cls.name = cls.name.upper()


print(Person.name)  # Dima
Person.name_upper()
print(Person.name)  # DIMA
p = Person()
print(p.name)  # DIMA

# class Pizza:
#     def __init__(self, ingredients = ['palki', 'govno']):
#         self.ingredients = ingredients
#     def __repr__(self):
#         return f'Pizza is made from ingredients: {self.ingredients}'
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])