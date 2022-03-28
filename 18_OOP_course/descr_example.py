# задачка для самостоятельной:
# напиши при помощи дескрипторов:
# класс у которого есть атрибут epoch при вызове которго будет отдаваться текущий unix ts


from time import time


# class Epoch:
#     def __get__(self, instance, owner_class):
#         print(f'{self=}')
#         print(f'{instance=}')
#         print(f'{owner_class=}')
#         return int(time())

class MyTime:
    # epoch = Epoch()
    epoch = int(time())

d = MyTime()
print(d.epoch)