#!/usr/bin/env python3
# Создайте класс Автомобиль. В этом классе создайте несколько переменных, которые будут отвечать за характеристики автомобиля. Создайте метод, который будет присваивать значения всем переменным и метод, который будет выводить все переменные на экран. Создайте два объекта и используйте оба метода для объектов.

class Car:
    color = 'black'
    def __init__ (self) :
        self.max_speed = 10
        self.car_marc = 'lada'
    def set (self, speed, c_marc) :
        self.max_speed = speed
        self.car_marc = c_marc
    def get (self) :
        print ("max speed = ", self.max_speed, ", car_marc =", self.car_marc, ", color  = ", self.color, "\n")

bmv = Car()
bmv.set(200, 'semera')
bmv.get()

#Создайте пустой класс без ничего и на его основе создайте два объекта. Теперь добавьте к одному из объектов новую переменную newValue" со значением 5.

class Empty:
    pass# иначе ошибка
obj1 = Empty()

obj1.newval = 10
print ("newval = ", obj1.newval)

# Создайте класс с одной переменной и одним методом. При вызове этого метода просто выводите переменную класса, а также параметр, что будет передан в эту функцию. Обратитесь к этой функции через объект.

class Boat:
    speed = 10
    def wind_speed (self,w_speed):
        print ("init_speed = ",self.speed,"wind_speed = ",w_speed)

kanoe = Boat()
kanoe.wind_speed(3)
