
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
np.random.seed(10)
# Генерирует массив из 200 случайных чисел, распределенных по нормальному закону с средним значением 100 и стандартным отклонением 20
data = np.random.normal(100, 20, 30)
print(data)

fig = plt.figure(figsize = (10, 7))

# Creating plot
plt.boxplot(data)
plt.scatter(data)

# show plot
plt.show()