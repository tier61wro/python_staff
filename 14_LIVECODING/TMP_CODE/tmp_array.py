# Импорт модуля array
from array import array

# Создание массива целых чисел
my_array = array('i', [1, 2, 3, 4, 5])

# Добавление элемента в конец массива
my_array.append(6)

print(type(my_array))