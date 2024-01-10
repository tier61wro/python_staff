from datetime import datetime

#Декоратор
def timeit(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper

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


# start = datetime.now()
n = 10000
if args['mode'] == '1':
    one(n)
else:
    two(n)
# print(datetime.now() - start)

l1 = timeit(one)(10) # => wrapper(10)
print(type(l1))
print(__name__)
print(l1.__name__)
print(vars(l1).keys())
print(dir(l1))
