"""
train_date: 04.05.2020
kata link: https://www.codewars.com/kata/55de9c184bb732a87f000055
points: 6 kyu
type BASIC
-------------
DESCRIPTION:

Write a function that will take in any array and reverse it.

Sounds simple doesn't it?

NOTES:

Array should be reversed in place! (no need to return it)
Usual builtins have been deactivated. Don't count on them.
You'll have to do it fast enough, so think about performances

-------------
TRANSLATION:

Напишите функцию, которая принимает любой массив и переворачивает его.

ПРИМЕЧАНИЯ:

Массив должен быть перевернут на месте! (не нужно его возвращать)
Обычные встроенные функции были деактивированы. Не рассчитывайте на них.
Вы должны сделать это достаточно быстро, так что подумайте о производительности.

Вам не разрешается использовать следующее:
- Синтаксис срезов
- Определение пустого списка: []. Вместо этого используйте "x=list()", если это необходимо
- Списковые включения (list comprehensions)
- Оператор распространения внутри квадратных скобок
- Встроенные функции "tuple" и "reversed" были деактивированы

Встроенная функция "list" была заменена другой реализацией со следующими спецификациями:
- list.reverse запрещен
- list.reversed запрещен
- Срезы запрещены
Все остальные обычные методы класса списка остаются прежними.
-------------
===TRAINED====
pop не просто выталкивает последний элемент из массива, но и возвращает его в переменную
чтобы получить индексы элементов массива через range надо использовать range(0, len(seq))
поменять местами значения двух элементов массива можно через tuple, без промежуточной переменной

"""

def reverse(seq):
    reversed_list = list()
    for k in range(0, len(seq)):
        reversed_list.append(seq.pop())

    return reversed_list

# второе решение которое codewars отказался принимать непонятно почему
def reverse(seq):
    start = 0
    end = len(seq) - 1
    while start <  end:
        seq[start], seq[end]  = seq[end], seq[start]
        start += 1
        end -= 1



#seq = ['?','you','are','how','world','hello']
seq = [{'b':2},{'a':1}]

l = reverse(seq)
print(l)