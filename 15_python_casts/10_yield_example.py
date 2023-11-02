# 10 lesson python casts

# напишем функцию, которая возвращает список цифр от n до 0, для 4: [3, 2, 1, 0]
# эта функция делает список целиком и отдает его пользователю
def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result


print(countdown(4))  # [3, 2, 1, 0]


def gen_countdown(n):
    while n != 0:
        n -= 1
        yield n


g = gen_countdown(4)
print(type(g))  # <class 'generator'>
print(next(g))