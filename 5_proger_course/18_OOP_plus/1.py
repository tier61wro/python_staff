#!/usr/bin/env python3
#Создайте класс Автомобиль. В этом классе создайте несколько переменных, которые будут отвечать за характеристики автомобиля. Создайте конструктор,  метод, который будет присваивать значения всем переменным и метод, который будет выводить все переменные на экран. Создайте два объекта и используйте оба метода для объектов.
#Создайте теперь класс Мотоцикл и сделайте его наследником класса Автомобиль. Добавьте в него методы, а также свои собственные переменные. Создайте объект на основе нового класса и через этот объект обратитесь к методам главного класса Автомобиль.
#В классе Car есть метод get. Используйте полиморфизм чтобы переделать этот метод в классе наследнике. При вызове harley.get () должен выдаваться следующий текст: Транспорт  Harley Davidson  может ехать со скоростью  200  на всех  2  колесах!, moto engine is: Powerfull

class Car:
    color = 'black'
    def __init__(self, speed, mark):
        speed = 0
        mark = 'unknown'
    def set (self, speed, mark):
        self.speed = speed
        self.mark = mark
    def get (self):
        self.__protectedf()
        print ("speed = ", self.speed, ", mark =", self.mark, ", color = ", self.color)
    # пример инкапсуляции:
    def __protectedf(self):#в классе __ ок, вне класса _protecdedf - еще вызовется, __protectedf - выдает ошибку
        print ("protected finction was called")

lada = Car(9,'granta')
lada.set(10,'priora')
lada.get()
#lada.__protectedf()# AttributeError: 'Car' object has no attribute '__protectedf'

#пример наследования:
class Moto(Car):
    wheels = 3 # переменная уникальная для класса Moto
    engine = 'default'
    def have_stroler(self):
        if self.wheels == 3:
            return True
        else:
            return False
    def __init__(self, speed, mark, engine):
        self.engine = engine
        super().__init__(speed, mark) # без self!

    def get (self): #переопределяем метод, пример полиморфизма
        super().get()# super () - это обращение к главному классу
        print ("moto engine is:",self.engine)

yamaha = Moto(20,'vm', 'middle engine')
yamaha.set(250, 'vmmax')
yamaha.get()
yamaha.wheels = 4
print ("have stroler = ",yamaha.have_stroler())

