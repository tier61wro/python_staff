# makes numer beetween 0 and 1000
class OneTwousandNumber:
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type):
        return self.value.get(obj)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Input value must be an integer")
        if value < 0 or value > 1000:
            raise ValueError("Number must be between 0 and 1000")
        self.value[obj] = value

class Car:
    @property
    def width(self):
        print("width was requested")
        return self._width

    @width.setter
    def width(self, value):
        print("width was set")
        self._width = value


class Pupil:
    height = OneTwousandNumber()


class Monitor:
    width = OneTwousandNumber()

p1 = Pupil()
p1.height = 185
print(p1.height)

m1 = Monitor()
m1.width = 600
print(m1.width)

Ford = Car()
Ford.width = 900
print(Ford.width)