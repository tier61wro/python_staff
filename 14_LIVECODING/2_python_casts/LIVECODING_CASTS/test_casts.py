# yields
# напиши функцию которая используя yield создает список чисел фибоначи для заданного числа N
from typing import Generator


def fib(number: int) -> int:
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

# print(fib(5))




def generate_fibonacci_seq(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield fib(i)
        print(f"previous was {i}")

iter_seq = generate_fibonacci_seq(10)

# print(list(iter_seq))

for i, fn in enumerate(iter_seq):
    print(f'{i} -- {fn}')
    break
# map

# filter