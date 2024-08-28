import numpy as np


a = np.array([[3, 4], [5, 6]]) # вектор данных
w = np.array([1, 2]) # вектор весов


res = np.dot(a, w)
print(f'{res=}')