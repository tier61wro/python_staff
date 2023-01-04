name = 'Ivan'

class Person:
    name = 'Dima'

    def print_name(self):
        print(self.name)

    @classmethod
    def change_class_name(cls, name):
        cls.name = name

p = Person()
print(Person.name)
p.change_class_name('Igor')
print(Person.name)
# p.print_name()