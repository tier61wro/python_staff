jack = {
    'name': 'jack',
    'car': 'bmw'
}

john = {
    'name': 'john',
    'car': 'audi'
}

users = [jack, john]   # это список словарей

# хотим сгенерировать список состоящий только из машин

cars = [u.get('car', '') for u in users]
print(cars)

new_cars = []
for p in users:
    new_cars.append(p.get('car', ''))

print(new_cars)

'''общий вид
(values) = [(expression) for (value) in (collection)]
'''

# фильтрация
names = ['jack', 'john', 'oleg', 'sasha']
j_names = [n for n in names if n.startswith('j')]
print(j_names)


new_names = []
for n in names:
    if n.startswith('j'):
        new_names.append(n)

'''общий вид
(values) = [(expression) for (value) in (collection) if (condition)]

вместо традиционного:
(values) = []
for (value) in (collection):
    if (condition):
        (values).append((expression))
'''