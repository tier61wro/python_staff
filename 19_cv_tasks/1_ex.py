# name = 'Ivan'
#
# class Person:
#     name = 'Dima'
#
#     def print_name(self):
#         print(name)
#
# p = Person()
# p.print_name()
#
# print(Person.name)


# a = [1, 2, 4]
# print (len(a))


def f(val, a = []):
    a.append(val)
    return a

print(f(18))
print(f(19, []))
print(f(33))