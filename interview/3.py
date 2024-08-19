class Parent:
    x = 2

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)

Child1.x = 5
print(Parent.x, Child1.x, Child2.x)

Parent.x = 8
print(Parent.x, Child1.x, Child2.x)

