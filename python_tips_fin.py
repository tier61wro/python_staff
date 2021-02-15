#========================================================

#!/usr/bin/env python
Строка shebang обычно записывается в одной из двух форм:
#!/usr/bin/python3
или:
#!/usr/bin/env python3
В первом случае она определяет используемый интерпретатор.
Вторая форма может потребоваться для программ на языке Python, запускаемых вебсервером, хотя абсолютный путь в каждом конкретном случае может отличаться от того, что показан здесь. Во втором случае будет использован первый интерпретатор python3, найденный в текущем окружении.

# утф печать
# -*- coding: utf-8 -*-
....

# разделитель
print "." * 10

#импорт модуля
from sys import argv

# аргументы на вход
script_name, weight, height = argv

# обработка исключений
try:
    i = int(s)
    print ("Valid!")
except ValueError as er:
    print ("Oshibka:",er)
    
try:
    y = square(input('Please enter a number\n'))
    print(y)
except ValueError as ve:
    print(type(ve), '::', ve)
except TypeError as te:
    print(type(te), '::', te)
except Exception as e:
    print (f"Exception got:{e}")
    
len(9) 			-> TypeError: object of type 'int' has no len() - у этого типа нет такого метода - поэтому type error
int('mama')		-> ValueError: invalid literal for int() with base 10: 'mama'
    
#=======================
track = traceback.format_exc()
print(track)
#======================
# блок if
if expr:
    suite1
elif expres2:
    suite2
else:
    suite3
#======================
# приглашение к вводу с консоли
line = input("integer: ")

#============== кортеж
Кортеж - это неизменяемый и более быстрый аналог списка
>>> my_tuple = () # Создание кортежа с помощью литерала
>>> my_tuple = tuple() # Создание кортежа с помощью встроенной функции
my_tuple = (1,2,['a','b'],4,5) # Инициализация кортежа
my_tuple = tuple('hello world') # Создание кортежа из итерируемого объекта
my_tuple = tuple(2**x for x in [0, 1, 2, 3]) # Генератор кортежей

#============== множества
массивы без повторений
>>> my_something = {} # !!! Попытка создать множество при помощи литерала даст нам словарь
#так как литерал совпадает с литералом для дикта
>>> my_set = set() # Создание при помощи встроенной функции
>>>
>>> my_set = {1,2,3,4,5} # Инициализация множества
my_set = {x for x in range(10)} # Генератор множеств

#kata
как при помощи множества оставить только уникальные элементы в массиве
l = set(l)

#==== Cписки - аналог массивов
>>> my_list = [] # Создание пустого списка с помощью литерала списка
>>> my_list = list() # Создание пустого списка с помощью встроенной функции

mylist =  [6, 5, 4, 3, 2, 1]
mylist.append (23) - вставка элемента
mylist.append (b) - расширение списка l списком b
mylist.insert (1,23) - меняет первое значение на 23
mylist.remove (34) - удалит первое вхождение 34 в списке ничего не возвратит, просто модифицирует список
mylist.pop () - удаляет последний элемент
mylist.pop (5) - удаляет пятый элемент
pop не просто выталкивает последний элемент из массива, но и возвращает его в переменную
mylist.count (34) - считает количество элементов
l = [3,4,4]
l.count(4)
2
sort -сортировка
reverse - переворачивание
clear  - очистка
len (mylist) = 6

#kataadd
удали в массиве произвольных чисел элемент равный 4
ответ mylist.remove(4)

#kataadd
скопируй все элементы массива a в новый массив b, чтобы потом удалить минимальный элемент в b
ответ:
b = a[:]
b.remove(min(b))

#kataadd
скопируй 10 первых символов строки в новую переменную
tail = bad_url[0:10]

#kataadd: 
написать проверку того, что число является квадратом другого целого
if math.sqrt(sq) % 1:

#kataadd
возведи число 5 в степень 3
ответ
5**3

#kataadd
замерить временной интервал команды
import time
start = time.time()
#блок кода
end = time.time()
print(end - start)

