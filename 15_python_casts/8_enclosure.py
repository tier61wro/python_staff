#  Замыкание c сохраняет значение count между вызовами,
#  поэтому переменная count увеличивается на единицу каждый раз, когда мы вызываем c.

def counter():
    count = 111

    def inner():
        # nonlocal count
        # count += 1
        return count
    return inner

c = counter()
print(c())  # 1
# print(type(c))
# print(dir(c))
# print(c.__closure__[0])
print(dir(c.__closure__[0].cell_contents))
print(c.__closure__[0].cell_contents)


print(c())  # 2
print(c())  # 3

################################################################
# config = {
#     'language': 'ru',
#     'timezone': 'UTC'
# }
#
#
# def get_config(key):  # внешняя функция
#     def inner():  # внутрення функция
#         return config.get(key, None)
#     return inner
#
# get_language = get_config('language') # inner запоминает значение language
# get_language это замыкание
# get_timezone = get_config('timezone') # inner запоминает значение timezone
# get_timezone это замыкание

# print(get_language())  # ru
# print(get_timezone())  # UTC

################################################################

# def jopa_size():
#     val = 'jopa'
#
#     def inner():
#         nonlocal val
#         val += 'a'
#         return val
#
#     return inner
#
# cl = jopa_size()
#
#
# print(cl())  # jopaa
# print(cl()) # jopaaa

#################### Фибоначи


