class MyClass:
    greet = 1  # Атрибут класса

    def greet(self):  # Метод класса
        print("Hello!")

# Попытка создать экземпляр класса
obj = MyClass()

# Попытка доступа к greet
print(obj.greet) # <bound method MyClass.greet of <__main__.MyClass object at 0x7f2ca2c57680>>


class MetaPerson(type):
    def __new__(cls, name, bases, dct):
        # Определяем метод greet в метаклассе
        def greet(self):
            print("Hello from method!")

        # Добавляем метод greet в класс
        dct['greet'] = greet

        # Создаем новый класс
        return super().__new__(cls, name, bases, dct)
