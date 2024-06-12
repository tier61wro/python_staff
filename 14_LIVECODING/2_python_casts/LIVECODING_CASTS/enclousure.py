def one():
    x = ['one', 'two']
    def inner():
        print(x)
        pass
    return inner


o = one()

o()

'''
задание для САМПО
дан словарь 
d = {'dima':4, 'alex':5, 'ivan': 5}
сделай две замкнутые функции 
get_all_4
get_all_5
'''
d = {'dima': 4, 'alex': 5, 'ivan': 5}

def get_all(param):
    def inner():
        return {(k, v) for k, v in d.items() if v == param}
    return inner


get_all_4 = get_all(4)
get_all_5 = get_all(5)

r = get_all_4()
print(r)
r = get_all_5()
print(r)