#===========
сортировки массивов
The difference between sort and sorted is that sort is a list method that modifies the list



﻿h = {}
        if r.operator not in h:
            h[r.operator] = {}

        if r.action in h[r.operator]:
            h[r.operator][r.action] += 1
            
in place whereas sorted is a built-in function that creates a new list without touching
the original one.
#kataadd - примеры на разницу между sort и sorted
#sort не возвращает нового словаря поэтому вернет None тут
l = [1,2,3]
print (l.sort(reverse=True))
None
в то время как sorted вернет:
print (sorted(l, reverse = True))
[4, 3, 2]

#kata - напиши функцию которая вернет сумму двух минимальных эелементов массива

#kataadd - отсортируй массив по убыванию
l.sort(reverse=True)

#===============
#kata объединение двух массивов через распаковку
In [1]: l2 = ['corp.my.com','biz.mail.ru']
In [2]: l3 = ['corp.mail.ru', *l2]
In [3]: print(l3)
['corp.mail.ru', 'corp.my.com', 'biz.mail.ru']

#=====================
# объявление функции

def count_middle(a,b):
    c = (a+b)/2;
    return c;


# ЦИКЛЫ
#======================
# цикл от 1 до 2 !!! строго до последнего элемента! не как в перле
#kataadd - сделать цикл от 1 до 3 включительно
for _ in range (1, 4): 
    print (_)
#вариант break + else ???
for j in 'hello world':
	if j == 'w':
		break
else:
	print ("Буквы а нету в слове")
	

kata что вернет выражение
print (len([1,2]))
ответ 2
#======================
# цикл while
while 1:
    line = input("please enter number ")
    
Или так
while True:
    line = input("enter a number or Enter to finish: ")

# условие if or
if lowest is None or lowest > number:
#=========================
#kataadd
тернарный оператор
k = 1 if a > 8 else 0
#=========================
#kataadd - посмотреть документацию по модулю
#стандартная документация
python -m pydoc <module_name>

#==============================
#kata
# конкатенации строк, способ "%" 
"your %s is in the %s" % (object, location)
# конкатенации строк, способ "+"
"your " + object + " is in the " + location 

#================================
#агалог perl -c???
python -m py_compile  3_vogon_poetry.py

#================================
#инкремент ++ - не поддерживается
lines += 1
#декремент
lines -= 1

#=====================
 аналог перлового exit
#sys.exit()

 perem = """her"s mother"""
