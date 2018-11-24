#!/usr/bin/python

# Попросите пользователя чтобы он ввел какое-либо слово с клавиатуры. Теперь каждый символ этого слова запишите как отдельный элемент в список.

word = input ("input word: ")
list = []
for i in word :
    list.append(i)

print ("fin list= ",list)
