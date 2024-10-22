class MetaPerson(type):
    def __new__(cls, name, bases, dct):
        dct['mamals_type'] = 'Human'
        if 'age' not in dct:
            raise AttributeError
        return super().__new__(cls, name, bases, dct)

class MStudent(metaclass=MetaPerson):
    age = 20

s2 = MStudent()
print(s2.age)
print(s2.mamals_type)
