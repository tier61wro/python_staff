#!/usr/bin/env python3


#Попросите пользователя ввести n-раз какие-либо данные (числа или же строки). Число n также должен ввести пользователь. После этого, добавьте полученные данные к этому списку:
some = [9, "Hi", 23.5, "A"]

strings_num = int(input ("vvedite chislo strok "))

addition_list = []
for i in range (1, strings_num):
    print ("i = ", i)
    el = input ("введите пожалуйста строку ")
    addition_list.append(el)

some.extend(addition_list)

print ("final list", some )
