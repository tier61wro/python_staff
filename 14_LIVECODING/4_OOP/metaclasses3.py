class Parent:
    def greet(self):
        print("Hello from Parent!")

class MetaPerson(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        print(f"Bases: {bases}")
        return super().__new__(cls, name, bases, dct)

# Класс Student наследует от Parent, поэтому bases будет непустым
class Student(Parent, metaclass=MetaPerson):
    age = 20

# Создаем экземпляр класса Student
s = Student()
s.greet()  # Вызов метода, унаследованного от Parent


t = (1, 2, 4)

# Попытка вычислить хэш
try:
    print(hash(t))
    print("The tuple is hashable.")
except TypeError:
    print("The tuple is not hashable.")
