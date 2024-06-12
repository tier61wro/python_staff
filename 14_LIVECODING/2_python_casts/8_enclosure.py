'''
Замыкания это функция, в теле которой присутствуют ссылки на переменные,
объявленные вне тела этой функции в окружающем коде и не являющиеся её параметрами

у нас есть вот такие области видимости:
Local
Enclosed
Global
Builtins
пример от Молчанова
'''

def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
        pass
    return inner

# в примере выше inner + x дают нам замыкание

o = one()
o()
a = o.__closure__[0].cell_contents
print(id(a))
print("============")


'''
в примере ниже
Замыкание c сохраняет значение count между вызовами,
поэтому переменная count увеличивается на единицу каждый раз, когда мы вызываем c.
'''

# тут inner в совокупности с count которую она захватила, является замыканием
def counter():
    count = 0 # enclosed

    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter() # с это замкнутая функция, переменная, которая ссылается на наше замыкание
print(c())  # 1
print(c())  # 2
print(c())  # 3

# если заглянуть внутрь замкнутой функции, мы найдем там нашу переменную count
print(len(c.__closure__))
print(f'after end = {c.__closure__[0].cell_contents}')


################################################################
config = {
    'language': 'ru',
    'timezone': 'UTC'
}


def get_config(key):  # внешняя функция
    def inner():  # внутрення функция
        return config.get(key, None)
    return inner

get_language = get_config('language')  # inner запоминает значение language
# get_language это замыкание
get_timezone = get_config('timezone')  # inner запоминает значение timezone
# get_timezone это замыкание

print(get_language())  # ru
print(get_timezone())  # UTC

#######################################################
def pasta_recipe(ingredient):
    def inner():
        print(f"You eat pasta with {ingredient}")
    return inner


cheese_pasta = pasta_recipe('cheese')
meat_pasta = pasta_recipe('meat')

cheese_pasta()
meat_pasta()


'''
задание для САМПО
дан словарь 
d = {'dima':4, 'alex':5, 'ivan': 5}
сделай две замкнутые функции 
get_all_4
get_all_5
'''
# решение
d = {'dima':4, 'alex':5, 'ivan': 5}

def outer(mark):
    def inner():
        list_out = []
        for key, val in d.items():
            if val == mark:
                list_out.append(key)
        print(", ".join(list_out))

    return inner

def outer_comp(mark):
    def inner():
        return {k: v for k, v in d.items() if k == mark}

get_all_5 = outer(5)
get_all_4 = outer(4)

get_all_5()