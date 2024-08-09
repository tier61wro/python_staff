d1 = {'a':1, 'b':2}

d2 = {'c': 3}
d2.update(d1)
print(d2)

from collections import Counter

str = 'mama mila'

# Подсчитываем количество каждой буквы в строке
letter_counter = Counter(str)

# Сортируем по количеству в порядке убывания
sorted_letter_counter = letter_counter.most_common()
print(sorted_letter_counter)


from datetime import datetime
current_time = datetime.now()
print(current_time)
readable_date = current_time.strftime('%Y-%m-%d %H:%M:%S')
print(readable_date)