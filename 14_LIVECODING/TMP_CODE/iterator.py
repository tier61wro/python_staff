class MyIterable:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")



# Создаем экземпляр класса MyIterable
my_iterable = MyIterable([1, 2, 3, 4, 5])

print(next(my_iterable))
# for i in my_iterable:
#     print(i)

# 1
# 2
# 3
# 4
# 5


# # Используем его в цикле for
# for item in my_iterable:
#     print(item)
#
# # Используем его в явной итерации
# iterator = iter(my_iterable)
# print(next(iterator))  # Вывод: 1
# print(next(iterator))  # Вывод: 2
# print(next(iterator))  # Вывод: 3
# print(next(iterator))  # Вывод: 4
# print(next(iterator))  # Вывод: 5
# print(next(iterator))  # Это вызовет StopIteration, так как элементы закончились


