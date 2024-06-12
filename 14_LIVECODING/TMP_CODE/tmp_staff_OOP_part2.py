# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     def get_name(self):
#         print('from get name')
#         return self._name
#
#     def set_name(self, value):
#         print('from set name')
#         self._name = value
#
#
#     name = property(fget=get_name, fset=set_name)
#     # name = становится атрибутом класса!!!, его не будет в пространстве имен экземпляра
#
# p = Person('Dima')
#
# print(Person.__dict__['name'])
#
# print(getattr(Person, 'name'))
#
# print(p.name)
# print(p.__dict__)
'''
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('from get name')
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, (int, float)):
            raise TypeError("Name must be a string, not a number.")
        print('from set name')
        self._name = value


p = Person('Alice')
p.name = 'Bob'  # Работает нормально
# p.name = 123    # Вызовет TypeError


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_with_custom_name(cls, original_name):
        name_mapping = {
            "Артем": 'ЛСДУЗ',
            "Игорь": 'ЙФЯУ9'
        }
        return cls(name=name_mapping.get(original_name, "DefaultName"))

a = Person.create_with_custom_name("Артем")
print(a.name)

'''

"""
class Person:
    _name = "John"
    __surname = "Doe"

p = Person()
print(p.__dict__)
print(dir(p))

print(p._name) # John
# print(p.__surname) # AttributeError
"""

"""
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('from get name')
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, (int, float)):
            raise TypeError("Name must be a string, not a number.")
        print('from set name')
        self._name = value

print(getattr(Person, 'name'))
print("=================")
# print(Person.__dict__)
p = Person('Alice')
# print(Person.__dict__)
p.name = 'Bob'  # Работает нормально
# # p.name = 123    # Вызовет TypeError
# print(p.__dict__)

# print(Person.__dict__)
print(p.name)
print(f"dir = {dir(p)}")
print(f"var = {vars(p)}")

print(hasattr(p, 'name'))
print(p._name)
print(type(p.name))
print(type(getattr(p, 'name')))

"""

# class Person:
#     pass
#
# class Student(Person):
#     pass
#
# s = Student()
# print(s.__class__.mro())  # [<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]
# print(Student.mro())  # [<class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>]

'''
class Person:
    def __init__(self, name):
        self._name = name

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return isinstance(other, Person) and self._name == other._name

p1 = Person('Ivan')
p2 = Person('Ivan')
p3 = Person('Sasha')

print(p1 == p2)  # True
print(p2 == p3)  # False


print(hash(p1))  # циферка
'''

'''
class Person:
    count = 100
    def __repr__(self):
        return str(self.count)

    def __sub__(self, other):
        self.count -= 1
        return self.count

p1 = Person()
p1 - 'jopa'
print(p1)
'''
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"{self.name=}, {self.salary=}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"{self.department=}")

p = Manager('Mike', 10000, 'HR')
print(p.department)
p.display_info()



class Person:
    @staticmethod  # если тут не будет декоратора, то на строке ниже будет ошибка, типа нет self
    def goodbye():
        print('Bye')

p1 = Person()
p2 = Person()
print(id(p1.goodbye)) #140218835469216
print(id(p2.goodbye)) #140218835469216
'''
'''
class Temperature:
    def __init__(self):
        self.values = {}

    def __get__(self, instance, owner_class):
        print("LOG: get temp was called")
        return self.values.get(instance, "Не установлено")

    def __set__(self, instance, value):
        print("LOG: set temp was called")
        if not isinstance(value, int):
            raise ValueError("Температура должна быть числом")
        self.values[instance] = value

class Dog:
    def __init__(self, temp=38, age=8):
        self.temp = temp  # Используйте дескриптор для инициализации
        self.age = age

    temp = Temperature()

Luna = Dog(40, 9)
print(Luna.temp)
'''

# descriptors.py

'''

class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print(f"{self=}")
        print(f"{obj=}")
        print(f"{type=}")
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

# тоже самое что и
class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)


my_foo_object = Foo()


x = my_foo_object.attribute1
print(x)
'''

# obj = "some object"
# obj_id = id(obj)  # 140667592506736
# address = hex(id(obj))  # 0x7f2c9406be70
#
#
# a = [1, 2, 3]
# b = [1, 2]
# b.append(3)
# print(a)
# # print(b)
#
# class Person:
#     def __init__(self):
#         self.name = 'Ivan'
#
#     def __new__(cls):
#         return None
#
# p = Person()
# print(type(p)) # NONE
# print(p.name)


# class BankAccount:
#     def __init__(self, account):
#         self._account = account
#
#     @property
#     def account(self):
#         return self._account
#
#
# b = BankAccount('100')
#
# print(b.account)
# b.account = 200  # AttributeError: can't set attribute

# class Less200Number:
#     def __init__(self, value):
#         self._value = value
#
#     def __set__(self, obj, value):
#         if not isinstance(value, int):
#             raise ValueError(f"{type(value)} Not a number we need")
#         self._value = value
#
#     def __get__(self, obj, type = None):
#         return self._value
#
#
# class Human:
#     age = Less200Number(0)
#     weight = Less200Number(0)
#
# p = Human()
# print(p.age)
# p.age = 50
# print(p.weight)
# p.weight = 140
#
#
# print(f"P{p.age} --- {p.weight}")
#
# p1 = Human()
# print(p1.age)
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# p = Person('Ivan')
# p.age = 18
# print(p.__dict__)
#
# print(dir())

# class Person:
#     name = 'Ivan'
#
# # a = Person()
# # setattr(Person, 'name', 'Sasha')
# # print(a.name)
# attr_name = 'name'
# Person.attr_name = 'Igor'
# print(Person.name)

class Monkey():
    def __init__(self, name):
        print("monkey init was called")
        self.name = name

    def hello(self):
        print("hello monkey")


class Human(Monkey):
    def __init__(self, name, age):
        print("human init was called")
        super().__init__(name)
        self.age = age
    # def hello(self):
    #     print("hello human")

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def hello(self):
        super().hello()

s1 = Student(2,3,4)
s1.hello()

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)
l = [None] * 10
print(len(l))

list1 = ['a', 'A', 'B']
print(max(list1))