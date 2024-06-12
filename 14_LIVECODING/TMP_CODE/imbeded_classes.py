class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        print(f"Двигатель запущен. Мощность: {self.horsepower} л.с., Тип топлива: {self.fuel_type}.")


class Tire:
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def rotate(self):
        print(f"Шины вращаются. Размер: {self.size}, Тип: {self.type}.")


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine(150, "бензин")
        self.tires = [Tire("205/55 R16", "летние") for _ in range(4)]

    def start(self):
        print(f"Автомобиль {self.make} {self.model} готов к поездке.")
        self.engine.start()
        for tire in self.tires:
            tire.rotate()


# Создание экземпляра автомобиля
my_car = Car("Toyota", "Corolla")
my_car.start()