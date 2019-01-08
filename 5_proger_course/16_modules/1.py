#!/usr/bin/env python3
#Импортируйте в ваш проект из модуля math только значение pi и функцию ceil. Для функции ceil сделайте псевдоним "c"
from math import pi
from math import ceil as c

print ("pi=", pi)
print ("b=", c(12.3))#13

#Создайте свой модуль и добавьте в него одну функцию и две переменных. Импортируйте функцию, а также только одну переменную.
from Mymod import pi_short
from Mymod import add
print ("pi_incremented = ",add(pi_short,1))

#При помощи модуля random создайте случайное число. За это отвечает метод randint, который принимает два параметра в качестве промежутка чисел.В цикле просите пользователя ввести число, если оно не совпадает со случайным числом, то вы должны давать пользователю подсказки. Если число является большим, то вы должны написать что "Число что вы пытаетесь угадать больше" или же наоборот.

from random import randint
rand_number = randint(1,5) #первое и последнее число включительно
print ("rand_number=",rand_number)
a = 0
while 1:
    a = int(input("try to insert some number "))
    if a > rand_number :
        print ("your number is bigger")
    elif a < rand_number :
        print ("your number is smaller")
    else :
        print ("you win")
        break

#Импортируйте модуль datetime. Он отвечает за работу с датой и временем. Выведите на экран полную дату. За это отвечает datetime и его метод now.Из модуля импортируйте только саму функцию datetime при этом добавьте к ней псевдоним, чтобы было проще с ней работать.

from datetime import datetime as dt
#datetime.datetime.strptime
print ("now is ", dt.now())
