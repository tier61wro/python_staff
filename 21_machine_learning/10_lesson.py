import numpy as np
import matplotlib.pyplot as plt

height_women_new = [1.48, 1.49, 1.49, 1.50, 1.51, 1.52, 1.52, 1.53, 1.53, 1.54, 1.55, 1.56, 1.57, 1.57, 1.58, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.65, 1.66, 1.67, 1.67, 1.68, 1.68,  1.69, 1.70, 1.70, 1.71, 1.71, 1.71, 1.74, 1.75, 1.76, 1.77, 1.77, 1.78]
neck_women = [29.1, 30.0, 30.1, 30.2, 30.4, 30.6, 30.8, 30.9, 31.0, 30.6, 30.7, 30.9, 31.0, 31.2, 31.3, 32.0, 31.4, 31.9, 32.4, 32.8, 32.8, 33.3, 33.6, 33.0, 33.9, 33.8, 35.0, 34.5, 34.7, 34.6, 34.2, 34.8, 35.5, 36.0, 36.2, 36.3, 36.6, 36.8, 36.8, 37.0, 38.5]

print(type(height_women_new))
print(height_women_new)

# переведем наши списки в особый формат, массив Numpy
X = np.array(height_women_new)
print(type(X))
print(X)

# преобразуем наш список X сначала в одномерный массив Numpy, а затем добавим второе измерение
# X = np.array(X).reshape(-1, 1)
X = np.array(X).reshape(-1)
print(X)

y = np.array(neck_women)
quit(0)

# создадим модель с помощью функции polyfit()
# slope и intercept - это наклон и сдвиг вверх-вниз нашей прямой
# и одновременно те самые веса модели w и e
slope, intercept = np.polyfit(X, y, 1)


print(f'{np.round(slope, 3)=}')
print(f'{np.round(intercept, 3)=}')

plt.figure(figsize=(10, 8))

# снова построим точечную диаграмму на основе двух нампай массивов
# plt.scatter(X, y)

slope = 60
intercept = 1
plt.plot(X, X * slope + intercept, 'r')

plt.xlabel('Рост женщин в России, м', fontsize = 16)
plt.ylabel('Обхват шеи, см', fontsize = 16)
plt.title('Зависимость роста и окружности шеи у женщин в России', fontsize = 18)
plt.show()