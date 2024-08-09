import datetime
import time

str = 'Abmama mila ramu rama mila mamu'
# посчитать сколько каких букв в строке и распечатать хитпарад в порядке убывания


# str_list = [*str]
#
# print(str_list)
letter_dict = {}

# for i in str_list:
#     if i in letter_dict.keys():
#         letter_dict[i] = letter_dict[i] + 1
#     else:
#         letter_dict[i] = 1

for l in str:
    letter_dict[l] = letter_dict.get(l, 0) + 1
print(letter_dict)

# sorted_dict = map(lambda , for k,  letter_dict)
sorted_dict = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)




from collections import Counter
#
# str = 'Abmama mila ramu rama mila mamu'
#
# # Подсчитываем количество каждой буквы в строке
# letter_counter = Counter(str)
#
# # Сортируем по количеству в порядке убывания
# sorted_letter_counter = letter_counter.most_common()
#
# print(sorted_letter_counter)
#
# print(vars(letter_counter))

# print(letter_counter.__dict__)

class Person:
    age = 12
    # def __init__(self, age):
    #     self.age = age

p = Person()
print(vars(p))