#======================
определение кода символа в юникоде
print (hex(ord (evr)))
0x20ac
#========================
>>> ent_three = s[-3:]
>>> print (ent_three)
#========================
name = "Дмитрий"
age = 25
print("Меня зовут {}. Мне {} лет.".format(name, age)# кортеж
Меня зовут Дмитрий. Мне 25 лет.
print("Меня зовут {name} Мне {age} лет.".format(age=age, name=name) #словарь
Меня зовут Дмитрий. Мне 25 лет.

###### 2 CHAPTER
Список ключевых слов:
Ключевые слова

False - ложь.
True - правда.
None - "пустой" объект.
and - логическое И.
with / as - менеджер контекста.
assert условие - возбуждает исключение, если условие ложно.
break - выход из цикла.
class - пользовательский тип, состоящий из методов и атрибутов.
continue - переход на следующую итерацию цикла.
def - определение функции.
del - удаление объекта.
elif - в противном случае, если.
else - см. for/else или if/else.
except - перехватить исключение.
finally - вкупе с инструкцией try, выполняет инструкции независимо от того, было ли исключение или нет.
for - цикл for.
from - импорт нескольких функций из модуля.
global - позволяет сделать значение переменной, присвоенное ей внутри функции, доступным и за пределами этой функции.
if - если.
import - импорт модуля.
in - проверка на вхождение.
is - ссылаются ли 2 объекта на одно и то же место в памяти.
lambda - определение анонимной функции.
nonlocal - позволяет сделать значение переменной, присвоенное ей внутри функции, доступным в объемлющей инструкции.
not - логическое НЕ.
or - логическое ИЛИ.
pass - ничего не делающая конструкция.
raise - возбудить исключение.
return - вернуть результат.
try - выполнить инструкции, перехватывая исключения.
while - цикл while.
yield - определение функции-генератора.

#-----------------------------------
#kata 
lambda для сортировки
l = [['karo',36],['sasha',35]]
print(sorted(l, key= lambda x: x[1]))
[['sasha', 35], ['karo', 36]]
#----------------------------------- 
dir() - возвращает список атрибутов объекта

начальный символ - любой из A-Z + набор нац симфолов, символ продолжения + цифры
_ - результат последнего вычисленного выражения

В логических выражениях число 0 и значение False представляют False,
а любое другое целое число и значение True представляют True.
В числовых выражениях значение True представляет 1, а False – 0.


0b - двоичное число (первое 0)
0o - восьмеричное
0x - шестнадцатиричное
int(s, base) - преобразование числа в целое, иначе ValueError

>>> dv = "0b101"
>>> decim = int (dv, 2)
>>> print ("decim=",decim)
decim= 5


x // Y - деление с усечением дробной части
x ** y - возведение в степень  = pow(x,y) (Return x raised to the power y)

#==============
# принт без пробелов
print ("decim=",decim, sep='')
# принт без \n
print ("decim=",decim, end='')
#можно оба сразу:
print (i,",", sep = '', end = '')

Преобразование целых
чисел в тип float можно выполнить с помощью функции float()


===========================
>>> n = int(1.9)
>>> print (n)
1
#---------------------------
>>> n = math.floor(1.6)
>>> print (n)
1
#---------------------------
>>> n = math.ceil(1.6)
>>> print (n)

#-----------------------
>>> m = decimal.Decimal(2/3);
>>> print (m)
0.66666666666666662965923251249478198587894439697265625
===========================
задампить как строку???
print(f"=============== {url_params['date']!r} ================")

#--------------------------------
#Строки в языке Python представлены неизменяемым типом данных str, который хранит последовательность символов Юникода.

#Решить эту проблему можно, используя «сырые» (raw) строки. Это обычные строки в кавычках или в тройных кавычках, в которые перед
#первой кавычкой добавлен символ r. Внутри таких строк все символы интерпретируются как обычные символы, поэтому отпадает необходимость
#экранировать символы, которые в других типах строк имеют специальное значение.

#==================
#>>> text = r"тут можно писать что хочешь ';\[]{}"
#>>> print (text)
#тут можно писать что хочешь ';\[]{}

#==========
s = ("Это отличный способ объединить две длинные строки, "
" потому что он основан на конкатенации строковых литералов.")

#=================
>>> euros = "\u20AC"
>>> print (euros)
€
>>> print (ord(euros))
8364
#=== argv ===================
kataadd
как считать первый аргумент командной строки
ответ
import sys
size = int(sys.argv[1])

#===================
#Работа с файлами
f = open("myfile.txt", "x")
f.write("Woops! I have deleted the content!")
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist

# поиск всех файлов в папке по маске:
onlyfiles = glob.glob(folder_name + "/*.png")

#====================================
#принтования
print ("num = ",num," rub")
#-------------------

#GENERATORS
shortest = min((word for word in good_avas_list if word), key=len) # поиск самого короткого слова в словаре

#DICTS
#katano
способы объявления словарей:
# нормальные
d0= {'test' : 1, 'prod': 2}
d1= dict (short = 'dict', longer = 'dictionary')
#извращенные
d2= dict ([(23,34),(56,87)])
d3= dict.fromkeys(['a','b'], 3)

for ava_src in avatars_src_dict.keys():

kata: как сделать reverse hash 
num_letter_dict = {v: k for k, v in letters_num_dict.items()}

kata -лучший способ увеличить индекс словаря это через проверку get
freq_dict[el] = freq_dict.get(el, 0) + 1

kata маркировка букв  слова в хэш
letters = { x : i.count(x) for x in i }

kata сравнить 2 дикта
d1 == d2

#===========================
# про main
if __name__ == "__main__":

Когда интерпретатор Python читает исходный файл, он исполняет весь найденный в нем код. Перед тем, как начать выполнять команды, он определяет несколько специальных переменных. Например, если интерпретатор запускает некоторый модуль (исходный файл) как основную программу, он присваивает специальной переменной __name__ значение "__main__". Если этот файл импортируется из другого модуля, переменной __name__ будет присвоено имя этого модуля.

В случае с вашим сценарием, предположим, что код исполняется как основная функция, например:

python threading_example.py
После задания специальный переменных интерпретатор выполнит инструкцию import и загрузит указанные модули. Затем он проанализирует блок def, создаст объект-функцию и переменную под названием myfunction, которая будет указывать на этот объект.

Затем он прочтет инструкцию if, «поймёт», что __name__ эквивалентен "__main__", и выполнит указанный блок.

Одна из причин делать именно так – тот факт, что иногда вы пишете модуль (файл с расширением .py), предназначенный для непосредственного исполнения. Кроме того, он также может быть импортирован и использован из другого модуля. Производя подобную проверку, вы можете сделать так, что код будет исполняться только при условии, что данный модуль запущен как программа, и запретить исполнять его, если его хотят импортировать и использовать функции модуля отдельно.

#=================
#работа с путями
import os
big_image_path = os.path.join(base_folder_path, "180x180", domain_name)

#========================

#kataadd sleep 
import time
time.sleep(5)

#=======================
#запуск внешнего скрипта
import subprocess
        args = [ 
            '/usr/local/bin/emlrecover',
            '-h', ip, 
            '-s', path,
            '-u', uidl,
            '-o', '/dev/stdout',
        ]
r = subprocess.run(args, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#=======================
#получили ответ от сервера в виде хэша

    resp = mailapi.user_profile(email)
    r = json.dumps(resp)
    parsed = json.loads(r)
    #print(json.dumps(parsed, indent=4, sort_keys=True))

#========================== сломал плечо - начинаю марафон
#Уроки Python casts
#1 pip

установка модулей через pip
yum install python3-pip
python3.5 -m pip install validate_email
#-------------------
pip3 help list -   посмотреть справку по конкретной команде

#kata
pip3 install -r requirements.txt 
pip3 freeze - получить список зависимостей
pip3 list
pip3 list -o - список outdated пакетов 
pip3 show - информация о пакете
pip3 check  - Verify installed packages have compatible dependencies

Существует так называемый Python Package Index (PyPI) – это репозиторий, открытый для всех Python разработчиков, в нем вы можете найти пакеты для решения практически любых задач. 

pip freeze > requirements.txt — команда, которая позволяет создать текстовый документ в котором перечислены все установленные и необходимые для работы Python приложения программные пакеты (чаще всего Django).

#=======================

#2 переменные окружения
virtualenv venv
source venv/bin/activate
если надо выйти 
deactivate

#обращение к переменным окружения
a = os.environ['testvar']

#katadd
выведи на печать значение переменной окружения USER в питоне
print (os.environ['USER'])

#=======================
3 args-kwargs

проблема - обработка функцией переменнного количества аргументов

*args - упаковка всех переменных в кортеж
https://tproger.ru/translations/python-args-and-kwargs/

*args и **kwargs — специальный синтаксис, позволяющий передавать в функцию переменное количество аргументов. При этом, совсем не обязательно использовать имена аргументов args и kwargs;
*args используется для неименованных аргументов, с которыми можно работать как со списком;
пример
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result
    
**kwargs используется для именованных аргументов, с которыми можно работать как со словарём;
если вы хотите использовать и *args, и **kwargs, то это делается так: func(fargs, *args, **kwargs), порядок следования аргументов важен;



#питоняшка
# написать функцию которая  выведет все аргументы поданные на вход в таком виде 
arg_printer(1, *[2, 3 ... n], **{'a' : 1 ... 'z' : 26})
например:
arg_printer(1, *[2, 3], **{'c' : 9})
даст: 
arg=1, sum = (2, 3), kwargs={'c': 9}

#=======================
#kataadd
4 main
if __name__ == "__main__":
в питоне есть функция 
globals()
{'__name__': 'cut_ts', 
- если запускать напрямую скрипт,
тогда выполнится main

def main():
	pass

if __name__ == "__main__":
#=======================
5 генераторы
list comprehension
#kataadd
напиши генератор который сделает массив из квадратов чисел от 1 до 5
squares = [x*x for x in [1,2,3,4,5]]

напиши генератор который добавляет только слова из 4-х  слов
return [f for f in x if len(f) == 4]

пробежаться по массиву регуляркой (выдрать юзеров из строк вида a.ilyinsky:::rinfo.sms)
new_list = [re.search(r"([^\:]+)", str).group(1) for str in new_list]

# создаем словарь через генератор
sum_dict = {st.name: st.fives * 5 + st.tens * 10  for st in students}

#=======================
6 декораторы

#=======================
регулярки
regexp
## RE
# заменить и сохранить измененное в новую переменную:
weblink_short = re.sub(r'^.*public\/', '', weblink)

re.match()#Этот метод ищет по заданному шаблону в начале строки. 
re.search()#Как match() но ищет не только в начале строки = m// в перле
re.findall()#Этот метод возвращает *список* всех найденных совпадений.
#result = re.findall(r'AV', 'AV Analytics Vidhya AV')
re.split() #result = re.split(r'y', 'Analytics') результат:['Anal', 'tics']
re.sub()#аналог s//#result = re.sub(r'm', 'p', 'mama')
re.compile()#собрaет регулярное выражение в отдельный объект, который может быть использован для поиска.
#pattern = re.compile('AV')
#result = pattern.findall('AV Analytics Vidhya AV')
# сохранить заматченные части в переменные
reg = re.compile("\d{3}\d{3}\d{4}")
m = re.match(r"([DW]) (\d+)", str_in)
if m :
    tr_type = m.group(1)
    summ = m.group(2)


success = re.compile(r'Successfully\s+subscribed')
if success.search(r.text):
        logger.info(f'subscription to {sub} (email: {email}) success')


захват регулярками
аналог перлового m = $1 if (string_one =~ /^file/)
m  = re.search(r'^file', string_one).group(1)       
        
#============= with as
http://python-3.ru/page/instrukcija-with-as-v-python

Для работы с протоколом менеджеров контекста предназначена инструкции with ... as. Инструкция имеет следующий формат:

with <Выражение>[ as <Переменная>]:
    <Блок, в котором перехватываем исключения>
    
Вначале вычисляется <Выражение>, которое должно возвращать объект, поддерживающий протокол. 
Этот объект должен иметь два метода: __enter__() и __exit__(). Метод __enter__() вызывается после создания объекта. 
Значение, возвращаемое этим методом, присваивается переменной, указанной после ключевого слова as. 
Далее выполняется выражения внутри тела инструкции with. Если при выполнении возникло исключение, то управление передается методу __exit__().
#kataadd:
#каноническое открытие файла
#запись
with open("test.txt", "a") as f:
    f.write("Строка\n") # Записываем строку в конец файла

#чтение    
with open('new_rinfo_auth') as f_old:
    old_list = f_old.readlines()

#===================
#kataadd:
бросить эксепшен из функции
raise IOError("текст исключения")

#написать свой
class MyException(Exception):
    pass
    
#=====================
#kataadd:

Жестко указать принимаемые и возврвщаемые значения как Олег, (типизиварование)
from typing import List
def remove_smallest(numbers: List[int]) -> List[int]:
    if numbers:

#=======================
Как прикрутить юниттесты
import unittest

class TestStringMethods(unittest.TestCase):

  def test_ok(self):
      pangram = "The quick, brown fox jumps over the lazy dog!"
      self.assertEqual(is_pangram(pangram), True)

def is_pangram(s):
...

if __name__ == '__main__':
    unittest.main()

#===========================
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

==========
#kataadd
создать папку если ее не существует
import os
if not os.path.exists(directory):
    os.makedirs(directory)
    
    
=================
#kataadd
простой http запрос по урлу через urllib
import urllib.request
page = urllib.request.urlopen(filin_url)
content = page.read()


from urllib import request, parse
data_dict = {'weblink':'3Ea1/5D9J7GWAj'}
data = parse.urlencode(data_dict).encode()
req =  request.Request('http://intapi.win87.dev.mail.ru/api/v2/', data=data) # this will make the method "POST"
resp = request.urlopen(req)
print (f'resp = {resp}')
----
import requests
import traceback
from requests.exceptions import ConnectTimeout

url = 'http://intapi.win87.dev.mail.ru/api/v2/'
data = ({'weblink':'3Ea1/5D9J7GWAj'})

try :
    res = requests.post(url, json=data, timeout = 5)
    print (res)
except ConnectTimeout as ce:
    print ("timeout")
except Exception as e:
    print (f"Exception got:{e}")
    print("\n")
    print (type(e).__name__)
    #track = traceback.format_exc()
    #print(track)
    
=====================
#katano
добавить все ключи одного хэша в другой
context.update(whois_form.whois())

#katano
join list to str separated with ;
cloud_flags = ';'.join(flags_list)

===========ключа с фолбэком
получение 
.get('body', {}).get('len', 0)
.get('freeze_info', {}).get('state')

===========
путь к scratch файлам в pycharm
/Users/a.kondrikov/Library/Preferences/PyCharm2018.3/scratches
========
OOP
отличие метода от функции
Функция меняет свое имя на «method», когда она находится внутри класса. 
Обратите внимание на то, что каждый метод должен иметь как минимум один аргумент, что в случае с обычной функцией уже не вяжется.
объявление класса и создание экземпляра
class Vehicle:
    """docstring"""
 
    def __init__(self):
        """Constructor"""
        pass

создать подклас от класса
class Car(Vehicle):


=====================
python3.6 -m pip install  ipwhois

# generate random from interval (от 0 до 10 не включая 10 )
from random import randrange
print(randrange(10))

=============================
ключ хэша в зависимости от того определена ли переменная:

https://stackoverflow.com/questions/14263872/only-add-to-a-dict-if-a-condition-is-met/55341342#55341342
================
make docker-django-shell
ipython
================================================
прикольная статья про звездочки в питоне
https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/

=========================
интерактивные оболочки питона
ipython3

==========================
красивый дамп в питоне, аналог Dumper
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

еще один красивый способ:
import json
print(json.dumps(phones, indent=4))

пиздатый способ распечатать объект с атрибутами и их значениями
from pprint import pprint
pprint(vars(self))

если нужно считать хэш из файла и работать с ним как с файлом:

In [1]: with open('user_short') as f:
   ...:     user = f.read()
   ...:     print (user)
user_d = eval(user)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(user_d)
========================
лайфхак когда тебе не нужна переменная
login, _ = self.parse_corp_email(email)


===============================================================
добавлять ключ-значение в словарь в зависимости от условия
https://stackoverflow.com/questions/14263872/only-add-to-a-dict-if-a-condition-is-met
params = urllib.urlencode({
    'apple': apple,
    **({'orange': orange} if orange else {}),
})

===============================================================
аннотация типов в питоне
from typing import Dict, Optional, Any


def add(self) -> str:
def weblink_owner(weblink: str) -> Dict[str, Any]:
def link_delete(weblink: str) -> None:

def account_social_bind(email:str) -> List[str]:
def account_social_bind_remove(social_account:str) -> None:


=================
красивое преобразование дикта от данилы
затиарем пароль только в том случае если он был в исходном дикте
check_clean = {**check, **({'password': '***'} if 'password' in check else {})}

==============
красивая проверка на неправвильные табы в файлике
python -m tabnanny yourfile.py

===============================
каноническое считывание файла с командной строки и стрипание

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
sms_users_old = [line.rstrip() for line in args.file]

===========
принты с версии 3.8
logger.info(f'got check monitor request {rinfo_type=}, {email=}, {operator=}')

============


