#!/usr/bin/env python3
#Создайте какой-либо кортеж и попробуйте вывести его в цикле while.
tup0 = tuple('abcd')
i = 0
print ("len of tup0 = ", len(tup0))# 4
while i < len(tup0) :
    print ("element with number", i, "is equal to", tup0[i])
    i = i + 1

#Создайте кортеж при помощи слова tuple, а также без использования его.
tup1 = tuple('abcd')
tup2 = ('e','f')
print ("tup1=",tup1)
print ("tup2=",tup2)

#Создайте кортеж из слова "Привет мир!" и выведите его в цикле for.
tup_mir = tuple('Привет мир')
for letter in tup_mir:
    print (letter)

#Выведите лишь третий элемент с конца в кортеже:
tup = (3.4, 56, "Some", "Hi", 7, 3.8, 44)
print ("tup = ",tup)
print ("Вывод ", tup[-3])
print ("каждый второй начиная с 3",tup[2::2])
