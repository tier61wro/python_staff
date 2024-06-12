class OneThousandNumericValue():
    def __set_name__(self, owner, name):
        # owner: класс Car
        print(f"we setted: {name}")
        self.name = name

    def __get__(self, obj, type=None) -> object:
        # obj - Ford
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value) -> None:
        if not (0 <= value <= 1000) or not isinstance(value, int):
            raise ValueError("Number must be an integer between 0 and 1000")
        obj.__dict__[self.name] = value

class Car():
    weight = OneThousandNumericValue() # через name
    max_speed = OneThousandNumericValue()


# Пример использования
Ford = Car()
print(dir(Ford))
Ford.weight = 500
Ford.max_speed = 300
print(dir(Car.weight))

