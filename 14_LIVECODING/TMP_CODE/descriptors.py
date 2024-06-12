# descriptors3.py
class OneTo():
    def __init__(self):
        self.value = {}
        print(f'init {self=}')

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value
        print(f'setting {(self.value)}')

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_foo_object2 = Foo()

my_foo_object.number = 3
print(my_foo_object.number)

my_foo_object2.number = 9
print(my_foo_object2.number)
