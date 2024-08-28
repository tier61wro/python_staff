import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

# cоздадим датафрейм
# названия столбцов возьмем из cancer.feature_names
cancer_df = pd.DataFrame(cancer.data, columns = cancer.feature_names)

# добавим целевую переменную
cancer_df['target'] = cancer.target

# посмотрим на первые пять наблюдений
print(cancer_df.head())

print(cancer_df.isnull().sum())

print(cancer_df.describe().round(2))

res = round((61 + 104)/(61 + 104 + 2 + 4), 2)
print(res)