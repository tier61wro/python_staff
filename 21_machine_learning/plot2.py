import numpy as np
import matplotlib.pyplot as plt

# Creating dataset
np.random.seed(10)
# Генерирует массив из 30 случайных чисел, распределенных по нормальному закону с средним значением 100 и стандартным отклонением 20
data = np.random.normal(170, 10, 200)
print(data)

fig = plt.figure(figsize=(10, 7))

# Creating a histogram (купол)
plt.hist(data, bins=25, edgecolor='black')

# Adding labels and title
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()
