'''
Задание для САМПО
написать функцию create_konvert
которая создает стикер на конверт,
она принимает на вход:
• первую позиционную переменную и сохраняет ее в индекс
• дальше все позиционные переменные склеивает в имя
одну переменную Лунаида сохраняет в переменную nickname
• и дальше все именованные переменные сохраняет в адрес

index: 053200, username: Лунаида Коновалова, addr: street Broadway, house 10, flat 1,
create_konvert('053200', 'Лунаида', 'Коновалова', street = 'Broadway', house = '10', flat = '1')
'''

from typing import Tuple, Dict

def create_konvert(index: str, *args: str, **kwargs: str) -> str:
    address = ", ".join([f'{k}: {v}' for k, v in kwargs.items()])
    konvert_sticker = f"{index}, {' '.join(args)}, {address}"
    return konvert_sticker

sticker = create_konvert('053200', 'Лунаида', 'Коновалова', street='Broadway', house='10', flat='1')
print(sticker)



import random

tries = 10
random_number = random.randint(1, 100)
# print(random_number)
