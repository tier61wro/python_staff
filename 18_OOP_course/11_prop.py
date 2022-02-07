class Person:
    def __init__(self, name):
        self._name = name

    # def get_name(self):
    #     print('from get name')
    #     return self._name
    #
    # def set_name(self, value):
    #     print('from set name')
    #     self._name = value
    #
    # name = property(fget=get_name, fset=set_name)
    # # name = становится атрибутом класса

    @property
    def name(self):
        print("from decorated name")
        return self._name

     name = property(name)

    @name.setter
    def name(self, value):
        self._name = value

    # name = name.setter(set_name)

p = Person('Dima')