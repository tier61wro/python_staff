import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score
# from sklearn.model_selection import train_test_split

# Генерация данных
# np.random.seed(42)
# X = np.random.rand(100, 1) * 10  # 100 значений x от 0 до 10
# y = 2 * X + 1 + np.random.randn(100, 1)  # y = 2x + 1 + шум
#
# print(X)


l = np.random.randn(100, 1)
max_value = np.max(l)
print("Максимальное значение:", max_value)


class SensitiveField:
    def __init__(self):
        self.value = 100000

    def __get__(self, obj, obj_type=None):
        print("sensitive data was accessed")
        return self.value


class BankAccount:
    account = SensitiveField()

a = BankAccount()
print(a.account)



