# class Person:
#     def __init__(self, name):
#         self._name = name

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

    # @property
    # def name(self):
    #     print("from decorated name")
    #     return self._name
    #
    #  name = property(name)
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value

    # name = name.setter(set_name)


class Person:
    def __init__(self, name="Dima"):
        self._name = name # нижнее подчеркивание тут не зря, без него ошибка рекурсси

    def get_jopa(self):
        print("from getter")
        return self._name

    def set_jopa(self, value):
        print("from setter")
        self._name = value

    name = property(fget=get_jopa, fset=set_jopa)


p = Person()

p.name = 'Ivan'  # from setter
print(p.name)  # from getter; Ivan