class MyClass:
    __slots__ = ('attr1', 'attr2', 'attr3')

    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

# Пример использования
obj = MyClass(1, 2, 3)
print(obj.attr1)
print(obj.__slots__) # TypeError
print(vars(obj)) # TypeError
# obj.attr4 = 4  # AttributeError: 'MyClass' object has no attribute 'attr4'