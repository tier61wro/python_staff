from datetime import datetime

# наш декоратор
def timeit(func):
    def jopa():  # обычно используют wrapper
        start = datetime.now()
        result = func()
        print(datetime.now() -start)
        return result
    return jopa


@timeit
def one():
    l = []
    for i in range(1, 10001):
        if i % 2 == 0:
            l.append(i)
    return l




