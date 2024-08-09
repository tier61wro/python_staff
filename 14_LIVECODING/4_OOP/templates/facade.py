class SubsystemA:
    def operation_a(self):
        print("SubsystemA: Operation A")

class SubsystemB:
    def operation_b(self):
        print("SubsystemB: Operation B")

class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()

# Использование фасада
facade = Facade()
facade.operation()

#  python3 facade.py
# SubsystemA: Operation A
# SubsystemB: Operation B
