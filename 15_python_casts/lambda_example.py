# Задачи для тренировки:
#
# 1) Написать lambda-функцию, принимающую 1 аргумент — сторону квадрата, и возвращающую периметр квадрата.
# 2) Написать lambda-функцию, которая выводит среднее арифметическое 3 чисел.
# https://www.youtube.com/watch?v=PESQ755dHGg


square_area = lambda a: a * a

print(square_area(10))


average = lambda a, b, c : (a + b + c)/3

print(average(2, 4, 3))
