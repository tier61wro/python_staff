from datetime import datetime

#Декоратор
def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func
        print(datetime.now() - start)
        return result
    return wrapper()

@timeit
# декорируемая функция
def one(n):
    print(f'called one with param = {n}')
    l = []
    for i in range(10000):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
def two():
    print('two')
    return [x for x in range(10**6) if x % 2 == 0]


