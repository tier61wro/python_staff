# 2024 version
from datetime import datetime

# наш декоратор
def timeit(func):
    def wrapper():  # обычно используют wrapper
        start = datetime.now()
        result = func()
        print(datetime.now() -start)
        return result
    return wrapper()

@timeit
def one():
    l = []
    # start = datetime.now()
    for i in range(1, 10001):
        if i % 2 == 0:
            l.append(i)

    return l

@timeit
def two():
    # start = datetime.now()
    l = [x for x in range(1, 1001) if x % 2 == 0]
    # print(datetime.now() - start)
    return l


l1 = one()
l2 = two()
# print(l1)
# print(l2)



