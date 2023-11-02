# 2023 version
from datetime import datetime

# наш декоратор
def timeit(func):
    def jopa():  # обычно используют wrapper
        start = datetime.now()
        result = func()
        print(datetime.now() -start)
        return result
    return jopa


@timeit
def one():
    l = []
    # start = datetime.now()
    for i in range(1, 10001):
        if i % 2 == 0:
            l.append(i)

    # print(datetime.now() - start)

    return l

@timeit
def two():
    # start = datetime.now()
    l = [x for x in range(1, 1001) if x % 2 == 0]
    # print(datetime.now() - start)
    return l


l1 = one()
l2 = two()
# print(l1)
# print(l2)

# Проблемы тут у нас какие?
# 1. нарушен принцип Единой ответственности - целевого кода мало и много нецелевого
# 2. у нас нарушен принцип DRY - мы повторяем строки замеряния времени
# нам нужны волшебные скобочки - типа обернул функцию и тебе время посчиталось - это и есть декораторы

# прежде чем мы это сделаем полезно вспомнить о том что:
# функции это тн объекты первого класса
# 1) их можно присваивать переменным
# 2) их можно передавать в качестве аргумента в другие функции (например map принимает первым аргументом функции)
# 3) функции могут иметь вложенные функции

# напишем свой с блэкджеком и шлюхами (замыканиями и вложенными функциями :-))


