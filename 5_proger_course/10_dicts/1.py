#!/usr/bin/env python3
#Создайте словарь из учеников в классе. Должны быть такие характеристики как: имя, возраст, средняя оценка. Выведите все эти данные на экран через цикл for. Выведите ключи и значения этих ключей.
dict_pupil = {'abramov':{'age':12, 'sr_ball':4}, 'petrov':{'age':13, 'sr_ball':5}}
for name in dict_pupil.keys() :
    print ("name=", name)
    print ("age =", dict_pupil[name]['age'], "ocenka=", dict_pupil[name]['sr_ball'])

# Создайте словарь, в котором вместо ключей будут кортежи. Выведите элементы такого словаря.
#Хочу также заметить, что подобное нельзя сделать со списками. Только кортежи могут выступать в качестве ключей для словаря.
tup1 = tuple('hello')
tup2 = tuple('hell')
dict_tuple = {tup1:5,tup2:4}
for key , value in dict_tuple.items():
    print ("key = ", key, "value =", value)

#При помощи цикла for сгенерируйте словарь из простых чисел от 1 до 7.
d = {a: a*a for a in range(7)}
print (d)

#Cоздайте словарь при помощи нескольких способов: фигурные скобки, при помощи функции dict и метода fromkeys.
dict_1 = {'a': 1, 'b': 2}
dict_2 = dict(c = 3, d = 4)
arr = ['e','f']
dict_3 = dict.fromkeys(arr, 1)
print ("dict_1 =", dict_1)
print ("dict_2 =", dict_2)
print ("dict_3 =", dict_3)

d_src = {"Один" : "Питон", "Два" : "C++", "Три" : "Java", "Четыре" : "C#"}
#Сделайте копию этого словаря и удалите оригинал. Из копии удалите ключ и значение "Три" : "Java". Добавьте новое значение в конец словаря: "Новое" : "Kotlin".
d_dst = d_src.copy();
#d_dst = d_src;
d_src.clear();
print ("dst = ",d_dst)
d_dst.pop('Три')
print ("dst = ",d_dst)
d_dst.update({'New':'Kotlin'})
print ("dst = ",d_dst)
