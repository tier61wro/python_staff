#!/usr/bin/env python
#-*- coding: utf-8 -*-
######Чтобы вычислить его, возьмите свой вес в килограммах и разделите его на квадрат роста в метрах. Например, ИМТ для девушки ростом 170 см (1,7 м) и весом 54 кг, составит 18,69.
from sys import argv

script_name, weight, height = argv
height = float(height)
weight = float(weight)
name = raw_input('enter your name\n')
imt = weight/(height**2)

print "height = ", height

print "Hi %s your weight = %s, your height = %s" % (name, weight, height)

print "IMT is equal =%s"  % imt

if (imt > 25):
    print '''you are fat %s
you must start to use
sport and diet''' % name
elif (imt < 18):
    print "you are thin"
else:
    print "you are normal"
