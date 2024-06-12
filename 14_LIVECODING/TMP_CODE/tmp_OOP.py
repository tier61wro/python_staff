class Person:
    def __init__(self):
        self.__name = "Vasja"
        self._surname = 'Ivanov'

a  = Person()
# print(a.__name)
print(a._surname)
# print(a._Person__name)
a._surname = "jopa"
a.__name = "jopa"
a._Person__name = 'Jopa'
print(a.__dict__)