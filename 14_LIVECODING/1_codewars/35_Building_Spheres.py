
'''
train_date: 20.04.2022
kata link: https://www.codewars.com/kata/55c1d030da313ed05100005d
points: 7 kyu
type: OOP
-------------
DESCRIPTION:

Now that we have a Block let's move on to something slightly more complex a Sphere.

#Arguments for the constructor

radius -> integer or float (do not round it)
mass -> integer or float (do not round it)

#Methods to be defined

get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

##Example

ball = Sphere(2,50)
ball.get_radius() ->       2
ball.get_mass() ->         50
ball.get_volume() ->       33.51032
ball.get_surface_area() -> 50.26548
ball.get_density() ->      1.49208

Any feedback would be much appreciated
-------------
TRANSLATION:
нужно написать класс который будет создавать объект сферы Sphere
конструктор должен принимать на вход массу и радиус
так же надо определить три метода которые будут возвращать определенные параметры:

радиус
ball.get_radius() ->       2
массу
ball.get_mass() ->         50
объем
ball.get_volume() ->       33.51032
площадь поверхности
ball.get_surface_area() -> 50.26548
плотность
ball.get_density() ->      1.49208

-------------
===TRAINED====
использование pi в питоне
from math import pi
возведение в степень
round(4 * pi * radius**3 / 3, 5)
-------------
==== КРАСОТА ====
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = round(4 * pi * radius**3 / 3, 5)
        self.surface_area = round(4 * pi * radius**2, 5)
        self.density = round(self.mass / self.volume, 5)

    def __getattr__(self, name):
        return lambda: getattr(self, name[4:])
'''
import codewars_test as test


from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4/3 * pi * (self.radius ** 3)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(self.volume, 5)

    def get_surface_area(self):
        return round(4 * pi * (self.radius ** 2), 5)

    def get_density(self):
        return round(self.get_mass()/self.volume, 5)


ball = Sphere(2,50)

test.assert_equals(ball.get_radius(),2, "Check radius")
test.assert_equals(ball.get_mass(),50, "Check mass")
test.assert_equals(ball.get_volume(), 33.51032, "Check volume")
test.assert_equals(ball.get_surface_area(),50.26548, "Check area")
test.assert_equals(ball.get_density(),1.49208, "Check density")
