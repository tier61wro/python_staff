#!/usr/bin/python

#В Python нет цикла do..while, тем не менее его можно с легкостью создать собственноручно. Создайте такой цикл.
#Для тех кто не знает, цикл do..while это цикл который выполняется хотя бы один раз сто процентов, после чего проверяет условие и если оно не верно, то выходит из цикла, иначе продолжает следующую итерацию.
#do smth while i = 1
i = 0 
while 1 :
    print (i)
    i += 1
    if i > 0:
        break
