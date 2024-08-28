import pandas as pd

# Загружаем набор данных
boston_df = pd.read_csv('housing.csv')

print("===================")
print(boston_df.head())
print("===================")
print(boston_df.isnull().sum())


