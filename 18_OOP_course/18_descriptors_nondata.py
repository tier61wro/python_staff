class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        print('name getter called')
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None
        return self._name

    @property
    def surname(self):
        print('surname getter called')
        return self._name

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None
        return self._surname

p = Person('sasha', 'smirnov');