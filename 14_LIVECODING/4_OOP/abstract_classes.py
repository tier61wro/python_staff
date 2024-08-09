from abc import ABC, abstractmethod

# Определяем абстрактный класс Animal, наследующий от ABC
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # Объявляем абстрактный метод make_sound, который должен быть реализован в подклассах
    @abstractmethod
    def make_sound(self):
        pass

# Создаем конкретный класс Dog, который наследуется от Animal
class Dog(Animal):
    # Реализуем абстрактный метод make_sound для класса Dog
    def make_sound(self):
        print(f"{self.name} says: Woof!")

# Создаем конкретный класс Cat, который наследуется от Animal
class Cat(Animal):
    # Реализуем абстрактный метод make_sound для класса Cat
    def make_sound(self):
        print(f"{self.name} says: Meow!")

class Cow(Animal):
    # Реализуем абстрактный метод make_sound для класса Cat
    pass

# Пример использования
def main():
    # Создаем экземпляры Dog и Cat
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    cat = Cow("Browny")

    # Сохраняем их в список animals
    animals = [dog, cat]

    # Проходим по списку и вызываем методы make_sound для каждого животного
    for animal in animals:
        animal.make_sound()

# Проверяем, если этот файл запущен как основной
if __name__ == "__main__":
    main()
