#!/usr/bin/env python3
#example:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print ("end of work")

#Попросите пользователя ввести возраст, если он ввел не возраст, то скажите ему об этом и попросите сделать это еще раз. Сделайте это в цикле, чтобы каждый раз спрашивался возраст, пока пользователь его наконец не введет

age_int = None
while (age_int == None):
    try:
        #age = input("insert age\n")
        age = 12
        age_int = int(age)
    except:
        print ("age is not ok")
    else:
        print ("ok")

#Создайте исключение, которое сработает при использовании несуществующей переменной. К примеру, вы хотите присвоить значение несуществующей переменной к другой переменной. Такое исключение носит название NameError.

try :
    #exist = unexist + 1
    res = 3/1
except NameError:
    print ("smth bad")
except ZeroDivisionError:
    print ("zero div")
else:
    print ("ok")
try:
    bad_func(3)
except NameError:
    print ("bad f")
