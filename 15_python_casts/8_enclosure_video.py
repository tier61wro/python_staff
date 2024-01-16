"""
Замыкание это функция, в теле которой присутствуют ссылки на переменные,
объявленные вне тела этой функции в окружающем коде и не являющиеся её параметрами

у нас есть вот такие области видимости:
Local
Enclosed
Global
Builtins

в примере ниже у нас list x остается доступным в памяти после того как функция one
завершает работу
"""


def one():
    x = ['one', 'two']  # enclosed

    def inner():
        print(x)
        print(id(x))
        # pass
    return inner
# в примере выше inner + x дают нам замыкание


o = one()  # создаем замкнутую функцию
o()
a = o.__closure__[0].cell_contents
print(id(a))
print("="*10)


"""
применения замыканий:
1.Создание декораторов, в декораторах на вход передается декорируемая функция
2.Фабрики функций
3.Сохранение состояний (пример со счетчиком)
"""

"""
в примере счетчика ниже
Замыкание c сохраняет значение count между вызовами,
поэтому переменная count увеличивается на единицу каждый раз, когда мы вызываем c.
"""


# тут inner в совокупности с count которую она захватила, является замыканием
def counter():
    count = 0  # enclosed

    def inner():
        nonlocal count
        count += 1
        print(id(count))
        return count
    return inner


c = counter()  # с это замкнутая функция, переменная, которая ссылается на наше замыкание
print(c())  # 1
print(c())  # 2
print(c())  # 3

# если заглянуть внутрь замкнутой функции, мы найдем там нашу переменную count
print(f'after end = {c.__closure__[0].cell_contents}')
print(id(c.__closure__[0].cell_contents))


### Пример фабрики функций
def pasta_recipe(ingredient):
    def inner():
        print(f"You eat pasta with {ingredient}")
    return inner


cheese_pasta = pasta_recipe('cheese')
meat_pasta = pasta_recipe('meat')

cheese_pasta()
meat_pasta()