def add_numbers(a, b):
    print(a, b)

# с двумя переменными все ок - но что делать если переменных больше, мы же не будем переписывать всю функцию?
# нам приходит на помощь вот такая функция


def add(*args):
    print(type(args))  # tuple
    print(f'args = {args}')
    print(sum(args))


add(2, 3, 4)


# но если надо передать список в функцию со *, список надо передавать на вход тоже со *

l = [1, 2, 3]

#add(l) # так свалимся в эксепшен
add(*l)


# нужно быть очень внимательными с позиционными переменными
# при вызове add(*l), если есть позиционная переменная - то нулевой элемент l уйдет в нее

# так же плохая идея передавать генератор на вход такой функции - он раскрутится тогда полностью, а суть генераторов не раскручиваться полностью
# ** - упаковка входящих позиционных аргументов в словарь
# а **kwargs — сокращение от «keyword arguments» (именованные аргументы).


def show_args(*args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


a = [1, 2, 3]
d = {'street': 'tapicerska', 'house': 5}

show_args(*a, street = 'tapicerska', house = 5)
# и вот так тоже:
show_args(*a, **d)


# Самозадание
'''
написать функцию которая принимает на вход
первую позиционную переменную индекс
дальше все позиционные переменные в имя
и все именованные переменные в адрес
'''

def create_konvert(index, *args, **kwargs):
    name = ' '.join(args)
    addres = ""
    for k, v in kwargs.items():
        addres += k + ' ' + v + ',' + ' '
    konvert_sticker = f'index: {index}, username: {name}, addr: {addres}'
    return konvert_sticker

konvert = create_konvert('053200', 'Лунаида', 'Ивановна', 'Коновалова', street = 'Broadway', house = '10', flat = '1')
#index: 053200, username: Лунаида Ивановна Коновалова, addr: street Tapicerska,house 5,flat 1,
print(konvert)
