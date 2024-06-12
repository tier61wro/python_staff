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


def create_konvert(index_number: int, *args, **kwargs) -> str:
    print(f"{type(args)} -- {args}")
    print(f"{type(kwargs)} -- {kwargs}")
    name = " ".join(args)
    tail = ""
    for k, v in kwargs.items():
        tail = tail + " " + k + " " + v

    return f'{index_number} {name}{tail}'

res = create_konvert('053200', 'Лунаида', 'Коновалова', street = 'Broadway', house = '10', flat = '1')
print(res)

def create_profile(username, age, language):
    print(f"Username: {username}, Age: {age}, Favorite Language: {language}")


create_profile("Masha", age=12, language='russian')
