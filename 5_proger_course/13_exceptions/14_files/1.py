#!/usr/bin/env python3
#Создайте файл hi.txt и поместите туда строку "Какая-угодно информация!" и закройте файл.
#Откройте файл только для чтения и выведите информацию на экран.
f = open('file.txt', 'w+') # если r+ то файл не создастся
f.write('Какая-угодно информация3!')
f.seek(0)
a = f.read();
print ("a=", a)

#Постарайтесь открыть файл, которой вы не создавали. Создайте исключение, которое сработает при не нахождении такого файла. Такое исключение называется FileNotFoundError.
try:
    f=open("unexist_file", 'r')
except FileNotFoundError:
    print ("second error")
except: #default exept must be last or error
    print ("error with file open")

#Создайте файл "example.txt" и впишите туда текст "Привет" после чего закройте его. Теперь постарайтесь открыть этот же файл при помощи команды "x", которая открывает файл для чтения, если такого нет. Вам будет выдана ошибка, которую вы должны обработать в исключении. Ошибка будет называться FileExistsError. В finally пропишите закрытие файла, а в except пропишите верное открытие файла при помощи 'a'
file_name = "example.txt";
f = open (file_name, 'w')
f.write('some info')

try:
    f = open (file_name, 'x')
except FileExistsError:
    print ("error was excepted")
    f = open (file_name, 'a')
finally:
   f.close ()
